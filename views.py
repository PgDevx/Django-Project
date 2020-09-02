from django.shortcuts import render,redirect
from .models import Bank, Contact
from django.contrib.auth.models import User,auth
from django.contrib import messages

def home(request):
    return render(request,'home.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/login')

    else:
        return render(request,'login.html')

def about(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']

        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request,'about.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['confirm']

        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('/register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                user.save()
                phone = request.POST['phone']
                account_number = request.POST['account_number']
                account_balance = request.POST['account_balance']
                if Bank.objects.filter(account_number=account_number).exists():
                    messages.info(request, 'Use Different Account Number..!!')
                    return redirect('/register')
                newuser = Bank(phone=phone, account_number=account_number, account_balance=account_balance, name=user)
                newuser.save()
                messages.success(request,'User Created Successfully!!')
                return redirect('/login')

        else:
            messages.error(request,'Password not Matching...')
            return redirect('/register')
        redirect('/')

    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def add_money(request):
    if request.method=='POST':
        balance =int(request.POST['amount'])
        user = Bank.objects.get(name= request.user)
        user.account_balance = int(user.account_balance) + balance
        user.save()
        messages.success(request, 'Money Added Successfully!!')
        data=Bank.objects.filter(name = request.user)
        return render(request,'add_money.html', {'data':data})
    else:
        data=Bank.objects.filter(name = request.user)
        return render(request, 'add_money.html', {'data':data})

def withdraw(request):
    if request.method=='POST':
        balance = int(request.POST['amount'])
        user = Bank.objects.get(name = request.user)
        if(int(user.account_balance) ==0):
            messages.warning(request, 'No money in account')
            return redirect('/withdraw')
        elif(int(user.account_balance)<= balance):
            messages.warning(request, 'Withdrawl amount is greater than account balance')
            return redirect('/withdraw')
        else:
            user.account_balance = int(user.account_balance) - balance
            user.save()
            messages.success(request, 'Money Withdrawn Successfully!!')
            data = Bank.objects.filter(name=request.user)
            return render(request,'withdraw.html',{'data':data})
    else:
        data = Bank.objects.filter(name=request.user)
        return render(request, 'withdraw.html', {'data': data})

def transfer(request):
    if request.method=='POST':
        user1 = Bank.objects.get(name=request.user)
        balance = int(request.POST['amount'])
        accno = request.POST['accno']
        try:
            user2 = Bank.objects.get(account_number=accno)
        except Bank.DoesNotExist:
            user2 = None
        if user2 is None:
            messages.warning(request, 'Account Does not exist...!!')
            return redirect('/transfer')
        print("WHY",user1.account_number,accno)
        if user1.account_number == accno:
            print("YOYO")
            messages.warning(request, 'Invalid Input...!!')
            return redirect('/transfer')
        else:
            if (int(user1.account_balance) == 0):
                print("AHH YEAH")
                messages.warning(request, 'No money in account')
                return redirect('/transfer')
            if (int(user1.account_balance) <= balance):
                messages.warning(request, 'transfer amount is greater than account balance')
                return redirect('/transfer')
            user1.account_balance = int(user1.account_balance) - balance
            user1.save()
            user2.account_balance = int(user2.account_balance) + balance
            user2.save()
            messages.success(request, 'Money Transferred Successfully!!')
            data = Bank.objects.filter(name=request.user)
            return render(request, 'transfer.html', {'data': data})
    else:
        data = Bank.objects.filter(name=request.user)
        return render(request, 'transfer.html', {'data': data})

def delete(request):
    data = Bank.objects.get(name = request.user)
    data.delete()
    return redirect('/')

def change_paswd(request):
    if request.method=='POST':
        current = request.POST['opswd']
        new = request.POST['npswd']
        cnf_new = request.POST['cpswd']
        user = User.objects.get(id = request.user.id)
        un = user.username
        check = user.check_password(current)
        if check==False:
            messages.warning(request,'Incorrect Current Password')
            return redirect('/changepaswd')
        else:
            if(new==cnf_new):
                user.set_password(new)
                user.save()
                messages.success(request, 'Password changed successfully!!')
                user = User.objects.get(username=un)
                print("YOYO")
                auth.login(request,user)
                return redirect('/changepaswd')
    else:
        return render(request,"change_pwd.html")
