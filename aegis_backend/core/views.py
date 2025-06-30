from rest_framework import viewsets
from rest_framework import permissions
from .models import Organization, User, ComplianceFramework, Control, Task, Policy, TrainingModule, UserTrainingStatus, PhishingCampaign, CampaignResult
from .serializers import (
    OrganizationSerializer,
    UserSerializer,
    ComplianceFrameworkSerializer,
    ControlSerializer,
    TaskSerializer,
    PolicySerializer,
    TrainingModuleSerializer,
    UserTrainingStatusSerializer,
    PhishingCampaignSerializer,
    CampaignResultSerializer,
)

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ComplianceFrameworkViewSet(viewsets.ModelViewSet):
    queryset = ComplianceFramework.objects.all()
    serializer_class = ComplianceFrameworkSerializer
    permission_classes = [permissions.IsAuthenticated]

class ControlViewSet(viewsets.ModelViewSet):
    queryset = Control.objects.all()
    serializer_class = ControlSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class PolicyViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    permission_classes = [permissions.IsAuthenticated]

class TrainingModuleViewSet(viewsets.ModelViewSet):
    queryset = TrainingModule.objects.all()
    serializer_class = TrainingModuleSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserTrainingStatusViewSet(viewsets.ModelViewSet):
    queryset = UserTrainingStatus.objects.all()
    serializer_class = UserTrainingStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

class PhishingCampaignViewSet(viewsets.ModelViewSet):
    queryset = PhishingCampaign.objects.all()
    serializer_class = PhishingCampaignSerializer
    permission_classes = [permissions.IsAuthenticated]

class CampaignResultViewSet(viewsets.ModelViewSet):
    queryset = CampaignResult.objects.all()
    serializer_class = CampaignResultSerializer
    permission_classes = [permissions.IsAuthenticated]
