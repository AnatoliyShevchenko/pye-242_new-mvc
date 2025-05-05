import logging
from typing import Literal

from django.views import View
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from comments.models import Comments


logger = logging.getLogger()


class AddComment(View):
    def post(self, request: HttpRequest, pk: int):
        pass
