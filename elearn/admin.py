from django.contrib import admin
from .models import *

admin.site.register([Class,FeeNotification,EventNotification,Books,Settings,FeedBack])
