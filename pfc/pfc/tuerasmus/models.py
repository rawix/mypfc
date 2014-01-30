#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

# ------------------------------------------------------------------------------
#                               Users class.
# ------------------------------------------------------------------------------
class Users(models.Model):
    username = models.OneToOneField(User);
    email = models.CharField(max_length=30);
    # Professor or student (the colour of the main page is different)
    type_user = models.CharField(max_length=1);
    day = models.DateField();


# ------------------------------------------------------------------------------
#                               Universities class.
# ------------------------------------------------------------------------------
class Universities(models.Model):
    # Name of the university
    noun = models.CharField(max_length=50);  
    country = models.CharField(max_length=50);

    # Alphabetical Order  
    class Meta:
        verbose_name_plural = u'Universities'
        ordering = ['country', 'noun']

    def __unicode__(self):
        return self.country + " - " + self.noun;


# ------------------------------------------------------------------------------
#                               Countries class.
# ------------------------------------------------------------------------------
class Countries(models.Model):
    country = models.CharField(max_length=50);

    # Alphabetical Order  
    class Meta:
        verbose_name_plural = u'Countries'
        ordering = ['country']

    def __unicode__(self):
        return self.country;


# ------------------------------------------------------------------------------
#                               University class.
# ------------------------------------------------------------------------------
class University(models.Model):
    uni = models.CharField(max_length=50);  
    # Scholarship: Erasmus or Mundus
    scholarship = models.CharField(max_length=10);
    acronym = models.CharField(max_length=20, null=True, blank=True);
    city = models.CharField(max_length=50);
    country = models.CharField(max_length=50);
    description = models.TextField(help_text='Escribe algo que describe esta universidad', null=True, blank=True);
    location = models.URLField();
    link = models.URLField();
    image = models.URLField(null=True, blank=True);
  
    # Alphabetical Order  
    class Meta:
        verbose_name_plural = u'University'
        ordering = ['country', 'uni']

    def __unicode__(self):
        return self.uni;  


# ------------------------------------------------------------------------------
#                               UniErasmus class.
# ------------------------------------------------------------------------------
class UniErasmus(models.Model):
    uni = models.CharField(max_length=50);
    # Scholarship: Erasmus
    scholarship = models.CharField(max_length=10);  

    # Alphabetical Order  
    class Meta:
        verbose_name_plural = u'UniErasmus'
        ordering = ['uni']

    def __unicode__(self):
        return self.uni;


# ------------------------------------------------------------------------------
#                               UserProfile class.
# ------------------------------------------------------------------------------
class UserProfile(models.Model):
    username = models.OneToOneField(User);
    name = models.CharField(max_length=30, null=True, blank=True);
    lastname = models.CharField(max_length=30, null=True, blank=True);
    description = models.TextField(help_text='Escribe tus pensamientos, frases', null=True, blank=True)
    n_university = models.IntegerField(default=0);
    # Image data is stored in the profiles folder, title: Image
    image = models.ImageField(upload_to='profiles', verbose_name='Image',blank=True, null=True)
    university = models.ManyToManyField(University, blank=True, null=True);
    # Scholarship Erasmus
    sserasmus = models.CharField(max_length=10, null=True, blank=True);
    # Scholarship Mundus
    ssmundus = models.CharField(max_length=10, null=True, blank=True);
     

# ------------------------------------------------------------------------------
#                               UserUniversity class.
# ------------------------------------------------------------------------------
class UsersUniversity(models.Model):
    uni = models.OneToOneField(University);
    nusers = models.IntegerField(default=0);
    useuni = models.ManyToManyField(User);



# ------------------------------------------------------------------------------
#                               Comments class.
# ------------------------------------------------------------------------------
class Comments(models.Model):
    username = models.CharField(max_length=30);
    comment = models.CharField(max_length=200);
    day = models.DateField();

    # Alphabetical Order  
    class Meta:
        verbose_name_plural = u'Comments'
        ordering = ['day']

    def __unicode__(self):
        return self.comment;








# ------------------------------------------------------------------------------
#                               Category class.
# ------------------------------------------------------------------------------
#class Category(models.Model):
    #cat = models.CharField(max_length=20);

    #def __unicode__(self):
        #return self.cat;


# ------------------------------------------------------------------------------
#                               Comment class.
# ------------------------------------------------------------------------------

#class Comment(models.Model):
    #comment = models.TextField(help_text='Comenta sobre la universidad...', null=True, blank=True);
    #categories = models.ManyToManyField(Category, null=True, blank=True);







# ------------------------------------------------------------------------------
#                               UniversityInfo class.
# ------------------------------------------------------------------------------

#class UniversityInfo(models.Model):
    #uni = models.OneToOneField(University);
    #nuser = models.IntegerField();
    #ncomments = models.IntegerField();
    #score = models.IntegerField();





# ------------------------------------------------------------------------------
#                               UniversityComments class.
# ------------------------------------------------------------------------------

#class UniversityComment(models.Model):
    #uni = models.OneToOneField(University);
    #users = models.ManyToManyField(User, null=True, blank=True);
    #comments = models.ManyToManyField(Comment, null=True, blank=True);


# ------------------------------------------------------------------------------
#                               City class.
# ------------------------------------------------------------------------------
#class City(models.Model):
    #name = models.CharField(max_length=20);
    #image = models.URLField();
    # Using Google Maps
    #goo = models.URLField();


# ------------------------------------------------------------------------------
#                               Subjects class.
# ------------------------------------------------------------------------------

#class Subjects(models.Model):
    #subname = models.CharField(max_length=20);
    #college = models.CharField(max_length=20);
    #credits = models.IntegerField(max_length=20);



