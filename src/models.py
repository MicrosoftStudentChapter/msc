from __future__ import unicode_literals
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator


from PIL import Image
from io import StringIO, BytesIO
import os
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile

def validate_image(image):
    file_size = image.file.size
    limit_kb = 150
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit)

    #limit_mb = 8
    #if file_size > limit_mb * 1024 * 1024:
    #    raise ValidationError("Max size of file is %s MB" % limit_mb)


class Secretarie(models.Model):
    name = models.CharField(max_length=50)
    USER_TYPE_CHOICES=(('1st','GENERAL SECRETARY'),('2nd','FINANCIAL SECRETARY'),('3rd','JOINT SECRETARY'))
    post = models.CharField(max_length=50,choices=USER_TYPE_CHOICES,default='3rd')
    #Image = models.FileField(blank=True)
    Image = models.ImageField(upload_to="secretaries")
    def save(self):
		#Opening the uploaded image
        im = Image.open(self.Image)

        output = BytesIO()

		#Resize/modify the image
        im = im.resize( (250,250) )

		#after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

		#change the imagefield value to be the newley modifed image value
        self.Image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.Image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(Secretarie,self).save()


    fb_link=models.URLField(max_length=50, null=True,blank=True)
    git_link=models.URLField(max_length=50,null=True,blank=True)
    linkedin_link=models.URLField(max_length=50,null=True,blank=True)

class About_us(models.Model):
    #text=models.TextField(blank=True)
    Img=models.ImageField(upload_to="about-us",blank=True, null=True)
    def save(self):
		#Opening the uploaded image
        im = Image.open(self.Img)

        output = BytesIO()

		#Resize/modify the image
        im = im.resize( (600,375) )

		#after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

		#change the imagefield value to be the newley modifed image value
        self.Img = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.Img.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(About_us,self).save()
    #def __str__(self):
    #    return self.text+"-"+self.Img

class About_us_content(models.Model):
    content = models.TextField()
    display = models.BooleanField(default=False)


class Events(models.Model):
    logo=models.ImageField(upload_to="event-logo",blank=True, null=True)
    heading=models.CharField(max_length=30)
    description=models.TextField(blank=True)
    url=models.CharField(max_length=200, default='#')
    USER_TYPE_CHOICES=(('msweek','MS Week'),('inspirus','Inspirus'),('rumble','Rumble'))
    type=models.CharField(max_length=50,choices=USER_TYPE_CHOICES,default='msweek')


class MSWEEK_gallery(models.Model):
    caption=models.TextField(blank=True)
    Image=models.ImageField(upload_to="ms-week",blank=True,null=True)
    def save(self):
		#Opening the uploaded image
        im = Image.open(self.Image)

        output = BytesIO()

		#Resize/modify the image
        im = im.resize( (300,324) )

		#after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

		#change the imagefield value to be the newley modifed image value
        self.Image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.Image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(MSWEEK_gallery,self).save()

    timestamp=models.DateTimeField(auto_now=True)

class INSPIRUSUS_gallery(models.Model):
    caption=models.TextField(blank=True)
    Image=models.ImageField(upload_to="inspirus",blank=True,null=True)
    def save(self):
		#Opening the uploaded image
        im = Image.open(self.Image)

        output = BytesIO()

		#Resize/modify the image
        im = im.resize( (300,324) )

		#after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

		#change the imagefield value to be the newley modifed image value
        self.Image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.Image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(INSPIRUSUS_gallery,self).save()
    timestamp=models.DateTimeField(auto_now=True)

class RUMBLE_gallery(models.Model):
    caption=models.TextField(blank=True)
    Image=models.ImageField(upload_to="rumble",blank=True,null=True)
    def save(self):
		#Opening the uploaded image
        im = Image.open(self.Image)

        output = BytesIO()

		#Resize/modify the image
        im = im.resize( (300,324) )

		#after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

		#change the imagefield value to be the newley modifed image value
        self.Image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.Image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(RUMBLE_gallery,self).save()

    timestamp=models.DateTimeField(auto_now=True)

class index_gallery(models.Model):
    Image=models.ImageField(upload_to="gallery-index",blank=True,null=True)
    def save(self):
		#Opening the uploaded image
        im = Image.open(self.Image)

        output = BytesIO()

		#Resize/modify the image
        im = im.resize( (264,250) )

		#after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

		#change the imagefield value to be the newley modifed image value
        self.Image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.Image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(index_gallery,self).save()


class Team(models.Model):
    image=models.ImageField(upload_to="team",blank=True,null=True)
    def save(self):
		#Opening the uploaded image
        im = Image.open(self.image)

        output = BytesIO()

		#Resize/modify the image
        im = im.resize( (200,200) )

		#after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

		#change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(Team,self).save()

    name=models.CharField(max_length=50)
    USER_TYPE_CHOICES=(('1st','Technical'),('2nd','Event Strategy and Planning'),('3rd','Design and UX'),('4th','Marketing and Communications'))
    department=models.CharField(max_length=50,choices=USER_TYPE_CHOICES,default='4th')


