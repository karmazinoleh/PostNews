from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from news.models import Articles
from .serializer import ArticleSerializer

@api_view(['GET'])
def get_articles(request):
    return Response(ArticleSerializer(Articles.objects.all(), many=True).data)

@api_view(['GET'])
def get_article(request, pk):
    return Response(ArticleSerializer(Articles.objects.get(pk=pk)).data)

@api_view(['POST'])
def create_article(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_article(request, pk):
    article = Articles.objects.get(pk=pk)
    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_article(request, pk):
    article = Articles.objects.get(pk=pk)
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)