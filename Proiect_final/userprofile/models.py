from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class UserExtend(User):

    location = models.ForeignKey('ap1.Reteta', on_delete=models.CASCADE, null=True)