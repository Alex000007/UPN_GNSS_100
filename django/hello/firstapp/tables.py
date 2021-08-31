import django_tables2 as tables
from django_tables2 import TemplateColumn

from .models import UpnGnssProject100

class dataTable(tables.Table):
	# name = tables.columns.Column()
	B1 = '<button type="button" class="btn js-update" update-link="{{ record.id }}">edit</button>'
	Edit = tables.TemplateColumn(B1, template_name='edit.html')
	class Meta:
		model = UpnGnssProject100
		attrs = {'class': 'table table-sm'}
		template_name = "django_tables2/bootstrap.html"
		fields = ("Edit", "id", "number", "region", "nameua", "nameen", "coatuu_code", "y", "x", "status_np_za_admin_podil", "districtce", "meteo", "status", "norway_project", "grounding", "site_repor", "reconaissa", "cabinet", "statusid", "dgk", "dgk_contac", "agreement", "primary_co", "rigc_ready", "sitechange", "installati", "notes")
        
