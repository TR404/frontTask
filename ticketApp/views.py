from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'ticketApp/index.html')
	
	
def disputeTicket(request):
	return render(request, 'ticketApp/disputeTicket.html')

	
def generateTicket(request):
	return render(request, 'ticketApp/generateTicket.html')

	
def todayOffer(request):
	return render(request, 'ticketApp/todayOffer.html')
