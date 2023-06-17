from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from .models import Locked
from .serializers import LockedSerializer

class LockedSendOTPView(APIView):
    def post(self, request):
        user = request.user
        mail = user.email

        otp = get_random_string(length=6, allowed_chars='0123456789')

        locked = Locked(user=user, mail=mail, otp=otp)
        locked.save()

        subject = 'OTP Verification'
        message = f'Your OTP is: {otp}'

        send_mail(
            subject,
            message,
            'cloudpi.2023.secure@gmail.com',  
            [mail],
            fail_silently=False,
            auth_user='cloudpi.2023.secure@gmail.com',  
            auth_password='ypmipfxwadtmoiik',  
            connection=None,
            html_message=None
        )

        return Response({'detail': 'OTP sent successfully'})

class LockedVerifyOTPView(APIView):
    def post(self, request):
        user = request.user
        otp = request.data.get('otp')
        try:
            locked = Locked.objects.get(user=user, otp=otp)
        except Locked.DoesNotExist:
            return Response({'detail': 'Invalid OTP'})

        return Response({'detail': 'OTP verified successfully'})
