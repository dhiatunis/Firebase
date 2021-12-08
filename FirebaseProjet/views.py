from django.shortcuts import render
import pyrebase

Config = {
    'apiKey': "AIzaSyAB8C_hEhAmlej-sHlytVfZxjrOkT5yp9Q",
    'authDomain': "cpanel-d67be.firebaseapp.com",
    'projectId': "cpanel-d67be",
    'storageBucket': "cpanel-d67be.appspot.com",
    'messagingSenderId': "174722531574",
    'appId': "1:174722531574:web:0428a3addfa370d0d4acd7",
    'measurementId': "${config.measurementId}",
    'databaseURL': ""
};

firebase = pyrebase.initialize_app(Config)
authe = firebase.auth()
database = firebase.database()


def home(request):
    return render(request, "Home.html")


def signUp(request):
    return render(request, "Registration.html")


def postsignUp(request):
    email = request.POST.get('email')
    passs = request.POST.get('pass')
    name = request.POST.get('name')
    try:
        user = authe.create_user_with_email_and_password(email, passs)
    except:
        return render(request, "Registration.html")
