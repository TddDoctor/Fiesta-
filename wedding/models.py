from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Category(models.Model):
    """
    A model class describing a category.
    """
    name = models.CharField(u'Name', max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(u'Description', blank=True)

    class Meta:
        verbose_name = u'Category'
        verbose_name_plural = u'Categories'

    def __unicode__(self):
        return self.name

# Create your models here.
class Recipe(models.Model):
    """
    A model describing a coobook recipe.
    """
    DIFFICULTY_EASY = 1
    DIFFICULTY_MEDIUM = 2
    DIFFICULTY_HARD = 3
    DIFFICULTY_JUBIL = 4
    DIFFICULTIES = (
        (DIFFICULTY_EASY, u'Give Away'),
        (DIFFICULTY_MEDIUM, u'Introduction'),
        (DIFFICULTY_HARD, u'Wedding'),
        (DIFFICULTY_JUBIL, u'Jubile'),
    )
    title = models.CharField(u'Title', max_length=255)
    slug = models.SlugField(unique=True)
    bride = models.CharField(u'Bride Names', max_length=255)
    slug = models.SlugField(unique=True)

    gloom = models.CharField(u'Gloom Names', max_length=255)
    slug = models.SlugField(unique=True)


    ingredients = models.TextField(u'Indigrents',
        help_text=u'One indigrent per line')
    preparation = models.TextField(u'Preparation')
    time_for_preparation = models.IntegerField(u'Preparation time',
        help_text=u'Zeit in Minuten angeben', blank=True, null=True)
    number_of_portions = models.PositiveIntegerField(u'Number of portions')
    difficulty = models.SmallIntegerField(u'Difficulty',
        choices=DIFFICULTIES, default=DIFFICULTY_MEDIUM)
    category = models.ManyToManyField(Category, verbose_name=u'Categories')
    author = models.ForeignKey(User, verbose_name=u'Author')
    date_created = models.DateTimeField(editable=False)
    date_updated = models.DateTimeField(editable=False)

    class Meta:
        verbose_name = u'Recipe'
        verbose_name_plural = u'Recipes'
        ordering = ['-date_created']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(Recipe, self).save(*args, **kwargs)
