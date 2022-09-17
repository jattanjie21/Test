from django.db import models



class Slider(models.Model):
    heading_1       = models.CharField(max_length=255,verbose_name='Heading One')
    heading_2       = models.CharField(max_length=255,verbose_name='Heading Two')
    short_paragraph = models.TextField(verbose_name='Short Paragraph')


    class Meta:
        verbose_name_plural = 'Slider'

    def __str__(self):
        return self.heading_1


class WhatWeDo(models.Model):
    card_image = models.ImageField(upload_to='what_we_do',verbose_name='Card Image',height_field=260,width_field=360)
    card_title = models.CharField(max_length=255,verbose_name='Card Title')
    card_text  = models.TextField(verbose_name='Card Text')

    class Meta:
        verbose_name_plural = 'What We Do'

    def __str__(self):
        return self.card_title


class AboutUs(models.Model):
    youtube_link = models.URLField(verbose_name='Youtube Link')
    image_background = models.ImageField(upload_to='about_us',verbose_name='Image Background',height_field=562,width_field=602)

    class Meta:
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.youtube_link