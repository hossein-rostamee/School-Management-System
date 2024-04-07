from django.db import models
# Create your models here.

class Volunteer(models.Model):
    fullName                                = models.CharField(max_length=30, db_column='anvar_fullName'                   , blank=False)
    fatherName                              = models.CharField(max_length=30, db_column='anvar_fatherName'                 , blank=False)
    birthCity                               = models.CharField(max_length=30, db_column='anvar_birthCity'                  , blank=False)
    schoolName                              = models.CharField(max_length=30, db_column='anvar_schoolName'                 , blank=False)
    classNumber                             = models.CharField(max_length=30, db_column='anvar_classNumber'                , blank=True)
    passField                               = models.CharField(max_length=50, db_column='anvar_passField'                  , blank=False)
    birthDate                               = models.DateField(db_column='anvar_birthDate'                                 , blank=False)
    nationalCode                            = models.CharField(max_length=15, db_column='anvar_nationalCode'               , blank=False)
    fatherPhoneNumber                       = models.CharField(max_length=15, db_column='anvar_fatherPhoneNumber'          , blank=False)
    motherPhoneNumber                       = models.CharField(max_length=15, db_column='anvar_motherPhoneNumber'          , blank=False)
    schoolShift                             = models.CharField(max_length=30, db_column='anvar_schoolShift'                , blank=False)
    religion                                = models.CharField(max_length=30, db_column='anvar_religion'                   , blank=False)
    grade                                   = models.CharField(max_length=30, db_column='anvar_grade'                      , blank=False)
    whatIsParentsGrade                      = models.TextField(db_column='anvar_whatIsParentsGrade'                        , blank=True)
    howDidGetToKnowQuranSessions            = models.TextField(db_column='anvar_howDidGetToKnowQuranSessions'              , blank=True)
    WhoEncourageYouToComeQuranSessions      = models.TextField(db_column='anvar_WhoEncourageYouToComeQuranSessions'        , blank=True)
    WhichSessionDidYouParticipate           = models.TextField(db_column='anvar_WhichSessionDidYouParticipate'             , blank=True)
    WhichSportsDoYouInterestedIn            = models.TextField(db_column='anvar_WhichSportsDoYouInterestedIn'              , blank=True)
    WhichBooksDoYouRecentlyRead             = models.TextField(db_column='anvar_WhichBooksDoYouRecentlyRead'               , blank=True)
    WhichBooksDoYouLikeToRead               = models.TextField(db_column='anvar_WhichBooksDoYouLikeToRead'                 , blank=True)
    WriteTheNamesOfYourTwoFriends           = models.TextField(db_column='anvar_WriteTheNamesOfYourTwoFriends'             , blank=True)
    WhichCulturalActivitiesDoYouInterested  = models.TextField(db_column='anvar_WhichCulturalActivitiesDoYouInterested'    , blank=True)
    WhichFieldsDoYouTalentedIn              = models.TextField(db_column='anvar_WhichFieldsDoYouTalentedIn'                , blank=True)
    HowMuchDoYouFamiliarWithQuran           = models.TextField(db_column='anvar_HowMuchDoYouFamiliarWithQuran'             , blank=True)
    WhichCommitionsDoYouInterestedIn        = models.TextField(db_column='anvar_WhichCommitionsDoYouInterestedIn'          , blank=True)
    HowDoYouSpendYourHolidays               = models.TextField(db_column='anvar_HowDoYouSpendYourHolidays'                 , blank=True)
    personelPhoto                           = models.ImageField(upload_to='documents/', db_column='anvar_personelPhoto'    , blank=False)
    birthCertificate                        = models.ImageField(upload_to='documents/', db_column='anvar_birthCertificate' , blank=False)
    WhatLevelofSkillDoYouHaveInCulturalActivity = models.TextField(db_column='anvar_WhatLevelofSkillDoYouHaveInCulturalActivity'  , blank=True)
    date                                    = models.DateField(db_column='anvar_date'                                      , blank=False)

    def _str_(self):
        return self.anvar_fullName

class Users(models.Model):
    user_name = models.CharField(max_length=100, primary_key=True)
    user_password = models.CharField(max_length=100)
    user_role = models.PositiveIntegerField()
    def __str__(self):
        return self.user_name


