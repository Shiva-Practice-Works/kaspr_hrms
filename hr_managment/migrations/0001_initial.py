# Generated by Django 2.2.14 on 2020-11-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_uniq_portal_id', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('company_location', models.CharField(max_length=100)),
                ('company_pincode', models.CharField(max_length=100)),
                ('company_mail', models.EmailField(max_length=254)),
                ('company_number', models.IntegerField()),
                ('company_type', models.CharField(max_length=100)),
                ('company_gstin', models.CharField(max_length=100)),
                ('doj_portal', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hr_Detailes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hr_uniq_portal_id', models.CharField(max_length=100)),
                ('hr_name', models.CharField(max_length=100)),
                ('hr_company', models.CharField(max_length=100)),
                ('hr_mail', models.EmailField(max_length=254)),
                ('hr_dob', models.DateField()),
                ('hr_number', models.IntegerField()),
                ('hr_joining_date', models.DateField()),
                ('doj_portal', models.CharField(max_length=100)),
            ],
        ),
    ]
