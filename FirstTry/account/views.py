from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.urls  import reverse

from django.contrib.auth.models import User

from account.models import UserInfo
from item.models import item

from . import forms
from item import forms as item_forms


def user_profile(request,name):
    userdetail=User.objects.get(username=name)
    items=item.objects.filter(user=userdetail)
    user=User.objects.filter(username=name)
    infos=UserInfo.objects.all()
    for info in infos:
        if info.user.username==name:
            pic       = info.profile_pic
            city      = info.city
            gender    = info.gender
            country   = info.country
            address   = info.address
            p_no      = info.phone_number
            date_time = info.date_time
            break
    context_dict={
        'items':items,
        'name':name,
        'pic':pic,
        'city':city,
        'gender':gender,
        'country':country,
        'address':address,
        'p_no':p_no,
        'date_time':date_time,
    }

    return render(request,'account/profile_user.html',context=context_dict)

def post(request,name):
    #here name is name of user
    form=item_forms.ItemPostForm()
    items=item.objects.all()
    length=len(items)
    if request.method=="POST":
        form=item_forms.ItemPostForm(request.POST,request.FILES)
        if form.is_valid():
            user=request.user
            item_name=form.cleaned_data['item_name']
            category=form.cleaned_data['category']
            price_expected=form.cleaned_data['price_expected']
            description=form.cleaned_data['description']
            old=form.cleaned_data['old']
            item_image=form.cleaned_data['item_image']
            item_post=item(
                user=user,
                item_name=item_name,
                category=category,
                price_expected=price_expected,
                description=description,
                old=old,
                item_image=item_image
            )
            item_post.save()
            messages.success(request, f'post created for {name}')
            # redirect('post')

            print("Button is pressed")
    
    return render(request,'posts_base/post_base.html',{'form':form,'range':range(len(items)),'length':length,'items':item.objects.all()})

    # return render(request,'profile_page/index.html',{'form':form,'range':range(10), 'user': request.user})

#posts_base/post_base.html

@login_required
def profile(request):
    return HttpResponseRedirect(reverse('post',args=[request.user.username]))


def home(request):
    CATEGORY=[
        'electronics',
        'clothing',
        'furniture',
        'accessories',
        'automobile',
        'stationary'
    ]
    context_dict={
        'elect':'electronics',
        'cloth':'clothing',
        'furn':'furniture',
        'access':'accessories',
        'auto':'automobile',
        'stat':'stationary'
    }
    return render(request, 'home.html',context=context_dict)


def register(request):
    registered=False

    django_form = forms.UserRegisterForm()
    my_form=forms.ProfileCompleteForm()

    if request.method == "POST":
        django_form = forms.UserRegisterForm(request.POST)
        my_form=forms.ProfileCompleteForm(request.POST)

        if django_form.is_valid() and my_form.is_valid():
            user=django_form.save()
            user.set_password(user.password)
            user.save()

            profile=my_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()
            registered=True

            # messages.success(request, f'account created for {username}')

            print("VALIDATION SUCCESS")
            return redirect('login')

    return render(request, 'account/register.html', {
                                'django_form':django_form,
                                'my_form':my_form,
                                'registered':registered
                                     }
                )

# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect('home')

# def user_login(request):

#     if request.method=="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')

#         user=authenticate(username=username,password=password)
        
#         if user:
#             if user.is_active:
#                 login(request,user)
#                 return redirect('/home/post/'+username+'/')
#                 # return HttpResponseRedirect(reverse(post,args=[username]))
#                 # return HttpResponseRedirect(reverse(''))
#             else :
#                 HttpResponse("Account not active")
#         else:
#             print("SOMEONE TRIED TO LOGIN AND FAILED")
#             return HttpResponse("Invalid Login details supplied")
    
#     else:
#         return render(request,'account/login.html',{})

