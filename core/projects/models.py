from django.db import models
from django.conf import settings
from stakeholders.models import Partner


class ProjectType(models.Model):
    project_type = models.CharField(max_length=200)
    description  = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.project_type

    class Meta:
        verbose_name_plural = "Project Type"

class Status(models.Model):
    status       = models.CharField(max_length=200)
    description  = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = "Status"

class Projects(models.Model):
    project_name        = models.CharField(max_length=255)
    project_type        = models.ForeignKey(ProjectType,on_delete=models.CASCADE,null=True,blank=True)
    project_budget      = models.FloatField()
    project_manager     = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    project_team        = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='users_project')
    project_stakeholder = models.ForeignKey(Partner,on_delete=models.CASCADE,related_name='project_partner')
    project_summary     = models.TextField(null=True,blank=True)
    staus               = models.ForeignKey(Status,on_delete=models.CASCADE,null=True,blank=True)
    project_start_date  = models.DateField()
    project_end_date    = models.DateField()

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name_plural = 'Projects'


class Deliverables(models.Model):
    project      = models.ForeignKey(Projects, on_delete=models.CASCADE)
    date         = models.DateField()
    todo         = models.CharField(max_length=255)
    completed    = models.BooleanField(default=False)
    delay_reason = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.todo

    class Meta:
        verbose_name_plural = 'Deliverables'
