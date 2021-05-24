from django.contrib import admin
from api.models import *


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    fields = ('q_text', 'q_type')


class QuestionnaireAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    inlines = (QuestionInline,)


admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(Answer)
