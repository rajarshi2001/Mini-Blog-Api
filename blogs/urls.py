from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('blogapi', views.postView, basename='blogapi')

urlpatterns = [
    path('', include(router.urls)),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)