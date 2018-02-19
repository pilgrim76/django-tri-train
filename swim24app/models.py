from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class tbls24Distance(models.Model):
    dst_Name = models.CharField(max_length=200)
    dst_SwimDuration = models.IntegerField(default=0)

    def __str__(self):
            return self.dst_Name + "(" + str(self.dst_SwimDuration) + ")"

    def __repr__(self):
            return self.dst_Name + "(" + str(self.dst_SwimDuration) + ")"


class tbls24Sportsman(models.Model):
    sm_Name = models.CharField(max_length=200)
    sm_Distance = models.ForeignKey(tbls24Distance, on_delete=models.CASCADE)

    def __str__(self):
        return self.sm_Name

    def __repr__(self):
        return self.sm_Name


class tbls24Results(models.Model):
    res_Sportsman = models.ForeignKey(tbls24Sportsman, on_delete=models.CASCADE)
    res_StartTime = models.DateTimeField(null=True)
    res_LastLapTime = models.DateTimeField(null=True)
    res_SwimLaps = models.IntegerField(default=0)
    res_FinishTime = models.DurationField(null=True)

    def __str__(self):
        return self.res_Sportsman.sm_Name + " " + self.res_Sportsman.sm_Distance.dst_Name + " " + str(self.res_SwimLaps);

    def __repr__(self):
        return self.res_Sportsman.sm_Name + " " + self.res_Sportsman.sm_Distance.dst_Name + " " + str(self.res_SwimLaps);

    def Less(self, r1):
        return self.res_SwimLaps < r1.res_SwimLaps;

    def Equal(self, r1):
        return self.res_SwimLaps == r1.res_SwimLaps;

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


class tbls24Counter(models.Model):
    cnt_user = models.ForeignKey(User)
    cnt_Sportsman = models.ForeignKey(tbls24Sportsman)


class tbls24ActionLog(models.Model):
    al_user = models.CharField(max_length=64)
    al_Timestamp = models.DateTimeField(null=False)
    al_Action = models.IntegerField(default=0)
    al_Comment = models.CharField(max_length=200)

    def add(user, timestamp, action_id, action_desc):
        log_entry = tbls24ActionLog(al_user=user, al_Timestamp=timestamp, al_Action=action_id, al_Comment=action_desc)
        log_entry.save()
        return;

