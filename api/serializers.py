from rest_framework import serializers
from .models import Task


# class TaskListSerialiser(serializers.ModelSerializer):

#     def create(self, validated_data):
#         result = [self.child.create(attrs) for attr in validated_data]

#         try:
#             self.child.Meta.model.objects.bilk_create(result)
#         except IntegrityError as e:
#             raise ValidationError(e)
#         return result


class TaskSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        instance = Task(**validated_data)

        if isinstance(self._kwargs["data"], dict):
            instance.save()
        return instance

    class Meta:
        model = Task
        fields = "__all__"

