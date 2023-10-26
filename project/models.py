
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import date

from django.db import models

# Model for project details
class Project(models.Model):
    PROJECT_REGION_CHOICES = [
        ('North', 'North'),
        ('East', 'East'),
        ('South', 'South'),
        ('West', 'West'),
    ]

    PROJECT_SUPPORT_WINDOW_CHOICES = [
        ('24/7', '24/7'),
        ('9:00 PM to 6:00 PM', '9:00 PM to 6:00 PM'),
        ('Custom', 'Custom'),
    ]

    PROJECT_PAYMENT_METHOD_CHOICES = [
        ('Monthly in Arrears', 'Monthly in Arrears'),
        ('Monthly in Advance', 'Monthly in Advance'),
        ('Quarterly in Arrears', 'Quarterly in Arrears'),
        ('Quarterly in Advance', 'Quarterly in Advance'),
        ('Custom', 'Custom'),
    ]

    project_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    region = models.CharField(max_length=10, choices=PROJECT_REGION_CHOICES)
    project_full_address = models.CharField(max_length=255)
    project_start_date = models.DateField()
    project_end_date = models.DateField()
    project_support_window = models.CharField(
        max_length=20,
        choices=PROJECT_SUPPORT_WINDOW_CHOICES
    )
    custom_support_window = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    project_value_inr = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(
        max_length=20,
        choices=PROJECT_PAYMENT_METHOD_CHOICES
    )

# Model for client details
class Client(models.Model):
    client_contact_name = models.CharField(max_length=255)
    client_contact_number = models.CharField(max_length=14)  # ISD code + Mobile number
    client_contact_email = models.EmailField()

# Model for project manager details
class ProjectManager(models.Model):
    project_manager_id = models.CharField(max_length=10)
    project_manager_title = models.CharField(max_length=255)
    project_manager_name = models.CharField(max_length=255)
    project_manager_email = models.EmailField()
    project_head_count = models.IntegerField()

# Model for engineer requirement details
class EngineerRequirement(models.Model):
    BAND_CHOICES = [
        ('G1', 'G1'),
        ('G2', 'G2'),
        ('G3', 'G3'),
        ('G4', 'G4'),
        ('G5', 'G5'),
        ('G6', 'G6'),
        ('G7', 'G7'),
        ('G8', 'G8'),
        ('G9', 'G9'),
        ('Intern', 'Intern'),
    ]

    band = models.CharField(max_length=10, choices=BAND_CHOICES)
    head_count = models.IntegerField(choices=[(i, str(i)) for i in range(1, 10)])
