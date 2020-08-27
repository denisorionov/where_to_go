from django.shortcuts import render
from django.views import View


class MainView(View):  # главная страница
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
