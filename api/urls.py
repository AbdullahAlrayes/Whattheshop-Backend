from django.urls import path
from .views import UserCreateAPIView
from rest_framework_jwt.views import obtain_jwt_token
from api import views


urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('users/list/', views.UserListView.as_view(), name='api-user-list'),
    path('users/create/', views.UserCreateAPIView.as_view(), name='api-user-create'),
    path('users/detail/<int:user_id>/', views.UserDetailView.as_view(), name='api-user-detail'),
    path('users/update/<int:user_id>/', views.UserUpdateView.as_view(), name='api-user-update'),
    path('users/delete/<int:user_id>/', views.UserDeleteView.as_view(), name='api-user-delete'),


    path('profiles/create/', views.ProfileCreateAPIView.as_view(), name='api-profile-create'),
    path('profiles/update/<int:profile_id>/', views.ProfileUpdateView.as_view(), name='api-profile-create'),
    path('profiles/delete/<int:profile_id>/', views.ProfileDeleteView.as_view(), name='api-profile-delete'),


    path('products/list/', views.ProductListView.as_view(), name='api-product-list'),
    path('products/create/', views.ProductCreateView.as_view(), name='api-product-create'),
    path('products/detail/<int:product_id>/', views.ProductDetailView.as_view(), name='api-product-detail'),
    path('products/update/<int:product_id>/', views.ProductUpdateView.as_view(), name='api-product-update'),
    path('products/delete/<int:product_id>/', views.ProductDeleteView.as_view(), name='api-product-delete'),
    path('products-status/list/', views.ProductStatusListView.as_view(), name='api-product-status-list'),
    path('products-types/list/', views.ProductTypeListView.as_view(), name='api-product-type-list'),


    path('orders/list/', views.OrderListView.as_view(), name='api-order-list'),
    path('orders/create/', views.OrderCreateView.as_view(), name='api-order-create'),
    path('orders/detail/<int:order_id>/', views.OrderDetailView.as_view(), name='api-order-detail'),
    path('orders/update/<int:order_id>/', views.OrderUpdateView.as_view(), name='api-order-update'),
    path('orders/delete/<int:order_id>/', views.OrderDeleteView.as_view(), name='api-order-delete'),
    path('orders-status/list/', views.OrderStatusListView.as_view(), name='api-order-status-list'),
    path('orders-types/list/', views.OrderTypeListView.as_view(), name='api-order-type-list'),


    path('tags/create/', views.TagCreateView.as_view(), name='api-tag-create'),
    path('tags/list/', views.TagListView.as_view(), name='api-tag-list'),

    path('order-serial-no/create/', views.OrderSerialNoCreateView.as_view(), name='api-order-serial-no-create'),
    path('order-serial-no/list/', views.OrderSerialNoListView.as_view(), name='api-order-serial-no-list'),
]
