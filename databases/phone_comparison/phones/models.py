from django.db import models


# Create your models here.
class Phone(models.Model):
    name = models.TextField()
    price = models.FloatField()
    os = models.TextField()
    screen_resolution = models.TextField()
    ram = models.FloatField()
    weight = models.FloatField()
    nfc = models.BooleanField()
    color = models.TextField()
    battery = models.FloatField()
    dual_camera = models.BooleanField()


class Apple(Phone):
    face_id = models.BooleanField()


class Samsung(Phone):
    borderless_screen = models.BooleanField()
