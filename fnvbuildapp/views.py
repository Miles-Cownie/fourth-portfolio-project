from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import CharacterBuild
from .forms import CommentForm, CharacterBuildForm

# Home Page View


class BuildList(generic.ListView):
    model = CharacterBuild
    queryset = CharacterBuild.objects.filter(status=2).order_by('-created_on')
    template_name = "index.html"
    paginate_by = 6

# Detailed Page View


class BuildDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = CharacterBuild.objects.filter(status=2)
        build = get_object_or_404(queryset, slug=slug)
        comments = build.comments.filter(approved=True).order_by('created_on')
        liked = False
        if build.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "build_detail.html",
            {
                "build": build,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = CharacterBuild.objects.filter(status=2)
        build = get_object_or_404(queryset, slug=slug)
        comments = build.comments.filter(approved=True).order_by('created_on')
        liked = False
        if build.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.build = build
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "build_detail.html",
            {
                "build": build,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

# Build Form Classes


class CharacterBuildCreate(generic.CreateView):
    model = CharacterBuild
    form_class = CharacterBuildForm
    template_name = 'characterbuild_form.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            characterbuild = CharacterBuildForm(request.POST)
            if characterbuild.is_valid():
                characterbuild.instance.email = request.user.username
                build = characterbuild.save(commit=False)
                build.slug = slugify(build.title)
                build.author = request.user
                build.save()
        return HttpResponseRedirect(reverse('home'))


class CharacterBuildUpdate(generic.UpdateView):
    model = CharacterBuild
    form_class = CharacterBuildForm
    template_name = 'characterbuild_form.html'


class CharacterBuildDelete(generic.DeleteView):
    model = CharacterBuild
    template_name = 'characterbuild_confirm_delete.html'
    success_url = reverse_lazy('index')

# Likes Class


class BuildLike(View):

    def post(self, request, slug, *args, **kwargs):
        build = get_object_or_404(CharacterBuild, slug=slug)

        if build.likes.filter(id=request.user.id).exists():
            build.likes.remove(request.user)
        else:
            build.likes.add(request.user)

        return HttpResponseRedirect(reverse('build_detail', args=[slug]))
