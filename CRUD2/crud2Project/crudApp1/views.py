from django.shortcuts import render, redirect
from .models import Profile
from django.contrib import messages
import os


# Create your views here.
def Home(request):
    return render(request, 'Home.html')


def profile(request):
    if request.method == 'POST':
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        E_mail = request.POST['E_mail']
        Phon_number = request.POST['Phon_number']
        Age = request.POST['Age']
        Gender = request.POST['Gender']
        NID_Number = request.POST['NID_Number']
        Address = request.POST['Address']
        Image = request.FILES.get('Image')
        if Image:
            a = Profile.objects.create(First_Name=First_Name, Last_Name=Last_Name, E_mail=E_mail, Phon_number=Phon_number,
                                Age=Age, Gender=Gender, NID_Number=NID_Number, Address=Address, Image=Image)
            a.save()
            return redirect('profile')
        else:
            a = Profile.objects.create(First_Name=First_Name, Last_Name=Last_Name, E_mail=E_mail, Phon_number=Phon_number,
                                    Age=Age, Gender=Gender, NID_Number=NID_Number, Address=Address)
            a.save()
            return redirect('profile')
    return render(request, 'profile.html')


def log(request):
    return render(request, 'login.html')


def reg(request):
    return render(request, 'Ragistration.html')


def showBProfile(request,id):
    Prof =Profile.objects.get(id=id)
    return render(request,'BIGProfile.html',locals())

#Search
def alldataa(request):
    src =request.GET.get('src')#search value or item we use it
    if src:
        allProfile =Profile.objects.filter(First_Name__icontains = src)
    
    elif src=='none':
        allProfile = Profile.objects.all()  
    else:
        allProfile = Profile.objects.all()
    print(allProfile)
    context ={
        'Prof' :allProfile,
        'src' :src
        }
    return render(request,'showdata.html',context)


#Delete proffile
def Deleteprofile( request, id):
    delete_Prof = Profile.objects.get(id = id) ##condition delet profile on media.To rsolve memory speace.
    if delete_Prof.Image!='default/default.jpg':
        os.remove(delete_Prof.Image.path)
    delete_Prof.delete()
    messages.success(request, 'Profile Has been deleted.')
    return  redirect('ALL')

#update section
def update (request ,id):
    updatep_Prof = Profile.objects.get(id = id)
    if request.method == 'POST':
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        E_mail = request.POST['E_mail']
        Phon_number = request.POST['Phon_number']
        Age = request.POST['Age']
        Gender = request.POST['Gender']
        NID_Number = request.POST['NID_Number']
        Address = request.POST['Address']
        Image = request.FILES.get('Image')
        
        
        if updatep_Prof.Image!='default/default.jpg':
            os.remove(updatep_Prof.Image.path)
        updatep_Prof.First_Name = First_Name
        updatep_Prof.Last_Name = Last_Name
        updatep_Prof.E_mail = E_mail
        updatep_Prof.Phon_number = Phon_number
        updatep_Prof.Age = Age
        updatep_Prof.Gender = Gender
        updatep_Prof.NID_Number = NID_Number
        updatep_Prof.Address = Address
        updatep_Prof.Image = Image
        updatep_Prof.save()
        return redirect('ALL')
    return render(request, 'update.html',locals())

    
            
