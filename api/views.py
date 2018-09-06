from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView ,
    ListAPIView,
    RetrieveUpdateAPIView ,
    DestroyAPIView)
from .serializers import (
    UserCreateSerializer,
    UserUpdateSerializer,
    UserListSerializer,
    ProductListSerializer,
    ProductCreateSerializer,
    ProductStatusListSerializer,
    ProductTypeListSerializer,
    OrderListSerializer,
    OrderCreateSerializer,
    OrderStatusListSerializer,
    OrderTypeListSerializer,
    ProfileListSerializer,
    TagListSerializer,
    OrderSerialNoListSerializer
    )
from django.contrib.auth.models import User
from .models import (
    Product,
    ProductType,
    ProductStatus,
    Order,
    OrderStatus,
    OrderType,
    Tag,
    Profile,
    OrderSerialNo
    )

# ==================== Users =====================#
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'user_id'

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class UserUpdateView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'user_id'

class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'user_id'

# ==================== Profile =====================#

class ProfileCreateAPIView(CreateAPIView):
    serializer_class = ProfileListSerializer

class ProfileUpdateView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'profile_id'

class ProfileDeleteView(DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'profile_id'

# ==================== Products =====================#

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'

class ProductCreateView(CreateAPIView):
    serializer_class = ProductListSerializer

class ProductUpdateView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'

class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'

class ProductStatusListView(ListAPIView):
    queryset = ProductStatus.objects.all()
    serializer_class = ProductStatusListSerializer

class ProductTypeListView(ListAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeListSerializer

# ==================== Orders =====================#
class OrderStatusListView(ListAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusListSerializer

class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'order_id'

class OrderCreateView(CreateAPIView):
    serializer_class = OrderCreateSerializer

class OrderUpdateView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'order_id'

class OrderDeleteView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'order_id'

class OrderTypeListView(ListAPIView):
    queryset = OrderType.objects.all()
    serializer_class = OrderTypeListSerializer

class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

# ==================== Products =====================#

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'

class ProductCreateView(CreateAPIView):
    serializer_class = ProductCreateSerializer

class ProductUpdateView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'

class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'

class ProductStatusListView(ListAPIView):
    queryset = ProductStatus.objects.all()
    serializer_class = ProductStatusListSerializer

class ProductTypeListView(ListAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeListSerializer


# ==================== Tags =====================#

class TagCreateView(CreateAPIView):
    serializer_class = TagListSerializer

class TagListView(ListAPIView):
    queryset = OrderSerialNo.objects.all()
    serializer_class = TagListSerializer

class OrderSerialNoCreateView(CreateAPIView):
    serializer_class = OrderSerialNoListSerializer

class OrderSerialNoListView(ListAPIView):
    queryset = OrderSerialNo.objects.all()
    serializer_class = OrderSerialNoListSerializer
