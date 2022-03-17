from django import forms
from .models import Books

class BookForm(forms.ModelForm):
    class Meta:
        model=Books
        fields="__all__"

        labels = {
            'bookName': "Book Name",
            'bookPrice': "Book Price",
            'bookAuthor': "Author Name",
            'bookSummary': "Book Summary",
            'image':"Load Image",
        }

