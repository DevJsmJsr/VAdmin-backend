# views.py
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from typing import IO
from django.conf import settings
import requests
import json
import base64


class GetOrCreatePropertyCardView(APIView):
  def post(self, request, *args, **kwargs):
    if 'file' not in request.FILES:
      return JsonResponse({'error': 'Expecting a file'}, status=400)

    file = request.FILES['file']
    property_card_data = self.read_property_card(file)
    print(property_card_data,"*************************************")
    
    
    
    """ archivo_obj, creado = Archivo.objects.get_or_create(
        nombre=nombre,
        defaults={'archivo': archivo}
    ) """

    return Response({
      'id': "archivo_obj.id",
    })
    
  def read_property_card(self, file: IO)-> dict:
    try:
      url = settings.AZURE_MODEL_ENDPOINT,
      file_base64 = base64.b64encode(file.read())
      payload = json.dumps({"base64Source": file_base64})
      headers = {
        'Ocp-Apim-Subscription-Key': settings.AZURE_SECRET_KEY,
        'Content-Type': 'application/json'
      }
      response = requests.request("POST", url, headers=headers, data=payload)
      response.raise_for_status()
      data = response.json()
      return data
    except Exception as e:
      return {"error": str(e)}






