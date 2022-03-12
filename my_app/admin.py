from django.contrib import admin
from .models import Question, Option, Teacher
# Register your models here.


class InlineQ(admin.TabularInline):
    model = Question
    extra = 1

class InlineO(admin.TabularInline):
    model = Option
    extra = 2


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('fish', 'fani', 'savollar_soni',)
    list_per_page = 5
    inlines = [InlineQ]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'savol', 'created_date', 'varaiantlari_soni', )
    list_per_page = 10
    inlines = [InlineO]


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'javob', 'is_correct',)
    list_per_page = 40
    list_editable = ('javob',)
    list_filter = ('question_id',)
    search_fields = ('question__javob',)