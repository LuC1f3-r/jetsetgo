# backend/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bookings.views import BookingViewSet
from accounts.views import RegisterView
from hotels.views import HotelViewSet
from flights.views import FlightViewSet
from payments.views import  PaymentViewSet
from cars.views import CarViewSet
from .views import booking_history
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'flights', FlightViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'cars', CarViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/accounts/register/', RegisterView.as_view(), name='register'),
    path('history/', booking_history, name='booking-history'),
    path('bookings/', include('bookings.urls')),
]
