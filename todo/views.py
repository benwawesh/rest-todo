from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Taskserializers
from.models import Tasks

@api_view(['GET'])
def overview(request):
    api_urls={
        "list":"list",
        "detail":'detail<int:item-id>/',
        'create':'create/',
        "update":"update<int-id/"
    }
    return Response(api_urls)

@api_view(['GET'])
def list(request):
    task=Tasks.objects.get()
    serializer=Taskserializers(task, many=False)
    return Response(serializer.data)

@api_view(['GET'])  
def detail(request,item_id):
    task=Tasks.objects.get(pk=item_id)
    serializer=Taskserializers(data=request.data)
    
    return Response(serializer.data)

@api_view(['POST']) 
def create(request):
    serializer= Taskserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['POST'])       
def update(request, item_id):
    task=Tasks.objects.get(id=item_id)
    serializer= Taskserializers(instance=task, data=request.data )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
@api_view(['DELETE'])    
def delete(request,item_id):
    task=Tasks.objects.get(id=item_id)
    task.delete()
    return Response("you have successfully deleted")

