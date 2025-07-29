from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect
from news.models import Articles, Comment
from news.forms import ArticlesForm, CommentsForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

    form = CommentsForm
    def post(self, request, *args, **kwargs):
        form = CommentsForm(request.POST)
        if form.is_valid():
            article = self.get_object()
            form.instance.author = request.user
            form.instance.article = article
            form.save()

            return redirect('news_home')

    def get_context_data(self, **kwargs):
        post_comments = Comment.objects.filter(article=self.get_object())
        context = super().get_context_data(**kwargs)
        context.update({
            'post_comments': post_comments,
            'form': self.form
        })
        return context

class NewsUpdateView(UpdateView):
    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object().author:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object().author:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    model = Articles
    success_url = '/news/'
    template_name = 'news/news_delete.html'

@login_required(login_url="/myauth/")
def create(request):
    if not request.user.groups.filter(name='Publisher').exists():
        raise PermissionDenied

    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('news_home')
        else:
            error = 'Invalid form'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)

