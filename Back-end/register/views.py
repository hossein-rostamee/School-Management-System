from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from .serializers import VolunteerSerializer, StudentSerializer
from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework.decorators import action
import json
from django.db.models import F
from django.shortcuts import get_object_or_404
from .models import Volunteer
import mimetypes
import os
from .models import Users, Class, Student, Volunteer
from melipayamak import Api
import datetime

def user_auth( username, password, role ) : 
    user = Users.objects.filter( user_name = username ).values()
    if user and user[0][ 'user_password' ] == password and user[0][ 'user_role' ] == role : 
        return True
    else :
        return False

def user_image_auth( username, id ) :
    student = Student.objects.filter( user_id = username ).values()
    print( student )
    if student[0] and student[0]['id'] == id : 
        return True
    else : 
        return False


@csrf_exempt
def index(request):
    if request.method == 'POST':
        fullName                               = request.POST.get('fullName') 
        fatherName                             = request.POST.get('fatherName') 
        birthCity                              = request.POST.get('birthCity') 
        schoolName                             = request.POST.get('schoolName') 
        classNumber                            = request.POST.get('classNumber') 
        passField                              = request.POST.get('passField') 
        birthDate                              = request.POST.get('birthDate') 
        nationalCode                           = request.POST.get('nationalCode')
        fatherPhoneNumber                      = request.POST.get('fatherPhoneNumber')
        motherPhoneNumber                      = request.POST.get('motherPhoneNumber')
        schoolShift                            = request.POST.get('schoolShift')
        religion                               = request.POST.get('religion')
        grade                                  = request.POST.get('grade')
        whatIsParentsGrade                     = request.POST.get('whatIsParentsGrade') 
        howDidGetToKnowQuranSessions           = request.POST.get('howDidGetToKnowQuranSessions') 
        WhoEncourageYouToComeQuranSessions     = request.POST.get('WhoEncourageYouToComeQuranSessions') 
        WhichSessionDidYouParticipate          = request.POST.get('WhichSessionDidYouParticipate') 
        WhichSportsDoYouInterestedIn           = request.POST.get('WhichSportsDoYouInterestedIn') 
        WhichBooksDoYouRecentlyRead            = request.POST.get('WhichBooksDoYouRecentlyRead') 
        WhichBooksDoYouLikeToRead              = request.POST.get('WhichBooksDoYouLikeToRead') 
        WriteTheNamesOfYourTwoFriends          = request.POST.get('WriteTheNamesOfYourTwoFriends') 
        WhichSessionDidYouParticipate          = request.POST.get('WhichSessionDidYouParticipate') 
        WhichCulturalActivitiesDoYouInterested = request.POST.get('WhichCulturalActivitiesDoYouInterested') 
        WhichFieldsDoYouTalentedIn             = request.POST.get('WhichFieldsDoYouTalentedIn') 
        HowMuchDoYouFamiliarWithQuran          = request.POST.get('HowMuchDoYouFamiliarWithQuran') 
        WhichCommitionsDoYouInterestedIn       = request.POST.get('WhichCommitionsDoYouInterestedIn') 
        HowDoYouSpendYourHolidays              = request.POST.get('HowDoYouSpendYourHolidays') 
        WhatLevelofSkillDoYouHaveInCulturalActivity = request.POST.get('WhatLevelofSkillDoYouHaveInCulturalActivity') 
        personelPhoto                          = request.FILES.get('personelPhoto') 
        birthCertificate                       = request.FILES.get('birthCertificate') 
        volunteer = Volunteer(  
            fullName                                = fullName                              ,
            fatherName                              = fatherName                            ,
            birthCity                               = birthCity                             ,
            schoolName                              = schoolName                            ,
            classNumber                             = classNumber                           ,
            passField                               = passField                             ,
            birthDate                               = birthDate                             ,
            nationalCode                            = nationalCode                          ,
            fatherPhoneNumber                       = fatherPhoneNumber                     ,
            motherPhoneNumber                       = motherPhoneNumber                     ,
            schoolShift                             = schoolShift                           ,
            religion                                = religion                              ,
            grade                                   = grade                                 ,
            whatIsParentsGrade                      = whatIsParentsGrade                    ,
            howDidGetToKnowQuranSessions            = howDidGetToKnowQuranSessions          ,
            WhoEncourageYouToComeQuranSessions      = WhoEncourageYouToComeQuranSessions    ,
            WhichSessionDidYouParticipate           = WhichSessionDidYouParticipate         ,
            WhichSportsDoYouInterestedIn            = WhichSportsDoYouInterestedIn          ,
            WhichBooksDoYouRecentlyRead             = WhichBooksDoYouRecentlyRead           ,
            WriteTheNamesOfYourTwoFriends           = WriteTheNamesOfYourTwoFriends         ,
            WhichCulturalActivitiesDoYouInterested  = WhichCulturalActivitiesDoYouInterested,
            WhichFieldsDoYouTalentedIn              = WhichFieldsDoYouTalentedIn            ,
            WhichBooksDoYouLikeToRead               = WhichBooksDoYouLikeToRead             ,
            WhatLevelofSkillDoYouHaveInCulturalActivity = WhatLevelofSkillDoYouHaveInCulturalActivity ,
            HowMuchDoYouFamiliarWithQuran           = HowMuchDoYouFamiliarWithQuran         ,
            WhichCommitionsDoYouInterestedIn        = WhichCommitionsDoYouInterestedIn      ,
            HowDoYouSpendYourHolidays               = HowDoYouSpendYourHolidays             ,
            personelPhoto                           = personelPhoto                         ,
            birthCertificate                        = birthCertificate                      ,
            date                                    = datetime.datetime.now()
        )
        volunteer.save()
        return HttpResponse("received")
    else:
        return HttpResponse("denied")


