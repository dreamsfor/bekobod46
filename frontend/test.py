from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib import admin


class Profile(models.Model):
    Name = models.CharField(max_length=200, verbose_name='Название теста')
    WorkTime = models.IntegerField(verbose_name='Время выполнения (мин)')
    QuestionsCount = models.IntegerField(verbose_name='Количество вопросов')
    Statisfactorily = models.IntegerField(verbose_name='Удовлетворительно')
    Good = models.IntegerField(verbose_name='Хорошо')
    Perfect = models.IntegerField(verbose_name='Отлично')

    class Meta:
        verbose_name = 'Тесты'
        verbose_name_plural = 'Тесты'



    def __str__(self):
        return self.Name


class Question(models.Model):
    ProfileId = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Тест')
    Text = models.TextField(verbose_name='Текст вопроса')
    Weight = models.FloatField(default=1, verbose_name='Вес')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.Text


class Answer(models.Model):
    QuestionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    Text = models.CharField(max_length=300)
    IsRight = models.BooleanField()

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.Text

class Result(models.Model):
    ProfileId = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Тест')
    UserName = models.CharField(max_length=300, verbose_name="ФИО")
    DateTime = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Время завершения")
    Rating =models.FloatField(verbose_name="Проценты")

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'




class QuestionsInline(admin.TabularInline):
    model = Answer

@admin.register(Question)
class BookAdmin(admin.ModelAdmin):
    inlines = [QuestionsInline]


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display=("ProfileId", "DateTime", "UserName", "Rating")

    def has_add_permission(self, request):
        return False