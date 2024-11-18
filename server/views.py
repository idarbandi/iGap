from django.shortcuts import render
from rest_framework import viewsets


class ServerListViewSet(viewsets):
    queryset = self.queryset
    
    def list(sself, request):
        category = request.query_params.get('category')
            