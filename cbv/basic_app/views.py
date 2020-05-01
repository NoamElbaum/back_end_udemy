from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models

# simple view
# Create your views here.
# def index(request):
#     return render(request, 'index.html')

# simple CBV
# class CBView(View):
#     def get(self, request):
#         return HttpResponse('CLASS BASED VIEW')

# TemplateView
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['val'] = 'Text'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'school_list.html'

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'school_detail.html'