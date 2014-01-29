##########################################################################
# @Author : Rawan Nazmi-Issa Khozouz                                     #
# @Date : 18/09/13.                                                      #
# @Description : Admin                                                   #
##########################################################################

# Import objects
from django.contrib import admin
from tuerasmus.models import Users, UniErasmus, University, Universities, UserProfile, UsersUniversity, Countries, Comments

#--------------------------------------
#--------------------------------------
#      Objects editable by admin      #
#--------------------------------------
#--------------------------------------

# Signed users
admin.site.register(Users)
# Signed universities
admin.site.register(UniErasmus)
# University profile
admin.site.register(University)
# European universities
admin.site.register(Universities)
# User profile
admin.site.register(UserProfile)
# Users that belong to the university
admin.site.register(UsersUniversity)
# Universities's countries
admin.site.register(Countries)
# Comments 
admin.site.register(Comments)




#admin.site.register(Category)
#admin.site.register(Comment)
#admin.site.register(UniversityComment)
#admin.site.register(City)
#admin.site.register(Subjects)
#admin.site.register(UniversityInfo)
