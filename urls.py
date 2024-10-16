from django.urls import path
from .views import*

# Base urls==>> http://127.0.0.1:8000/mediplus/

urlpatterns = [
    path('home/',view_home,name='home'),
    path('doctos/',view_doctos,name='doctos'),
    path('services/',veiw_services,name='services'),
]

