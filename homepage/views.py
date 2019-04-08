from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

class ShowArticlesView(ListView):
    model = Article
    template_name = 'homepage/home.html'
    context_object_name = 'articles'
    ordering = ['-date']

    def get_context_data(self,**kwards):
        ctx = super(ShowArticlesView, self).get_context_data(**kwards)
        ctx['title'] = 'Home Page'
        return ctx

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'homepage/article_detail.html'

    def get_context_data(self, **kwards):
        ctx = super(ArticleDetailView, self).get_context_data(**kwards)
        ctx['title'] = Article.objects.filter(pk=self.kwargs['pk']).first()
        return ctx


