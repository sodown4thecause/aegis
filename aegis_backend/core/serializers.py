from rest_framework import serializers
from .models import Organization, User, ComplianceFramework, Control, Task, Policy, TrainingModule, UserTrainingStatus, PhishingCampaign, CampaignResult

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ComplianceFrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplianceFramework
        fields = '__all__'

class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'

class TrainingModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingModule
        fields = '__all__'

class UserTrainingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTrainingStatus
        fields = '__all__'

class PhishingCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhishingCampaign
        fields = '__all__'

class CampaignResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignResult
        fields = '__all__'