class VolunteerView(viewsets.ModelViewSet):
    serializer_class = VolunteerSerializer
    queryset = Volunteer.objects.all()

class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def list( self, request, username, password ) :
        serializer = self.serializer_class( self.queryset, many=True )
    
        if user_auth( username, password ) :
            return JsonResponse( list( serializer.data ), safe=False  )
        else : 
            return HttpResponse( 'denied' )
        

def handleImage( object, id, type ) :
    if   object == 'v' :
        o = get_object_or_404(Volunteer, id=id)
    elif object == 's' :
        o = get_object_or_404(Student, id=id)
    else :
        return HttpResponseBadRequest
    
    image = getattr( o, type )
    file_path = image.path
    content_type = mimetypes.guess_type(file_path)[0]
    
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type=content_type)
        response["Access-Control-Allow-Origin"] = "*"
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
        return response   

def download_image_birthCertificate(request, id, object, username, password ):
    if user_auth( username, password, 1330 ) : 
        return handleImage( object, id, 'birthCertificate' )
    elif user_auth( username, password, 1540 ) :
        if user_image_auth( username, id ) : 
            return handleImage( object, id, 'birthCertificate' )
        else : 
            return HttpResponse( "denied" )
    else :
        return HttpResponse( "denied" )
    
def download_image_personelPhoto(request, id, object, username, password ):
    if user_auth( username, password, 1330 ) : 
        return handleImage( object, id, 'personelPhoto' )
    elif user_auth( username, password, 1540 ) :
        if user_image_auth( username, id ) : 
            return handleImage( object, id, 'personelPhoto' )
        else : 
            return HttpResponse( 'denied' )
    else : 
        return HttpResponse( 'denied' )
    
    
@csrf_exempt
def login(request):
    requested_user_name = request.POST.get('username')
    requested_user_password = request.POST.get('password')
    user = Users.objects.filter( user_name = requested_user_name ).values()
    
    def numbers_to_strings(argument):
        switcher = {
            1330: "HumanResources",
            1540: "Student",
            1710: "Teacher",
        }
        return switcher.get(argument, "nothing")

    if user and user[0]['user_password'] == requested_user_password:
        role_name = numbers_to_strings( user[0]['user_role'] )
        return HttpResponse("accepted" + f"/{role_name}")
    else:
        return HttpResponse("denied/")

def getClassIds( request, username, password ) : 
    if user_auth( username, password, 1330 ) :
        if request.method == 'GET' : 
            classesList = list( Class.objects.values( 'id', 'name' ) )
            return JsonResponse(classesList, safe=False)
        else :
            return HttpResponseBadRequest
    else :
        return HttpResponse( 'denied' )
    
