# Generated by Django 4.2.9 on 2024-01-17 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pin', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Chhatishgarh', 'Chhatishgarh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Daman & Diu', 'Daman & Diu'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujrat', 'Gujrat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerla', 'Kerla'), ('Lakshyadeep', 'Lakshyadeep'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Puducherry', 'Puducherry'), ('Punjab', 'Punjab'), ('Rajsthan', 'Rajsthan'), ('Sikim', 'Sikim'), ('Tamilnadu', 'Tamilnadu'), ('Tripura', 'Tripura'), ('Uttrakhand', 'Uttrakhand'), ('Uttrar Pradesh', 'Uttrar Pradesh'), ('West Bengal', 'West Bengal')], max_length=50)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('job_city', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(blank=True, upload_to='profileimg')),
                ('my_file', models.FileField(blank=True, upload_to='doc')),
            ],
        ),
    ]