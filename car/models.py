from django.db import models

# Create your models here.

class Car(models.Model):
    car_brand = models.CharField(max_length=30)
    year_production = models.IntegerField()
    price = models.IntegerField()
    color = models.CharField(max_length=25)


# class Customer(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     age = models.IntegerField()
#     phone = models.IntegerField(max_length=12)
#     email = models.EmailField(max_length=55)

#
#
# class Order(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     product_count = models.IntegerField()
#     price = models.IntegerField()
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    # order left join car where order.car.id = car.id
    # order left join customer where order.customer.id = customer.id
