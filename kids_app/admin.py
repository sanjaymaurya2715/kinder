from django.contrib import admin

# Register your models here.
from . models import Parent,Feedback,Contact,Content,Notification

class Notification_Admin(admin.ModelAdmin):
    list_display=['title','message','date']



class Parent_Admin(admin.ModelAdmin):
    list_display=['name','email','phone','pic']



class Contact_Admin(admin.ModelAdmin):
    list_display=['name','email','phone','question','date']


class FeedBack_Admin(admin.ModelAdmin):
    list_display=['name','email','rating','review']

admin.site.register(Parent,Parent_Admin)
admin.site.register(Feedback,FeedBack_Admin)
admin.site.register(Content)
admin.site.register(Contact,Contact_Admin)
admin.site.register(Notification,Notification_Admin)

admin.site.site_header="Kinder App"
admin.site.site_tittle="Kids studies"
admin.site.index_tittle="The joy of learning"
