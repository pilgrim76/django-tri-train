from django.db import models


# Create your models here.
class tblDistance(models.Model):
    dst_Name = models.CharField(max_length=200)
    dst_Swim = models.IntegerField(default=0)
    dst_Cicle = models.IntegerField(default=0)
    dst_Run = models.IntegerField(default=0)
    def __str__(self):
            return self.dst_Name + "(" + str(self.dst_Swim) + ", " + str(self.dst_Cicle) + ", " + str(self.dst_Run) + ")";
    def __repr__(self):
            return self.dst_Name + "(" + str(self.dst_Swim) + ", " + str(self.dst_Cicle) + ", " + str(self.dst_Run) + ")";

class tblSportsman(models.Model):
    sm_Name = models.CharField(max_length=200)
    sm_Distance = models.ForeignKey(tblDistance, on_delete=models.CASCADE)
    def __str__(self):
        return self.sm_Name;
    def __repr__(self):
        return self.sm_Name;

class tblResults(models.Model):
    res_Sportsman = models.ForeignKey(tblSportsman, on_delete=models.CASCADE)
    res_StartSwimTime = models.DateTimeField(null=True)
    res_EndSwimTime = models.DurationField(null=True)
    res_StartCicleTime = models.DurationField(null=True)
    res_EndCicleTime = models.DurationField(null=True)
    res_StartRunTime = models.DurationField(null=True)
    res_EndRunTime = models.DurationField(null=True)
    def __str__(self):
        return self.res_Sportsman.sm_Name + " " + self.res_Sportsman.sm_Distance.dst_Name;
    def __repr__(self):
        return self.res_Sportsman.sm_Name + " " + self.res_Sportsman.sm_Distance.dst_Name;
    def Less(self, r1):
        fields = [(self.res_EndRunTime, r1.res_EndRunTime), (self.res_StartRunTime, r1.res_StartRunTime), (self.res_EndCicleTime, r1.res_EndCicleTime), (self.res_StartCicleTime, r1.res_StartCicleTime), (self.res_EndSwimTime, r1.res_EndSwimTime), (self.res_StartSwimTime, r1.res_StartSwimTime)]
        for f in fields:
            if (f[1] is not None and f[0] is not None and f[0] > f[1]) or (f[0] is None and f[1] is not None):
                return True
            elif (f[1] is not None and f[0] is not None and f[0] <= f[1]) or (f[1] is None and f[0] is not None):
                return False
        return False
    def Equal(self, r1):
        fields = [(self.res_EndRunTime, r1.res_EndRunTime), (self.res_StartRunTime, r1.res_StartRunTime), (self.res_EndCicleTime, r1.res_EndCicleTime), (self.res_StartCicleTime, r1.res_StartCicleTime), (self.res_EndSwimTime, r1.res_EndSwimTime), (self.res_StartSwimTime, r1.res_StartSwimTime)]
        for f in fields:
            if (f[0] is None and f[1] is None) or (f[0] == f[1]):
                return True
        return False
    def __lt__(self, other):
        return self.Less(other)
    def __gt__(self, other):
        return not self.Less(other) and not self.Equal(other)
    def __eq__(self, other):
        return self.Equal(other)
    def __le__(self, other):
        return self.Less(other) or self.Equal(other)
    def __ge__(self, other):
        return self.__gt__(other, self) or self.Equal(other)


class tblActionLog(models.Model):
    al_user = models.CharField(max_length=64)
    al_Timestamp = models.DateTimeField(null=False)
    al_Action = models.IntegerField(default=0)
    al_Comment = models.CharField(max_length=200)
    def __str__(self):
        return self.al_user;
    def __repr__(self):
        return self.al_user;
    def add(user, timestamp, action_id, action_desc):
        log_entry = tblActionLog(al_user=user, al_Timestamp=timestamp, al_Action=action_id, al_Comment=action_desc)
        log_entry.save()
        return;

