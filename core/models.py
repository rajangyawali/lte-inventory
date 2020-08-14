from django.db import models

PROVINCES = (('Province 1','Province 1'),
            ('Province 2','Province 2'),
            ('Bagmati','Bagmati'),
            ('Gandaki','Gandaki'),
            ('Province 5','Province 5'),
            ('Karnali','Karnali'),
            ('Sudur Paschim','Sudur Paschim'))

REGIONS = (('EDR','EDR'),('CDR','CDR'),('KTM','KTM'),('WDR','WDR'),('MWDR','MWDR'),('FWDR','FWDR'))

DISTRICTS = (('Kathmandu','Kathmandu'),
            ('Bhaktapur','Bhaktapur'),
            ('Lalitpur','Lalitpur'))

BBU_MODELS = (('BBU3910','BBU3910'),)
UBBP_MODELS = (('UBBPe4','UBBPe4'),)
UMPT_MODELS = (('UMPTb9','UMPTb9'),)
UPEU_MODELS = (('UPEU','UPEU'),)
FAN_MODELS = (('FAN','FAN'),)
RRU_MODELS = (('RRU3959a','RRU3959a'),('RRU5901','RRU5901'),('RRU5308','RRU5308'))
SUBRACK_OPTIONS = (('70','70'),('71','71'),('72','72'),('80','80'),('81','81'),('82','82'))
BAND_OPTIONS = (('B3','B3'),('B20','B20'))
OPERATING_RANGE = (('TX1805-1880/RX1710-1785','TX1805-1880/RX1710-1785'),('TX791-821/RX832-862','TX791-821/RX832-862'))
CONFIGURATION_OPTIONS = (('2T2R','2T2R'),('2T4R','2T4R'),('4T4R','4T4R'))
SECTOR_ID = ((1,1),(2,2),(3,3),(4,4),(5,5),(6,6))


class Manufacturer(models.Model):
    manufacturer = models.CharField(max_length = 20, verbose_name='Manufacturer')

    class Meta:
        verbose_name_plural = 'Manufacturer'

    def __str__(self):
        return self.manufacturer

class BatteryModel(models.Model):
    batt_model = models.CharField(max_length=20, verbose_name='Battery Model')

    class Meta:
        verbose_name_plural = 'Battery Model'

    def __str__(self):
        return self.batt_model

class TransmissionEquipmentModel(models.Model):
    teq_model = models.CharField(max_length=20, verbose_name='Transmission Equipment Model')
    
    class Meta:
        verbose_name_plural = 'Transmission Equipment Model'

    def __str__(self):
        return self.teq_model

class RRUModel(models.Model):
    rru_model = models.CharField(max_length=20, verbose_name='RRU Model')
    
    class Meta:
        verbose_name_plural = 'RRU Model'

    def __str__(self):
        return self.rru_model

class RectifierModel(models.Model):
    rect_model = models.CharField(max_length=20, verbose_name='Rectifier Model')
    
    class Meta:
        verbose_name_plural = 'Rectifier Model'

    def __str__(self):
        return self.rect_model

class RectifierModuleModel(models.Model):
    rect_module_model = models.CharField(max_length=20, verbose_name='Rectifier Module Model')
    
    class Meta:
        verbose_name_plural = 'Rectifier Modules Model'

    def __str__(self):
        return self.rect_module_model

class AntennaModel(models.Model):
    ant_model = models.CharField(max_length=20, verbose_name='Antenna Model')
    
    class Meta:
        verbose_name_plural = 'Antenna Model'

    def __str__(self):
        return self.ant_model

class Site(models.Model):
    site_id = models.CharField(max_length=8, verbose_name='Site ID',unique=True)
    site_name = models.CharField(max_length=50, verbose_name='Site Name')
    province = models.CharField(choices = PROVINCES, max_length=20)
    region = models.CharField(choices = REGIONS, max_length=4)
    district = models.CharField(choices=DISTRICTS, max_length=20)
    municipality = models.CharField(max_length=40, verbose_name = 'Municipality/Rural Municipality',null=True)
    ward = models.PositiveIntegerField(verbose_name='Ward No',null=True)
    address = models.CharField(max_length=50, verbose_name='Address',null=True)
    latitude = models.FloatField(max_length=10,null=True,blank=True)
    longitude = models.FloatField(max_length=10,null=True,blank=True)
    added_on = models.DateTimeField(auto_now_add=True, verbose_name='Added On')
    updated_on = models.DateTimeField(auto_now=True, verbose_name='Updated On')
    
    class Meta:
        verbose_name_plural = 'Sites'
        ordering = ['-added_on']

    def __str__(self):
        return self.site_id + '-' + self.site_name

