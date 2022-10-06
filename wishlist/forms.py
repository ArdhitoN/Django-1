from django import forms
from .models import BarangWishlist


class Input_Form(forms.ModelForm):
    class Meta:
        model = BarangWishlist
        fields = [
            'nama_barang', 
            'harga_barang',
            'deskripsi',
            ]

        labels = {
            'nama_barang' : 'Nama barang',
            'harga_barang' : 'Harga barang',
            'deskripsi' : 'Deskripsi',

        }

        input_attrs = {
            'type' : 'text',
            'placeholder' : 'Nama barang',
        }

        input_attrs2 = {
            'type' : 'integer',
            'placeholder' : 'Harga barang',
        }
        
        input_attrs3 = {
            'type' : 'text',
            'placeholder' : 'Deskripsi',
        }


        widgets = {
            'nama_barang' : forms.TextInput(attrs=input_attrs),
            # 'harga_barang' : forms.IntegerField(),
            'deskripsi' : forms.TextInput(attrs=input_attrs3),
        }
