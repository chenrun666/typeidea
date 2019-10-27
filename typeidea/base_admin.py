from django.contrib import admin

from django.core.exceptions import FieldError


class BaseOwnerAdmin(admin.ModelAdmin):
    exclude = ("owner",)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        try:
            return qs.filter(owner=request.user)
        except FieldError:
            return qs
