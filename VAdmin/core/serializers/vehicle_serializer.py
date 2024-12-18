from rest_framework import serializers

from core.serializers.property_card_serializer import PropertyCardSerializer
from core.serializers.vehicle_accessories_serializer import VehicleAccessoriesSerializer
from core.serializers.vehicle_engine_serializer import VehicleEngineSerializer

from django.db import transaction
from core.models import PropertyCard
from core.models import Vehicle
from core.models import VehicleEngine
from core.models import VehicleAccessories


class VehicleSerializer(serializers.ModelSerializer):
  pk = serializers.IntegerField(required=False)
  doors_number = serializers.CharField(required=False)
  kilometric = serializers.CharField(required=False)
  property_card_id = serializers.IntegerField(write_only=True)
  property_card = PropertyCardSerializer(required=False)
  vehicle_accessories = VehicleAccessoriesSerializer(required=False)
  vehicle_engine = VehicleEngineSerializer(required=False)
  
  class Meta:
    model = Vehicle
    fields = ['pk','number_plate', 'model', 'brand', 'type_vehicle',
              'color', 'doors_number', 'fuel_type', 'kilometric',
              'property_card_id', 'property_card','vehicle_accessories',
              'vehicle_engine','initial_scan']
    
      
  @transaction.atomic
  def update(self, instance, validated_data):
    pc_validated = validated_data.get('property_card')
    if pc_validated:
      property_card = PropertyCard.objects.get(pk=pc_validated.get('pk'))
      property_card.issue_date = pc_validated.get('issue_date')
      property_card.enrollment_date = pc_validated.get('enrollment_date')
      property_card.transit_authority = pc_validated.get('transit_authority')
      property_card.save()
    
    vehicle_engine = validated_data.get('vehicle_engine')
    if vehicle_engine:
      VehicleEngine.objects.create(
        vehicle=instance,
        transmission=vehicle_engine.get('transmission'),
        horse_power=vehicle_engine.get('horse_power'),
        engine_type=vehicle_engine.get('engine_type'),
        brake_system=vehicle_engine.get('brake_system')
      )
    
    vehicle_accessories = validated_data.get('vehicle_accessories')
    if vehicle_accessories:
      VehicleAccessories.objects.create(
        vehicle=instance,
        reverse_cam=vehicle_accessories.get('reverse_cam'),
        sunroof=vehicle_accessories.get('sunroof'),
        power_mirrors=vehicle_accessories.get('power_mirrors'),
        power_seats=vehicle_accessories.get('power_seats'),
        voice_control=vehicle_accessories.get('voice_control'),
        driven_assistance=vehicle_accessories.get('driven_assistance'),
        bluetooth=vehicle_accessories.get('bluetooth'),
        air_conditioning=vehicle_accessories.get('air_conditioning'),
        cruise_control=vehicle_accessories.get('cruise_control'),
        parking_sensors=vehicle_accessories.get('parking_sensors'),
        anti_theft_system=vehicle_accessories.get('anti_theft_system'),
        alarm_system=vehicle_accessories.get('alarm_system'),
        remote_start=vehicle_accessories.get('remote_start'),
      )
    
    instance.doors_number = validated_data.get('doors_number')
    instance.kilometric = validated_data.get('kilometric')
    if pc_validated and vehicle_engine and vehicle_accessories:
      instance.initial_scan = Vehicle.COMPLETED
    instance.save()
    return instance
