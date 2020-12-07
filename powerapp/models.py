from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import validate_image_file_extension, validate_email
from django.contrib.auth.models import User
# Create your models here.

class Gallery(models.Model):
    Image = models.ImageField(upload_to='gallery_images', blank=True, null=True,
     validators = [validate_image_file_extension], help_text="If you have added a video, do not add this, else only the image will be shown", verbose_name='Add an image attachment')
    short_description=models.CharField(max_length=100)
    upload_date = models.DateTimeField( auto_now_add=True)
    added_by = models.ForeignKey(User, related_name="Added_by", on_delete=models.CASCADE)
    is_published = models.BooleanField(default =False, help_text="This will enable you to publish your post when you want to")

    def __str__(self):
        return self.short_description

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

    def __unicode__(self):
        return u'%s' %self.short_description


class About(models.Model):
    AppName = models.CharField(max_length=255, blank=True)
    who_we_are = RichTextField(blank = True, verbose_name ="Anything here will be shown as the new 'Who we are section on the website'", help_text='Image content is not allowed here', config_name="my-custom-toolbar")
    what_we_do = RichTextField(blank = True, verbose_name ="Anything here will be shown as the new 'What we do section on the website'", help_text='Image content is not allowed here', config_name="my-custom-toolbar")
    Where_we_are = models.CharField(blank = True, max_length=100, verbose_name ="Your address to be shown in the footer")
    our_official_phone = models.CharField(max_length = 14, blank = True, help_text ="If provided, this will be shown in the footer as an email")
    our_official_email = models.CharField(max_length =50, blank = True, help_text = "Also if provided, it will be shown in the footer as the phone number, please include the Country code")
    goals = RichTextField(blank = True, verbose_name ="Anything here will be shown as the new 'goals/objectives'", help_text='Image content is not allowed here', config_name="my-custom-toolbar")
    vision = RichTextField(blank = True, verbose_name ="Anything here will be shown as the vision on the 'vision section on the website'", help_text='Image content is not allowed here', config_name="my-custom-toolbar")
    Summary_Of_About_Us_to_show_in_footer = models.CharField(max_length=255)

    Use_New_App_Name = models.BooleanField(default=False)
    Use_New_Who_We_Are= models.BooleanField(default=False)
    Use_New_What_We_Do = models.BooleanField(default=False)
    Use_New_Where_We_Are = models.BooleanField(default=False)
    Use_New_Goals = models.BooleanField(default=False)
    Use_New_Vision = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'About the site'
        verbose_name_plural = 'About the site'

    def __str__(self):
        return self.AppName

    def __unicode__(self):
        return u'%s' %self.AppName


class Candidate(models.Model):
    full_name = models.CharField(max_length=255)
    post = models.CharField(max_length=255)
    area = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    email = models.EmailField(blank=True, null=True)
    short_bio = models.CharField(max_length=255)
    profile = RichTextField(config_name="my-custom-toolbar")
    added_by = models.ForeignKey(User, related_name="Registered_by", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='candidates', validators = [validate_image_file_extension])
    is_published = models.BooleanField(default =False)
    upload_date = models.DateTimeField( auto_now_add=True)

    class Meta:
        verbose_name = 'NRM candidate'
        verbose_name_plural = 'NRM candidates'

    def __str__(self):
        return self.full_name

    def __unicode__(self):
        return u'%s' %self.full_name

class AboutTheParty(models.Model):
    vision =  RichTextField(blank = True, verbose_name ="Vision of the party", help_text='Image content is not allowed here', config_name="my-custom-toolbar")
    mission =  RichTextField(blank = True, verbose_name ="The mission of the party", help_text='Image content is not allowed here', config_name="my-custom-toolbar")
    Goals =  RichTextField(blank = True, verbose_name ="The goalsof the party", help_text='Image content is not allowed here', config_name="my-custom-toolbar")
    background =  RichTextField(blank = True, verbose_name ="How the party came into existence", help_text='Image content is not allowed here', config_name="my-custom-toolbar")
    Use_New_About_The_Party = models.BooleanField(default = False)
    why_nrm = RichTextField(config_name='my-custom-toolbar')

    class Meta:
        verbose_name = 'About the party'
        verbose_name_plural = 'About the party'

    def __str__(self):
        return self.vision

    # def __unicode__(self):
    #     return u'%s' %self.full_name

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    Image = models.ImageField(upload_to='blog_posts_images', blank=True, null=True,
     validators = [validate_image_file_extension], help_text="If you have added a video, do not add this, else only the image will be shown", verbose_name='Add an image attachment')
    Video = models.FileField(blank=True, null = True, help_text = 'If you have added an image, do not add this, else only the image will be shown')
    upload_date = models.DateTimeField( auto_now_add=True)
    added_by = models.ForeignKey(User, related_name="Uploaded_by", on_delete=models.CASCADE)
    is_published = models.BooleanField(default =False, help_text="This will enable you to publish your post when you want to")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'

    def __unicode__(self):
        return u'%s' %self.title

class Prospective(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    Image = models.ImageField(upload_to='blog_posts_images', blank=True, null=True,
     validators = [validate_image_file_extension], help_text="If you have added a video, do not add this, else only the image will be shown", verbose_name='Add an image attachment')
    Video = models.FileField(blank=True, null = True, help_text = 'If you have added an image, do not add this, else only the image will be shown')
    upload_date = models.DateTimeField( auto_now_add=True)
    added_by = models.ForeignKey(User, related_name="Was_uploaded_by", on_delete=models.CASCADE)
    is_published = models.BooleanField(default =False, help_text="This will enable you to publish your post when you want to")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Prospective'
        verbose_name_plural = 'Prospectives'

    def __unicode__(self):
        return u'%s' %self.title

class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    post_body =RichTextField(verbose_name ="Body of the blog", help_text='Image content is not allowed here', config_name="my-custom-toolbar")
    Image = models.ImageField(upload_to='blog_files', blank=True, null=True,
     validators = [validate_image_file_extension], help_text="If you have added a video, do not add this, else only the image will be shown", verbose_name='Add an image attachment')
    Video = models.FileField(upload_to='blog_files', blank=True, null = True, help_text = 'If you have added an image, do not add this, else only the image will be shown')
    upload_date = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, related_name="Posted_by", on_delete=models.CASCADE)
    is_published = models.BooleanField(default =False, help_text="This will enable you to publish your post when you want to")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __unicode__(self):
        return u'%s' %self.title
