from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .models import *
from django.db.models import Q
from .forms import EditProfileForm, ChangePasswordForm
from django.forms import inlineformset_factory
from .forms import (SiteForm, EmployeeInformationForm, NTTeamLeadInformationForm, HouseOwnerInformationForm, BasebandEquipmentForm,
                    TransmissionEquipmentForm, RadioEquipmentForm, AntennaEquipmentForm,
                    RectifierEquipmentForm, BatteryEquipmentForm)
from django.db import transaction, IntegrityError

TransmissionEquipmentFormset = inlineformset_factory(Site, TransmissionEquipment, TransmissionEquipmentForm, extra=2, can_delete=True)
RadioEquipmentFormset = inlineformset_factory(Site, RadioEquipment, RadioEquipmentForm, extra=2, can_delete=True)   
AntennaEquipmentFormset = inlineformset_factory(Site, AntennaEquipment, AntennaEquipmentForm, extra=2, can_delete=True)   

# Create your views here.
def home(request):
    query = request.GET.get('site', '')
    if query:        
        sites = Site.objects.filter(Q(site_id__icontains=query) | Q(site_name__icontains=query))
    else:
        sites = Site.objects.all()
    
    page = request.GET.get('page', 1)
    paginator = Paginator(sites, 50)
    try:
        sites = paginator.page(page)
    except PageNotAnInteger:
        sites = paginator.page(1)
    except EmptyPage:
        sites = paginator.page(paginator.num_pages)

    context = {
        'sites': sites,
        'query':query
    }
    return render(request,'core/index.html',context)

def siteDetail(request, site_id):
    site = get_object_or_404(Site, site_id=site_id)
    team_lead = NTTeamLeadInformation.objects.filter(site_id=site.id)[0]
    house_owner = HouseOwnerInformation.objects.filter(site_id=site.id)[0]
    baseband_equipment = BasebandEquipment.objects.filter(site_id=site.id)[0]
    transmission_equipments = TransmissionEquipment.objects.filter(site_id = site.id)
    radio_equipments = RadioEquipment.objects.filter(site_id=site.id)
    antenna_equipments = AntennaEquipment.objects.filter(site_id=site.id)
    rectifier_equipment = RectifierEquipment.objects.filter(site_id=site.id)[0]
    battery_equipment = BatteryEquipment.objects.filter(site_id = site.id)[0]
    context = {
        'site': site,
        'team_lead': team_lead,
        'house_owner':house_owner,
        'baseband_equipment': baseband_equipment,
        'transmission_equipments':transmission_equipments,
        'radio_equipments': radio_equipments,
        'antenna_equipments': antenna_equipments,
        'rectifier_equipment': rectifier_equipment,
        'battery_equipment':battery_equipment
    }
    return render(request, 'core/site-detail.html', context)

