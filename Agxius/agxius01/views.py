from django.shortcuts import render
from django.http import HttpResponse
from .models import FarmDetail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from . import conf

# Create your views here.
def run(request):
    token=conf.token
    return HttpResponse(token)

def sign_up_func(request):
    return render(request, 'signup.html')


@csrf_exempt
def User_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['password']
        pass2 = request.POST['password2']

        if len(username) < 6:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('signup')

        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        try:

            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, " User been successfully created")
            return redirect('login')
        except Exception as e:
            messages.error(request, "Something went wrong! try again..")
            return redirect('signup')

    else:
        return HttpResponse("404 - Not found")



def login_func(request):
    return render(request, 'login.html')



@csrf_exempt
def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, 'Successfully logged in')
            # return render(request, 'profile2.html')
            request.session['is_logged']=True

            field_details = FarmDetail.objects.filter(username=request.user.username)
            counter=0
            for i in field_details:
                counter=counter+1
            print(counter,"counter ")
            if counter==0:
                return redirect('profile')
            else:
                return redirect('dash')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login')

    return HttpResponse('404 Not Found')


def user_logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('login')


def profile_page(request):

    if request.session.has_key('is_logged'):

        # return render(request, 'profile_page1.html')
        # return render(request, 'profile2.html')

        mapbox_token=str(conf.token)
        mapbox_token=json.dumps(mapbox_token)


        field_details = FarmDetail.objects.filter(username=request.user.username)
        nfields=((len(field_details)))

        context = {'nfields':range(nfields),
            'map_token': mapbox_token,
        }
        return render(request, 'profile.html',context)
    else:
        return redirect('login')


import json

@csrf_exempt
def search_view(request):
    field_details=FarmDetail.objects.filter(username=request.user.username)
    for i in field_details:
        print(i.area,)
    return HttpResponse(field_details)

# store profile data func starts here

# from .models import FarmDetail
# import pandas as pd
# 
# @csrf_exempt
# def store_profile_data(request):
#     # count = request.POST['count']
#     #
#     # print("hello")
#     #
#     # print("count status ", count)
# 
#     if request.method == 'POST':
# 
# 
#         commodity = request.POST['commodity']
#         sowing_date = request.POST['sowingdate']
#         cords=request.POST['cords']
#         area=request.POST['polygonarea']
#         cords=json.loads(cords)
#         cords = pd.DataFrame.from_dict(cords)
# 
#         field_map=cords['features'][0]['geometry']['coordinates'][0]
# 
#         username=request.user.username
#         crop_info=FarmDetail.objects.filter(username=request.user.username).filter(commodity=commodity)
# 
# 
#         counter=0
#         for i in crop_info:
#             counter=counter+1
#             print(i.commodity)
# 
#         if counter==0:
#             counter=counter+1
# 
# 
#         print(counter,'outside loop')
#         field_id = request.user.username+"_"+commodity +"_"+ str(counter)+"_"+(area)
#         print(field_id)
# 
# 
#         b = FarmDetail(username=username,commodity=commodity, sowing_date=sowing_date,field_map=field_map,area=area,field_id=field_id)
#         b.save()
#         print(username,commodity,sowing_date,field_map)
#   
#         prod=FarmDetail.objects.filter(username=request.user.username)
#         print("lenth : " , len(prod))
# 
#   
#         context = {
#                 'username':username,
#             'commodity':commodity,
#             'sowing_date':sowing_date,
#             'area':area,
#             'field_map':field_map,
#         }
#     return render(request,'profile_data.html',context)
# 

# potato_usern_area_counter
from pandas import DataFrame
# import json
# def show_dash1(request):
#     print(request.user.username)
#     field_details = FarmDetail.objects.filter(username=request.user.username)
#     flen=len(field_details)
#     data=[]
#     first_cords=[]
#     for i in field_details:
#         data.append(i)
#         first_cords.append(i.field_map)
#     first_cords=(str(first_cords).replace('[',''))
#
#     first_cords=(str(first_cords).replace(']',''))
#     first_cords = (str(first_cords).replace("'", ''))
#     first_cords = first_cords.split(',')
#     # print(list(first_cords))
#     map_center=[]
#     for i in list(first_cords):
#         map_center.append(i)
#
#     print(map_center[:2])
#     print(data)
#         # print(i.field_id,i.area,i.username,i.commodity,i.sowing_date,i.field_map)
#     dataDictionary = {
#         'hello': 'World',
#         'geeks': 'forgeeks',
#         'ABC': '123',
#         'list': ['geeks', 4, 'geeks'],
#         'dictionary': {'you': 'can', 'send': 'anything', 3: 1}
#     }
#
#     dataJSON = json.dumps(dataDictionary)
#     context = {
#         'field_details': data,
#         'flen':range(flen),
#         'data': dataJSON,
#     #     'commodity': commodity,
#     #     'sowing_date': sowing_date,
#     #     'area': area,
#     #     'field_map': field_map,
#     }
#     # return render(request,'dashbord1.html',context)
#
#     # dataDictionary = {
#     #     'hello': 'World',
#     #     'geeks': 'forgeeks',
#     #     'ABC': '123',
#     #     'list': ['geeks', 4, 'geeks'],
#     #     'dictionary': {'you': 'can', 'send': 'anything', 3: 1}
#     # }
#
#     # dataJSON = json.dumps(dataDictionary)
#     # return render(request, 'dash2.html', {'data': dataJSON})
#     return render(request, 'dash2.html',context)



