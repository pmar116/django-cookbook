from django.db import models

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
    FOOD_CATEGORY = [
        ('BREAKFAST', 'Breakfast'),
        ('LUNCH', 'Lunch'),
        ('DINNER', 'Dinner'),
        ('APPETIZER', 'Appetizer'),
        ('UNKOWN', 'Unkown')
    ]
    recipe_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=255, blank=True)
    servings = models.IntegerField()
    prep_time = models.IntegerField()
    cuisine = models.CharField(max_length=255, choices=CUISINE_CHOICES) # enum
    category = models.CharField(max_length=255, choices=FOOD_CATEGORY, blank=True) #enum
    notes = models.TextField(blank=True)
    video = models.URLField(blank=True)

    def __str__(self):
        return f'{self.recipe_name} by {self.author}'

class Techniques(models.Model):
    technique_name = models.CharField(max_length=255) # connect to recipe step table
    video_link = models.URLField()

    def __str__(self):
        return self.technique_name

class Recipe_Steps(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE) #connect to recipe table
    step_number = models.IntegerField()
    instruction = models.TextField()
    techique = models.ForeignKey(Techniques, on_delete=models.PROTECT) # connect to technical table

    def __str__(self):
        return self.step_number

class Ingredients(models.Model):
    INGREDIENT_TYPES=[
        ('NUT', 'Nut'),
        ('SHELLFISH', 'Shellfish'),
        ('SEAFOOD', 'Seafood'),
        ('VEGETABLE', 'Vegetable'),
        ('BEEF', 'Beef'),
        ('PORK', 'Pork'),
        ('CHICKEN', 'Chicken'),
        ('UNKNOWN', 'Unkown')
    ]
    ingredient_name = models.CharField(max_length=255)
    ingredient_type = models.CharField(max_length=255, choices=INGREDIENT_TYPES) # enum

    def __str__(self):
        return self.ingredient_name

class Recipe_Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE) # connect to recipe table
    ingredient = models.ForeignKey(Ingredients, on_delete=models.PROTECT) # connect to ingredients table
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.amount} {self.ingredient}s'
