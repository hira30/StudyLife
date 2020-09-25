from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import StudyLifeModel
from .forms import StudyLifeCreateForm
from datetime import datetime


class StudyLifeList(LoginRequiredMixin, ListView):
    template_name = 'studyapp/list.html'

    def get_queryset(self):
        return StudyLifeModel.objects.filter(user=self.request.user).order_by('-date')[:5]

    def get_context_data(self, **kwargs):
        labels = []
        data_list = []
        object_list = []
        context = super().get_context_data(**kwargs)
        queryset = StudyLifeModel.objects.filter(user=self.request.user).order_by('date')
        objects = StudyLifeModel.objects.filter(user=self.request.user).order_by('-date')[:5]
        for study_data in queryset:
            labels.append(study_data.date.strftime('%Y/%m/%d'))
            data_list.append(float(study_data.time))
        context={
            'labels': labels,
            'data_list': data_list,
            'object_list': objects
        }
        return context

# matplotlibでグラフ作成
# import io
# import matplotlib.pyplot as plt
# import numpy as np

# def setPlt():
#     study_data = StudyLifeModel.objects.order_by('date')[:5] # 学習データを取得
#     x = [data.date for data in study_data] # 日付
#     y = [data.time for data in study_data] # 学習時間
#     plt.bar(x, y, align="center") # 棒グラフを出力
#     plt.title("title")
#     plt.xlabel("x")
#     plt.ylabel("y")
#     plt.grid(True)

# # svgへの変換
# def pltToSvg():
#     buf = io.BytesIO()
#     plt.savefig(buf, format='svg', bbox_inches='tight')
#     s = buf.getvalue()
#     buf.close()
#     return s

# def get_svg(request):
#     setPlt()       # create the plot
#     svg = pltToSvg() # convert plot to SVG
#     plt.cla()        # clean up plt so it can be re-used
#     response = HttpResponse(svg, content_type='image/svg+xml')
#     return response


class StudyLifeCreate(LoginRequiredMixin, CreateView):
    template_name = 'studyapp/create.html'
    model = StudyLifeModel
    form_class = StudyLifeCreateForm
    success_url = reverse_lazy('studyapp:list')

    def form_valid(self, form):
        qryset = form.save(commit=False)
        qryset.user = self.request.user
        qryset.save()
        return redirect('studyapp:list')


class StudyLifeUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'studyapp/update.html'
    model = StudyLifeModel
    fields = ('date', 'time', 'task', 'memo')
    success_url = reverse_lazy('studyapp:list')


class StudyLifeDetail(LoginRequiredMixin, DetailView):
    template_name = 'studyapp/detail.html'
    model = StudyLifeModel


class StudyLifeDelete(LoginRequiredMixin, DeleteView):
    template_name = 'studyapp/delete.html'
    model = StudyLifeModel
    success_url = reverse_lazy('studyapp:list')

