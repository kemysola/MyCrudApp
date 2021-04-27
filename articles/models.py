from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.timezone  import now
from datetime import datetime
from django.utils import timezone



# Create your models here.
class Article(models.Model):
    '''
    date,author,address,slug,thubmnail
    '''
    title = models.CharField(max_length=500) 
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    
    def snippet(self):
        return self.body[:100] + ' ...'
    
    
    
class Comment(models.Model):
    post =models.ForeignKey(Article,on_delete=models.CASCADE,related_name ='comments')
    name = models.CharField(max_length=200)
    #email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(blank=True,null=True,help_text=('keep empty for activation'))
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering =['created_on']
        #abstract = False
        
        
    def __str__(self):
            return 'Comment {} by {} '.format ( self.body, self.name)
    