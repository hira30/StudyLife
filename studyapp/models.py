import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

TASK_CHOICES = [
    ('1', 'プログラミング'),
    ('2', '語学'),
    ('3', '資格'),
    ('4', '読書'),
    ('5', 'その他'),
]

class StudyLifeModel(models.Model):
    date = models.DateField(verbose_name='日付', default=timezone.datetime.today())
    time = models.DecimalField(
        verbose_name='学習時間',
        max_digits=3, # 数字部分の最大桁数
        decimal_places=1, # 小数点部分の桁数
        default=0.0,
        validators=[MinValueValidator(0.0), MaxValueValidator(24.0)]
    )
    task = models.CharField(verbose_name='学習内容', max_length=1, choices=TASK_CHOICES)
    memo = models.TextField(verbose_name='メモ', null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # モデルにユーザーを紐付ける

    # class Meta:
    #     constraints = [
    #         # 同じ日に同じタスクを重複させない
    #         models.UniqueConstraint(fields=['date', 'user'], name='unique_task'),
    #     ]

    # @classmethod
    # # 同じ日にタスクがすでに登録されているどうかを判定。登録されていたらTrue
    # def check_duplicate(cls, date: datetime.date, task: str) -> bool:
    #     return cls.objects.filter(date=date, task=task).exists()

    def __str__(self):
        return self.task
