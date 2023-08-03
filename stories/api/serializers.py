from rest_framework import serializers
from stories.models import Story

class StorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['title', 'body']