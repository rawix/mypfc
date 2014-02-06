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
    day = models.DateField(auto_now=True);

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
#                               UniversityInfo class.
# ------------------------------------------------------------------------------
class Info(models.Model):
    uni = models.CharField(max_length=50);  

    nuser = models.IntegerField(default=0);
    ncomments = models.IntegerField(default=0);
    score = models.IntegerField(default=0);

    acronym = models.CharField(max_length=20, null=True, blank=True);
    address = models.CharField(max_length=50, null=True, blank=True);
    city = models.CharField(max_length=50, null=True, blank=True);
    country = models.CharField(max_length=50, null=True, blank=True);
    
    #MEter las coordenadas para GOOGLE MAPS!!!!!!!!!!!!!!!!!!!!!
    #location = models.URLField(null=True, blank=True);
    latitud = models.DecimalField(default=0, max_digits=10, decimal_places=8);
    longitud = models.DecimalField(default=0, max_digits=10, decimal_places=8);
    link = models.URLField(null=True, blank=True);
    image = models.URLField(null=True, blank=True);

    description = models.TextField(help_text='Escribe algo', null=True, blank=True);
    qualification = models.TextField(help_text='Escribe algo', null=True, blank=True);
    specialty = models.TextField(help_text='Escribe algo', null=True, blank=True);
    teachingequipment = models.TextField(help_text='Escribe algo', null=True, blank=True);

    librariy = models.TextField(help_text='Escribe algo', null=True, blank=True);
    lab = models.TextField(help_text='Escribe algo', null=True, blank=True);
    computerequipment = models.TextField(help_text='Escribe algo', null=True, blank=True);

    others = models.TextField(help_text='Escribe algo', null=True, blank=True);
    dinningroom = models.TextField(help_text='Escribe algo', null=True, blank=True);
    cafeteria = models.TextField(help_text='Escribe algo', null=True, blank=True);
    sportactivities = models.TextField(help_text='Escribe algo', null=True, blank=True);
    asociation = models.TextField(help_text='Escribe algo', null=True, blank=True);
    languagecourse = models.TextField(help_text='Escribe algo', null=True, blank=True);
    schoolyear = models.TextField(help_text='Escribe algo', null=True, blank=True);
    vacations = models.TextField(help_text='Escribe algo', null=True, blank=True);
    compteleco = models.TextField(help_text='Escribe algo', null=True, blank=True);

    teachers = models.TextField(help_text='Escribe algo', null=True, blank=True);
    teaching = models.TextField(help_text='Escribe algo', null=True, blank=True);
    studies = models.TextField(help_text='Escribe algo', null=True, blank=True);

    # CostumeService
    costume = models.TextField(help_text='Escribe algo', null=True, blank=True);
    meetings = models.TextField(help_text='Escribe algo', null=True, blank=True);
    offices = models.TextField(help_text='Escribe algo', null=True, blank=True);

    # Documentation
    unidoc = models.TextField(help_text='Escribe algo', null=True, blank=True);
    residencelicence = models.TextField(help_text='Escribe algo', null=True, blank=True);
    getresidence = models.TextField(help_text='Escribe algo', null=True, blank=True);
    economicaid = models.TextField(help_text='Escribe algo', null=True, blank=True);
    bankaccount = models.TextField(help_text='Escribe algo', null=True, blank=True);

    # Acommodation
    residencehall = models.TextField(help_text='Escribe algo', null=True, blank=True);
    flatshare = models.TextField(help_text='Escribe algo', null=True, blank=True);

    # Subjects
    subjects = models.TextField(help_text='Escribe algo', null=True, blank=True);

    #Work
    scholarships = models.TextField(help_text='Escribe algo', null=True, blank=True);
    practices = models.TextField(help_text='Escribe algo', null=True, blank=True);
    contact = models.TextField(help_text='Escribe algo', null=True, blank=True);

    # City
    general = models.TextField(help_text='Escribe algo', null=True, blank=True);
    prices = models.TextField(help_text='Escribe algo', null=True, blank=True);
    theuniversity = models.TextField(help_text='Escribe algo', null=True, blank=True);
    studentlife = models.TextField(help_text='Escribe algo', null=True, blank=True);
    turism = models.TextField(help_text='Escribe algo', null=True, blank=True);
    goingout = models.TextField(help_text='Escribe algo', null=True, blank=True);
    culture = models.TextField(help_text='Escribe algo', null=True, blank=True);
    crime = models.TextField(help_text='Escribe algo', null=True, blank=True);
    shopping = models.TextField(help_text='Escribe algo', null=True, blank=True);
    erasmuslife = models.TextField(help_text='Escribe algo', null=True, blank=True);
    more = models.TextField(help_text='Escribe algo', null=True, blank=True);

    # Others
    others = models.TextField(help_text='Escribe algo', null=True, blank=True);

    # Alphabetical Order  
    class Meta:
        verbose_name_plural = u'University'
        ordering = ['country', 'uni']

    def __unicode__(self):
        return self.uni; 

