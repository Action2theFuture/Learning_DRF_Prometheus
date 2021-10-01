from user.models import User
from user.validate import validate_email, validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers

import bcrypt

class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['email', 'password']
        extra_kwargs = {
                'email': {
                    'validators': [
                        UniqueValidator(
                            queryset=User.objects.all()
                        )
                    ]
                }
            }

    def save(self):
        email = self.validated_data['email']
        password = self.validated_data['password']

        password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
        print(password)
        user =  User(
                email        = email,
                password     = password
            )
        
        user.save()
        return { "user" : user }

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        
        if not validate_email(email):
            raise serializers.ValidationError({'message':'INVALID EMAIL'})

        if not validate_password(password):
            print(password)
            raise serializers.ValidationError({'message':'INVALID PASSWORD'})
        
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'message':'DUPLICATE EMAIL'})

        return super().validate(data)
    
class UserSignInSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['email', 'password']
        

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None).encode('utf-8')
        
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'message': 'INVALID USER'})

        user            = User.objects.get(email=email)
        user_password   = user.password.encode('utf-8')

        if not bcrypt.checkpw(password, user_password):
            raise serializers.ValidationError({'message': 'INVALID_USER'})

        return { 'email' : email }