from django.db import models
from django.contrib.auth.models import User

class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professional_profile')
    specialty = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.specialty}"

class Reservation(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name='appointments')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, default='pending')  # pending, confirmed, canceled

    def __str__(self):
        return f"Reservation by {self.client.username} with {self.professional.user.username}"

