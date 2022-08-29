from django.urls import path
from .views import HomePageView,AbautPageView

urlpatterns = [
    path ('',HomePageView.as_view(),name = 'home'),
    path ('abaut/',AbautPageView.as_view(), name = 'about'),

]