class EmployeeInformation(models.Model):
    employee_name = models.CharField(max_length=100, verbose_name='Employee Name')
    employee_address = models.CharField(max_length=200, blank=True, null=True, verbose_name='Employee Address')
    employee_mobile = models.CharField(max_length=10,verbose_name='Mobile Number')
    employee_landline = models.CharField(max_length=9,blank=True, null=True, verbose_name='Landline Number')
    employee_id = models.PositiveIntegerField(verbose_name='Employee ID')
    added_on = models.DateTimeField(auto_now_add=True, verbose_name='Added On')
    updated_on = models.DateTimeField(auto_now=True, verbose_name='Updated On')
       
    class Meta:
        verbose_name_plural = 'NT Employees'
        ordering = ['employee_id']

    def __str__(self):
        return str(self.employee_name) + ' (' + str(self.employee_mobile) +')'

class NTTeamLeadInformation(models.Model):
    site = models.OneToOneField(Site, related_name='teamleader', on_delete=models.CASCADE)
    team = models.ForeignKey(EmployeeInformation, related_name='team', on_delete=models.CASCADE)
    team_added_on = models.DateTimeField(auto_now_add=True, verbose_name='Added On')
    team_updated_on = models.DateTimeField(auto_now=True, verbose_name='Updated On')
       
    class Meta:
        verbose_name_plural = 'NT Team Leaders'

    def __str__(self):
        return str(self.team.employee_name) + ' : Cell ' + str(self.team.employee_mobile)


class HouseOwnerInformation(models.Model):
    site = models.OneToOneField(Site, related_name='owner', on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=100, verbose_name='House Owner Name')
    owner_address = models.CharField(max_length=200, blank=True, null=True, verbose_name='House Owner Address')
    owner_mobile = models.CharField(max_length=10,verbose_name='Mobile Number')
    owner_landline = models.CharField(max_length=9,blank=True, null=True, verbose_name='Landline Number')
    key = models.CharField(max_length=1000, verbose_name='Key Information')
    owner_added_on = models.DateTimeField(auto_now_add=True, verbose_name='Added On')
    owner_updated_on = models.DateTimeField(auto_now=True, verbose_name='Updated On')

    class Meta:
        verbose_name_plural = 'House Owner Information'
        ordering = ['-owner_added_on']

    def __str__(self):
        return str(self.owner_name) + ' : Mobile Number ' + str(self.owner_mobile)

class BasebandEquipment(models.Model):
    site = models.ForeignKey(Site, related_name='basebandequipments', on_delete=models.CASCADE)
    bbu_model = models.CharField(choices = BBU_MODELS, max_length = 20, verbose_name='BBU Model')
    bbu_serial_number =  models.CharField(max_length=40, default='NA', blank=True, null=True, verbose_name='BBU Serial Number')
    ubbp_model = models.CharField(choices = UBBP_MODELS, max_length = 20, verbose_name='UBBP Model')
    ubbp_quantity = models.PositiveIntegerField(default = 1, blank = True, verbose_name='UBBP Quantity')
    umpt_model = models.CharField(choices = UMPT_MODELS, max_length = 20, verbose_name='UMPT Model')
    umpt_quantity = models.PositiveIntegerField(default = 1, blank = True, verbose_name='UMPT Quantity')
    upeu_model = models.CharField(choices = UPEU_MODELS, max_length = 20, verbose_name='UPEU Model')
    fan_model = models.CharField(choices = FAN_MODELS, max_length = 20, verbose_name='Fan Model')
    bbu_manufacturer = models.ForeignKey(Manufacturer,on_delete=models.SET_NULL, null=True, verbose_name='Manufacturer')
    bbu_added_on = models.DateTimeField(auto_now_add=True, verbose_name='Added On')
    bbu_updated_on = models.DateTimeField(auto_now=True, verbose_name='Updated On')

    class Meta:
        verbose_name_plural = 'Baseband Equipments'

    def __str__(self):
        return str(self.site.site_id) + ' -> Model: ' + str(self.bbu_model) + ' & Serial No: ' + str(self.bbu_serial_number)

class TransmissionEquipment(models.Model):
    site = models.ForeignKey(Site, related_name='transmissionequipments', on_delete=models.CASCADE)
    te_model = models.ForeignKey(TransmissionEquipmentModel,on_delete=models.SET_NULL, null=True,verbose_name='Model')
    te_transmission_type = models.CharField(choices=(('Optical','Optical'),('Radio','Radio')), max_length=10, verbose_name='Transmission Type')
    te_serial_number = models.CharField(max_length=40, default='NA', blank=True, null=True, verbose_name='Serial Number')
    te_sfps_number = models.PositiveIntegerField(verbose_name = 'Number of SFPs')
    te_manufacturer = models.ForeignKey(Manufacturer,on_delete=models.SET_NULL, null=True, verbose_name='Manufacturer')
    te_added_on = models.DateTimeField(auto_now_add=True, verbose_name='Added On')
    te_updated_on = models.DateTimeField(auto_now=True, verbose_name='Updated On')

    class Meta:
        verbose_name_plural = 'Transmission Equipments'

    def __str__(self):
        return str(self.site.site_id) + ' -> Model: ' + str(self.te_model.teq_model) + ' & Serial No: ' + str(self.te_serial_number)

