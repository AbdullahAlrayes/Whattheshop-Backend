from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),


    path('api/users/list/', views.UserListView.as_view(), name='api-user-list'),
    path('api/users/create/', views.UserCreateAPIView.as_view(), name='api-user-create'),
    path('api/users/detail/<int:user_id>/', views.UserDetailView.as_view(), name='api-user-detail'),
    path('api/users/update/<int:user_id>/', views.UserUpdateView.as_view(), name='api-user-update'),
    path('api/users/delete/<int:user_id>/', views.UserDeleteView.as_view(), name='api-user-delete'),


    path('api/profiles/create/', views.ProfileCreateAPIView.as_view(), name='api-profile-create'),
    path('api/profiles/update/<int:profile_id>/', views.ProfileUpdateView.as_view(), name='api-profile-create'),
    path('api/profiles/delete/<int:profile_id>/', views.ProfileDeleteView.as_view(), name='api-profile-delete'),


    path('api/products/list/', views.ProductListView.as_view(), name='api-product-list'),
    path('api/products/create/', views.ProductCreateView.as_view(), name='api-product-create'),
    path('api/products/detail/<int:product_id>/', views.ProductDetailView.as_view(), name='api-product-detail'),
    path('api/products/update/<int:product_id>/', views.ProductUpdateView.as_view(), name='api-product-update'),
    path('api/products/delete/<int:product_id>/', views.ProductDeleteView.as_view(), name='api-product-delete'),
    path('api/products-status/list/', views.ProductStatusListView.as_view(), name='api-product-status-list'),
    path('api/products-types/list/', views.ProductTypeListView.as_view(), name='api-product-type-list'),


    path('api/orders/list/', views.OrderListView.as_view(), name='api-order-list'),
    path('api/orders/create/', views.OrderCreateView.as_view(), name='api-order-create'),
    path('api/orders/detail/<int:order_id>/', views.OrderDetailView.as_view(), name='api-order-detail'),
    path('api/orders/update/<int:order_id>/', views.OrderUpdateView.as_view(), name='api-order-update'),
    path('api/orders/delete/<int:order_id>/', views.OrderDeleteView.as_view(), name='api-order-delete'),
    path('api/orders-status/list/', views.OrderStatusListView.as_view(), name='api-order-status-list'),
    path('api/orders-types/list/', views.OrderTypeListView.as_view(), name='api-order-type-list'),


    path('api/tags/create/', views.TagCreateView.as_view(), name='api-tag-create'),
    path('api/tags/list/', views.TagListView.as_view(), name='api-tag-list'),

]


if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
