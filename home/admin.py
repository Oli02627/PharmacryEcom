from django.contrib import admin
from .models import StaticPosts, SiteData, HomeSectionOne

# Register Static models
admin.site.register(StaticPosts)
# Register Site Data models
admin.site.register(SiteData)
# Register Site Data models
admin.site.register(HomeSectionOne)