from django.http import HttpResponse
# from django.shortcuts import render


def homepage(request):
    return HttpResponse("Welcome to the Homepage")

def aboutUs(request): # one can use any name parameter inplace of request
    # return render(request, 'aboutUs.html')
    return HttpResponse("<h1>About Us</h1><p>Welcome to Python programming.</p>")

def contactUs(request): 
    return HttpResponse("<h1>Contact Us</h1><p>For any query contact us here.</p>")

def course(request): 
    return HttpResponse("<h1>Course</h1><p>Welcome to Python and Django Course .</p>")

def courseDetails(request,courseid):
    return HttpResponse(courseid) 