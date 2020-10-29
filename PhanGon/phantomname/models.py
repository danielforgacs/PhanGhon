from django.db import models
from django.contrib import auth



class User(auth.models.AbstractUser):
    def has_phantomname(self):
        query = PhantomName.objects.filter(user=self)
        result = query.count() == 1

        return result




class GhostNameQS(models.QuerySet):
    def query_free_names(self, usedids):
        query = self.exclude(id__in=usedids)

        return query



class GhostNameManager(models.Manager):
    def get_queryset(self):
        queryset = GhostNameQS(self.model, using=self._db)
        return queryset


    def query_free_names(self):
        phantomnames = PhantomName.objects.values('ghostname')
        used_ids = [phantomnames['ghostname'] for phantomnames in phantomnames]
        freenames = self.get_queryset().query_free_names(usedids=used_ids)

        return freenames




class GhostName(models.Model):
    objects = GhostNameManager()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    @property
    def phantomname(self):
        result = None
        query = PhantomName.objects.get(ghostname=self)

        if query:
            result = query

        return result


    def __str__(self):
        return '<{}:{}>'.format(type(self).__name__, self.name)





class PhantomName(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    ghostname = models.ForeignKey(to='GhostName', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'ghostname'),
                name='unique_phantomname',),
        ]
