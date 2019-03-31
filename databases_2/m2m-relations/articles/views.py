from django.views.generic import ListView

from articles.models import Article, Relationship


class ArticleListView(ListView):
    template_name = 'articles/news.html'
    model = Article
    ordering = '-published_at'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_arcticles_list = []
        for article in context['object_list']:
            list_scopes = []
            for scope in Relationship.objects.filter(article=article).all():
                list_scopes.append(
                    {'topic': scope.section.sections, 'main_sec': scope.main_sec})
            article.scopes_new = sorted(list_scopes,
                                        key=lambda x: x['main_sec'],
                                        reverse=True)
            new_arcticles_list.append(article)
            context['object_list'] = new_arcticles_list
        return context
