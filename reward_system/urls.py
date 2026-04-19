from django.urls import path
from users.views import RegisterView, TopUpView
from products.views import ProductListView
from redemptions.views import RedeemView

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('products/', ProductListView.as_view()),
    path('redeem/', RedeemView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('topup/', TopUpView.as_view()),

    # Swagger
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]

