from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.db.models import Sum

from .models import Post, Tag, Image


class PostListView(ListView):
    model = Post
    template_name = "nodolist/post_list.html"
    context_object_name = "posts"
    success_url = reverse_lazy("nodolist:post_list")

    def get_context_data(self):
        obj = Post.objects.aggregate(total_time=Sum("complete_time"))
        context = super().get_context_data()
        context["total"] = obj["total_time"]
        return context

    def get_queryset(self):
        return self.model.objects.filter(created_user=self.request.user)


class PostDetailView(DetailView):
    model = Post
    template_name = "nodolist/post_detail.html"
    context_object_name = "post"


class TagListView(ListView):
    model = Tag
    template_name = "nodolist/tag_list.html"
    context_object_name = "tags"


class PostCreateView(CreateView):
    model = Post
    template_name = "nodolist/post_create.html"
    fields = ["tasks", "text", "complete_time", "tags"]
    context_object_name = "post_create"
    success_url = reverse_lazy("nodolist:post_list")

    def form_valid(self, form):
        posts_data = form.save(commit=False)
        new_tag = self.request.POST.get("new_tag")
        # post_user_id = self.request.user.id
        # form.created_user = post_user_id
        posts_data.save()

        if new_tag:
            for tag in new_tag.split():
                is_exists = Tag.objects.filter(name=tag)
                if not is_exists:
                    Tag.objects.create(name=tag)
        return redirect("nodolist:post_list")


class PostDeleteView(DeleteView):
    model = Post
    template_name = "nodolist/post_delete.html"
    success_url = reverse_lazy("nodolist:post_list")


class PostUpdateView(UpdateView):
    model = Post
    template_name = "nodolist/post_update.html"
    fields = PostCreateView.fields
    success_url = reverse_lazy("nodolist:post_list")
    
    
class PostTotalTimeView(ListView):
    model = Post
    template_name = "nodolist/post_total.html"
    context_object_name = "totals"


def toppage(request):
    image = Image.objects.get(pk=3)
    return render(request, "nodolist/toppage.html", {"image": image})
