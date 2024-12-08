from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tenure = models.PositiveIntegerField()
    approved = models.BooleanField(default=False)
    applied_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Loan #{self.id} - {self.user.username}"



class LoanApplication(models.Model):
    FULL_NAME_CHOICES = [
        ('Mr.', 'Mr.'),
        ('Ms.', 'Ms.'),
        ('Mrs.', 'Mrs.'),
        ('Dr.', 'Dr.'),
    ]

    title = models.CharField(max_length=10, choices=FULL_NAME_CHOICES)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    loan_purpose = models.TextField()
    address = models.TextField()
    employment_status = models.CharField(max_length=50)
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} {self.full_name} - {self.loan_amount} Application"
