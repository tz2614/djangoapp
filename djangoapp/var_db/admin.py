from django.contrib import admin
from .models import Chromosome
from .models import Variant

admin.site.register(Chromosome)
admin.site.register(Variant)
