from django.db import models

from db.user import User


class UrlShortener(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    title = models.CharField(max_length=100, blank=True, null=True)
    long_url = models.CharField(max_length=500, null=False)
    short_url = models.CharField(max_length=100, null=False,unique=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, db_column='updated_by',
                                   related_name='url_updated_by', null=False)
    updated_at = models.DateTimeField(null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, db_column='created_by',
                                   related_name='url_created_by', null=True)
    created_at = models.DateTimeField(null=False)

    class Meta:
        managed = False
        db_table = 'url_shortener'
