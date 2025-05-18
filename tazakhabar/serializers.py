from rest_framework import serializers

class TazaKhabarSerializer(serializers.Serializer):
    location = serializers.CharField(max_length=100)
    description = serializers.CharField()
    reporter = serializers.CharField(max_length=100)

    def validate_location(self, value):
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError("Location must contain only letters and spaces.")
        return value

    def validate_reporter(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Reporter name must be at least 2 characters long.")
        return value

    def validate(self, data):
        if data.get('location').lower() == data.get('reporter').lower():
            raise serializers.ValidationError("Location and reporter cannot be the same.")
        return data
