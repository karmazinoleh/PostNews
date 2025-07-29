from news.models import Articles, Comment
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons',
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text',
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Publication date',
            }),
        }

class CommentsForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Comment',
            })
        }