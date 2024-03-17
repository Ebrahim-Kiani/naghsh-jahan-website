from django.contrib import admin
from django.contrib import messages
from home_module.models import slide, instagram

# Register your models here.

admin.site.register(slide)



class instagramAdmin(admin.ModelAdmin):
    actions = ['delete_all_objects']

    def delete_all_objects(self, request, queryset):
        # Delete all objects
        deleted_count, _ = queryset.delete()

        # Display a success message
        self.message_user(request, f"{deleted_count} objects deleted successfully.", messages.SUCCESS)

    delete_all_objects.title = "Delete all objects"


admin.site.register(instagram, instagramAdmin)
