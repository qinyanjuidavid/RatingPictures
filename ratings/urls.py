from django.urls import path
from ratings import views

app_name="ratings"

urlpatterns=[
path('',views.main_view,name="main"),
path('rate-image',views.rate_image,name="rate_image")
]
