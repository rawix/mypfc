##########################################################################
# @Author : Rawan Nazmi-Issa Khozouz                                     #
# @Date : 18/09/13.                                                      #
# @Description : Admin                                                   #
##########################################################################

# Import objects
from django.contrib import admin
from tuerasmus.models import City, Cities, Comment, Countries, InfoBasic, InfoGeneral, InfoResidence, InfoStadistic, Others, Place, Resis, Score, Subjs, Subjects, Universities, University, UserProfile, Users, UsersUniversity

#--------------------------------------
#--------------------------------------
#      Objects editable by admin      #
#--------------------------------------
#--------------------------------------

# Comment
admin.site.register(Comment)

# Cities and countries
admin.site.register(City)
admin.site.register(Cities)
admin.site.register(Countries)

# Info
admin.site.register(InfoBasic)
admin.site.register(InfoGeneral)
admin.site.register(InfoResidence)
admin.site.register(InfoStadistic)
admin.site.register(Others)
admin.site.register(Place)
admin.site.register(Resis)
admin.site.register(Score)
admin.site.register(Subjs)
admin.site.register(Subjects)

# Universities
admin.site.register(Universities)
admin.site.register(University)

# Users
admin.site.register(Users)
admin.site.register(UserProfile)

# Users that belong to the university
admin.site.register(UsersUniversity)
