from django.urls import path
import mini_templates.views as mini_view
urlpatterns = [
    path('', mini_view.home, name="home"),
    path('mini_1', mini_view.mini_1, name="mini_1")
]
