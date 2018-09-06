from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user       = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile     = models.CharField(max_length=8)
    pic        = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.mobile

class Tag(models.Model):
    name = models.CharField(max_length=225)

    class Meta:
        ordering = ['name',]

    def __str__(self):
        return self.name

class OrderSerialNo(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name
# ================================ Orders =======================#

class OrderStatus(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class OrderType(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class Order(models.Model):
    status          = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    created_by      = models.ForeignKey(User, on_delete=models.CASCADE,related_name="createdby")
    updated_by      = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updatedby")
    created_on      = models.DateTimeField(auto_now_add = True)
    updated_on      = models.DateTimeField(auto_now = True)
    price           = models.FloatField(default=0)

    def __str__(self):
        return str(self.id)

# ================================ Products =======================#
class ProductType(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class ProductStatus(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class Product(models.Model):
    name            = models.CharField(max_length=225)
    description     = models.TextField(null=True,blank=True)
    status          = models.ForeignKey(ProductStatus, on_delete=models.CASCADE)
    type            = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    tag             = models.ManyToManyField(Tag, blank=True)
    orderSerialNo   = models.ManyToManyField(OrderSerialNo, blank=True)
    price           = models.FloatField(default=0)
    created_by      = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on      = models.DateTimeField(auto_now_add = True)
    updated_on      = models.DateTimeField(auto_now = True)
    pic             = models.ImageField(blank=True, null=True)
    order           = models.ForeignKey(Order, on_delete=models.CASCADE, null=True,blank=True)
    quantity        = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# ================================ Products =======================#