class Class(models.Model) :
    name         = models.CharField(max_length=30, db_column='anvar_name'       , blank=False)
    startTime    = models.TimeField(db_column='anvar_startTime'                 ,blank=False )
    endTime      = models.TimeField(db_column='anvar_endTime'                   ,blank=False )
    location     = models.CharField(max_length=30, db_column='anvar_location'   , blank=False)
    dayInWeek    = models.CharField(max_length=30, db_column='anvar_dayInWeek'   , blank=False)
    grade        = models.CharField(max_length=30, db_column='anvar_grade'      , blank=False)
    moreDetail   = models.TextField(db_column='anvar_moreDetail'                , blank=True)
    teacher      = models.CharField(max_length=30, db_column='anvar_teacher'    , blank=False)

    def _str_(self):
        return self.name 
    
    
class Student(models.Model):
    fullName                                = models.CharField(max_length=30, db_column='anvar_fullName'                   , blank=False)
    fatherName                              = models.CharField(max_length=30, db_column='anvar_fatherName'                 , blank=False)
    birthCity                               = models.CharField(max_length=30, db_column='anvar_birthCity'                  , blank=False)
    schoolName                              = models.CharField(max_length=30, db_column='anvar_schoolName'                 , blank=False)
    classNumber                             = models.CharField(max_length=30, db_column='anvar_classNumber'                , blank=True)
    birthDate                               = models.DateField(db_column='anvar_birthDate'                                 , blank=False)
    nationalCode                            = models.CharField(max_length=15, db_column='anvar_nationalCode'               , blank=False)
    fatherPhoneNumber                       = models.CharField(max_length=15, db_column='anvar_fatherPhoneNumber'          , blank=False)
    motherPhoneNumber                       = models.CharField(max_length=15, db_column='anvar_motherPhoneNumber'          , blank=False)
    schoolShift                             = models.CharField(max_length=30, db_column='anvar_schoolShift'                , blank=False)
    religion                                = models.CharField(max_length=30, db_column='anvar_religion'                   , blank=False)
    grade                                   = models.CharField(max_length=30, db_column='anvar_grade'                      , blank=False)
    personelPhoto                           = models.ImageField(upload_to='documents/', db_column='anvar_personelPhoto'    , blank=False)
    birthCertificate                        = models.ImageField(upload_to='documents/', db_column='anvar_birthCertificate' , blank=False)
    passField                               = models.CharField(max_length=50, db_column='anvar_passField'                  , blank=False)
    whatIsParentsGrade                      = models.TextField(db_column='anvar_whatIsParentsGrade'                        , blank=True)
    howDidGetToKnowQuranSessions            = models.TextField(db_column='anvar_howDidGetToKnowQuranSessions'              , blank=True)
    WhoEncourageYouToComeQuranSessions      = models.TextField(db_column='anvar_WhoEncourageYouToComeQuranSessions'        , blank=True)
    WhichSessionDidYouParticipate           = models.TextField(db_column='anvar_WhichSessionDidYouParticipate'             , blank=True)
    WhichSportsDoYouInterestedIn            = models.TextField(db_column='anvar_WhichSportsDoYouInterestedIn'              , blank=True)
    WhichBooksDoYouRecentlyRead             = models.TextField(db_column='anvar_WhichBooksDoYouRecentlyRead'               , blank=True)
    WhichBooksDoYouLikeToRead               = models.TextField(db_column='anvar_WhichBooksDoYouLikeToRead'                 , blank=True)
    WriteTheNamesOfYourTwoFriends           = models.TextField(db_column='anvar_WriteTheNamesOfYourTwoFriends'             , blank=True)
    WhichCulturalActivitiesDoYouInterested  = models.TextField(db_column='anvar_WhichCulturalActivitiesDoYouInterested'    , blank=True)
    WhichFieldsDoYouTalentedIn              = models.TextField(db_column='anvar_WhichFieldsDoYouTalentedIn'                , blank=True)
    HowMuchDoYouFamiliarWithQuran           = models.TextField(db_column='anvar_HowMuchDoYouFamiliarWithQuran'             , blank=True)
    WhichCommitionsDoYouInterestedIn        = models.TextField(db_column='anvar_WhichCommitionsDoYouInterestedIn'          , blank=True)
    WhatLevelofSkillDoYouHaveInCulturalActivity = models.TextField(db_column='anvar_WhatLevelofSkillDoYouHaveInCulturalActivity'  , blank=True)
    HowDoYouSpendYourHolidays               = models.TextField(db_column='anvar_HowDoYouSpendYourHolidays'                 , blank=True)
    date                                    = models.DateField(db_column='anvar_date'                                      , blank=False,  default='2018-11-20')
    user                                    = models.OneToOneField(  Users, null=False, on_delete=models.CASCADE )
    classitem                               = models.ForeignKey( Class, null=True, blank=True, on_delete=models.SET_NULL)
    def _str_(self):
        return self.fullName

