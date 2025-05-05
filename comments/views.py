import logging
from typing import Literal

from django.views import View
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from comments.models import Comments
from posts.models import Posts


logger = logging.getLogger()


class AddComment(View):
    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        client = request.user
        if not client:
            return JsonResponse(data={"error": "not authorized"})
        posts = Posts.objects.filter(id=pk)
        if not posts:
            return JsonResponse(
                data={"error": f"Post with id {pk} not found"}
            )
        comment = Comments(
            post=posts[0], user=client,
            text=request.POST.get("text")
        )
        comment.save()
        return render(
            request=request, template_name="pk_post.html",
            context={"post": posts[0], "author": client}
        )


class AddReply(View):
    def post(self):
        pass