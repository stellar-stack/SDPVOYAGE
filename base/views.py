from .models import User
from base.serializers import UserProfileSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Create your views here.

class CustomemTokenObtainPairView(TokenObtainPairView):
    def post(sel, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            token = response.data

            access_token = token['access']
            refresh_token = token['refresh']

            res = Response()

            res.data = {'success': True}

            res.set_cookie (
                key = "access_token",
                value = access_token,
                httponly = True,
                secure = True,
                samesite = 'None',
                path = '/'
            )

            res.set_cookie (
                key = "refresh_token",
                value = refresh_token,
                httponly = True,
                secure = True,
                samesite = 'None',
                path = '/'
            )

            return res
        except:
            return Response({'Success': False})
        

class CustomRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.COOKIES.get('refresh_token')

            request.data['refresh'] = refresh_token

            response = super().post(request, *args, **kwargs)
            token = response.data

            access_token = token['access']
            res = Response()

            res.data = {'success': True}


            res.set_cookie (
                key = "access_token",
                value = access_token,
                httponly = True,
                secure = True,
                samesite = 'None',
                path = '/'
            )
            return res
        except:
            return Response({'Success': False})




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile_data(request, pk):
    try:
        try:
            user = User.objects.get(username=pk)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=404)

        serializer = UserProfileSerializer(user, many=False)
        return Response(serializer.data)
    except:
        return Response({'error': 'error getting user details'})
