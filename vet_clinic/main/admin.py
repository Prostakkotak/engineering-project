from django.contrib import admin
from .models import *

admin.site.register(Doctor)
admin.site.register(Service)
admin.site.register(Review)
admin.site.register(DoctorReview)
admin.site.register(ServiceReview)
admin.site.register(Contact)