from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class Users (models.Model):
#     # id = models.IntegerField()
#     user_name = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)

class Lists (models.Model):
    # id = models.IntegerField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Sessions (models.Model):
    # id = models.IntegerField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date_time = models.DateTimeField()
    data_volume = models.IntegerField()
    transmitted_data = models.IntegerField()
    transmitted_packets = models.IntegerField()
    packages_without_errors = models.IntegerField()
    packages_with_errors = models.IntegerField()
    lost_packages = models.IntegerField()
    average_speed = models.IntegerField()

class Frequencies (models.Model):
    # id = models.IntegerField()
    id_list = models.ForeignKey(Lists, on_delete=models.CASCADE)
    rating = models.IntegerField()
    isWork = models.BooleanField()
    isCall = models.BooleanField()

class Bands (models.Model):
    # id = models.IntegerField()
    bandwidth = models.IntegerField()
