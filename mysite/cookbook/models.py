from django.db import models
from django.urls import reverse
import datetime

class Author(models.Model):
    author_name = models.CharField(max_length=100)
    author_bio = models.TextField(blank=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.author_name
    
    def get_absolute_url(self):
        kwargs = {
            'slug' : self.slug
        }
        return reverse('author_detail', kwargs=kwargs)

class Recipe(models.Model):
    CUISINE_CHOICES =  [
        ('CHINESE', 'Chinese'),
        ('JAPANESE', 'Japanese'),
        ('KOREAN', 'Korean'),
        ('VIETNAMESE', 'Vietnamese'),
        ('THAI', 'Thai'),
        ('FRENCH', 'French'),
        ('AMERICAN', 'American'),
        ('SPANISH', 'Spanish'),
        ('MEXICAN', 'Mexican'),
        ('UNKOWN','unknown')
    ]
    FOOD_COURSE = [
        ('APPETIZER', 'Appetizer'),
        ('BREAKFAST', 'Breakfast'),
        ('LUNCH', 'Lunch'),
        ('DINNER', 'Dinner'),
        ('DESSERT', 'Dessert'),
        ('SNACK', 'Snack'),
        ('BRUNCH', 'Brunch'),
        ('CONDIMENT', 'Condiment'),
        ('BAKING', 'Baking'),
        ('UNKNOWN', 'Unknown')
    ]
    recipe_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, blank=True)
    servings = models.IntegerField()
    prep_time = models.IntegerField()
    cuisine = models.CharField(max_length=255, choices=CUISINE_CHOICES) # enum
    category = models.CharField(max_length=255, choices=FOOD_COURSE, blank=True) #enum
    notes = models.TextField(blank=True)
    video = models.URLField(blank=True)
    pub_date = models.DateField("Date Published", default=datetime.date.today)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f'{self.recipe_name} by {self.author}'
    
    def was_published_recently(self):
        return self.pub_date >= datetime.date.today - datetime.timedelta(days=30)
    
    def convert_time(self):
        hours = self.prep_time / 60
        minutes = self.prep_time % 60
        if hours < 1:
            return f"{str(minutes)} minutes"
        elif minutes == 0:
            return f"{str(int(hours))} hours"
        else:
            return f"{int(hours)} hours and {minutes} minutes"

    def get_absolute_url(self):
        kwargs = {
            'slug' : self.slug
        }
        return reverse('recipe_detail', kwargs=kwargs)

class Technique(models.Model):
    technique_name = models.CharField(max_length=255) # connect to recipe step table
    technique_tutorial = models.TextField(blank=True)
    video_link = models.CharField(max_length=144)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.technique_name

    def get_absolute_url(self):
        kwargs = {
            'slug' : self.slug
        }
        return reverse('technique_detail', kwargs=kwargs)

class Recipe_Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE) #connect to recipe table
    step_number = models.IntegerField()
    instruction = models.TextField()
    techique = models.ForeignKey(Technique, on_delete=models.PROTECT, null=True, blank=True) # connect to technical table

    def __str__(self):
        return str(self.step_number)

class Ingredient(models.Model):
    INGREDIENT_TYPES=[
        ('NUT', 'Nut'),
        ('SHELLFISH', 'Shellfish'),
        ('SEAFOOD', 'Seafood'),
        ('VEGETABLE', 'Vegetable'),
        ('BEEF', 'Beef'),
        ('PORK', 'Pork'),
        ('CHICKEN', 'Chicken'),
        ('DAIRY', 'Dairy'),
        ('STARCH', 'Starch'),
        ('SEASONING', 'Seasoning'),
        ('UNKNOWN', 'unknown')
    ]
    ingredient_name = models.CharField(max_length=255)
    ingredient_type = models.CharField(max_length=255, choices=INGREDIENT_TYPES) # enum

    def __str__(self):
        return self.ingredient_name

class Recipe_Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE) # connect to recipe table
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT) # connect to ingredients table
    amount = models.CharField(max_length=144)

    def __str__(self):
        return f'{self.amount} {self.ingredient}s'
