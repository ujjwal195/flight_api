from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='Flight_Details')),  # Redirect to an existing URL
    path('Flight/<str:From>/<str:To>/', views.flight_details, name='Flight_Details'),
]
