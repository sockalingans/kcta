from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet \
                , AddressViewSet \
                , PersonAddressViewSet \
                , AssocViewSet \
                , StudentViewSet \
                , VaguppuViewSet \
                , VaguppuStudViewSet

router = DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'personaddresses', PersonAddressViewSet)
router.register(r'assocs', AssocViewSet)
router.register(r'students', StudentViewSet)
router.register(r'students', VaguppuViewSet)
router.register(r'enrollments', VaguppuStudViewSet)

urlpatterns = [
    path('', include(router.urls)),
]