from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

from django import forms
from django.contrib.auth.models import User
from .models import *

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ('site_id','site_name','province','region','district','municipality','ward','address','latitude','longitude')

class EmployeeInformationForm(forms.ModelForm):
    class Meta:
        model = EmployeeInformation
        fields = ('employee_name', 'employee_address','employee_mobile','employee_landline','employee_id')

class NTTeamLeadInformationForm(forms.ModelForm):
    class Meta:
        model = NTTeamLeadInformation
        fields = ('team',)

class HouseOwnerInformationForm(forms.ModelForm):
    class Meta:
        model = HouseOwnerInformation
        fields = ('owner_name','owner_address','owner_mobile','owner_landline','key')

class BasebandEquipmentForm(forms.ModelForm):
    class Meta:
        model = BasebandEquipment
        fields = ('bbu_model','bbu_serial_number','ubbp_model','ubbp_quantity','umpt_model','umpt_quantity','upeu_model','fan_model','bbu_manufacturer')

class TransmissionEquipmentForm(forms.ModelForm):
    class Meta:
        model = TransmissionEquipment
        fields = ('te_model', 'te_transmission_type','te_serial_number','te_manufacturer','te_sfps_number')

class RadioEquipmentForm(forms.ModelForm):
    class Meta:
        model = RadioEquipment
        fields = ('radio_model','radio_subrack_number','radio_band','radio_operating_range','radio_gain','radio_configuration','radio_power','radio_serial_number','radio_manufacturer')  

class AntennaEquipmentForm(forms.ModelForm):
    class Meta:
        model = AntennaEquipment
        fields = ('antenna_model','antenna_sector_id','antenna_serial_number','antenna_manufacturer')

class RectifierEquipmentForm(forms.ModelForm):
    class Meta:
        model = RectifierEquipment
        fields = ('rectifier_model', 'rectifier_serial_number', 'rectifier_module_model',
                    'rectifier_installed_module','rectifier_running_module','rectifier_manufacturer')

class BatteryEquipmentForm(forms.ModelForm):
    class Meta:
        model = BatteryEquipment
        fields = ('battery_model', 'battery_banks','battery_manufacturer','battery_added_by')

class EditProfileForm(UserChangeForm):
    password = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email','password')

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].label = 'First Name'

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].label = 'Last Name'

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = '<small class="form-text text-muted"> &nbsp; 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].label = 'Email'
    
class ChangePasswordForm(PasswordChangeForm):

    class Meta:
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].label = 'Old Password'

        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].label = 'New Password'
        self.fields['new_password1'].help_text = '<small><ul class="form-text text-muted"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul></small>'

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].label = 'Confirm New Password'