from django.contrib import admin
from django.urls import path,include
from graphene_django.views import GraphQLView
from movie_app.schema import schema
import graphql

urlpatterns = [
    path('graphql/', GraphQLView.as_view(graphiql=True , schema=schema)),
]
