from django.urls import path

from user.views import UserSignUpAPIView, UserSignInAPIView

urlpatterns = [
    path('signup/', UserSignUpAPIView.as_view()),
    path('signin/', UserSignInAPIView.as_view())
]