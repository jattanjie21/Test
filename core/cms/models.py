from django.db import models


class Contact(models.Model):
    header_title     = models.CharField(max_length=100,default='Get in touch')
    paragraph        = models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quisquam, quod.')
    address_one      = models.CharField(max_length=100)
    address_two      = models.CharField(max_length=100)
    phone_1          = models.IntegerField()
    phone_2          = models.IntegerField(null=True,blank=True)
    email            = models.EmailField()
    email_2          = models.EmailField(null=True,blank=True)
    telephone_line_1 = models.IntegerField()
    telephone_line_2 = models.IntegerField(null=True,blank=True)
    map_url          = models.URLField()


    def __str__(self):
        return self.address_one

    class Meta:
        verbose_name_plural = "Contact"


class Footer(models.Model):
    footer_summary = models.TextField(default='lorem ipsum nakalas')

    def __str__(self):
        return self.footer_summary


class Faqs(models.Model):
    question_asked  = models.CharField(max_length=255,verbose_name='Question Asked')
    question_answer = models.TextField()

    def __str__(self):
        return self.question_asked

    class Meta:
        verbose_name_plural = 'Faqs'


class Careers(models.Model):
    job_title       = models.CharField(max_length=200, verbose_name='Job Title')
    job_description = models.TextField(verbose_name='Job Description')
    job_location    = models.CharField(max_length=100,default='Gambia',verbose_name='Job Location')

    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name_plural = 'Careers'


class Testimonials(models.Model):
    testimonial_paragraph     = models.TextField()
    testimonial_by            = models.CharField(max_length=200)
    testimonial_by_profession = models.CharField(max_length=200)

    def __str__(self):
        return self.testimonial_by

    class Meta:
        verbose_name_plural = 'Testimonials'


class Team(models.Model):
    GENDER = [
        ('Male','Male'),
        ('Female','Female'),
    ]

    name    = models.CharField(max_length=255)
    gender  = models.CharField(max_length=10,choices=GENDER)
    role    = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='team/', height_field=650, width_field=650,null=True,blank=True)

    linkedin = models.URLField(null=True,blank=True)
    twitter  = models.URLField(null=True,blank=True)
    facebook = models.URLField(null=True,blank=True)
    google   = models.URLField(null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Team'

    def __str__(self):
        return self.name
