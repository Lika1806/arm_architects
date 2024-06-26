from django.db import models
from .location import Location

class Architect(models.Model):
    GENDERS = dict( F ='Female',
               M= 'Male')
    architect_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    
    last_name = models.CharField(max_length=50, 
                                 blank=True,null=True)
    
    fathers_name = models.CharField(max_length=30, blank=True,null=True)
    nickname = models.CharField(max_length=50, 
                                blank=True,null=True)
    gender = models.CharField(max_length=1, choices=GENDERS, 
                              blank=True,null=True) #mi guce dardznenq partadir?
    birth_location_id = models.ForeignKey(Location, on_delete=models.CASCADE, 
                                          null=True, blank=True,  
                                          verbose_name='birth location') #nayel inch a nshanakum on_delete=models.CASCADE
    date_of_birth = models.DateField(null=True,blank=True)
    date_of_death = models.DateField(null=True,blank=True)
    biography = models.TextField(blank=True,null=True)
    #image = models.ImageField(upload_to='architects/', null=True, blank=True, verbose_name='image')
    def __str__(self) -> str:
        res = f"{self.first_name} "
        if self.last_name:
            res+=self.last_name+' '
        if self.nickname:
            res+=f"({self.nickname})"
        return res