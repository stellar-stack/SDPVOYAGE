from .models import User
from base.serializers import UserProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
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
