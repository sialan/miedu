from django.db import models
from accounts.models import Account
from campaigns.models import Campaign


# Create your models here.
class Transaction(models.Model):
    RELATIONSHIP_CHOICES = (
        ('UN', 'Unknown'),
        ('MM', 'Male-Male'),
        ('FF', 'Female-Female'),
        ('MF', 'Male-Female'),
        ('FM', 'Female-Male'),
    )
    account = models.ForeignKey('accounts.Account')
    campaign = models.ForeignKey('campaigns.Campaign')

    # todo add a project field
    active = models.BooleanField()
    completed = models.BooleanField()
    consummated = models.BooleanField()
    transaction_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    last_viewed = models.DateTimeField(auto_now=True)
    amount_supported = models.IntegerField(blank=True, null=True)
    relationship = models.CharField(max_length=2, default='UN', choices=RELATIONSHIP_CHOICES)