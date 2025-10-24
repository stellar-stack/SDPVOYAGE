from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from base import views
urlpatterns = [
  path('user_data/<str:pk>/', views.get_user_profile_data, name='user_profile_data'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
