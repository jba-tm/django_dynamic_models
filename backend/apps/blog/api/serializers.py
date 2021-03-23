from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from ..models import Project, ArtProject, ResearchProject, ImageProject


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','topic',)


class ArtProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtProject
        fields = ('id','topic', 'artist')


class ResearchProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchProject
        fields = ('id','topic', 'supervisor')

class ImageProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProject
        fields = ('id', 'topic', 'image', 'caption')

class ProjectPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Project: ProjectSerializer,
        ArtProject: ArtProjectSerializer,
        ResearchProject: ResearchProjectSerializer,
        ImageProject: ImageProjectSerializer
    }
