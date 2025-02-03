from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # Linking user to the Django built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Basic user information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=False)
    birth_date = models.DateField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    # Medical Information
    blood_group = models.CharField(max_length=10, blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)
    current_medications = models.TextField(blank=True, null=True)
    chronic_conditions = models.TextField(blank=True, null=True)
    family_medical_history = models.TextField(blank=True, null=True)
    
    # Lifestyle Information
    PHYSICAL_ACTIVITY_CHOICES = [
        ('Sedentary', 'Sedentary'),
        ('Active', 'Active'),
        ('Very Active', 'Very Active'),
    ]
    physical_activity_level = models.CharField(max_length=50, choices=PHYSICAL_ACTIVITY_CHOICES, blank=True, null=True)
    diet_type = models.CharField(max_length=50, blank=True, null=True)
    sleep_pattern = models.CharField(max_length=50, blank=True, null=True)
    
    # Ayurvedic-specific information
    dosha_type = models.CharField(max_length=20, choices=[('Vata', 'Vata'), ('Pitta', 'Pitta'), ('Kapha', 'Kapha')], blank=True, null=True)
    prakriti = models.CharField(max_length=100, blank=True, null=True)
    
    # Health Status
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    bmi = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    pulse_rate = models.IntegerField(blank=True, null=True)
    
    # Date of last health checkup
    last_checkup_date = models.DateField(blank=True, null=True)
    
    # Optional: Profile picture for the user
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.user.username}"

    def save(self, *args, **kwargs):
        # Custom logic to calculate BMI
        if self.height and self.weight:
            self.bmi = self.weight / ((self.height / 100) ** 2)
        super(UserProfile, self).save(*args, **kwargs)