@csrf_exempt
def registerStudent( request, username, password ) :
    if user_auth( username, password, 1330 ) :
        if request.method == 'POST' : 
            
            class_id     = request.POST[ 'class_id'     ] 
            volunteer_id = request.POST[ 'volunteer_id' ]

            volunteer = Volunteer.objects.filter( id = volunteer_id ).values()
            volunteer = list( volunteer )
            volunteer = volunteer[0]


            u = Users(
                user_name     = f'u1402{ volunteer_id }'      ,
                user_password = volunteer.get( 'passField' )  ,
                user_role     = 1540                          ,
            )


            u.save()

            c = Class.objects.get( id = class_id )

            s = Student(
                fullName                                = volunteer.get( 'fullName'          )                     ,
                fatherName                              = volunteer.get( 'fatherName'        )                     ,
                birthCity                               = volunteer.get( 'birthCity'         )                     ,
                schoolName                              = volunteer.get( 'schoolName'        )                     ,
                classNumber                             = volunteer.get( 'classNumber'       )                     ,
                birthDate                               = volunteer.get( 'birthDate'         )                     ,
                nationalCode                            = volunteer.get( 'nationalCode'      )                     ,
                fatherPhoneNumber                       = volunteer.get( 'fatherPhoneNumber' )                     ,
                motherPhoneNumber                       = volunteer.get( 'motherPhoneNumber' )                     ,
                schoolShift                             = volunteer.get( 'schoolShift'       )                     ,
                religion                                = volunteer.get( 'religion'          )                     ,
                grade                                   = volunteer.get( 'grade'             )                     ,
                personelPhoto                           = volunteer.get( 'personelPhoto'     )                     ,
                birthCertificate                        = volunteer.get( 'birthCertificate'  )                     ,
                passField                               = volunteer.get( 'passField'         )                     ,
                whatIsParentsGrade                      = volunteer.get( 'whatIsParentsGrade')                     ,
                howDidGetToKnowQuranSessions            = volunteer.get( 'howDidGetToKnowQuranSessions')           ,
                WhoEncourageYouToComeQuranSessions      = volunteer.get( 'WhoEncourageYouToComeQuranSessions')     ,
                WhichSessionDidYouParticipate           = volunteer.get( 'WhichSessionDidYouParticipate')          ,
                WhichSportsDoYouInterestedIn            = volunteer.get( 'WhichSportsDoYouInterestedIn')           ,
                WhichBooksDoYouRecentlyRead             = volunteer.get( 'WhichBooksDoYouRecentlyRead')            ,
                WhichBooksDoYouLikeToRead               = volunteer.get( 'WhichBooksDoYouLikeToRead')              ,
                WriteTheNamesOfYourTwoFriends           = volunteer.get( 'WriteTheNamesOfYourTwoFriends')          ,
                WhichCulturalActivitiesDoYouInterested  = volunteer.get( 'WhichCulturalActivitiesDoYouInterested') ,
                WhichFieldsDoYouTalentedIn              = volunteer.get( 'WhichFieldsDoYouTalentedIn')             ,
                HowMuchDoYouFamiliarWithQuran           = volunteer.get( 'HowMuchDoYouFamiliarWithQuran')          ,
                WhatLevelofSkillDoYouHaveInCulturalActivity  = volunteer.get( 'WhatLevelofSkillDoYouHaveInCulturalActivity')          ,
                WhichCommitionsDoYouInterestedIn        = volunteer.get( 'WhichCommitionsDoYouInterestedIn')       ,
                HowDoYouSpendYourHolidays               = volunteer.get( 'HowDoYouSpendYourHolidays')              ,
                date                                    = volunteer.get( 'date' )                                  ,
                user              = u                                                                              ,
                classitem         = c                                                                              ,
            )

            s.save()

            #########

            return HttpResponse( "saved" )
    else : 
        return HttpResponse( 'denied' ) 
    

@csrf_exempt
def delete_user(request, userid, username, password ):
    if user_auth( username, password, 1330 ) :
        if request.method == 'DELETE' : 
            user = Users.objects.filter( user_name = userid )
            user.delete()
            return HttpResponse( "deleted" )
        else:
            return HttpResponseBadRequest
    else :
        return HttpResponse( 'denied' )


def listStudents( request, op, stu_id, username, password ) :
    if user_auth( username, password, 1330 ) :
        if op == 'get' and request.method == 'GET' :
            students = Student.objects.all().values()
            students = list( students )
            return JsonResponse( students, safe=False ) 
        elif op == 'delete' and request.method == 'GET' : 
            student = Student.objects.filter( id = stu_id )
            student.delete()
            return HttpResponse( 'deleted' )
        else : 
            return HttpResponse( 'denied' ) 
    else : 
        return HttpResponse( 'denied' )

@csrf_exempt
def listVolunteers( request, op, vln_id, username, password ) : 
    if user_auth( username, password, 1330 ) : 
        if op == 'get' and request.method == 'GET' :
            volunteers = Volunteer.objects.all().values()
            volunteers = list( volunteers )
            return JsonResponse( volunteers, safe=False ) 
        elif op == 'delete' and request.method == 'GET' : 
            volunteer = Volunteer.objects.filter( id = vln_id ) 
            volunteer.delete()
            return HttpResponse( 'deleted' ) 
        elif op == 'update' and request.method == 'POST' :
            Volunteer.objects.filter( id = vln_id ).update( 
                fullName          = request.POST.get('fullName'          ),
                fatherName        = request.POST.get('fatherName'        ),
                birthCity         = request.POST.get('birthCity'         ),
                schoolName        = request.POST.get('schoolName'        ),
                classNumber       = request.POST.get('classNumber'       ),
                birthDate         = request.POST.get('birthDate'         ),
                nationalCode      = request.POST.get('nationalCode'      ),
                fatherPhoneNumber = request.POST.get('fatherPhoneNumber' ),
                motherPhoneNumber = request.POST.get('motherPhoneNumber' ),
                schoolShift       = request.POST.get('schoolShift'       ),
                religion          = request.POST.get('religion'          ),
                grade             = request.POST.get('grade'             ),
            )
            return HttpResponse('updated')
        else :
            return HttpResponse( 'denied' ) 
    else : 
        return HttpResponse( 'denied' )