class RadioEquipment(models.Model):
    site = models.ForeignKey(Site, related_name='radioequipments', on_delete=models.CASCADE)
    radio_model = models.ForeignKey(RRUModel, on_delete=models.SET_NULL, null=True,verbose_name='RRU Model')
    radio_subrack_number = models.CharField(choices=SUBRACK_OPTIONS, max_length=10, verbose_name='Subrack Number')
    radio_band = models.CharField(choices = BAND_OPTIONS, max_length = 20, verbose_name='Band')
    radio_operating_range = models.CharField(choices = OPERATING_RANGE, max_length = 40, blank=True,null=True,verbose_name='Operating Range (MHz)')
    radio_gain = models.FloatField(default = 9.8,max_length= 20,verbose_name='Gain')
    radio_configuration = models.CharField(choices = CONFIGURATION_OPTIONS, max_length = 20, verbose_name='Configuration')
    radio_power = models.PositiveIntegerField(default = 40, verbose_name='Power')
    radio_serial_number = models.CharField(max_length=40,  default='NA', blank=True, null=True, verbose_name='RRU Serial Number')
    radio_manufacturer = models.ForeignKey(Manufacturer,on_delete=models.SET_NULL, null=True, verbose_name='Manufacturer')
    radio_added_on = models.DateTimeField(auto_now_add=True, verbose_name='Added On')
    radio_updated_on = models.DateTimeField(auto_now=True, verbose_name='Updated On')

    class Meta:
        verbose_name_plural = 'Radio Equipments'

    # def __str__(self):
    #     return str(self.site.site_id) + ' -> RRU Model : ' + str(self.radio_model.rru_model) + ' & Serial Number : ' + str(self.radio_serial_number)

    
class AntennaEquipment(models.Model):
    site = models.ForeignKey(Site, related_name='antennaequipments', on_delete=models.CASCADE)
    antenna_model = models.ForeignKey(AntennaModel,on_delete=models.SET_NULL, null=True, verbose_name='Antenna Model')
    antenna_sector_id = models.PositiveIntegerField(choices = SECTOR_ID, verbose_name='Sector ID')
    antenna_serial_number = models.CharField(max_length=40, default='NA', blank=True, null=True, verbose_name='Antenna Serial Number')
    antenna_manufacturer = models.ForeignKey(Manufacturer,on_delete=models.SET_NULL, null=True, verbose_name='Manufacturer')
    antenna_added_on = models.DateTimeField(auto_now_add=True, verbose_name='Added On')
    antenna_updated_on = models.DateTimeField(auto_now=True, verbose_name='Updated On')
    
    class Meta:
        verbose_name_plural = 'Antenna Equipments'

    def __str__(self):
        return str(self.site.site_id) + ' -> Antenna Model : ' + str(self.antenna_model.ant_model) + ' & Serial No: ' + str(self.antenna_serial_number)

class RectifierEquipment(models.Model):
    site = models.ForeignKey(Site, related_name='rectifierequipments', on_delete=models.CASCADE)
    rectifier_model = models.ForeignKey(RectifierModel,on_delete=models.SET_NULL, null=True, verbose_name = 'Rectifier Model')
    rectifier_serial_number = models.CharField(max_length=40, default='NA', blank=True, null=True, verbose_name='Rectifier Serial Number')
    rectifier_module_model = models.ForeignKey(RectifierModuleModel,on_delete=models.SET_NULL, null=True, verbose_name='Rectifier Module Model')
    rectifier_installed_module = models.PositiveIntegerField(verbose_name='Installed Modules')
    rectifier_running_module = models.PositiveIntegerField(verbose_name='Running Modules')
    rectifier_manufacturer = models.ForeignKey(Manufacturer,on_delete=models.SET_NULL, null=True, verbose_name='Manufacturer')
    rectifier_added_on = models.DateTimeField(auto_now_add=True, verbose_name='Added On')
    rectifier_updated_on = models.DateTimeField(auto_now=True, verbose_name='Updated On')

    class Meta:
        verbose_name_plural = 'Rectifier Equipments'

    def __str__(self):
        return str(self.site.site_id) + ' -> Rectifier Model : ' + str(self.rectifier_model.rect_model) + ' & Serial No: ' + str(self.rectifier_serial_number)

class BatteryEquipment(models.Model):
    site = models.ForeignKey(Site, related_name='batteryequipments', on_delete=models.CASCADE)
    battery_model = models.ForeignKey(BatteryModel,on_delete=models.SET_NULL, null=True, verbose_name = 'Battery Model')
    battery_banks = models.CharField(max_length=1, choices=(('1','1'),('2','2'),('3','3'),('4','4')), verbose_name='Number of Banks')
    battery_manufacturer = models.ForeignKey(Manufacturer,on_delete=models.SET_NULL, null=True, verbose_name='Manufacturer')
    battery_added_by = models.CharField(max_length = 20, verbose_name='Added By', null=True)
    battery_added_on = models.DateTimeField(auto_now_add=True, verbose_name='Added On')
    battery_updated_on = models.DateTimeField(auto_now=True, verbose_name='Updated On')

    class Meta:
        verbose_name_plural = 'Battery Equipments'

    def __str__(self):
        return str(self.site.site_id) + ' -> Battery Model : ' + str(self.battery_model.batt_model)




