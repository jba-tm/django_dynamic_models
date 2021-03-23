from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from .models import Project, ArtProject, ResearchProject, ImageProject


class ModelChildAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = Project  # Optional, explicitly set here.

    # By using these `base_...` attributes instead of the regular ModelAdmin `form` and `fieldsets`,
    # the additional fields of the child models are automatically added to the admin form.
    # base_form = ...
    # base_fieldsets = (
    #     ...
    # )


@admin.register(ArtProject)
class ArtProjectAdmin(ModelChildAdmin):
    base_model = ArtProject  # Explicitly set here!
    # define custom features here


@admin.register(ResearchProject)
class ResearchProjectAdmin(ModelChildAdmin):
    base_model = ResearchProject  # Explicitly set here!
    show_in_index = True  # makes child model admin visible in main admin site
    # define custom features here


@admin.register(ImageProject)
class ImageProjectAdmin(ModelChildAdmin):
    base_model = ImageProject


@admin.register(Project)
class ProjectAdmin(PolymorphicParentModelAdmin):
    base_model = Project
    child_models = (ArtProject, ResearchProject, ImageProject)

    list_filter = (PolymorphicChildModelFilter,)
