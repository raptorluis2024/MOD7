from django.db import models

# Create your models here.
class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    nombre_region = models.CharField(max_length=40, null=False, blank=False)
    
    def __str__(self):
        return f"{self.id_region}"
    
class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nombre_comuna = models.CharField(max_length=40, null=False, blank=False)
    region = models.ForeignKey(Region, related_name="comunaregion", on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('id_comuna', 'region')
    
    def __str__(self):
        return f"{self.id_comuna}"
    

    
    