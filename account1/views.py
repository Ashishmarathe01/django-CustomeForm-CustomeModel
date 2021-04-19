from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .form import RestrionForm,Authenticates

# Create your views here.
def signup(request):
    context={}
    if request.method == 'POST':
        form = RestrionForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account )
            return redirect('home')
        else:
            context['restrion_form']=form
    else:
        form=RestrionForm()
        context['restrion_form']=form
    return render(request,'register.html',context)



def login_view(request):
    context={}
    user=request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST :
        form=Authenticates(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(email=email,password=password)
            if user:
                login(request,user)
                return redirect("home")
    else:
        form = Authenticates()
    context['login_form']=form
    return render(request,'login.html',context)

def home(request):
    return render(request,'home.html')
