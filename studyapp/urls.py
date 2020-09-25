from django.urls import path
from .views import StudyLifeList, StudyLifeDetail, StudyLifeCreate, StudyLifeDelete, StudyLifeUpdate
from . import views

app_name = 'studyapp'

urlpatterns = [
    path('list/', StudyLifeList.as_view(), name='list'),
    path('detail/<int:pk>/', StudyLifeDetail.as_view(), name='detail'),
    path('create/', StudyLifeCreate.as_view(), name='create'),
    path('delete/<int:pk>/', StudyLifeDelete.as_view(), name='delete'),
    path('update/<int:pk>/', StudyLifeUpdate.as_view(), name='update'),
]
