from django.db import models
from django.urls import reverse


class ArticleCategory(models.Model):
    """Class for the categories of articles and their description

       name: name of the category
       description: description of the category
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    
    def __str__(self): # Returns the title of a specific article
    
        return '{}'.format(self.name)

    class Meta: 
        ordering = ['name'] # Orders the name of the categories by ascending order
        verbose_name_plural = "categories"
    
class Article(models.Model):
    """Class for the specific details of the article

        title: title of the article
        category: category of the article
        entry: entry of the user in regards to the article
        created_on: date and time the article was created; automatic
        updated_on: date and time the article was last updated; automatic
    """
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticleCategory, 
                                    on_delete=models.SET_NULL, 
                                    null=True,
                                    related_name='category')
    entry = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self): # Returns the title of a specific article
        return '{}'.format(self.title) 
    
    def get_absolute_url(self): # Returns the url of a specific article
        return reverse("blog:article-detail", args=[self.pk])
    
    class Meta: 
        ordering = ['-created_on'] # Orders the date of creation of the articles by descending order

