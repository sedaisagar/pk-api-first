from django.urls import path, include

from apis.icon.views import IconMakerFromImageView

urlpatterns = [    
    path('icon-make-from-image/', IconMakerFromImageView.as_view()),   
]