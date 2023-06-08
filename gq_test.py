import datetime
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard.settings')
django.setup()

from django.db.models import Count, Max
from todo.models import Post, Comments
from user.models import User

# qs = Post.objects.all()
# us= User.objects.all()
# print(qs.values('title', 'user'))
# user_one = User.objects.get(id=1)
# print(user_one.posts.all().count())
#--------------------------------------------------------------
# user_qs = Post.objects.all().annotate(Count('user_id'))
# user_qs = User.objects.all().select_related('')
# user_qs = User.objects.all().prefetch_related('posts').annotate(Count('posts'))


# Добавить пункт меню "Пользователи", где будет перечень пользователей 👥, отсортированный по убыванию
# 📉 кол-ва созданных ими записей 🗒 (не выводить, у кого нет записей), а также datetime🕘 последней публикации.
# (Подсказка: Max можно применять на типе datetime)

#Перечень пользователей по убыванию количества постов
qs_post = Post.objects.all().select_related('user')\
                            .values('user__username', 'user_id')\
                            .annotate(Count('user_id'))\
                             .annotate(Max('created'))\
                            .order_by("-user_id__count")
print(qs_post)
#----------------------------------------------------------------

# Добавить пункт меню "Наиболее обсуждаемые", где будет перечень заметок, отсортированный по убыванию 📉 кол-ва комментариев,
# и у которых более 2х новых комментариев за последние 12 часов.
# (Подсказка: для начала надо отсортировать заметки так, чтобы выводились те, у которых за последние 12
# часов есть комментарии - comments__created__gte=(datetime.now() - timedelta(hours=12)))

# coments = Comments.objects.all()\
#                             .select_related('post').\
#                             filter(created__gte = (datetime.datetime.now() - datetime.timedelta(hours=12)))\
#                             .values('post_id')\
#                             .annotate(Count('post_id')).order_by('-post_id__count')\
#                             .filter(post_id__count__gt = 2)\
#
#
# print(coments.query)
# print(coments)



