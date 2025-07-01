from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def get_data(request):
    """
    A simple API view that returns items.
    """
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data, status=200)

@api_view(['POST'])
def add_data(request):
    """
    A simple API post that create returns an item.
    content-type: application/json
    Example:
    {
        "name": "Sample Item",
        "description": "This is a sample item."
    }
    This will create a new item and return it.
    """
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
