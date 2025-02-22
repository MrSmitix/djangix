from django.contrib.admin import ModelAdmin


class ReadOnlyModelAdmin(ModelAdmin):
    """ Базовая read-only админка """

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
