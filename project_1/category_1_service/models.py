from django.db import models

class AWB(models.Model):
    awb_id = models.CharField(max_length=100, unique=True)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    flight_no = models.CharField(max_length=100)
    flight_date = models.DateField()
    pieces = models.IntegerField()
    weight = models.FloatField()
    volume = models.FloatField()
    goods_approved = models.BooleanField(default=False)
    manifest = models.CharField(max_length=255, blank=True, null=True)
    execute_status = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"AWB {self.awb_id}"
