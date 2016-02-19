from django.contrib import admin

from .models import Profile, Post, Notice, Document, Activity


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Notice)
admin.site.register(Document)
admin.site.register(Activity)
