"""
La llave primaria ya se genera con la herencia
Para iniciar un proyecto:
----> django-admin startproject nombre_de_tu_proyecto
Para inicializar el servidor en el puerto 5000, por defecto tiene 
el 8000:
----> py manage.py runserver 5000
Para inicializar una app:
----> py manage.py startapp nombre_de_tu_aplicacion
y seguido, debe hacerse el ORM, agregar la app a INSTALED_APPS
de settings, y ejecutar:
----> py manage.py makemigrations nombre_de_tu_aplicacion
y despues:
----> py manage.py migrate
El makemigrations y el migrate deben ejecutarse siempre que se 
ocurre un cambio en nuestra aplicacion

Para usar la consola interactiva de django podemos usar el 
comando:
----> py manage.py shell
-------------------------
ej:
from polls.models import Question
query = list(Question.object.all())
print(query[0].question_text)
print(query[0].pub_date)
-------------------------
El codigo anterior imprime los atritubos de nuestra tabla
Question.
Para agregar un dato podemos hacer lo siguiente:
ej:
---------------------------------------
from django.utils import timezone
from polls.models import Question
data = Question(question_text='PREGUNTA',pub_date=timezone.now())
data.save()
---------------------------------------
"""
import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return str(self.question_text)
    
    def was_published_recently(self) -> bool:
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.choise_text)