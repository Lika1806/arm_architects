from django.db import models

# Create your models here.
class Location(models.Model):
    LOCATION_TYPES = dict(  COUNTRY ='Country',
                            REGION='Region',
                            CITY='City',
                            VILLAGE='Village',
                            DISTRICT='District',
                            STREET='Street',
                            ADDRESS='Address')
    
    #Can't be missing
    location_id = models.BigAutoField(primary_key=True)
    location_type = models.CharField(max_length=20,choices=LOCATION_TYPES)
    name = models.CharField(max_length=50)

    #Can be missing
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)
    unit_number = models.CharField(max_length=20, blank=True)
    street_id = models.ForeignKey('self', on_delete=models.CASCADE, 
                                  blank=True, null=True, 
                                  related_name='streets', 
                                  verbose_name='related street')
    district_id = models.ForeignKey('self', on_delete=models.CASCADE, 
                                    blank=True, null=True, 
                                    related_name='districts', 
                                    verbose_name='related district')
    settlement_id = models.ForeignKey('self', on_delete=models.CASCADE, 
                                        blank=True, null=True, 
                                        related_name='city_village', 
                                        verbose_name='related city or village')
    region_id = models.ForeignKey('self', on_delete=models.CASCADE, 
                                  blank=True, null=True, 
                                  related_name='region', 
                                  verbose_name='related region')
    country_id = models.ForeignKey('self', on_delete=models.CASCADE, 
                                  blank=True, null=True, 
                                  related_name='country', 
                                  verbose_name='related country')
    
    

    def __str__(self) -> str:
        return f"{self.location_type}-{self.name}"
    