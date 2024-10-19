from rest_framework import generics
from .serializers import UserSerializer

class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer


from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]



from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from .models import Event, Ticket

class TicketPurchaseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        event = Event.objects.get(pk=id)
        quantity = request.data.get('quantity')

        if event.tickets_sold + quantity > event.total_tickets:
            raise ValidationError("Not enough tickets available")

        event.tickets_sold += quantity
        event.save()

        ticket = Ticket.objects.create(user=request.user, event=event, quantity=quantity)
        return Response({"message": "Tickets purchased successfully"}, status=status.HTTP_201_CREATED)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .models import User

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = make_password(request.data.get('password'))  # Hash the password
        role = request.data.get('role', 'user')  # Default to 'user'

        # Create the user with provided role
        user = User.objects.create(username=username, password=password, role=role)
        return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
