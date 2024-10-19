from django.urls import path
from .views import RegisterUser
from .views import EventListCreateView, TicketPurchaseView,RegisterView,EventListCreateView



urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list'),
    path('events/<int:id>/purchase/', TicketPurchaseView.as_view(), name='purchase-ticket'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('api/events/', EventListCreateView.as_view(), name='event-list-create'),

]