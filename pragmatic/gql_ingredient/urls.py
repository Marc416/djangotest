from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from gql_ingredient.schema import schema

app_name = 'gql_ingredient'

urlpatterns = [
    path('graph_basic/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
