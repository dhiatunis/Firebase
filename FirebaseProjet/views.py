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


def signIn(request):
    return render(request, "Login.html")


def home(request):
    return render(request, "Home.html")


def postsignIn(request):
    email = request.POST.get('email')
    pasw = request.POST.get('pass')
    try:
        user = authe.sign_in_with_email_and_password(email, pasw)
    except:
        message = "Invalid Credentials!!Please ChecK your Data"
        return render(request, "Login.html", {"message": message})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, "Home.html", {"email": email})


def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request, "Login.html")


def signUp(request):
    return render(request, "Registration.html")


def postsignUp(request):
    email = request.POST.get('email')
    passs = request.POST.get('pass')
    name = request.POST.get('name')
    try:
        user = authe.create_user_with_email_and_password(email, passs)
        uid = user['localId']
        idtoken = request.session['uid']

    except:
        return render(request, "Registration.html")
    return render(request, "Login.html")


def reset(request):
    return render(request, "Reset.html")


def postReset(request):
    email = request.POST.get('email')
    try:
        authe.send_password_reset_email(email)
        message = "A email to reset password is successfully sent"
        return render(request, "Reset.html", {"msg": message})
    except:
        message = "Something went wrong, Please check the email you provided is registered or not"
        return render(request, "Reset.html", {"msg": message})