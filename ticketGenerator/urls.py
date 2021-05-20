# Welcome Commander...

from django.urls import path, include
from . import views

app_name = 'ticketGenerator'

urlpatterns = [
   path('', views.disputeTicket, name = 'disputeTicket'),
   path('generateNewTicket/', views.generateNewTicket, name = 'generateNewTicket'),
   path('todayOffer/', views.todayOffer, name = 'todayOffer'),
]
