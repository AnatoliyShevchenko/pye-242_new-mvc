from django.urls import path

from comments.views import AddComment

urlpatterns = [
    path(route="add_comment/<int:pk>", 
        view=AddComment.as_view(), name="add_comment"
    ),
]
