from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

# simple view
# Create your views here.
# def index(request):
#     return render(request, 'index.html')

# simple CBV
# class CBView(View):
#     def get(self, request):
#         return HttpResponse('CLASS BASED VIEW')

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['val'] = 'Text'
        return context