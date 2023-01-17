from rest_framework import serializers

from user.models.user import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    @classmethod
    def create(self, validated_data):
        password = validated_data.pop("password")
        user_instance = self.Meta.model(**validated_data)
        user_instance.set_password(password)
        user_instance.save()
        return user_instance
    
    class Meta:
        model = User