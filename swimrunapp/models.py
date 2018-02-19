from django.db import models


# Create your models here.
class tblDistance(models.Model):
    dst_Name = models.CharField(max_length=200)
    dst_SplitsNumber = models.IntegerField(default=0)
    def __str__(self):
        return self.dst_Name + "(" + str(self.dst_SplitsNumber) + ")"

class tblDistanceType(models.Model):
    dt_Name = models.CharField(max_length=200)
    def __str__(self):
        return self.dt_Name

class tblDistanceSplits(models.Model):
    ds_Distance = models.ForeignKey(tblDistance, on_delete=models.CASCADE)
    ds_SplitID = models.IntegerField(default=0)
    ds_Type = models.ForeignKey(tblDistanceType, on_delete=models.CASCADE)
    ds_Length = models.IntegerField(default=0)
    def __str__(self):
        return self.ds_Distance.dst_Name + "(" + str(self.ds_SplitID) + ") " + self.ds_Type.dt_Name + ", " + str(self.ds_Length)

class tblSportsman(models.Model):
    sm_Name = models.CharField(max_length=200)
    sm_Distance = models.ForeignKey(tblDistance, on_delete=models.CASCADE)
    def __str__(self):
        return self.sm_Name;

class tblResult(models.Model):
    res_Sportsman = models.ForeignKey(tblSportsman, on_delete=models.CASCADE)
    res_SplitID = models.ForeignKey(tblDistanceSplits, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.res_Sportsman.sm_Name + " " + self.res_Sportsman.sm_Distance.dst_Name;

class tblSplitsResult(models.Model):
    sr_SportsmanResult = models.ForeignKey(tblResult, on_delete=models.CASCADE)
    sr_Split = models.ForeignKey(tblDistanceSplits, on_delete=models.CASCADE)
    sr_SplitTime = models.DateTimeField(null=True)
    def __str__(self):
        return self.sr_SportsmanResult.res_Sportsman.sm_Name + "(" + str(self.sr_Split) + ") " + str(self.sr_SplitTime)