class Post(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="post",blank=True,null=True)
    def save(self):
		#Opening the uploaded image
        im = Image.open(self.image)

        output = BytesIO()

		#Resize/modify the image
        im = im.resize( (260,240) )

		#after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

		#change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(Post,self).save()

    author = models.CharField(max_length=200,default=" ")
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
    content=models.TextField(null=True)
    source_link = models.CharField(max_length=200,blank=True)
    def get_absolute_url(self):
        return reverse('newsfeed-detail',kwargs={'pk': self.pk})

    def __str__(self):
        return (self.title)

    class Meta:
        ordering = ["-timestamp"]


class MSWeek_Event(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to="event-msweek",blank=True,null=True)
    register_link = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=False,auto_now_add=False)
    description = models.TextField(null=True)

class Inspirus_Event(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to="event-inpirus",blank=True,null=True)
    register_link = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=False,auto_now_add=False)
    description = models.TextField(null=True)

class Rumble_Event(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to="event-rumble",blank=True,null=True)
    register_link = models.CharField(max_length=200)
    date = models.DateField(auto_now=False,auto_now_add=False)
    time = models.CharField(max_length=15,blank=True,null=True)
    venue = models.CharField(max_length=80,blank=True,null=True)
    description = models.TextField(null=True)


class Heading_Content(models.Model):
    heading=models.CharField(max_length=100)
    content=models.TextField(max_length=600)



class Head_Team(models.Model):
    name = models.CharField(max_length=50)
    USER_TYPE_CHOICES=(('1st','Technical'),('2nd','Event Strategy and Planning'),('3rd','Design and UX'),('4th','Marketing and Communications'),('5th', 'Social and Web Management'))
    department = models.CharField(max_length=50,choices=USER_TYPE_CHOICES,default='4th')
    USER_TYPE_CHOICES_1=(('1st','HEAD'),('2nd','VICE-HEAD'))
    post = models.CharField(max_length=50,choices=USER_TYPE_CHOICES_1,default='2nd')
    Image = models.ImageField(upload_to="team-heads",blank=True,null=True)
    def save(self):
		#Opening the uploaded image
        im = Image.open(self.Image)

        output = BytesIO()

		#Resize/modify the image
        im = im.resize( (200,200) )

		#after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

		#change the imagefield value to be the newley modifed image value
        self.Image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.Image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(Head_Team,self).save()





class event_registration(models.Model):
    # title=models.CharField(max_length=200,default="Entries")
    name = models.CharField(max_length=200,blank=True)
    email = models.CharField(max_length=200,blank=True)
    contact = models.CharField(max_length=200,blank=True)
    year = models.CharField(max_length=200,blank=True)
    # USER_TYPE_CHOICES=(('1st','Tech Quiz'),('2nd','Django Workshop'),('3rd','Knockout Coding'),('4th','Hackerrank'),('5th','Mock ICPC'))
    # event=models.CharField(max_length=50,choices=USER_TYPE_CHOICES,default='4th')
    # a = models.BooleanField(default=False)
    # b = models.BooleanField(default=False)
    # c = models.BooleanField(default=False)
    # d = models.BooleanField(default=False)
    # e = models.BooleanField(default=False)

class registration(models.Model):
    # title=models.CharField(max_length=200,default="Entries")
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    roll_number = models.CharField(max_length=12)
    contact = models.CharField(max_length=200)
    year_choices = (
                ('1','First Year'),
                ('2', 'Second  Year'),
                ('3', 'Third Year'),
    )
    year = models.CharField(max_length=2)
    # USER_TYPE_CHOICES=(('1st','Tech Quiz'),('2nd','Django Workshop'),('3rd','Knockout Coding'),('4th','Hackerrank'),('5th','Mock ICPC'))
    # event=models.CharField(max_length=50,choices=USER_TYPE_CHOICES,default='4th')
    a = models.BooleanField(default=False)
    b = models.BooleanField(default=False)
    # c = models.BooleanField(default=False)
    # d = models.BooleanField(default=False)
    # e = models.BooleanField(default=False)

class contact_request(models.Model):
    contact_name = models.CharField(max_length=200,blank=True)
    contact_email = models.EmailField(max_length=200,blank=True)
    content = models.TextField(null = True)

class hkct_register(models.Model) :
    name = models.CharField(max_length=200,blank=True)
    email = models.CharField(max_length=200,blank=True)
    contact = models.CharField(max_length=200,blank=True)
    year = models.CharField(max_length=200,blank=True)
    # USER_TYPE_CHOICES=(('1st','Tech Quiz'),('2nd','Django Workshop'),('3rd','Knockout Coding'),('4th','Hackerrank'),('5th','Mock ICPC'))
    # event=models.CharField(max_length=50,choices=USER_TYPE_CHOICES,default='4th')
    a = models.BooleanField(default=False)
    b = models.BooleanField(default=False)
    c = models.BooleanField(default=False)
    d = models.BooleanField(default=False)
    e = models.BooleanField(default=False)
    f = models.BooleanField(default=False)

class hkct_ouside(models.Model):
    name = models.CharField(max_length=200,blank=True)
    email = models.CharField(max_length=200,blank=True)
    contact = models.CharField(max_length=200,blank=True)
    location = models.CharField(max_length=200,blank=True)
    institute = models.CharField(max_length=500,blank=True)
