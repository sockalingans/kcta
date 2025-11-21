from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssocTypeViewSet, SchoolViewSet, AcademyYrViewSet, AcademyLvlViewSet

router = DefaultRouter()
router.register(r'assoctypes', AssocTypeViewSet)
router.register(r'schools', SchoolViewSet)
router.register(r'academyyrs', AcademyYrViewSet)
router.register(r'academylvls', AcademyLvlViewSet)

urlpatterns = [
    path('', include(router.urls)),
]