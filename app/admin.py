from django.contrib import admin
#管理画面でデータを登録できるようにする
from .models import Profile, Work, Experience, Education, Software, Technical

admin.site.register(Profile)
admin.site.register(Work)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Software)
admin.site.register(Technical)