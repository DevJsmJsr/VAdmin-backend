# views.py
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from typing import IO
from django.conf import settings
from django.db import transaction
from rest_framework import status
import requests
import json
import base64
from core.models import User
from core.serializers import PersonSerializer, VehicleSerializer, PropertyCardSerializer, UserSerializer


class CheckPropertyCardAPIView(APIView):
  def get(self, request, *args, **kwargs):
    azure_uuid = request.GET.get("azure_request_uuid")
    response = self.check_property_card(azure_uuid)
    if response:
      response = self.create_person(response)
      return Response({
        'data': {
          'message': f"Person {response['person_name']} was created with vehicle {response['number_plate']}, was created!",
          'person_name': response['person_name'],
          'number_plate': response['number_plate']
        }
      })
    
    return Response({
      'data': "Data could not be found",
    })
    
  def check_property_card(self, azure_uuid: str)-> dict:
    url = settings.AZURE_MODEL_CHECK_ENDPOINT
    url = url.replace("azure_request_uuid",f"{azure_uuid}")
    headers = {
      'Ocp-Apim-Subscription-Key': settings.AZURE_SECRET_KEY,
      'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)
    response.raise_for_status()
    response = response.json()
    return response
  
  @transaction.atomic
  def create_person(self, response):
    fields = response['analyzeResult']['documents'][0]['fields']
    identification = fields['id_propietario']['content'].split(' ')
    
    user_fields = {
      'username':identification[1], 
      'email':'newUser@vadmin.com',
      'rol':"USER",
      'is_superuser': False,
      'first_name':fields['nombre_propietario']['content'],
      'password': identification[1]
    }
    user_serializer = UserSerializer(data=user_fields)
    if user_serializer.is_valid(raise_exception=True):
      user = user_serializer.save()
    else:
      print(user_serializer.errors)
      return user_serializer.errors
    
    person_obj = self.create_person_obj(fields, identification[0], identification[1], user)
    pc_obj = self.property_card_obj(fields, person_obj)
    vehicle_obj = self.create_vehicle_obj(fields, pc_obj)
    
    if person_obj and vehicle_obj and pc_obj:
      return {
        'number_plate': vehicle_obj.number_plate,
        'person_name': person_obj.name
      }
    else:
      return "One object was not created"
    
  def create_person_obj(self, fields, document_type, document_number, user):
    person_fields = {
      'name': fields['nombre_propietario']['content'],
      'document_type': document_type,
      'document_number': document_number,
      'user_id': user.pk
    }
    person_serializer = PersonSerializer(data=person_fields)
    if person_serializer.is_valid(raise_exception=True):
      person_obj = person_serializer.save()
      return person_obj
    else:
      print(person_serializer.errors)
      return person_serializer.errors
    
  def property_card_obj(self, fields, person_obj):
    property_card_fields = {
        'property_card_number': fields['numero_licencia']['content'],
        'person_id': person_obj.uuid,
      }
    
    pc_serializer = PropertyCardSerializer(data=property_card_fields)
    if pc_serializer.is_valid(raise_exception=True):
      pc_obj = pc_serializer.save()
      return pc_obj
    else:
      print(pc_serializer.errors)
      return pc_serializer.errors

  def create_vehicle_obj(self, fields, pc_obj):
    vehicle_fields = {
      'number_plate': fields['placa']['content'],
      'model': fields['modelo']['content'],
      'brand': fields['marca']['content'],
      'color': fields['color']['content'],
      'type_vehicle': fields['clase_vehiculo']['content'],
      'fuel_type': fields['combustible']['content'],
      'property_card_id': pc_obj.pk
    }
    
    vehicle_serializer = VehicleSerializer(data=vehicle_fields)
    if vehicle_serializer.is_valid(raise_exception=True):
      vehicle_obj = vehicle_serializer.save()
      return vehicle_obj
    else:
      print(vehicle_serializer.errors)
      return vehicle_serializer.errors






