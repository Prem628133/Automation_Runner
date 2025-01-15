from django.http import JsonResponse
from django.views import View
from .models import Check
from .serializers import CheckSerializer


class CheckAPI(View):
    def get(self, request):
        # Print "Hello" to the terminal
        print(" Hello ")
        
        # Save log to the database
        choice = Check.objects.create(message="Hello")
        
        # Serialize the log
        serializer = CheckSerializer(choice)
        return JsonResponse(serializer.data)
