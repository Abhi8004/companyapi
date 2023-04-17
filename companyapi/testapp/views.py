from django.shortcuts import render
from testapp.models import Company,Employee
from rest_framework import viewsets
from testapp.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action



# Create your views here.

class CompanyViewSets(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

    #companies/{companyId}/employees
    @action(detail=True, methods=['get'])
    def employees(self,request,pk=None):
        try:
            company=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=company)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Company might not exits !! Error '
            })


class EmployeeViewSets(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
