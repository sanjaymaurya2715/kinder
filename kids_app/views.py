from django.shortcuts import render,redirect
from .models import Parent,Feedback,Contact,Content,Notification
from django.contrib import messages
# Create your views here.
def home(request):
    feedback_list=Feedback.objects.order_by('-date')[:6]

    notices = Notification.objects.order_by('-date')
    context={"feedback_key":feedback_list,"notices":notices}#created a Dictonary
    #select* from feedback order by date desc limit 10
    return render(request,'kids_app/html/index.html',context)# send it on index.html

def register(request):
    if request.method=="GET":
        return render(request, 'kids_app/html/registration.html')
    if request.method=="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        phone_no = request.POST["phone_no"]
        profile_pic = request.FILES["profile_pic"]
        parent = Parent.objects.create(name=name, email=email, password=password, phone=phone_no,pic=profile_pic)
        parent.save()
        messages.success(request, "Registration Successfull")
        return render(request, 'kids_app/html/registration.html')
def login(request):
    if request.method=="GET":
        return render(request, 'kids_app/html/login.html')
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        status =  Parent.objects.filter(email=email,password=password)
        if len(status)>0:
            request.session["session_key"]=email
            request.session["st_pic"]=status[0].pic.url
            return redirect("parent_home")
        else:
            messages.error(request, "Invalid Credentials")
            return render(request, 'kids_app/html/login.html')

def hindi_alphabet(request):
    return render(request, 'kids_app/kids/hindi_alphabet.html')
def english_alphabet(request):
    return render(request,"kids_app/kids/english_alphabet.html")
def numbers(request):
    return render(request,"kids_app/kids/numbers.html")

def animals(request):
    return render(request,"kids_app/kids/animals.html")
def color(request):
    return render(request,"kids_app/kids/color.html")

def parent_edit_profile(request):
  if request.method=="GET":
     parent_email=request.session["session_key"]##fetching the value from session
     parent_obj=Parent.objects.get(email=parent_email)
     context={
        "parent_key":parent_obj
     }
     return render(request,'kids_app/kids/parent_edit_profile.html',context)       
  if request.method=="POST":
       parent_email=request.session["session_key"]
       parent_obj=Parent.objects.get(email=parent_email)
       nm=request.POST["u_name"]
       ph=request.POST["u_phone"]
       parent_obj.name=nm
       parent_obj.phone=ph
       parent_obj.save()#it will modify the old object with new values
       messages.success(request,"Profile Updated Successfully")
       return redirect("parent_home")


def parent_dashboard(request):
    parent_email=request.session["session_key"]##fetching the value from session
    parent_obj=Parent.objects.get(email=parent_email)
    context={
        "parent":parent_obj
    }
    return render(request,"kids_app/kids/home.html",context)



def parent_feedback(request):

 if request.method=="GET":##HTTP PROTOCOL METHOD
    return render(request,'kids_app/kids/parent_feedback.html')
 if request.method=="POST":
    nm=request.POST["u_name"]##request.post is builti dict#
    #fetch the value from control
    em=request.POST["u_email"]
    rt=request.POST["rating"]
    rw=request.POST["u_review"]
    pic = request.session["st_pic"]
    FeedBack_obj =Feedback(name=nm,email=em,rating=rt,review=rw,pic=pic)#object of feedback model

    FeedBack_obj.save()#object save->it will map data with table column
    messages.success(request,"Thank You For Your FeedBack")
    return render(request,'kids_app/kids/parent_feedback.html')

def about_us(request):
    return render(request,'kids_app/html/about_us.html')
def gallery(request):
    return render(request,'kids_app/html/gallery.html')
def contact(request):
   if request.method=="GET":
        return render(request,"kids_app/kids/contact_us.html" )
   if request.method=="POST":
        nm=request.POST["u_name"] 
        em=request.POST["u_email"]
        ph=request.POST["u_phone"]
        qt=request.POST["u_question"]
        contact_obj=Contact(name=nm,email=em,phone=ph,question=qt)
        contact_obj.save() #object save ->it will map data with table column
        messages.success(request,"Thankyou for contact us ")
        return render(request,"kids_app/kids/contact_us.html" )
   
def parent_logout(request):
    del request.session["session_key"]
    return redirect("login")

# code for display content ..........


def poem(request):
    poem = Content.objects.filter(content_type="poem")
    context={"poem":poem}
    return render(request, 'kids_app/html/poem.html',context)
def story(request):
    story = Content.objects.filter(content_type="story")
    return render(request, 'kids_app/html/story.html',{'story':story})

