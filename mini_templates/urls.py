from django.urls import path
import mini_templates.views as mini_view
urlpatterns = [
    path('', mini_view.index)
]
