from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Contact, JobApplication, ClientFeedback

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST['name'], 
            email=request.POST['email'], 
            message=request.POST['message']
        )
        return redirect('home')
    return render(request, 'contact.html')

def jobs(request):
    if request.method == 'POST':
        JobApplication.objects.create(
            name=request.POST['name'], 
            email=request.POST['email'], 
            coverletter=request.POST['coverletter'], 
            resume=request.FILES['resume']
        )
        return redirect('home')
    return render(request, 'jobs.html')

def feedback(request):
    if request.method == 'POST':
        ClientFeedback.objects.create(
            name=request.POST['name'], 
            email=request.POST['email'], 
            feedback=request.POST['feedback']
        )
        return redirect('home')
    return render(request, 'feedback.html')

def dashboard(request):
    contacts = Contact.objects.all()
    applications = JobApplication.objects.all()
    reviews = ClientFeedback.objects.all()
    return render(request, 'dashboard.html', {
        'contacts': contacts,
        'applications': applications,
        'reviews': reviews,
    })
