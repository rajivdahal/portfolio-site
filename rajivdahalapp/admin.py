from django.contrib import admin
from .models import Message
from .models import Post
from .models import Blog,Trendingpost,Mainpost


# Register your models here.
admin.site.register(Message)
admin.site.register(Post)
admin.site.register(Blog)
admin.site.register(Trendingpost)
admin.site.register(Mainpost)
