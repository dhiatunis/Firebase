from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('signUp/', views.signUp),
	path('postsignUp/', views.postsignUp),
]
