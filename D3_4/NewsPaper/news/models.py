from django.db import models
from django.conf import settings

class Author(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    rating = models.IntegerField(default = 0)
    def getPosts(self):
        return Post.objects.filter(author = self)
    def getComments(self):
        return Comment.objects.filter(user = self)
    def updateRating(self):
        sum = 0
        for _post in self.getPosts():
            sum += _post.rating * 3
            for _comment in _post.getComments():
                sum += _comment.rating
        for _comment in Comment.objects.filter(user=self.user):
            sum += _comment.rating
        self.rating = sum
        self.save()
        return sum
        
    

class Category(models.Model):
    name = models.CharField(max_length = 255, unique = True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)

    news = 'NE'
    article = 'AR'
    TYPES=[
        (news,'Новость'),
        (article,'Статья')    
         ]
    type = models.CharField(max_length = 2, choices = TYPES, default = article)
    title = models.CharField(max_length = 255, unique = True)
    content = models.TextField(default = '')
    rating = models.IntegerField(default = 0)
    timestamp = models.DateTimeField(auto_now_add = True)
    category = models.ManyToManyField(Category, through = 'PostCategory')
    
    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.content[:124] +'...'

    def getComments(self):
        return Comment.objects.filter(post = self)

    def repr(self):
        _auth = self.author.user.username
        _rate = str(self.rating)
        _tit = self.title
        _pre = self.preview()
        _date = self.timestamp.strftime('%d %B %Y')
        return('Автор: ' + _auth +'\n' +
               'Рейтинг: ' + _rate + '\n' +
               'Название: ' + _tit + '\n' +
               'Начало: ' + _pre + '\n' +
               'Дата: ' + _date )

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    content = models.TextField(default = '')
    timestamp = models.DateTimeField(auto_now_add = True)
    rating = models.IntegerField(default = 0)
    
    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
    def repr(self):
        _auth = self.user.username
        _rate = str(self.rating)
        _tit = self.content
        _date = self.timestamp.strftime('%d %B %Y')
        return('Автор: ' + _auth +'\n' +
               'Рейтинг: ' + _rate + '\n' +
               'Текст: ' + _tit + '\n' +
               'Дата: ' + _date )