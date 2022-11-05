from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SongViewSet, ArtisteViewSet, LyricViewSet

from . import views


router = DefaultRouter()
router.register(r'songs', SongViewSet, basename='songs')
router.register(r'artiste', ArtisteViewSet, basename='artistes')
router.register(r'lyric', LyricViewSet, basename='lyrics')


urlpatterns = [
    path('', include(router.urls)),
    path('create/', include(router.urls)),
    path('all/', include(router.urls)),
    path('songs/update/<int:pk>/', include(router.urls)),
    path('songs/<int:pk>/delete/', include(router.urls)),
    
]

urlpatterns += router.urls
