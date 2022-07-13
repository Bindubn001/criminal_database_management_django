from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required
from .models import Crime,Prison,Criminal,Trial,Victim
from .forms import CrimeForm, PrisonForm, CriminalForm, TrialForm, VictimForm,CreateUserForm

def users_list_view(request):
    if not request.user.has_perm('auth.view_user'):
        raise PermissionDenied()

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')  
        context = {'form':form}
        return render(request, 'register.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
  
@login_required(login_url='login')
def home(request):    
    template = loader.get_template('home.html')
    context={ }
    return render(request, 'home.html', context=context)

def about_us(request):    
    template = loader.get_template('about_us.html')
    context={ }
    return render(request, 'about_us.html', context=context)

# Model Crime
@login_required(login_url='login')
def crimeList(request):  
    crimes = Crime.objects.all()  
    return render(request,"crime-list.html",{'crimes':crimes})

@login_required(login_url='login')
def crimeCreate(request):  
    if request.method == "POST":  
        form = CrimeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('crime-list')  
            except:  
                pass  
    else:  
        form = CrimeForm()  
    return render(request,'crime-create.html',{'form':form})  


@login_required(login_url='login')
@permission_required('auth.view_user')
def crimeUpdate(request, crime_id):  
    crime = Crime.objects.get(crime_id=crime_id)
    form = CrimeForm(initial={'crime_id': crime.crime_id, 'crime_date': crime.crime_date, 'crime_type': crime.crime_type, 
    'crime_level': crime.crime_level, 'location':crime.location, 'punishment':crime.punishment})
    if request.method == "POST":  
        form = CrimeForm(request.POST, instance=crime)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/crime-list')  
            except Exception as e: 
                pass    
    return render(request,'crime-update.html',{'form':form})

@login_required(login_url='login')
@permission_required('auth.view_user')
def crimeDelete(request, crime_id):
    crime = Crime.objects.get(crime_id=crime_id)
    try:
        crime.delete()
    except Exception:
        print(Exception)
        pass
    return redirect('crime-list')

#Model Prison
@login_required(login_url='login')
def prisonList(request):  
    prisons = Prison.objects.all()  
    return render(request,"prison-list.html",{'prisons':prisons})

@login_required(login_url='login')
def prisonCreate(request):  
    if request.method == "POST":  
        form = PrisonForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('prison-list')  
            except:  
                pass  
    else:  
        form = PrisonForm()  
    return render(request,'prison-create.html',{'form':form})  


@login_required(login_url='login')
@permission_required('auth.view_user')
def prisonUpdate(request, prison_id):  
    prison = Prison.objects.get(prison_id=prison_id)
    form = PrisonForm(initial={'prison_id': prison.prison_id, 'prison_name': prison.prison_name, 'city': prison.city,'prison_level': prison.prison_level})
    if request.method == "POST":  
        form = PrisonForm(request.POST, instance=prison)  
        if form.is_valid():   
            try:  
                form.save() 
                model = form.instance
                return redirect('/prison-list')  
            except Exception as e: 
                pass    
    return render(request,'prison-update.html',{'form':form})

@login_required(login_url='login')
@permission_required('auth.view_user')
def prisonDelete(request, prison_id):
    prison = Prison.objects.get(prison_id=prison_id)
    try:
        prison.delete()
    except Exception:
        print(Exception)
        pass
    return redirect('prison-list')

# Model Criminal
@login_required(login_url='login')
def criminalList(request):  
    criminals = Criminal.objects.all()  
    return render(request,"criminal-list.html",{'criminals':criminals})  

@login_required(login_url='login')
def criminalCreate(request):  
    if request.method == "POST":  
        form = CriminalForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('criminal-list')  
            except:  
                pass  
    else:  
        form = CriminalForm()  
    return render(request,'criminal-create.html',{'form':form}) 


@login_required(login_url='login')
@permission_required('auth.view_user')
def criminalUpdate(request, criminal_id):  
    criminal = Criminal.objects.get(criminal_id=criminal_id)
    form = CriminalForm(initial={'criminal_id': criminal.criminal_id, 'cname ': criminal.cname, 'birthdate': criminal.birthdate, 
    'address': criminal.address, 'dependent_name': criminal.dependent_name, 'prison_id': criminal.prison_id, 'prison_id': criminal.prison_id, 
    'prison_term': criminal.prison_term})
    if request.method == "POST":  
        form = CriminalForm(request.POST, instance=criminal)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/criminal-list')  
            except Exception as e: 
                pass    
    return render(request,'criminal-update.html',{'form':form})  

@login_required(login_url='login')
@permission_required('auth.view_user')
def criminalDelete(request,criminal_id):
    criminal = Criminal.objects.get(criminal_id=criminal_id)
    try:
        criminal.delete()
    except:
        pass
    return redirect('criminal-list')

# Model Trial
@login_required(login_url='login')
def trialList(request):  
    trials = Trial.objects.all()  
    return render(request,"trial-list.html",{'trials':trials})  

@login_required(login_url='login')
def trialCreate(request):  
    if request.method == "POST":  
        form = TrialForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('trial-list')  
            except:  
                pass  
    else:  
        form = TrialForm()  
    return render(request,'trial-create.html',{'form':form})  

@login_required(login_url='login')
@permission_required('auth.view_user')
def trialUpdate(request, case_id):  
    trial = Trial.objects.get(case_id=case_id)
    form = TrialForm(initial={'case_id': trial.case_id, 'evidence': trial.evidence, 'section_of_law': trial.section_of_law,
    'case_status': trial.case_status, 'lawyer_id': trial.lawyer_id, 'criminal': trial.criminal, 'victim': trial.victim, 
    'crime': trial.crime})
    if request.method == "POST":  
        form = TrialForm(request.POST, instance=trial)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/trial-list')  
            except Exception as e: 
                pass    
    return render(request,'trial-update.html',{'form':form})  

@login_required(login_url='login')
@permission_required('auth.view_user')
def trialDelete(request, case_id):
    trial = Trial.objects.get(case_id=case_id)
    try:
        trial.delete()
    except:
        pass
    return redirect('trial-list')

# Model Victim
@login_required(login_url='login')
def victimList(request):  
    victims = Victim.objects.all()  
    return render(request,"victim-list.html",{'victims':victims})  

@login_required(login_url='login')
def victimCreate(request):  
    if request.method == "POST":  
        form = VictimForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('victim-list')  
            except:  
                pass  
    else:  
        form = VictimForm()  
    return render(request,'victim-create.html',{'form':form}) 


@login_required(login_url='login')
@permission_required('auth.view_user')
def victimUpdate(request, victim_id):  
    victim = Victim.objects.get(victim_id=victim_id)
    form = VictimForm(initial={'victim_id': victim.victim_id, 'vname': victim.vname, 'age': victim.age,
    'address': victim.address, 'phone': victim.phone, 'crime': victim.crime})
    if request.method == "POST":  
        form = VictimForm(request.POST, instance=victim)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/victim-list')  
            except Exception as e: 
                pass    
    return render(request,'victim-update.html',{'form':form})  

@login_required(login_url='login')
@permission_required('auth.view_user')
def victimDelete(request, victim_id):
    victim = Victim.objects.get(victim_id=victim_id)
    try:
        victim.delete()
    except:
        pass
    return redirect('victim-list')