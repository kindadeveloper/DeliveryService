from django.db import models

class Review(models.Model):
    review_text = models.TextField('review_text')
    pub_date = models.DateTimeField('publication_date')
    author_name = models.CharField('author', max_length=50)
