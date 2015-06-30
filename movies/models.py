from django.db import models

from django.db import models
import ast

class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class Tag(models.Model):
    tag = models.CharField(max_length=120,primary_key=True)
    is_adult = models.IntegerField(default=1)
    num = models.IntegerField()


class Movie(models.Model):
    id = models.CharField(max_length=120,primary_key=True)
    url = models.CharField(max_length=120,default='')
    title = models.CharField(max_length=120,default='')
    link = models.CharField(max_length=120,default='')
    ginfo_url = models.CharField(max_length=120,default='')
    play_time = models.CharField(max_length=120,default='')
    thumbnail = models.CharField(max_length=120,default='')
    fav = models.IntegerField()
    playing = models.IntegerField()
    is_adult = models.IntegerField(default=1)
    tag = models.CharField(max_length=120,default=[])

    def __str__(self):
        return self.title