# ------------------------------------------------------------------------------
#                               Subjects class.
# ------------------------------------------------------------------------------
class Subjects(models.Model):
    subname = models.CharField(max_length=20);
    college = models.CharField(max_length=20);
    credits = models.IntegerField(max_length=20);

# ------------------------------------------------------------------------------
#                               University class.
# ------------------------------------------------------------------------------
class University(models.Model):
    uni = models.CharField(max_length=50);  
    # Scholarship: Erasmus or Mundus
    scholarship = models.CharField(max_length=10);

    # Alphabetical Order  
    class Meta:
        verbose_name_plural = u'University'
        ordering = ['uni']

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
    uni1 = models.CharField(max_length=30, null=True, blank=True);
    uni2 = models.CharField(max_length=30, null=True, blank=True);
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
class Comment(models.Model):
    username = models.CharField(max_length=30);
    comment = models.CharField(max_length=200);
    day = models.DateField();
    time = models.DateTimeField(auto_now=True);

    # Alphabetical Order  
    class Meta:
        verbose_name_plural = u'Comments'
        ordering = ['-time']

    def __unicode__(self):
        return str(self.day) + " - " + self.username;

# ------------------------------------------------------------------------------
#                               ResiComment class.
# ------------------------------------------------------------------------------

class ResiComment(models.Model):
    comment = models.TextField(help_text='Comenta sobre la universidad...', null=True, blank=True);
    username = models.CharField(max_length=30);
    day = models.DateField();
    time = models.DateTimeField(auto_now=True);

    # Alphabetical Order  
    class Meta:
        verbose_name_plural = u'ResiComment'
        ordering = ['-time']

    def __unicode__(self):
        return str(self.day) + " - " + self.username;

# ------------------------------------------------------------------------------
#                               Residences class.
# ------------------------------------------------------------------------------
class Residences(models.Model):
    resi = models.CharField(max_length=50);
    address = models.CharField(max_length=60);
    latitud = models.DecimalField(default=0, max_digits=6, decimal_places=4);
    longitud = models.DecimalField(default=0, max_digits=6, decimal_places=4);
    comments = models.ManyToManyField(ResiComment, null=True, blank=True);

    def __unicode__(self):
        return str(self.resi);

# ------------------------------------------------------------------------------
#                               UniversityComments class.
# ------------------------------------------------------------------------------

class UniComment(models.Model):
    uni = models.OneToOneField(University);
    users = models.ManyToManyField(User, null=True, blank=True);
    comments = models.ManyToManyField(Comment, null=True, blank=True);

    def __unicode__(self):
        return str(self.uni);

# ------------------------------------------------------------------------------
#                               City class.
# ------------------------------------------------------------------------------
class City(models.Model):
    name = models.CharField(max_length=20);
    description = models.TextField(help_text='Breve descripción de la ciudad');
    image = models.URLField();
    # Using Google Maps
    latitud = models.DecimalField(default=0, max_digits=6, decimal_places=4);
    longitud = models.DecimalField(default=0, max_digits=6, decimal_places=4);

    def __unicode__(self):
        return str(self.city);




