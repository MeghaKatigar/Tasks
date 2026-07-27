from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from .serializers import TaskSerializer

from .models import Task

from silk.profiling.profiler import silk_profile

class TaskListCreateAPIView(APIView):
    serializer_class = TaskSerializer

    def get(self, request):
        tasks = Task.objects.all().order_by("-created_at")
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        many = False
        if isinstance(request.data, list):
            many = True    

        serializer = TaskSerializer(data=request.data, many=many)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            tasks = [Task(**item) for item in validated_data]
            tasks = Task.objects.bulk_create(tasks)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, data=status.HTTP_400_BAD_REQUEST)

class TaskRetrieveUpdateAPIView(APIView):
    serializer_class = TaskSerializer

    def get_object(self, id):
        task = Task.objects.filter(id=id)
        if task:
            return task.first()
        raise Http404

    def get(self, request, id):
        task = self.get_object(id=id)
        serializer = TaskSerializer(instance=task)
        return Response(serializer.data)

    def patch(self, request, id):
        task = self.get_object(id=id)

        serializer = TaskSerializer(
            instance=task,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskBulkCreateUpdateAPIView(APIView):
    serializer_class = TaskSerializer

    def get_object(self, id):
        task = Task.objects.filter(id=id)
        if task:
            return task.first()
        raise Http404(f"Task with Id - {id} does not exist.")   

    @silk_profile(name='View Blog Post')
    def post(self, request):
        success, error = [], []
        for data in request.data:
            serializer = TaskSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                success.append(serializer.data)
            else:
                error.append(serializer.errors)
        return Response({"success": success, "error": error}, status=status.HTTP_200_OK)     
    
    @silk_profile(name='View Blog Patch')
    def patch(self, request):
        success, error = [], []

        for data in request.data:
            id = data.get("id")
            task = self.get_object(id=id)
            serializer = TaskSerializer(instance=task, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                success.append(serializer.data)
            else:
                error.append(serializer.errors)
        
        return Response({"success":success, "error":error}, status=status.HTTP_200_OK)



