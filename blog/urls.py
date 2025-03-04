from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, PublicationListCreateView, PublicationDetailView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Для ViewSet (Category)
    path('publications/', PublicationListCreateView.as_view(), name='publication-list'),
    path('publications/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail'),
]
