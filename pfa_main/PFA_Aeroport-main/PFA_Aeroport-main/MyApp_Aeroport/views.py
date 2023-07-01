from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def book_flight(request):
    if request.method == 'POST':
        departure = request.POST.get('departure')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        airline = request.POST.get('airline')

        # Perform any necessary operations with the flight details (e.g., save to database)

        # Return a JSON response indicating successful booking
        response = {'message': 'Flight booked successfully!'}
        return JsonResponse(response)

    return render(request, 'flight/book_flight.html')
