# user/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny

class SignupView(APIView):
    """
    Signup view to create a new user.
    Returns user details along with JWT tokens.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'username': user.username,
                'is_first_category': user.is_first_category,
                'is_second_category': user.is_second_category,
                'is_third_category': user.is_third_category,
                'is_fourth_category': user.is_fourth_category,
                'message': 'User created successfully'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Here we reuse the TokenObtainPairView to handle login and generate JWT tokens
# This view already comes from `rest_framework_simplejwt` and handles both access and refresh tokens.

class LoginView(TokenObtainPairView):
    """
    Login view to obtain JWT tokens and add user category information.
    """
    
    def post(self, request, *args, **kwargs):
        # Obtain the token response
        response = super().post(request, *args, **kwargs)
        
        # Authenticate the user (this step is necessary to fetch user info)
        user = authenticate(username=request.data['username'], password=request.data['password'])
        
        if user is not None:
            # Add user category information to the response
            response.data['username'] = user.username
            response.data['is_first_category'] = user.is_first_category
            response.data['is_second_category'] = user.is_second_category
            response.data['is_third_category'] = user.is_third_category
            response.data['is_fourth_category'] = user.is_fourth_category
            response.data['message'] = 'Login successful'
        else:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return response

# Token refresh view remains unchanged
class TokenRefreshView(TokenRefreshView):
    """
    Token refresh view to get a new access token using refresh token.
    """
    pass
