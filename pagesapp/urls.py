from django.urls import path
from .views import HomePageView,AbautPageView,NewPageView

urlpatterns = [
    path ('',HomePageView.as_view(),name = 'home'),
    path ('abaut/',AbautPageView.as_view(), name = 'about'),
    path ('new/',NewPageView.as_view(),name = 'new')

]