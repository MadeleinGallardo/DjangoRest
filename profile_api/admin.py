from django.contrib import admin 
#digo que modelos aparecen en el admin
from profile_api import models


admin.site.register(models.UserProfile)



