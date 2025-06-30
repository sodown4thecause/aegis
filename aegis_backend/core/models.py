from django.db import models
from django.contrib.auth.models import AbstractUser

class Organization(models.Model):
    name = models.CharField(max_length=255)
    subscription_plan = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='users')
    ROLE_CHOICES = [
        ('owner', 'Owner'),
        ('employee', 'Employee'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')

class ComplianceFramework(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Control(models.Model):
    framework = models.ForeignKey(ComplianceFramework, on_delete=models.CASCADE, related_name='controls')
    identifier = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ('framework', 'identifier')

    def __str__(self):
        return f"{self.framework.name} - {self.identifier}"

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    controls = models.ManyToManyField(Control, related_name='tasks')

    def __str__(self):
        return self.name

class Policy(models.Model):
    policy_name = models.CharField(max_length=255)
    content_template = models.TextField()

    def __str__(self):
        return self.policy_name

class TrainingModule(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class UserTrainingStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='training_statuses')
    training_module = models.ForeignKey(TrainingModule, on_delete=models.CASCADE, related_name='user_statuses')
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ('user', 'training_module')

class PhishingCampaign(models.Model):
    name = models.CharField(max_length=255)
    template_used = models.ForeignKey(Policy, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateTimeField()

    def __str__(self):
        return self.name

class CampaignResult(models.Model):
    STATUS_CHOICES = [
        ('opened', 'Opened'),
        ('clicked', 'Clicked'),
        ('reported', 'Reported'),
        ('ignored', 'Ignored'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='campaign_results')
    campaign = models.ForeignKey(PhishingCampaign, on_delete=models.CASCADE, related_name='results')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('user', 'campaign')
