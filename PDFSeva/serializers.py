from rest_framework import serializers

class DeviceSerializer(serializers.Serializer):
    device_id = serializers.CharField(max_length=255)
    fcm_token = serializers.CharField(max_length=512)
    app_version = serializers.CharField(max_length=50)
    version_code = serializers.IntegerField()
    locale = serializers.CharField(max_length=10)