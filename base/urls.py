from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import get_user_profile_data, CustomemTokenObtainPairView, CustomRefreshView

urlpatterns = [
    path('token/', CustomemTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomRefreshView.as_view(), name='token_refresh'),
    path('user_data/<str:pk>/', get_user_profile_data, name='user_profile_data'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
