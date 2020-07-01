from django.shortcuts import render,get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView ,DetailView ,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.
def home(request):
    context = {
        'post' : Post.objects.all()
    }
    return render (request,"blog/home.htm",context)

class PostListView(ListView): 
    model = Post 
    template_name = 'blog/home.htm'
    context_object_name = 'post'
    ordering = ['-date'] 
    paginate_by = 4

class UserPostListView(ListView):
    model = Post 
    template_name = 'blog/user_post.htm'
    context_object_name = 'post'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')

class SUserPostListView(ListView):
    model = Post.author 
    template_name = 'blog/user_post.htm'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.htm' 

class PostcreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'blog/post_form.htm' 
    fields = [ 'title','content' ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostupdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = 'blog/post_form.htm' 
    fields = [ 'title','content' ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostdeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/' 
    template_name = 'blog/post_confirm_delete.htm'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

   
    
def about(request):
    return render (request,"blog/about.htm",{'title':'about'})



