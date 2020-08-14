from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from .models import (Site, EmployeeInformation, BasebandEquipment, TransmissionEquipment, RadioEquipment, AntennaEquipment, BatteryEquipment, 
                    RectifierEquipment, Manufacturer, RRUModel, RectifierModel, BatteryModel, TransmissionEquipmentModel,
                    RectifierModuleModel, AntennaModel, HouseOwnerInformation, NTTeamLeadInformation)
#  Register your models here.
class SiteModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin,admin.ModelAdmin):
    list_display = ['province','region','site_id','site_name']
    list_filter = ['province','region']
    search_fields = ['site_id','site_name']

    class Meta:
        model = Site

class EmployeeModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    class Meta:
        model = EmployeeInformation

class NTTeamLeadModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    class Meta:
        model = NTTeamLeadInformation

class HouseOwnerModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    class Meta:
        model = HouseOwnerInformation

class BasebandEquipmentModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    class Meta:
        model = BasebandEquipment

class TransmissionEquipmentModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    class Meta:
        model = TransmissionEquipment

class RadioEquipmentModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    class Meta:
        model = RadioEquipment

class AntennaEquipmentModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    class Meta:
        model = AntennaEquipment

class RectifierEquipmentModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    class Meta:
        model = RectifierEquipment

class BatteryEquipmentModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    class Meta:
        model = BatteryEquipment

admin.site.register(Site, SiteModelAdmin)
admin.site.register(EmployeeInformation, EmployeeModelAdmin)
admin.site.register(NTTeamLeadInformation, NTTeamLeadModelAdmin)
admin.site.register(HouseOwnerInformation, HouseOwnerModelAdmin)
admin.site.register(BasebandEquipment, BasebandEquipmentModelAdmin)
admin.site.register(TransmissionEquipment, TransmissionEquipmentModelAdmin)
admin.site.register(RadioEquipment, RadioEquipmentModelAdmin)
admin.site.register(AntennaEquipment, AntennaEquipmentModelAdmin)
admin.site.register(RectifierEquipment, RectifierEquipmentModelAdmin)
admin.site.register(BatteryEquipment, BatteryEquipmentModelAdmin)
admin.site.register(BatteryModel)
admin.site.register(Manufacturer)
admin.site.register(AntennaModel)
admin.site.register(RRUModel)
admin.site.register(RectifierModel)
admin.site.register(RectifierModuleModel)
admin.site.register(TransmissionEquipmentModel)

