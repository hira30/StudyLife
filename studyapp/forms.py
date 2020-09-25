from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import StudyLifeModel


class StudyLifeCreateForm(forms.ModelForm):

    class Meta:
        model = StudyLifeModel
        fields = ('date', 'time', 'task', 'memo',)
        widgets = {
            'date': AdminDateWidget(),
        }
        help_texts = {
                'time': '※単位は時間(h)です',
        }

    # task = forms.ModelChoiceField(queryset=TaskModel.objects.all(), label='学習内容')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['task'].empty_label = '選択して下さい'

    # def check(date, task):
    #     if StudyLifeModel.check_duplicate(date, task):
    #         raise forms.ValidationError(f'{date}にこの{task}は既に登録されています')
