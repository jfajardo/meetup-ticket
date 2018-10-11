import uuid
from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    check_in = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


