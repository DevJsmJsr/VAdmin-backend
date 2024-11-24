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


class ReadPropertyCardAPIView(APIView):
  def post(self, request, *args, **kwargs):
    if 'pcFile' not in request.FILES:
      return JsonResponse({'error': 'Expecting a file'}, status=400)

    file_uploaded = request.FILES['pcFile']
    file_content = file_uploaded.read()
    azure_model_request_uuid = self.read_property_card(file_content)
    
    return Response({
      'azure_request_uuid': azure_model_request_uuid,
    })
    
  def read_property_card(self, file_content: IO)-> dict:
    url = settings.AZURE_MODEL_ANALYZER_ENDPOINT
    file_base64 = base64.b64encode(file_content).decode('utf-8')
    payload = json.dumps({
      "base64Source": file_base64
    })

    headers = {
      'Ocp-Apim-Subscription-Key': settings.AZURE_SECRET_KEY,
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    response.raise_for_status()
    response_headers = response.headers
    
    return response_headers["apim-request-id"]






