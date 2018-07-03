from django.db import models

# Create your models here.

class articles(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    articlecoverimgurl = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    content = models.TextField(default='')
    pushdate = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return '%s' % (self.id)

    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


class moves(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    movecoverimgurl = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    moveurl = models.CharField(max_length=100)
    pushdate = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % (self.id)

    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

