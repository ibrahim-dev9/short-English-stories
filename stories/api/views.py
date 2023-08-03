from rest_framework.response import Response
from rest_framework.decorators import api_view
from stories.models import Story
from .serializers import StorySerializers

@api_view(["GET", ])
def stories_api(request):
    stories = Story.objects.all()
    serializers = StorySerializers(stories, many=True)

    return Response(serializers.data)