from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'ticketApp/index.html')
	
	
def organizationDetails(request):
	return render(request, 'ticketApp/organizationDetails.html')

	
def billingAddress(request):
	return render(request, 'ticketApp/billingAddress.html')

	
def paymentMethods(request):
	return render(request, 'ticketApp/paymentMethods.html')
	
	
def changePassword(request):
	return render(request, 'ticketApp/changePassword.html')
	

