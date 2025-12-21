from rest_framework import serializers

class DeviceSerializer(serializers.Serializer):
    device_id = serializers.CharField(max_length=255)
    fcm_token = serializers.CharField(max_length=512)
    app_version = serializers.CharField(max_length=50)
    version_code = serializers.IntegerField()
    locale = serializers.CharField(max_length=10)
    brand = serializers.CharField(max_length=100)
    manufacturer = serializers.CharField(max_length=100)
    model= serializers.CharField(max_length=100)
    android_version = serializers.CharField(max_length=10)
    sdk_version = serializers.CharField()
    os_choices=[('Android', 'android'), ('iOS', 'iOS')]
    os= serializers.ChoiceField(choices=os_choices)