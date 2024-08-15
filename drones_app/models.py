from django.db import models




class DroneCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)


    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']



class Drone(models.Model):
    drone_name = models.ForeignKey(DroneCategory, on_delete=models.CASCADE,
                                   related_name='drone')
    name = models.CharField(max_length=200, unique=True)
    manufacturing_date = models.DateTimeField(auto_now_add=True)
    drone_participated_in_at_least_one_competition = models.BooleanField(default=False)    
    inserted_timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']



class Pilot(models.Model):
    
    gender = (
        ('MALE', 'male'),
        ('FEMALE', 'female'),
    )
    name = models.CharField(max_length=200, unique=True)
    gender_value = models.CharField(max_length=10, choices=gender)
    no_of_races = models.PositiveIntegerField(default=0)
    inserted_timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    class Meta:
        ordering = [
            'name'
        ]




class Competition(models.Model):
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    distance_value = models.PositiveIntegerField(help_text='measured in feet')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            '-distance_value',
        ]


