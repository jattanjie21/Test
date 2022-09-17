from django.db import models
from utilities.models import Social_Links


class Partner(Social_Links):

    STAKEHOLDER_TYPE = [
        ('Donor', 'Donor'),
        ('Organization', 'Organization'),
        ('Institutional Partner', 'Institutional Partner'),
    ]

    name                = models.CharField(max_length=255, unique=True)
    type_of_stakeholder = models.CharField(max_length=255, choices=STAKEHOLDER_TYPE, default='Donor', verbose_name='Type of Stakeholder')
    description         = models.TextField(blank=True)
    website             = models.URLField(blank=True,null=True)
    telephone           = models.CharField(max_length=255, blank=True)
    email               = models.EmailField(unique=True)
    address             = models.CharField(max_length=255)
    country             = models.CharField(max_length=255)
    logo                = models.ImageField(upload_to="partners", blank=True,null=True)
    active              = models.BooleanField(default=True)

    # get all active partners
    @staticmethod
    def get_all_partners():
        return Partner.objects.filter(is_active=True)

    # get all partners and sort them by name
    @staticmethod
    def get_all_partners_by_name():
        return Partner.objects.all().order_by("name")

    # get all partners logos
    @staticmethod
    def get_all_partners_logos():
        return Partner.objects.filter(logo__isnull=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering            = ["name"]
        verbose_name_plural = "Partners"