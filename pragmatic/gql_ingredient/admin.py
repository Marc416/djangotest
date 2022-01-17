from django.contrib import admin

from gql_ingredient.models import Category, Ingredient

admin.site.register(Category)
admin.site.register(Ingredient)