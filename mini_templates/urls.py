from django.urls import path
import mini_templates.views as mini_view
urlpatterns = [
    path('', mini_view.home, name="home"),
    path('mini_1', mini_view.mini_1, name="mini_1"),
    path('mini_2', mini_view.mini_2, name="mini_2"),
    path('mini_3', mini_view.mini_3, name="mini_3"),
    path('mini_4', mini_view.mini_4, name="mini_4"),
    path('mini_5', mini_view.mini_5, name="mini_5"),
]
