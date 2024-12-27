from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .models import AWB
from .serializers import AWBSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes


@api_view(['GET'])
def list_awbs(request):
    if request.method == 'GET':
        awbs = AWB.objects.all()
        serializer = AWBSerializer(awbs, many=True)
        return Response(serializer.data)

# @api_view(['POST'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])

# def add_awb(request):
#     print(f"User: {request.user}")  # This should show the user associated with the token
#     print(f"User's is_first_category: {request.user.is_first_category}")  # Check if category-specific flag is set
#     print("Received request:", request)  # Print the request object
    
#     if request.method == 'POST':
#         print("Request data:", request.data)  # Print the request data

#         # Initialize the serializer with the data
#         serializer = AWBSerializer(data=request.data)
#         print("Serializer initialized:", serializer)  # Print the initialized serializer object
        
#         if serializer.is_valid():
#             print("Serializer is valid!")  # Indicate that the serializer is valid
#             serializer.save()
#             print("Data saved:", serializer.data)  # Print the saved data
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         print("Serializer errors:", serializer.errors)  # Print the validation errors if any
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_awb(request):
    print(f"Received Authorization header: {request.headers.get('Authorization')}")
    print(f"User: {request.user}")  # Check if user is correctly authenticated
    
    if request.method == 'POST':
        print("Request data:", request.data)  # Print the request data
        
        serializer = AWBSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            print("Data saved:", serializer.data)  # Print saved data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Serializer errors:", serializer.errors)  # Print errors if any
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
