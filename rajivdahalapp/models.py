from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save # it is for slug generator: there are presave and post save : sluggenerator is used to geerate slug.
from rajivdahal.utils import unique_slug_generator

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Post(models.Model):
  
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    content=models.CharField(max_length=2000)
    image=models.ImageField(default='tt.jpg',blank=True,upload_to='postimage')
    date=models.DateField(default=timezone.now)
    slug=models.SlugField(max_length=200,blank=True,null=True)
    

    def __str__(self):
        return self.title    

# it generates slug for title:we create slugfield in models and in that inside slug will be generated 
# this function's 2 line says: if instance i.e object i.e slug is empty : place inside SLUG as slug            

def slug_generator(sender,instance,*args, **kwargs):
    if not instance.slug:
      #  instance.slug='SLUG'
      instance.slug=unique_slug_generator(instance)
      
#now we must call something : for every time we save the model in db this function must run so to run following steps are necessary 
# there are 2 methods : presave and postsave : presave is for adding slug to slugfield before saving the model's db: postsave is after saving 
# instance.slug="slug" : this is done when there is nothing : but after calling utils.py instance.slug=unique_slug_generator(instance) : this is performed
# calling of presave and post save is done above in import section
pre_save.connect(slug_generator,sender=Post)# this connect slug_generator and Post class
# if we go to  admin section and watch there is slugfield and before saving SLUG will be there : which is done by this function
      
class Blog(models.Model):
    title = models.CharField(max_length=500)
    content=models.CharField(max_length=2000)
    image=models.ImageField(default='tt.jpg',blank=True,upload_to='postimage')
    date=models.DateField(default=timezone.now)
    
    slug=models.SlugField(max_length=200,blank=True,null=True)
    

    def __str__(self):
        return self.title

def slug_generator(sender,instance,*args, **kwargs):
    if not instance.slug:
      #  instance.slug='SLUG'
      instance.slug=unique_slug_generator(instance)     

pre_save.connect(slug_generator,sender=Blog)         


class Trendingpost(models.Model):
  
    title = models.CharField(max_length=200)
    category=models.CharField(max_length=200,verbose_name="eg. like iphone or android or macbook or dslr")
    image=models.ImageField(default='',blank=True,upload_to='postimage')
    date=models.DateField(default=timezone.now)
    content=models.CharField(max_length=20000)
    description=models.CharField(max_length=2000)
    slug=models.SlugField(max_length=300,blank=True,null=True)
    

    def __str__(self):
        return self.title    

def slug_generator(sender,instance,*args, **kwargs):
    if not instance.slug:
      #  instance.slug='SLUG'
      instance.slug=unique_slug_generator(instance)     

pre_save.connect(slug_generator,sender=Trendingpost)  

class Mainpost(models.Model):
  
    main_title = models.CharField(max_length=200,verbose_name="insert main title to show on left side",default='')
    main_image=models.ImageField(default='yy.jpg',blank=True,upload_to='postimage',verbose_name="insert main image to show on left side")
    date=models.DateField(default=timezone.now)
    main_content=models.CharField(max_length=20000,verbose_name="insert main content to show on left side",default='')
    main_description=models.CharField(max_length=2000,verbose_name="insert main description to show on left side",default='')
    right_up_title = models.CharField(max_length=200,verbose_name="insert secondary1 title to show on right up side",default='')
    right_up_image=models.ImageField(default='jj.jpg',blank=True,upload_to='postimage',verbose_name="insert secondary1 image to show on right up side")
    right_up_content=models.CharField(max_length=1000,verbose_name="insert secondary1 content to show on right up side-max:word 1000",default='')
    right_up_description=models.CharField(max_length=500,verbose_name="insert secondary1 description to show on right up side:max:word 500",default='')
    right_down_title = models.CharField(max_length=200,verbose_name="insert secondary2 title to show on right down side",default='')
    right_down_image=models.ImageField(default='pp.jpg',blank=True,upload_to='postimage',verbose_name="insert secondary2 image to show on right down side")
    right_down_content=models.CharField(max_length=1000,verbose_name="insert secondary2 content to show on right down side -max:word 1000",default='')
    right_down_description=models.CharField(max_length=500,verbose_name="insert secondary2 description to show on right down side -max:word 500",default='')

    def __str__(self):
        return self.main_title




      

