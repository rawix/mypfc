#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

# ------------------------------------------------------------------------------
#                               Users class.
# ------------------------------------------------------------------------------
class Users(models.Model):
    username = models.OneToOneField(User, unique=True);
    email = models.CharField(max_length=30);
    # Professor or student
    type_user = models.CharField(max_length=1);
    # Sign up day
    day = models.DateField(auto_now=False);
        
    def __str__(self):
        return str(self.username);
        
# ------------------------------------------------------------------------------
#                               Universities class.
# ------------------------------------------------------------------------------
class Universities(models.Model):
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
#                               Comment class.
# ------------------------------------------------------------------------------
class Comment(models.Model):
    username = models.CharField(max_length=30);
    title = models.CharField(max_length=30);
    text = models.TextField(help_text="Comenta lo que opinas");
    # Image data is stored in the city folder, title=comment title: 
    image = models.ImageField(upload_to='city', verbose_name=u'title' , blank=True, null=True)
    # Publication day
    day_publicated = models.DateField();
    time = models.DateTimeField(auto_now=True);

    # Alphabetical Order  
    class Meta:
        verbose_name_plural = u'Comment'
        ordering = ['-time']

    def __unicode__(self):
        return str(self.day) + " - " + self.username + ": " + self.title;
        
# ------------------------------------------------------------------------------
#                               University class.
# ------------------------------------------------------------------------------
class University(models.Model):
    uni = models.CharField(max_length=50);  
    # Scholarship: Erasmus or Mundus
    scholarship = models.CharField(max_length=10);

    # Alphabetical Order  
    class Meta:
        ordering = ['uni']
        
    def __unicode__(self):
        return self.uni;

# ------------------------------------------------------------------------------
#                               Score class.
# ------------------------------------------------------------------------------
class Score(models.Model):
    excellent = models.IntegerField(default=5);
    verygood = models.IntegerField(default=4);
    good = models.IntegerField(default=3);
    notbad = models.IntegerField(default=2);
    bad = models.IntegerField(default=1);

# ------------------------------------------------------------------------------
#                               Place class.
# ------------------------------------------------------------------------------
class Place(models.Model):
    name= models.CharField(max_length=40);
    image = models.URLField(null=True, blank=True);
    # Using Google Maps
    address = models.CharField(max_length=40);
    latitud = models.DecimalField(default=0, max_digits=6, decimal_places=4);
    longitud = models.DecimalField(default=0, max_digits=6, decimal_places=4);
    comment = models.ForeignKey(Comment, null=True, blank=True);
    score = models.ForeignKey(Score, null=True, blank=True);
    
    # Alphabetical Order  
    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name;

# ------------------------------------------------------------------------------
#                               InfoBasic class.
# ------------------------------------------------------------------------------
class InfoBasic(models.Model):
    # Basic
    uni = models.CharField(max_length=50);
    address = models.CharField(max_length=50);
    city = models.CharField(max_length=30);
    country = models.CharField(max_length=50);
    latitud = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True);
    longitud = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True);
    description = models.TextField(help_text='Cómo describirías esta universidad');
    link = models.URLField();
    image = models.URLField();
    comment = models.ForeignKey(Comment, null=True, blank=True);
    score = models.ForeignKey(Score, null=True, blank=True);

    # Alphabetical Order  
    class Meta:
        verbose_name_plural = u'Basic'
        ordering = ['uni']
 
    def __str__(self):
        return self.uni
        
# ------------------------------------------------------------------------------
#                               InfoStadistic class.
# ------------------------------------------------------------------------------
class InfoStadistic(models.Model):
    # Stadistics
    uni = models.CharField(max_length=50);
    nuser = models.IntegerField(default=0);
    ncomments = models.IntegerField(default=0);
    score = models.ForeignKey(Score, null=True, blank=True);
    
    # Alphabetical Order  
    class Meta:
        verbose_name_plural = u'Stadistics'
        ordering = ['uni']
        
    def __unicode__(self):
        return self.uni; 


# ------------------------------------------------------------------------------
#                               Subjects class.
# ------------------------------------------------------------------------------
class Subjects(models.Model):
    subname = models.CharField(max_length=20);
    uni = models.ForeignKey(University);
    credits = models.IntegerField(default=0);
    subnameout = models.CharField(max_length=40);
    comment = models.ForeignKey(Comment, null=True, blank=True);
    score = models.ForeignKey(Score, null=True, blank=True);
    
    # Alphabetical Order  
    class Meta:
        ordering = ['subname']
        
    def __unicode__(self):
        return self.uni;
        
