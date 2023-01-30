from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from .utils import TokenGenerator,generate_token
from django.utils.encoding import force_bytes,force_text
from django.core.mail import EmailMessage
from django.conf import settings
from django.views.generic import View
# Create your views here.    

def operatesignup(request):
    if request.method == "POST":

        get_email = request.POST['email']
        get_password = request.POST['pass1']
        get_confirm_password = request.POST['pass2']
        if get_password != get_confirm_password:
        
            messages.info(request,"Password not matching")
            return redirect("/authen/signup/")

        try:
            if User.objects.get(username=get_email):
                messages.warning(request,"User already exist")
                return redirect('/authen/signup/')
        except Exception as identifier:
            pass
        myuser = User.objects.create_user(get_email,get_email,get_password)
        myuser.is_active=True
        myuser.save()


    # emailing for activation
        # email_subject="Verify your account"
        # message = render_to_string('activate.html', {
        #     'user':myuser,
        #     'domain':'127.0.0.1:8000', 
        #     'uid':urlsafe_base64_encode(force_bytes(myuser.pk)) ,
        #     'token':generate_token.make_token(myuser),


        # })
        
        # email_message = EmailMessage(
        # 'Hello',
        # 'Body goes here',
        #  settings.EMAIL_HOST_USER,
        # [get_email],)       
        # email_message.send()
        # messages.success(request,"Verification link sent to your email")
        # # return redirect('/authen/login/')







        # messages.success(request,'User is Created Please Login')
        return redirect('/authen/login/')
    return render(request,'authentications/signup.html')



#code to activate the account
# class ActivateAccount(View):
#     def get(self,request,uidb64,token):
#         try:
#             uid=force_text(urlsafe_base64_decode(uidb64))
#             myuser=User.objects.get(pk=uid)
#         except Exception as identifier:
#             myuser = None
#         if myuser is not None and generate_token.check_token(myuser,token):
#             myuser.is_active=True
#             myuser.save()
#             messages.info(request,"Account activated Successfully")
#             return redirect('/authen/login')
#         return render(request,'activatefail.html')




def operatelogin(request):

        if request.method == "POST":
            get_email = request.POST.get('email')
            get_password = request.POST.get('pass1')
            myuser = authenticate(username=get_email,password=get_password)
                
            if myuser is not None :
                login(request,myuser)
                messages.success(request,"login successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid Credentials")
                

        return render(request,'authentications/login.html')
     
def operatelogout(request):
    logout(request)
    messages.info(request,"Logout successfully")



    return redirect('/authen/login')