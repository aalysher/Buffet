from django.contrib import admin

from .models import Pin, User, Course, Student, Buffet, Operation, OperationDetail


@admin.action(description='Mark selected stories as payment')
def make_published(modeladmin, request, queryset):
    """Меняет статус на оплачен"""
    queryset.update(status=1)


class OperationSettings(admin.ModelAdmin):
    list_display = ('id', 'add_date', 'edit_date',
                    'total_sum', 'debt_sum', 'pin',
                    'status')
    actions = [make_published]


class OperationDetailSettings(admin.ModelAdmin):
    list_display = ('amount', 'buffet', 'operations')


admin.site.register(Pin)
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Operation)
admin.site.register(OperationDetail)

