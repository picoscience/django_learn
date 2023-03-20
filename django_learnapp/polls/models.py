from django.db import models

"""
La llave primaria ya se genera con la herencia

Para inicializar una app:
----> py manage.py startapp nombre_de_tu_aplicacion
y seguido, debe hacerse el ORM, agregar la app a INSTALED_APPS
de settings, y ejecutar:
----> py manage.py makemigrations nombre_de_tu_aplicacion
y despues:
----> py manage.py migrate

"""

class Question(models.Model):
    
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

class Choices(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)