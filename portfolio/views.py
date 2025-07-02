from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ContactMessage
from .serializers import ContactMessageSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .serializers import ContactMessageSerializer

class ContactMessageView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Compose a fashionable, nicely formatted email message ✨
            message_body = f"""
🌸 New Message Received via Portfolio Contact Form! 🌸

👤 Name   : {serializer.validated_data['name']}
📧 Email  : {serializer.validated_data['email']}

💬 Message:
———————————————————————————
{serializer.validated_data['message']}
———————————————————————————
helloooo
Have a lovely day, Vigneshwari! 🌼
"""

            # Send that email
            send_mail(
                subject=f"🌟 New Contact from {serializer.validated_data['name']}",
                message=message_body,
                from_email=None,  # uses DEFAULT_FROM_EMAIL
                recipient_list=['vigneshwarisakthivel8@gmail.com'],
                fail_silently=False,
            )

            return Response({"message": "✨ Your message has been sent successfully! ✨"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

