from django.db import models


# Create your models here.


class Passenger(models.Model):
    age = models.IntegerField()
    siblings_and_spouse_count = models.IntegerField()
    parent_and_children_count = models.IntegerField()
    gender = models.CharField(max_length=6)
    ticket_number = models.CharField(max_length=100)
    passenger_class = models.CharField(max_length=10)
    cabin_number = models.CharField(max_length=20)
    fare = models.IntegerField()
    port_of_embarkation = models.CharField(max_length=20)
    name = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name + ' - ' + str(self.age) + ' - ' + self.gender


class Predictions(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    survival_prediction = models.IntegerField(default=1)
    prediction_confidence = models.IntegerField()

    def __str__(self):
        return str(self.passenger) + ' - ' + str(self.survival_prediction) + ' - ' + str(self.prediction_confidence)