# ------------------------------------------------------------------------------
#                               InfoGeneral class.
# ------------------------------------------------------------------------------
class InfoGeneral(models.Model):
    # Documentation
    uni = models.CharField(max_length=50);
    qualification = models.TextField(help_text='Escribe algo');
    specialty = models.TextField(help_text='Escribe algo');
    teachingequipment = models.TextField(help_text='Escribe algo');

    librariy = models.TextField(help_text='Escribe algo');
    lab = models.TextField(help_text='Escribe algo');
    computerequipment = models.TextField(help_text='Escribe algo');

    others = models.TextField(help_text='Escribe algo');
    dinningroom = models.TextField(help_text='Escribe algo');
    cafeteria = models.TextField(help_text='Escribe algo');
    sportactivities = models.TextField(help_text='Escribe algo');
    asociation = models.TextField(help_text='Escribe algo');
    languagecourse = models.TextField(help_text='Escribe algo');
    schoolyear = models.TextField(help_text='Escribe algo');
    vacations = models.TextField(help_text='Escribe algo');
    compteleco = models.TextField(help_text='Escribe algo');

    teachers = models.TextField(help_text='Escribe algo');
    teaching = models.TextField(help_text='Escribe algo');
    studies = models.TextField(help_text='Escribe algo');

    # CostumeService
    costume = models.TextField(help_text='Escribe algo');
    meetings = models.TextField(help_text='Escribe algo');
    offices = models.TextField(help_text='Escribe algo');

    # Documentation
    unidoc = models.TextField(help_text='Escribe algo');
    residencelicence = models.TextField(help_text='Escribe algo');
    getresidence = models.TextField(help_text='Escribe algo');
    economicaid = models.TextField(help_text='Escribe algo');
    bankaccount = models.TextField(help_text='Escribe algo');
    
    #Subjects
    subject = models.ForeignKey(Subjects, null=True, blank=True);
    
    #Work
    scholarships = models.TextField(help_text='Escribe algo', null=True, blank=True);
    practices = models.TextField(help_text='Escribe algo', null=True, blank=True);
    contact = models.TextField(help_text='Escribe algo', null=True, blank=True);
    
    # Comments    
    comment = models.ForeignKey(Comment, null=True, blank=True);
    score = models.ForeignKey(Score, null=True, blank=True);

    # Alphabetical Order  
    class Meta:
        verbose_name_plural = u'General'
        ordering = ['uni']
        
    def __unicode__(self):
        return self.uni; 

# ------------------------------------------------------------------------------
#                               Residence class.
# ------------------------------------------------------------------------------
class InfoResidence(models.Model):
    uni = models.CharField(max_length=40);
    residence = models.ForeignKey(Place);
    flatshare = models.TextField(help_text='Dónde poder buscar pisos', null=True, blank=True);
    linktoshare = models.TextField(help_text='Link', null=True, blank=True);
    # Comments    
    comment = models.ForeignKey(Comment, null=True, blank=True);
    score = models.ForeignKey(Score, null=True, blank=True);

    # Alphabetical Order  
    class Meta:
        verbose_name_plural = u'Residence'
        ordering = ['uni']
        
    def __unicode__(self):
        return self.uni; 

# ------------------------------------------------------------------------------
#                               UserProfile class.
# ------------------------------------------------------------------------------
class UserProfile(models.Model):
    username = models.OneToOneField(User);
    name = models.CharField(max_length=30);
    lastname = models.CharField(max_length=30);
    description = models.TextField(help_text='Escribe tus pensamientos, frases');
    n_university = models.IntegerField(default=0);
    # Image data is stored in the profiles folder, title: Image
    image = models.ImageField(upload_to='profiles', verbose_name=u'image_profile', blank=True, null=True);
    uni1 = models.CharField(max_length=30, null=True, blank=True);
    uni2 = models.CharField(max_length=30, null=True, blank=True);
    university = models.ForeignKey(University, null=True, blank=True);
    # Scholarship Erasmus
    sserasmus = models.CharField(max_length=10, null=True, blank=True);
    # Scholarship Mundus
    ssmundus = models.CharField(max_length=10, null=True, blank=True);
     
# ------------------------------------------------------------------------------
#                               UsersUniversity class.
# ------------------------------------------------------------------------------
class UsersUniversity(models.Model):
    uni = models.CharField(max_length=50);
    nusers = models.IntegerField(default=0);
    useuni = models.ManyToManyField(User);
    
    # Alphabetical Order  
    class Meta:
        ordering = ['uni']
        
    def __unicode__(self):
        return self.uni;
             
# ------------------------------------------------------------------------------
#                               City class.
# ------------------------------------------------------------------------------
class City(models.Model):
    cityname = models.CharField(max_length=50);
    prices = models.TextField();
    uniarea = models.TextField();
    studentlife = models.TextField();
    turism = models.TextField();
    party = models.TextField();
    culture = models.TextField();
    crime = models.TextField();
    shopping = models.TextField();
    erasmuslife = models.TextField();
    more = models.TextField();
        
    # Alphabetical Order  
    class Meta:
        ordering = ['cityname']

 





