from typing import List
from django.db.models import fields
import graphene
from graphene.relay import mutation
from graphene.types import schema
from graphene_django import DjangoObjectType,DjangoListField
from .models import movie

class movietype(DjangoObjectType):
    class Meta:
        model = movie
        fields = ("id","name","actorname","realeasedate","rating","type")

class Query(graphene.ObjectType):
    all_movie = graphene.List(movietype)
    movie_by_id = graphene.List(movietype , id = graphene.Int())

    def resolve_all_movie(root,info):
        return movie.objects.all()
    def resolve_movie_by_id(root, info , id):
        return movie.objects.filter(pk = id)

class createmovie(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        actorname = graphene.String()
        realeasedate = graphene.Date() 
        type = graphene.String() 
        rating = graphene.Int() 

    movie = graphene.Field(movietype)

    def mutate(self, info, name , actorname=None, realeasedate =None, type=True, rating=None):
        new_movie = movie.objects.create(
            name = name,
            actorname = actorname,
            realeasedate = realeasedate,
            type = type,
            rating = rating
        )
        
        return createmovie(movie=new_movie)

class deletemovie(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    movie = graphene.Field(movietype)

    def mutate(self,info,id):
        movies = movie.objects.get(id=id)
        movies.delete()
        return 

class updatemovie(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        actorname = graphene.String()
        realeasedate = graphene.Date() 
        type = graphene.String() 
        rating = graphene.Int()
        
    movie = graphene.Field(movietype)

    def mutate(self, info, id, name=None , actorname=None, realeasedate=None , type=None, rating=None):
        update_movie = movie.objects.get(id=id)
        update_movie.name = name if name is not None else movie.name
        update_movie.actorname = actorname if actorname is not None else movie.actorname
        update_movie.realeasedate = realeasedate if realeasedate is not None else movie.realeasedate
        update_movie.type = type if type is not None else movie.type
        update_movie.rating = rating if rating is not None else movie.rating
        update_movie.save()
        return updatemovie(movie = update_movie)
    
class Mutation(graphene.ObjectType):
    createmovie = createmovie.Field()
    deletemovie = deletemovie.Field()
    updatemovie = updatemovie.Field()


schema = graphene.Schema(query=Query , mutation=Mutation)