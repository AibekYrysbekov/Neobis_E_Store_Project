from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'userprofile', UserProfileViewSet)
router.register(r'order', OrderViewSet)


urlpatterns = [
    path('', include(router.urls), name='product'),
    path('', include(router.urls), name='order'),
    # path('users/', UserListView.as_view(), name='user-list'),
    # path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('auth/', include('rest_framework.urls')),

]
