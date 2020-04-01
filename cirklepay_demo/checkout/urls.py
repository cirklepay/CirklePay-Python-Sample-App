from django.urls import path
from .views import home, cirklepay_checkout, cirklepay_success


urlpatterns = [
    path('', home, name="home"),
    path('cirklepay_checkout', cirklepay_checkout, name="cirklepay_checkout"),
    path('cirklepay/success', cirklepay_success, name="cirklepay_success"),
  

]