def siteCreate(request):
    TransmissionEquipmentFormset = inlineformset_factory(Site, TransmissionEquipment, TransmissionEquipmentForm, extra=2, can_delete=True)
    RadioEquipmentFormset = inlineformset_factory(Site, RadioEquipment, RadioEquipmentForm, extra=6, can_delete=True)   
    AntennaEquipmentFormset = inlineformset_factory(Site, AntennaEquipment, AntennaEquipmentForm, extra=6, can_delete=True)   

    if request.method == "POST":
        form = SiteForm(request.POST)
        team_lead_form = NTTeamLeadInformationForm(request.POST)
        owner_form = HouseOwnerInformationForm(request.POST)
        baseband_form = BasebandEquipmentForm(request.POST)
        transmission_formset = TransmissionEquipmentFormset(request.POST)
        radio_formset = RadioEquipmentFormset(request.POST)
        antenna_formset = AntennaEquipmentFormset(request.POST)
        rectifier_form = RectifierEquipmentForm(request.POST)
        battery_form = BatteryEquipmentForm(request.POST)
        if form.is_valid() and team_lead_form.is_valid() and owner_form.is_valid() and baseband_form.is_valid() and transmission_formset.is_valid() and radio_formset.is_valid() and antenna_formset.is_valid() and rectifier_form.is_valid() and battery_form.is_valid():
            site = form.save(commit=False)
            site.save()
            if team_lead_form.is_valid():
                team_lead = team_lead_form.save(commit=False)
                team_lead.site = site
                team_lead.save()
            if owner_form.is_valid():
                owner = owner_form.save(commit=False)
                owner.site = site
                owner.save()
            if baseband_form.is_valid():
                baseband_equipment = baseband_form.save(commit=False)
                baseband_equipment.site = site
                baseband_equipment.save()
            if transmission_formset.is_valid():
                for t in transmission_formset:
                    try:
                        transmission_equipment = t.save(commit=False)
                        transmission_equipment.site = site
                        transmission_equipment.save()
                    except:pass
            if radio_formset.is_valid():
                for r in radio_formset:
                    try:
                        radio_equipment = r.save(commit=False)
                        radio_equipment.site = site
                        radio_equipment.save()
                    except:pass
            if antenna_formset.is_valid():
                for a in antenna_formset:
                    try:
                        antenna_equipment = a.save(commit=False)
                        antenna_equipment.site = site
                        antenna_equipment.save()
                    except:pass
            if rectifier_form.is_valid():
                rectifier_equipment = rectifier_form.save(commit=False)
                rectifier_equipment.site = site
                rectifier_equipment.save()
            if battery_form.is_valid():
                battery_equipment = battery_form.save(commit=False)
                battery_equipment.site = site
                battery_equipment.save()
            messages.success(request, 'Site has been added !!')
            return redirect('home')
        else:
            messages.error(request, 'Error adding Site. Try with valid information !!')     
    else:
        form = SiteForm()
        team_lead_form = NTTeamLeadInformationForm()
        owner_form = HouseOwnerInformationForm()
        baseband_form = BasebandEquipmentForm()
        transmission_formset = TransmissionEquipmentFormset()
        radio_formset = RadioEquipmentFormset()
        antenna_formset = AntennaEquipmentFormset()
        rectifier_form = RectifierEquipmentForm()
        battery_form = BatteryEquipmentForm()
        context = {
            'form': form,
            'team_lead_form': team_lead_form,
            'owner_form': owner_form,
            'baseband_form': baseband_form,
            'transmission_formset':transmission_formset,
            'radio_formset': radio_formset,
            'antenna_formset':antenna_formset,
            'rectifier_form': rectifier_form,
            'battery_form':battery_form
        }
        return render(request, 'core/site-create.html', context)

def siteDelete(request, site_id):
    site = get_object_or_404(Site, site_id=site_id)
    if request.method == 'POST':
        site.delete()
        messages.success(request, 'Site has been deleted !!')
        return redirect('core:home')
    return render(request, 'core/site-delete.html')

def siteEdit(request, site_id):
    site = get_object_or_404(Site, site_id=site_id)
    team_lead = get_object_or_404(NTTeamLeadInformation, site__id=site.id)
    owner = get_object_or_404(HouseOwnerInformation, site__id = site.id)
    baseband_equipment = get_object_or_404(BasebandEquipment, site__id = site.id)
    rectifier_equipment = get_object_or_404(RectifierEquipment, site__id = site.id)
    battery_equipment = get_object_or_404(BatteryEquipment, site__id = site.id)
    if request.method == "POST":
        form = SiteForm(request.POST, prefix='site', instance=site)
        team_lead_form = NTTeamLeadInformationForm(request.POST, instance=team_lead)
        owner_form = HouseOwnerInformationForm(request.POST, instance=owner)
        baseband_form = BasebandEquipmentForm(request.POST, instance=baseband_equipment)
        transmission_formset = TransmissionEquipmentFormset(request.POST, instance=site)
        radio_formset = RadioEquipmentFormset(request.POST, instance=site)
        antenna_formset = AntennaEquipmentFormset(request.POST, instance=site)
        rectifier_form = RectifierEquipmentForm(request.POST, instance=rectifier_equipment)
        battery_form = BatteryEquipmentForm(request.POST, instance=battery_equipment)
        if form.is_valid():
            form.save()
        if team_lead_form.is_valid():
            team_lead_form.save()
        if owner_form.is_valid():
            owner_form.save()
        if baseband_form.is_valid():
            baseband_form.save()
        if radio_formset.is_valid():
            radio_formset.save()
        if transmission_formset.is_valid():
            transmission_formset.save()        
        if antenna_formset.is_valid():
            antenna_formset.save()
        if rectifier_form.is_valid():
            rectifier_form.save()
        if battery_form.is_valid():
            battery_form.save()
        messages.success(request, 'Site has been edited !!')
        return redirect('home')
    else:
        form = SiteForm(prefix='site', instance=site)
        team_lead_form = NTTeamLeadInformationForm(instance=team_lead)
        owner_form = HouseOwnerInformationForm(instance=owner)
        baseband_form = BasebandEquipmentForm(instance=baseband_equipment)
        transmission_formset = TransmissionEquipmentFormset(instance=site)
        radio_formset = RadioEquipmentFormset(instance=site)
        antenna_formset = AntennaEquipmentFormset(instance=site)
        rectifier_form = RectifierEquipmentForm(instance=rectifier_equipment)
        battery_form = BatteryEquipmentForm(instance=battery_equipment)
        context = {
            'site': site,
            'form': form,
            'team_lead_form': team_lead_form,
            'owner_form': owner_form,
            'baseband_form': baseband_form,
            'transmission_formset':transmission_formset,
            'radio_formset': radio_formset,
            'antenna_formset':antenna_formset,
            'rectifier_form': rectifier_form,
            'battery_form':battery_form
        }
        return render(request, 'core/site-edit.html', context)

