from django.contrib import admin
from django.urls import path
from crop_model.views import predict_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', predict_image, name='home'),
]
