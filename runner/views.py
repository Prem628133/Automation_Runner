from django.http import HttpResponse
from django.views import View
import os
import time


class CheckApiView(View):
    def get(self, request):
        #Logic to create a unique file
        file_path = os.path.join(os.getcwd(), f"file_{int(time.time())}.txt")
    
        # For creating and writing content in file
        with open(file_path, "w") as file:
            file.write("Automation Runner.")
        return HttpResponse(f"File created at {file_path}")

