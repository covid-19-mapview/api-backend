from rest_framework import serializers

from core.models import Disease, DiseaseInfectionStatus


class DiseaseInfectionStatusListSerializer(serializers.ModelSerializer):
    """
    DiseaseInfectionStatusListSerializer

    Serializes and outputs infection status
    """
    id = serializers.CharField(read_only=True)
    desc = serializers.CharField(source='infection_status')

    class Meta:
        model = DiseaseInfectionStatus
        fields = ('id', 'desc')


class DiseaseSerializer(serializers.ModelSerializer):
    """
    Serializes disease information including all the infection status associated with it.
    """
    id = serializers.CharField(read_only=True)
    infection_status = DiseaseInfectionStatusListSerializer(many=True, source='diseaseinfectionstatus_set',
                                                            read_only=True)

    class Meta:
        model = Disease
        fields = ('id', 'name', 'infection_status')


class DiseaseInfectionStatusDetailSerializer(serializers.Serializer):
    """
    DiseaseInfectionStatusDetailSerializer

    Serializes the disease infection status create and update data
    """
    id = serializers.CharField(read_only=True)
    infection_status = serializers.CharField(max_length=255)

    def validate_disease_id(self, disease_id):
        """
        Validates the given disease ID, checks if an associated disease exists !

        :param disease_id:
        :return:
        """
        try:
            Disease.objects.get(id=disease_id)
        except Disease.DoesNotExist:
            raise serializers.ValidationError('Please provide a valid disease ID !')
        return disease_id

    def create(self, validated_data):
        """
        Creates a disease record

        :param validated_data:
        :return:
        """
        disease = validated_data.pop("disease")
        return DiseaseInfectionStatus.objects.create(infection_status=validated_data.get('infection_status'),
                                                     disease=disease)

    def update(self, instance, validated_data):
        """
        Updates a disease record

        :param instance:
        :param validated_data:
        :return:
        """
        instance.infection_status = validated_data.get('infection_status', instance.infection_status)
        instance.save()

        return instance
