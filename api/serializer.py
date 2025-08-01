from rest_framework import serializers
from news.models import Articles

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'
        read_only_fields = ('id',)