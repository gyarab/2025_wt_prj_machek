from ninja import NinjaAPI, Schema
from typing import List, Optional
from datetime import date
from app.models import Book, Author

api = NinjaAPI()


class BookIn(Schema):
    title: str
    published_date: date
    author_id: int

class BookOut(Schema):
    id: int
    title: str
    published_date: date
    author_id: int

# --- Endpointy ---

# 1. Seznam knih
@api.get("/book", response=List[BookOut])
def list_books(request):
    return Book.objects.all()

# 2. Detail knihy
@api.get("/book/{book_id}", response=BookOut)
def get_book(request, book_id: int):
    return Book.objects.get(id=book_id)

# 3. Vytvoření nové knihy
@api.post("/book", response=BookOut)
def create_book(request, payload: BookIn):
    book = Book.objects.create(**payload.dict())
    return book

# 4. Úprava existující knihy
@api.put("/book/{book_id}", response=BookOut)
def update_book(request, book_id: int, payload: BookIn):
    book = Book.objects.get(id=book_id)
    for attr, value in payload.dict().items():
        setattr(book, attr, value)
    book.save()
    return book
