from django.shortcuts import render

# Create your views here.

def disputeTicket(request):
	return render(request, 'ticketGenerator/disputeTicket.html')
	
	
	
def generateNewTicket(request):
	return render(request, 'ticketGenerator/generateNewTicket.html')
	
	
def todayOffer(request):
	return render(request, 'ticketGenerator/todayOffer.html')	

