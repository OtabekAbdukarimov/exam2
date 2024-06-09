from django.shortcuts import render
from .models import books, borrowingrecords

def book_list(request):
    book_s = books.objects.all()
    book_details = []
    for book in book_s:
        current_borrower = borrowingrecords.objects.filter(book=book, return_date__isnull=True).first()
        book_details.append({
            'title': book.title,
            'author': book.author.name,
            'borrower': current_borrower.member.name if current_borrower else 'Available'
        })
    return render(request, 'main.html', {'book_details': book_details})
