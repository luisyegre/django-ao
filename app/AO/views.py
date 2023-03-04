from django.shortcuts import render
from .models import Appoinment,Organization
from .serializers import  AppoinmentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response    

class AppoinmentView(APIView):
    def get(self, request, appo_pk=None, org_pk=None):        
        many=False
        date=request.GET.get('date')

        if appo_pk!=None and org_pk!=None: 
            data = Appoinment.objects.filter(organization__pk=org_pk, pk=appo_pk).first()
            many = False
        elif org_pk != None: 
            data = Appoinment.objects.filter(organization__pk=org_pk)
            many=True
        elif appo_pk != None:
            data = Appoinment.objects.get(id=appo_pk)
            many = False
        else:
            data = Appoinment.objects.all()
            many = True
        data_serialized = AppoinmentSerializer(data, many=many)
        return Response(data_serialized.data)
    
    def post(self,request):
        data =request.data
        if (
            not data.get('first_name') or
            not data.get('last_name') or
            not data.get('org')
        ):
            return Response({"message":"Bad Request"},status=400)
        org = Organization.objects.get(id=data['org'])
        model_created = Appoinment(
            organization = org,
            first_name=data['first_name'],
            last_name=data['last_name'],
        )
        model_created.save()
        return Response('model created',status=201)
    