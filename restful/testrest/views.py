# coding=<utf-8>
from django.views.decorators.csrf import csrf_protect,requires_csrf_token,csrf_exempt
from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from testrest.serializers import UserSerializer, GroupSerializer,ADDITSerializer,testadd,CalcClass
from models import addit
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions,status
from rest_framework.decorators import api_view
from testrest.tasks import justtry

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AddViewSet(viewsets.ModelViewSet):
    queryset = addit.objects.all()
    serializer_class = ADDITSerializer

class MyRESTView(APIView):
    print 000
    print "------------"
    def get(self, request, format=None):
        print 1
        myClass = CalcClass()
        print 2
        result = myClass.do_work()
        print 3
        response = Response(result, status=status.HTTP_200_OK)
        print 4
        return response
    def post(self, request, format=None):
        print 5
        myClass = CalcClass()
        print 6
        result = myClass.do_work()
        print 7
        response = Response(result, status=status.HTTP_200_OK)
        print 8
        return response


@csrf_exempt
def home(req):
    print 11
    a=0
    a=justtry()
    print 22
    print a
    
    return render_to_response("Index.html",{},context_instance=RequestContext(req))


class DeleteoneViewSet(viewsets.ModelViewSet):
    queryset = addit.objects.all()
    serializer_class = GroupSerializer


