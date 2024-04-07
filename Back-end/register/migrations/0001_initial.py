# Generated by Django 4.2.3 on 2023-08-16 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='anvar_name', max_length=30)),
                ('startTime', models.TimeField(db_column='anvar_startTime')),
                ('endTime', models.TimeField(db_column='anvar_endTime')),
                ('location', models.CharField(db_column='anvar_location', max_length=30)),
                ('dayInWeek', models.CharField(db_column='anvar_dayInWeek', max_length=30)),
                ('grade', models.CharField(db_column='anvar_grade', max_length=30)),
                ('moreDetail', models.TextField(blank=True, db_column='anvar_moreDetail')),
                ('teacher', models.CharField(db_column='anvar_teacher', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('user_password', models.CharField(max_length=100)),
                ('user_role', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(db_column='anvar_fullName', max_length=30)),
                ('fatherName', models.CharField(db_column='anvar_fatherName', max_length=30)),
                ('birthCity', models.CharField(db_column='anvar_birthCity', max_length=30)),
                ('schoolName', models.CharField(db_column='anvar_schoolName', max_length=30)),
                ('classNumber', models.CharField(blank=True, db_column='anvar_classNumber', max_length=30)),
                ('passField', models.CharField(db_column='anvar_passField', max_length=50)),
                ('birthDate', models.DateField(db_column='anvar_birthDate')),
                ('nationalCode', models.CharField(db_column='anvar_nationalCode', max_length=15)),
                ('fatherPhoneNumber', models.CharField(db_column='anvar_fatherPhoneNumber', max_length=15)),
                ('motherPhoneNumber', models.CharField(db_column='anvar_motherPhoneNumber', max_length=15)),
                ('schoolShift', models.CharField(db_column='anvar_schoolShift', max_length=30)),
                ('religion', models.CharField(db_column='anvar_religion', max_length=30)),
                ('grade', models.CharField(db_column='anvar_grade', max_length=30)),
                ('whatIsParentsGrade', models.TextField(blank=True, db_column='anvar_whatIsParentsGrade')),
                ('howDidGetToKnowQuranSessions', models.TextField(blank=True, db_column='anvar_howDidGetToKnowQuranSessions')),
                ('WhoEncourageYouToComeQuranSessions', models.TextField(blank=True, db_column='anvar_WhoEncourageYouToComeQuranSessions')),
                ('WhichSessionDidYouParticipate', models.TextField(blank=True, db_column='anvar_WhichSessionDidYouParticipate')),
                ('WhichSportsDoYouInterestedIn', models.TextField(blank=True, db_column='anvar_WhichSportsDoYouInterestedIn')),
                ('WhichBooksDoYouRecentlyRead', models.TextField(blank=True, db_column='anvar_WhichBooksDoYouRecentlyRead')),
                ('WriteTheNamesOfYourTwoFriends', models.TextField(blank=True, db_column='anvar_WriteTheNamesOfYourTwoFriends')),
                ('WhichCulturalActivitiesDoYouInterested', models.TextField(blank=True, db_column='anvar_WhichCulturalActivitiesDoYouInterested')),
                ('WhichFieldsDoYouTalentedIn', models.TextField(blank=True, db_column='anvar_WhichFieldsDoYouTalentedIn')),
                ('HowMuchDoYouFamiliarWithQuran', models.TextField(blank=True, db_column='anvar_HowMuchDoYouFamiliarWithQuran')),
                ('WhichCommitionsDoYouInterestedIn', models.TextField(blank=True, db_column='anvar_WhichCommitionsDoYouInterestedIn')),
                ('HowDoYouSpendYourHolidays', models.TextField(blank=True, db_column='anvar_HowDoYouSpendYourHolidays')),
                ('personelPhoto', models.ImageField(db_column='anvar_personelPhoto', upload_to='documents/')),
                ('birthCertificate', models.ImageField(db_column='anvar_birthCertificate', upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(db_column='anvar_fullName', max_length=30)),
                ('fatherName', models.CharField(db_column='anvar_fatherName', max_length=30)),
                ('birthCity', models.CharField(db_column='anvar_birthCity', max_length=30)),
                ('schoolName', models.CharField(db_column='anvar_schoolName', max_length=30)),
                ('classNumber', models.CharField(blank=True, db_column='anvar_classNumber', max_length=30)),
                ('birthDate', models.DateField(db_column='anvar_birthDate')),
                ('nationalCode', models.CharField(db_column='anvar_nationalCode', max_length=15)),
                ('fatherPhoneNumber', models.CharField(db_column='anvar_fatherPhoneNumber', max_length=15)),
                ('motherPhoneNumber', models.CharField(db_column='anvar_motherPhoneNumber', max_length=15)),
                ('schoolShift', models.CharField(db_column='anvar_schoolShift', max_length=30)),
                ('religion', models.CharField(db_column='anvar_religion', max_length=30)),
                ('grade', models.CharField(db_column='anvar_grade', max_length=30)),
                ('personelPhoto', models.ImageField(db_column='anvar_personelPhoto', upload_to='documents/')),
                ('birthCertificate', models.ImageField(db_column='anvar_birthCertificate', upload_to='documents/')),
                ('passField', models.CharField(db_column='anvar_passField', max_length=50)),
                ('whatIsParentsGrade', models.TextField(blank=True, db_column='anvar_whatIsParentsGrade')),
                ('howDidGetToKnowQuranSessions', models.TextField(blank=True, db_column='anvar_howDidGetToKnowQuranSessions')),
                ('WhoEncourageYouToComeQuranSessions', models.TextField(blank=True, db_column='anvar_WhoEncourageYouToComeQuranSessions')),
                ('WhichSessionDidYouParticipate', models.TextField(blank=True, db_column='anvar_WhichSessionDidYouParticipate')),
                ('WhichSportsDoYouInterestedIn', models.TextField(blank=True, db_column='anvar_WhichSportsDoYouInterestedIn')),
                ('WhichBooksDoYouRecentlyRead', models.TextField(blank=True, db_column='anvar_WhichBooksDoYouRecentlyRead')),
                ('WriteTheNamesOfYourTwoFriends', models.TextField(blank=True, db_column='anvar_WriteTheNamesOfYourTwoFriends')),
                ('WhichCulturalActivitiesDoYouInterested', models.TextField(blank=True, db_column='anvar_WhichCulturalActivitiesDoYouInterested')),
                ('WhichFieldsDoYouTalentedIn', models.TextField(blank=True, db_column='anvar_WhichFieldsDoYouTalentedIn')),
                ('HowMuchDoYouFamiliarWithQuran', models.TextField(blank=True, db_column='anvar_HowMuchDoYouFamiliarWithQuran')),
                ('WhichCommitionsDoYouInterestedIn', models.TextField(blank=True, db_column='anvar_WhichCommitionsDoYouInterestedIn')),
                ('HowDoYouSpendYourHolidays', models.TextField(blank=True, db_column='anvar_HowDoYouSpendYourHolidays')),
                ('classitem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='register.class')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='register.users')),
            ],
        ),
    ]
