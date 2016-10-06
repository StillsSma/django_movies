from django.contrib import admin

# Register your models here.
from movie_data.models import Movies, Rater, Ratings
admin.site.register(Movies)
admin.site.register(Rater)
admin.site.register(Ratings)
