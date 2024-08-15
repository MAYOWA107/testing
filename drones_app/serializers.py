from rest_framework import serializers

from .models import Drone, DroneCategory, Pilot, Competition




class Drone_CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DroneCategory
        fields = ('url', 'id', 'name', )

        extra_kwargs = {
            'url': {'view_name': 'drone_categories-detail'}
        }

class DroneSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Drone
        fields = ('url', 'id', 'drone_name', 'name', 'manufacturing_date',
                  'drone_participated_in_at_least_one_competition', 'inserted_timestamp')
        
        
        extra_kwargs = {
            'url': {'view_name': 'drone-detail'}
        }


class CompetitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competition
        fields = '__all__'   



class PilotSerializer(serializers.ModelSerializer):
    competion = CompetitionSerializer(many=True, read_only=True)

    class Meta:
        model = Pilot
        fields = '__all__'































 




