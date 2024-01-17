from django.db import models



STATE_CHOICE = (
    ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chhatishgarh','Chhatishgarh'),
    ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
    ('Daman & Diu','Daman & Diu'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujrat','Gujrat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu & Kashmir','Jammu & Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerla','Kerla'),
    ('Lakshyadeep','Lakshyadeep'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Puducherry','Puducherry'),
    ('Punjab','Punjab'),
    ('Rajsthan','Rajsthan'),
    ('Sikim','Sikim'),
    ('Tamilnadu','Tamilnadu'),
    ('Tripura','Tripura'),
    ('Uttrakhand','Uttrakhand'),
    ('Uttrar Pradesh','Uttrar Pradesh'),
    ('West Bengal','West Bengal'),
    )

class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add = False)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=50)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profileimg',blank=True)
    my_file = models.FileField(upload_to='doc',blank=True)