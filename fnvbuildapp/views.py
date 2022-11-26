from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import CharacterBuild
from .forms import CommentForm

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
                "liked": liked,
                "comment_form": CommentForm()
            }
        )
