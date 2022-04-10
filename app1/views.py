from django.shortcuts import redirect, render
from app1.models import Owner

# Create your views here.
def main_page(request):
    return render(request,'mainpage.html')

def login(request):
    msg = ''
    if request.method == 'POST':
        owner_email = request.POST['owner_email']
        owner_password = request.POST['owner_password']

        owner_exist = Owner.objects.filter(owner_email = owner_email,owner_password = owner_password)

        if owner_exist:
            owner_data = Owner.objects.get(owner_email = owner_email,owner_password = owner_password)
            request.session['owner'] = owner_data.owner_id
            return redirect('app1:owner_home')
        else:
            msg = 'Unknown Owner..!'
    return render(request,'login.html',{'msg':msg})

def owner_home(request):
    return render(request,'owner_home.html')

def add_medicine(request):
    return render(request,'add_medicine.html')