from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Sighting:
    STATUS_PENDING = 0
    STATUS_PROCESSING = 1
    STATUS_PROCESSED = 2
    TYPE_WASP = 0
    TYPE_NEST = 1

    lat = models.DecimalField(null=False, blank=False, verbose_name='Latitud')
    lng = models.DecimalField(null=False, blank=False, verbose_name='Longitud')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, related_name="sightings", verbose_name='Localización')
    status = models.IntegerField(null=False, blank=False, verbose_name="Estado", default=STATUS_PENDING)
    location_free_text = models.CharField(null=False, blank=False, max_length=512, verbose_name='Texto sobre localización')
    public = models.BooleanField(null=False, blank=False, default=False, verbose_name='Publicado')
    sighting_type = models.IntegerField(null=False, blank=False, verbose_name="Tipo de avistamiento")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')
    answers = models.ManyToManyFiled(DefaultAnswer, related_name="sightings")
    reported_by = models.ForeignKey('auth.models.User', related_name="Usuario reportador")
    moderator = models.ForeignKey('auth.models.User', related_name="Experto moderador")

class Location:
    name = models.CharField(max_lengthField=128, null=False, blank=False, verbose_name='Nombre')
    lat = models.DecimalField(null=False, blank=False, verbose_name='Latitud')
    lng = models.DecimalField(null=False, blank=False, verbose_name='Longitud')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

class Picture:
    #Com gestiona path?
    name = models.ImageField(null=False, blank=False, upload_to="sightings/")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

class Question:
    title = models.CharField(max_lengthField=128, null=False, blank=False, verbose_name='Título')
    is_active = models.BooleanField(default=True, null=False, blank=False, verbose_name="Activa")
    question_type = models.IntegerField(verbose_name="Tipo de pregunta", )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')


class DefaultAnswer:
    value = models.CharField(max_lengthField=128, null=False, blank=False, verbose_name='Título')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')
    question = models.ForeignKey(Question, related_name="default_answer")

class ExpertComment:
    comment = models.CharField(null=False, blank=False, max_length=512, verbose_name='Comentario')
    is_valid = models.NullBoleanField(verbose_name="Avistamiento válido")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')
    user_id = models.ForeignKey('auth.models.User', related_name="expert_comments")


class UserComment:
    comment = models.CharField(null=False, blank=False, max_length=512,  verbose_name='Comentario')
    visible = models.BoleanField(verbose_name="Moderado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')
    user_id = models.ForeignKey('auth.models.User', related_name="user_comments")