def listClasses( request, username, password ) :
    if user_auth( username, password, 1330 ) :  
        if request.method == 'GET' : 
            classesList = Class.objects.all().values()
            classesList = list( classesList )
            for classItem in classesList :
                students = Student.objects.filter( classitem = classItem.get('id') ).values( 
                    'id'
                    ,'fullName'                                
                    ,'fatherName'                              
                    ,'schoolName'                              
                    ,'birthDate'                               
                    ,'nationalCode'                            
                    ,'fatherPhoneNumber'                       
                    ,'motherPhoneNumber'                       
                    ,'schoolShift'                             
                    ,'grade'                                   
                )
                classItem[ 'students' ] = list( students ) 
            return JsonResponse( classesList, safe=False )
        else :
            return HttpResponseBadRequest
    else : 
        HttpResponse( "denied" )

@csrf_exempt  
def changeClass( request, username, password ) :
    if user_auth( username, password, 1330 ) :
        if request.method == 'POST' : 
            class_id   = request.POST[ 'class_id'   ] 
            student_id = request.POST[ 'student_id' ]
            print( class_id )
            print( student_id )
            Student.objects.filter( id = student_id ).update( classitem = class_id )
            return HttpResponse( "changed" )
        else :
            return HttpResponseBadRequest
    else :
        return HttpResponse( 'denied' )

def studentInfo( request, username, password ) : 
    if user_auth( username, password, 1540 ) :
        if request.method == 'GET' : 
            student = Student.objects.filter( user = username ).values(
                'id'
                ,'fullName'                                
                ,'fatherName'                              
                ,'birthCity'                               
                ,'schoolName'                              
                ,'classNumber'                             
                ,'birthDate'                               
                ,'nationalCode'                            
                ,'fatherPhoneNumber'                       
                ,'motherPhoneNumber'                       
                ,'schoolShift'                             
                ,'religion'                                
                ,'grade'                                   
                ,'passField'                               
                ,'whatIsParentsGrade'                      
                ,'howDidGetToKnowQuranSessions'            
                ,'WhoEncourageYouToComeQuranSessions'      
                ,'WhichSessionDidYouParticipate'           
                ,'WhichSportsDoYouInterestedIn'            
                ,'WhichBooksDoYouRecentlyRead'   
                ,'WriteTheNamesOfYourTwoFriends'           
                ,'WhichCulturalActivitiesDoYouInterested'  
                ,'WhichFieldsDoYouTalentedIn'              
                ,'HowMuchDoYouFamiliarWithQuran'           
                ,'WhichCommitionsDoYouInterestedIn'        
                ,'HowDoYouSpendYourHolidays'               
                ,'WhichBooksDoYouLikeToRead'  
                ,'WhatLevelofSkillDoYouHaveInCulturalActivity'        
                ,'user'                                    
                ,'classitem'                               
            )
            student = list( student )
            student = student[0]
            classItem = Class.objects.filter( id = student[ 'classitem' ] ).values( 'name' )
            classItem = list( classItem )
            classItem = classItem[0]
            student[ 'class_name' ] = classItem[ 'name' ]
            student.pop( 'classitem' ) 

            return JsonResponse( student, safe=True )
        else :
            return HttpResponseBadRequest
    else :
        return HttpResponse( 'denied' ) 
    
def classInfo( request, username, password ) :
    if user_auth( username, password, 1540 ) : 
        if request.method == 'GET' : 
            student = Student.objects.filter( user = username ).values( 'classitem' )
            student = list( student )
            student = student[0]
            classItem = Class.objects.filter( id = student[ 'classitem' ] ).values(
                'name'         
                ,'startTime'    
                ,'endTime'      
                ,'location'     
                ,'dayInWeek'    
                ,'grade'        
                ,'moreDetail'   
                ,'teacher'      
            )
            student_list = Student.objects.filter( classitem = student[ 'classitem' ] ).values(
                'fullName'
            )
            classItem = list( classItem )
            classItem = classItem[0]
            classItem[ 'students' ] = list( student_list )
            return JsonResponse( classItem, safe=True )

        else : 
            return HttpResponseBadRequest
    else :
        return HttpResponse( 'denied' ) 