import pandas as pd
def show_dash(request):
    if request.session.has_key('is_logged'):
        field_details = FarmDetail.objects.filter(username=request.user.username)
        record={
            'field_id':field_details[0].field_id,
            'commodity':field_details[0].commodity,
            'sowing_date':field_details[0].sowing_date,
            'area':field_details[0].area,
            'username':field_details[0].sowing_date,
            'field_map':field_details[0].field_map,

        }
        # print(record)

        records=field_details[1:]
        # print(records)


        # getting first_coordinates of user and field ids

        cordinates=[]

        field_ids=[]

        cords_for_draw_polygon=[]

        for i in field_details:
            field_ids.append(i.field_id)
            cords_for_draw_polygon.append(i.field_map)
        # print('field_id : ',field_ids)


        # getting first lattitude and longitude coordinates

        for i in field_details:
            # print(i.field_map)
            first_cords = (str(i.field_map).replace('[', ''))
            first_cords = (str(first_cords).replace(']', ''))
            first_cords = (str(first_cords).replace("'", ''))
            first_cords=(first_cords.split(','))
            cordinates.append(first_cords[:2])

        # print(cordinates[0])

        dict = {'cordinates': cordinates,
                'field_ids': field_ids,
                'field_details':field_details

                }


        field_details = (list(field_details.values()))
        field_details = json.dumps(field_details)
        # print('after dumps',type(field_details))
        # field_details = field_details.replace("'", '"')
        #


        cent=[]


        # create list of dicts tha append in cent(center for make div active)

        for i in cordinates:
            res = {"center": i ,
                   'zoom': int(15.5),
                   'pitch': int(20),
                   'bearing': int(27),
                   }


            cent.append(res)


        # created nested dict with fieldids and cent

        js_data = {field_ids[i]: cent[i] for i in range(len(field_ids))}
        js_data=json.dumps(js_data)

        # created nested list of all feilds coordinates to draw polygon

        cords_for_draw_polygon=str(cords_for_draw_polygon).replace("'","")


        draw_cords = cords_for_draw_polygon
        draw_cords = json.dumps(draw_cords)

        # print(draw_cords)

        mapbox_token = str(conf.token)
        mapbox_token = json.dumps(mapbox_token)

        context = {
            'record1': record,
            'records': records,
            'field':field_details,
            'js_data':js_data,
            'draw_cords': draw_cords,
            'map_token': mapbox_token,
        }




        # return render(request, 'dash3.html',context)
        return render(request, 'dash.html', context)

    else:
        return redirect('login')





from .models import FarmDetail
import pandas as pd


@csrf_exempt
def store_profile_data(request):


    if request.method == 'POST':

        commodity = request.POST['commodity']
        sowing_date = request.POST['sowingdate']
        cords = request.POST['cords']
        area = request.POST['polygonarea']
        cords = json.loads(cords)
        cords = pd.DataFrame.from_dict(cords)

        field_map = cords['features'][0]['geometry']['coordinates'][0]

        username = request.user.username
        crop_info = FarmDetail.objects.filter(username=request.user.username).filter(commodity=commodity)
        print('len of crop    : ',len(crop_info))

        counter = len(crop_info)
        print("counter before loop : ",counter)


        if counter==0:
            counter=1
            field_id = request.user.username + "_" + commodity + "_" + str(counter) + "_" + (area)
        else:
            counter = len(crop_info)+1
            field_id = request.user.username + "_" + commodity + "_" + str(counter) + "_" + (area)




        print(counter, 'outside loop')
        # field_id = request.user.username + "_" + commodity + "_" + str(counter) + "_" + (area)
        print(field_id)

        b = FarmDetail(username=username, commodity=commodity, sowing_date=sowing_date, field_map=field_map, area=area,
                       field_id=field_id)
        b.save()
        # print(username, commodity, sowing_date, field_map)

        prod = FarmDetail.objects.filter(username=request.user.username)

        # print("lenth : ", len(prod))





        context = {
            'username': username,
            'commodity': commodity,
            'sowing_date': sowing_date,
            'area': area,
            'field_map': field_map,

        }
    return redirect('dash')

