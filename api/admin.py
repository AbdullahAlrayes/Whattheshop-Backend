from django.contrib import admin
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

admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(OrderType)
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(ProductStatus)
admin.site.register(Tag)
admin.site.register(OrderSerialNo)
