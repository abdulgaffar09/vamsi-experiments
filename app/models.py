from django.db import models
#from django.contrib.auth.models import User


from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class PersonCategory(models.Model):
    category_name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.category_name


class Registration(models.Model):
    name=models.CharField(max_length=50, null=True)
    email=models.EmailField(max_length=30, null=True)
    phnNo= PhoneNumberField(max_length=15, null=True)

    personcategory = models.ForeignKey(PersonCategory,max_length=30, null=True,on_delete=models.SET_NULL)

    password=models.CharField(max_length=30,null=True)
    last_login = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Locations(models.Model):

    location_name=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.location_name




class Idea(models.Model):
    idea_name=models.CharField(max_length=30,null=True)
    '''
    ideas = (
        ('chai', 'Chai'),
        ('bakery', 'Bakery'),
        ('chineese', 'Chineese'),
        ('milk shakes', 'Milk Shakes'),
        ('biryani', 'Biryani'),
        ('tiffins', 'Tiffins'),
        ('meals', 'Meals'),
        ('others', 'Others')

    )
    '''
    def __str__(self):
        return self.idea_name


class Capital(models.Model):

    capita_ranges = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.capita_ranges


class Investor(models.Model):

    your_investment=models.ManyToManyField(Capital)
    interests = models.ManyToManyField(Idea)
    desired_locations=models.ManyToManyField(Locations)
    comments=models.TextField(null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)
    user_details=models.ForeignKey(Registration,null=True,on_delete=models.SET_NULL)

class MoneyFinder(models.Model):

    skilled_in=models.ManyToManyField(Idea)
    experience_in_years=models.IntegerField(null=True)
    preferred_location=models.ManyToManyField(Locations)
    comments=models.TextField(null=True)
    required_amount=models.ManyToManyField(Capital)
    date = models.DateTimeField(auto_now_add=True, null=True)
    user_details = models.ForeignKey(Registration, null=True, on_delete=models.SET_NULL)


class Others(models.Model):
    user_Details=models.ForeignKey(Registration,null=True,on_delete=models.SET_NULL)
    your_ideas=models.TextField(null=True)


