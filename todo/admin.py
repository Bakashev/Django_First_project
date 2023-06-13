import textwrap

from django.contrib import admin
from .models import Post, Comments

# Register your models here.
@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['short_title', 'created', 'user', 'comments_count', 'comments']
    search_fields = ["title"]
    list_filter = ['user__username']
    list_per_page = 10
    date_hierarchy = 'created'
    list_select_related = ['user']


    @admin.display(description='Заголовок')
    def short_title(self, obj: Post) -> str:
        size = 5
        if len(obj.title) <= size:
            return obj.title
        else:
            return textwrap.wrap(obj.title, size)[0] + '.....'
    @admin.display(description='Кол_во комментариев')
    def comments_count(self, obj: Post):
        #return obj.comments_count
        return obj.comments.all().count()


    @admin.display(description='Наличие комментариев', boolean=True)
    def comments(self, obj: Post):
        if obj.comments.all().count():
            return True
        else:
            return False


@admin.register(Comments)
class AdminComments(admin.ModelAdmin):
    list_display = ["post", "username", "useremail", "conten", "created" ]
