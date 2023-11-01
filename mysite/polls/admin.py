from django.contrib import admin


from .models import MyChoice, MyQuestion


class MyChoiceInline(admin.TabularInline):
    model = MyChoice
    extra = 3


class MyQuestionAdmin(admin.ModelAdmin):
    search_fields = ["question_text"]
    list_filter = ["pub_date"]
    list_display = ("question_text", "pub_date", "was_published_recently")
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [MyChoiceInline]


admin.site.register(MyQuestion, MyQuestionAdmin)
