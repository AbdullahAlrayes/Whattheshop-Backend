from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (Profile, ProductStatus, ProductType, Product, OrderStatus, OrderType, Order, Tag)




# ================================ Order Type & Status =======================#
class OrderStatusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'

class OrderTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderType
        fields = '__all__'
# ================================ Tag =======================================#

class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

# ================================ ProductsType & Status =====================#

class ProductTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'

class ProductStatusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductStatus
        fields = '__all__'

# ================================ Profile =====================================#

class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

# ================================ Users =====================================#
class UserProductListSerializer(serializers.ModelSerializer):
    type= ProductTypeListSerializer()
    status = ProductStatusListSerializer()
    tag =TagListSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id','name','description','created_on','updated_on','pic','type','status','tag' ]

class UserOrderListSerializer(serializers.ModelSerializer):
    status = OrderStatusListSerializer()
    class Meta:
        model = Order
        fields = ['id','created_on','updated_on','status' ]

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class UserListSerializer(serializers.ModelSerializer):
    profile = ProfileListSerializer()
    orders = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id','first_name','last_name','username','email','is_superuser','is_staff','is_active','date_joined','last_login','profile', 'orders', 'products']

    def get_orders(self, obj):
        orders = obj.createdby.all()
        return UserOrderListSerializer(orders, many=True).data

    def get_products(self, obj):
        products = obj.product_set.all()
        return UserProductListSerializer(products, many=True).data

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','username','email','is_superuser','is_staff','is_active']

# ================================ Orders =====================================#

class CommonUserListSerializer(serializers.ModelSerializer):
    profile = ProfileListSerializer()

    class Meta:
        model = User
        fields = ['id','first_name','last_name','username','email','is_superuser','is_staff','is_active','date_joined','last_login','profile']

class OrderListSerializer(serializers.ModelSerializer):
    created_by = CommonUserListSerializer()
    status = OrderStatusListSerializer()
    class Meta:
        model = Order
        fields = ['id','created_on','updated_on','status','price', 'created_by' ]

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','created_on','updated_on','price','status', 'created_by',  ]

# ================================ Product =====================================#

class ProductListSerializer(serializers.ModelSerializer):
    created_by = CommonUserListSerializer()
    type= ProductTypeListSerializer()
    status = ProductStatusListSerializer()
    order = OrderListSerializer()
    tag =TagListSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id','name','description','created_on','updated_on','pic','type','status','tag', 'created_by', 'order','price' ]

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','description','created_on','updated_on','pic','type','status','tag', 'created_by' ,'price']
