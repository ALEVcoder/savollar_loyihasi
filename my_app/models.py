from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
class Teacher(models.Model):
    fish = models.CharField(max_length=256)
    fani = models.CharField(max_length=50)
    question_n = models.SmallIntegerField(default=0)

    def __str__(self) -> str:
        return self.fani

    @property
    def savollar_soni(self):
        return Question.objects.filter(fan=self).count()

    def clean(self) -> None:
        if self.fish == self.fish:
            raise ValidationError(('Bunday O`qituvchi bor'))
        return super().clean()

    class Meta:
        verbose_name = 'O`qituvchi'
        verbose_name_plural = "O`qituvchilar"


class Question(models.Model):
    fan = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    savol = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    options_number = models.SmallIntegerField(default=0)

    def __str__(self) -> str:
        return self.savol


    @property
    def varaiantlari_soni(self):
        return Option.objects.filter(question=self).count()

    def clean(self) -> None:
        savol_s = Question.objects.filter(fan_id=self.fan_id).count()
        if savol_s > 9:
            raise ValidationError(('1 fanga faqat 10 ta savol kiritish mumkin!'))
        return super().clean()

    class Meta:
        verbose_name = 'Savol'
        verbose_name_plural = "Savollar"



class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    javob = models.CharField(max_length=245)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.javob

    def clean(self) -> None:
        options = Option.objects.filter(question_id=self.question_id, is_correct=True).count()
        if options > 1:
            raise ValidationError(('Faqat bitta to`g`ri javob bo`lishi kerak'))
        return super().clean()

    class Meta:
        verbose_name = 'Variant'
        verbose_name_plural = "Variantlar"