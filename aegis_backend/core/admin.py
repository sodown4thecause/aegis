from django.contrib import admin
from .models import (
    Organization,
    User,
    ComplianceFramework,
    Control,
    Task,
    Policy,
    TrainingModule,
    UserTrainingStatus,
    PhishingCampaign,
    CampaignResult,
)

admin.site.register(Organization)
admin.site.register(User)
admin.site.register(ComplianceFramework)
admin.site.register(Control)
admin.site.register(Task)
admin.site.register(Policy)
admin.site.register(TrainingModule)
admin.site.register(UserTrainingStatus)
admin.site.register(PhishingCampaign)
admin.site.register(CampaignResult)
