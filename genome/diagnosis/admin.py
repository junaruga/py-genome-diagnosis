from django.contrib import admin

from diagnosis.models import Disease
from diagnosis.models import Genome
from diagnosis.models import Snp
from diagnosis.models import SnpDisease


# Customize the layout on admin page.
class DiseaseAdmin(admin.ModelAdmin):
    fields = ['name', 'disease_id']


admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Genome)
admin.site.register(Snp)
admin.site.register(SnpDisease)