def employeeInfo(request):
    query = request.GET.get('q', '')
    if query:        
        employees = EmployeeInformation.objects.filter(Q(employee_name__icontains=query) | Q(employee_id__icontains=query))
    else:
        employees = EmployeeInformation.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(employees, 20)
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)

    context = {
        'employees': employees,
        'query':query
    }
    return render(request, 'core/employees.html', context)

def employeeCreate(request):
    if request.method == 'POST':
        form = EmployeeInformationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team leader has been added !!')
            return redirect('core:employees')
        else:
            messages.error(request, 'Error adding Team leader !!')
    else:
        form = EmployeeInformationForm()
    context = {
        'form':form
    }
    return render(request, 'core/employee-create.html', context)

def employeeEdit(request, employee_id):
    employee = get_object_or_404(EmployeeInformation, employee_id=employee_id)
    if request.method == 'POST':
        form = EmployeeInformationForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team leader has been edited !!')
            return redirect('core:employees')
        else:
            messages.error(request, 'Error editing Team leader !!')
    else:
        form = EmployeeInformationForm(instance=employee)
    context = {
        'form':form
    }
    return render(request, 'core/employee-edit.html', context)

def employeeDelete(request, employee_id):
    employee = get_object_or_404(EmployeeInformation, employee_id=employee_id)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Team leader has been deleted !!')
        return redirect('core:employees')
    return render(request, 'core/employee-delete.html')

def ownerInfo(request):
    query = request.GET.get('q', '')
    if query: 
        owners = HouseOwnerInformation.objects.filter(Q(owner_name__icontains=query) | Q(site__site_id__icontains=query))
    else:
        owners = HouseOwnerInformation.objects.all()
    
    page = request.GET.get('page', 1)
    paginator = Paginator(owners, 20)
    try:
        owners = paginator.page(page)
    except PageNotAnInteger:
        owners = paginator.page(1)
    except EmptyPage:
        owners = paginator.page(paginator.num_pages)

    context = {
        'owners': owners,
        'query':query
    }
    return render(request,'core/owners.html',context)

def ownerEdit(request, id):
    owner = get_object_or_404(HouseOwnerInformation, id = id)
    if request.method == 'POST':
        form = HouseOwnerInformationForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            messages.success(request, 'House Owner has been edited !!')
            return redirect('core:owners')
        else:
            messages.error(request, 'Error editing house owner !!')
    else:
        form = HouseOwnerInformationForm(instance=owner)
    context = {
        'form':form
    }
    return render(request, 'core/owner-edit.html', context)
    
def error_404(request, exception):
    return render(request, 'error_404.html', status='404')

def error_500(request):
    return render(request, 'error_500.html', status='500')

def editProfile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been edited and now logged in !')
            return redirect('home')
    else:
        form = EditProfileForm(instance = request.user)
    context = {'form':form}
    return render(request, 'registration/editProfile.html', context)

def changePassword(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data = request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password has been changed and now logged in !')
            return redirect('home')
    else:
        form = ChangePasswordForm(user = request.user)
    context = {'form':form}
    return render(request, 'registration/changePassword.html', context)
