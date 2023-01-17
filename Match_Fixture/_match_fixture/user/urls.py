from django.urls import path

from user.views.fetch_user_info_view import FetchUserInfoView
from user.views.login_view import LoginView
from user.views.otp_verify_view import OtpVerifyView
from user.views.signup_view import SingupView

urlpatterns = [
    path('', FetchUserInfoView.as_view()),
    path('login', LoginView.as_view()),
    path('otp_ver', OtpVerifyView.as_view()),
    path('signup', SingupView.as_view())
]