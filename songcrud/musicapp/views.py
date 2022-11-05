from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Song
from .serializers import SongSerializer

# Create your views here.
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
    @action(detail=True, methods=['post', 'delete', 'put'])
    def set_password(self, request, pk=None):
        song = self.get_object()
