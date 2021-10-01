from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status

from user.models import User
from user.serializers import UserSignUpSerializer, UserSignInSerializer

class UserSignUpAPIView(GenericAPIView):
    serializer_class = UserSignUpSerializer

    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "ok"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST )

class UserSignInAPIView(GenericAPIView):
    serializer_class = UserSignInSerializer
 
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message': 'INVALID USER'}, status = status.HTTP_400_BAD_REQUEST )
        
        serializer = UserSignInSerializer(user, data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({'message': 'INVALID USER'}, status = status.HTTP_400_BAD_REQUEST )
        
        return Response(serializer.data['email'])
        
        

      
        


# import json, bcrypt, requests, json
# from django.http            import JsonResponse, HttpResponse
# from django.views import View

# class Signup(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         try:
#             email        = data['email']
#             password     = data['password']

#             if not validate_email(email):
#                 return JsonResponse({'message':'INVALID EMAIL'}, status=400)

#             if not validate_password(password):
#                 return JsonResponse({'message':'INVALID PASSWORD'}, status=400)

#             if User.objects.filter(email = email).exists():
#                 return JsonResponse({'message':'DUPLICATE EMAIL'}, status=400)

#             if User.objects.filter(phone_number = phone_number).exists():
#                 return JsonResponse({'message':'DUPLICATE PHONE_NUMBER'}, status=400)

#             user = User.objects.create(
#                 email        = email,
#                 password     = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
#             )

#             return JsonResponse({'message':'SUCCESS'}, status=200)
#         except KeyError:
#             return JsonResponse({'message':'KEY ERROR'}, status=400)

# class Signin(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         try:
#             email    = data['email']
#             password = data['password'].encode('utf-8')

#             if not User.objects.filter(email=email).exists():
#                 return JsonResponse({'message': 'INVALID_USER'}, status=401)

#             user            = User.objects.get(email=email)
#             user_password   = user.password.encode('utf-8')

#             if not bcrypt.checkpw(password, user_password):
#                 return JsonResponse({'message': 'INVALID_USER'}, status=401)

#             return JsonResponse({'message':'SUCCESS'}, status=200)

#         except KeyError:
#             return JsonResponse({'message':'KEYERROR'}, status=400)