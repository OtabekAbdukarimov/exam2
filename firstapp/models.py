from django.db import models

class members(models.Model):
    name = models.CharField(max_length=128)
    join_date = models.DateField()

class authors(models.Model):
    name = models.CharField(max_length=128)


class books(models.Model):
    title = models.CharField(max_length=128)
    author_id = models.ForeignKey(authors, on_delete=models.CASCADE)
    published_id = models.DateField()


class borrowingrecords(models.Model):
    book_id = models.ForeignKey(books, on_delete=models.CASCADE)
    member_id = models.ForeignKey(members, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField()
