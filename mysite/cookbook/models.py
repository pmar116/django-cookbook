from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
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
    notes = models.TextField(blank=True)
    pub_date = models.DateField("Date Published", default=datetime.datetime.now)
    tags = TaggableManager()
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f'{self.recipe_name} by {self.author}'
    
    def was_published_recently(self):
        return self.pub_date >= datetime.date.today - datetime.timedelta(days=30)
    
    def display_prep_time(self):
        hours = int(self.prep_time / 60)
        minutes = int(self.prep_time % 60)
        time = ""
        if hours > 1:
            time = time + f"{str(hours)} hours "
        elif hours == 1:
            time = time + f"{str(hours)} hour "
        if hours > 0 and minutes > 0:
            time = time + "and "
        if minutes == 1:
            time = time + f"{str(minutes)} minute"
        elif minutes != 0:
            time = time + f"{str(minutes)} minutes"
        return time
    
    def display_cook_time(self):
        hours = int(self.cook_time / 60)
        minutes = int(self.cook_time % 60)
        time = ""
        if hours > 1:
            time = time + f"{str(hours)} hours "
        elif hours == 1:
            time = time + f"{str(hours)} hour "
        if hours > 0 and minutes > 0:
            time = time + "and "
        if minutes == 1:
            time = time + f"{str(minutes)} minute"
        elif minutes != 0:
            time = time + f"{str(minutes)} minutes"
        return time

    def get_absolute_url(self):
        kwargs = {
            'slug' : self.slug
        }
        return reverse('recipe_detail', kwargs=kwargs)

class Recipe_Instructions(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    section_title = models.CharField(max_length=100, null=True, blank=True)
    instructions = models.TextField()

    def recipe_generate_steps(self):
        steps = []
        for line in self.instructions.split("\r\n"):
            if len(line) != 0:
                steps.append(line)
        return steps

class Recipe_Ingredients(models.Model):
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
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE) # connect to recipe table
    section_title = models.CharField(max_length=100, null=True, blank=True)
    ingredient_list = models.TextField()

    def ingredient_generate_list(self):
        ingredients = []
        for line in self.ingredient_list.split("\r\n"):
            if len(line) != 0:
                ingredients.append(line)
        return ingredients

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
