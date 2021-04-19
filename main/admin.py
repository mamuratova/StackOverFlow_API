from django.contrib import admin

from .models import CodeImage, Problem, Comment, Reply


class CodeImageInline(admin.TabularInline):
    model = CodeImage
    min_num = 1
    max_num = 10


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    inlines = [ CodeImageInline,]


class CommentInline(admin.TabularInline):
    model = Comment

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    inlines = [CommentInline,]
    list_filter = ('created',)
