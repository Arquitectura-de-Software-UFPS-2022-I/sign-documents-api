from django.urls import path
from .views import ValidateSignatureView

urlpatterns = [
    path('', ValidateSignatureView.as_view())
]