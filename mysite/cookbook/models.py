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
    recipe_name = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, blank=True)
    source = models.URLField(blank=True)
    cuisine = models.CharField(max_length=255, choices=CUISINE_CHOICES) # enum
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    servings = models.IntegerField(null=True)
    instructions = models.TextField()
    notes = models.TextField(blank=True)
    pub_date = models.DateField("Date Published", default=datetime.datetime.now)
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

    def recipe_generate_steps(self):
        steps = []
        line = ""
        for char in str(self.instructions):
            if(char == '\n'):
                steps.append(line)
                line = ""
            else:
                line = line+char
        steps.append(line)
        return steps

    def get_absolute_url(self):
        kwargs = {
            'slug' : self.slug
        }
        return reverse('recipe_detail', kwargs=kwargs)

class Ingredient(models.Model):
    ALLERGY_TYPE =  [
        ('NUT', 'Nut'),
        ('PEANUT', 'Peanut'),
        ('SHELLFISH', 'Shellfish'),
        ('FISH', 'Fish'),
        ('MILK', 'Milk'),
        ('EGGS', 'Eggs'),
        ('SOY', 'Soy'),
        ('WHEAT', 'Wheat'),
        ('NONE','none')
    ]
    ingredient_name = models.CharField(max_length=255)
    allergy = models.CharField(max_length=255, choices=ALLERGY_TYPE) # enum

    def __str__(self):
        return self.ingredient_name

class Recipe_Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE) # connect to recipe table
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT) # connect to ingredients table
    amount = models.CharField(max_length=144)

    def __str__(self):
        return f'{self.amount} {self.ingredient}s'

class Recipe_Photos(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE) # connect to recipe table
    photo = models.ImageField()

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
