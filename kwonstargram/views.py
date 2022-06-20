from rest_framework.views import APIView
from django.shortcuts import render


class Sub(APIView):
    def get(self, request):
        return render(request, 'kwonstargram/main.html')

    def post(self, request):
        return render(request, 'kwonstargram/main.html')