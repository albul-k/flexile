from django.db import models


class Profile(models.Model):
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    birthdate = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now_add=True)
    role = models.ForeignKey(
        'Role',
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return self.first_name

class Role(models.Model):
    role_name = models.CharField(
        max_length=100,
        unique=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)