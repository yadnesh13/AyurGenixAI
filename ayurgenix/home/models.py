from django.db import models

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # Linking user to the Django built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Basic user information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    birth_date = models.DateField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    # Medical Information
    blood_group = models.CharField(max_length=10, blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)  # Any previous conditions, allergies, etc.
    current_medications = models.TextField(blank=True, null=True)  # Currently prescribed medications
    chronic_conditions = models.TextField(blank=True, null=True)  # Chronic conditions like diabetes, hypertension, etc.
    family_medical_history = models.TextField(blank=True, null=True)  # Family history of diseases
    
    # Lifestyle Information
    diet_type = models.CharField(max_length=50, blank=True, null=True)  # Vegetarian, Non-Vegetarian, Vegan, etc.
    physical_activity_level = models.CharField(max_length=50, blank=True, null=True)  # Sedentary, Active, Very Active
    sleep_pattern = models.CharField(max_length=50, blank=True, null=True)  # Hours of sleep per night
    
    # Ayurvedic-specific information
    dosha_type = models.CharField(max_length=20, choices=[('Vata', 'Vata'), ('Pitta', 'Pitta'), ('Kapha', 'Kapha')], blank=True, null=True)
    prakriti = models.CharField(max_length=100, blank=True, null=True)  # The user’s natural constitution according to Ayurveda
    
    # Health Status
    height = models.FloatField(blank=True, null=True)  # In cm
    weight = models.FloatField(blank=True, null=True)  # In kg
    bmi = models.FloatField(blank=True, null=True)  # BMI calculation can be added as a property
    temperature = models.FloatField(blank=True, null=True)  # Current body temperature
    pulse_rate = models.IntegerField(blank=True, null=True)  # Pulse rate in beats per minute
    
    # Date of last health checkup
    last_checkup_date = models.DateField(blank=True, null=True)
    
    # Optional: Profile picture for the user
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.user.username}"

    def save(self, *args, **kwargs):
        # You can add any custom logic here, such as calculating BMI or adding default values
        if self.height and self.weight:
            self.bmi = self.weight / ((self.height / 100) ** 2)
        super(UserProfile, self).save(*args, **kwargs)

# Create your models here.
