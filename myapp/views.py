from django.http import HttpResponse, HttpRequest,HttpResponseNotFound,HttpResponseRedirect,HttpResponseForbidden
from django.shortcuts import render, get_object_or_404,redirect
from datetime import datetime
from django.urls import reverse_lazy,reverse
from myapp.models import Topic, Article, Profile
from myapp.forms import CommentForm, ArticleForm, UpdateArticleForm, CreateArticleForm
from myapp.forms import AuthenticationForm
from django.contrib.auth import login,logout,update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.edit import FormMixin,UpdateView,DeleteView,CreateView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.models import User
# from django.contrib.auth.forms import AuthenticationForm

#
def get_user_profile(user):
    try:
        profile, created = Profile.objects.get_or_create(user=user)
        return profile
    except Exception as e:
        print(f"Error fetching or creating profile: {e}")
        return None

def get_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# class CustomLoginView(LoginView):
#     template_name = 'login.html'
#     redirect_authenticated_user = True
#
#     def get_success_url(self):
#         return self.get_redirect_url() or '/'
# #
#
# class CustomLogoutView(LogoutView):
#     next_page = reverse_lazy('main')

def  art_logout(request):
    logout(request)
    return HttpResponseRedirect('/')



class ArticleListView(ListView):
    model = Article
    template_name = 'main.html'
    context_object_name = 'articles'
    ordering = ['-created_at']



#
class FeedView(ListView):
    model = Article
    template_name = 'my_feed.html'
    context_object_name = 'articles'

    def get_queryset(self):
        topics_name = Topic.objects.filter(name__in=['cinema', 'sport'])
        return Article.objects.filter(topic__in=topics_name).order_by('-created_at')


#
class ArticleDetailView(FormMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'
    form_class = CommentForm

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object
            comment.author = request.user
            comment.save()
            return redirect(self.get_success_url())
        return self.form_invalid(form)



#
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    form_class = UpdateArticleForm
    template_name = 'update_article.html'
    context_object_name = 'article'

    def get_success_url(self):
        return reverse('update_article', kwargs={'pk': self.object.pk})

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author

def main_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if article.author != request.user:
        return HttpResponseForbidden("You are not authorized to edit this article.")

    if request.method == "POST":
        form = UpdateArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('main')  # Redirect to the main page or another view
    else:
        form = UpdateArticleForm(instance=article)

    return render(request, 'update_article.html', {'form': form, 'article': article})


#

#
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('main')

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author



#
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = CreateArticleForm
    template_name = 'create_article.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()[:10]
        return context


#
class TopicListView(ListView):
    model = Topic
    template_name = 'topics.html'
    context_object_name = 'topics'

class TopicDetailView(DetailView):
    model = Topic
    template_name = 'topic.html'
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = self.object.articles.all()
        return context





class SubscribeTopicView(View):
    def post(self, request, topic_id):
        topic = get_object_or_404(Topic, id=topic_id)
        profile = get_user_profile(request.user)
        profile.subscriptions.add(topic)
        return redirect(request.META.get('HTTP_REFERER', '/topics'))


class UnsubscribeTopicView(View):
    def post(self, request, topic_id):
        topic = get_object_or_404(Topic, id=topic_id)
        profile = get_user_profile(request.user)
        profile.subscriptions.remove(topic)
        return redirect(request.META.get('HTTP_REFERER', '/topics'))




class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_user_profile(self.request.user)
        context['subscriptions'] = profile.subscriptions.all()
        context['all_topics'] = Topic.objects.all()
        return context

    

#
class UserRegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


#
class PasswordChangeView(LoginRequiredMixin, FormView):
    template_name = 'set_password.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('profile')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)



class MonthArchiveView(ListView):
    model = Article
    template_name = 'by_date.html'
    context_object_name = 'articles'

    def get_queryset(self):
        year = self.kwargs['year']
        month = self.kwargs['month']
        return Article.objects.filter(created_at__year=year, created_at__month=month).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = self.kwargs['year']
        context['month'] = self.kwargs['month']
        return context
