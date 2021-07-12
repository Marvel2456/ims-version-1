from django import forms
from .models import *


"""class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Item_name', 'category', 'quantity']"""

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"

    def clean_brand_name(self):
        brand_name = self.cleaned_data.get('brand_name')
        if not brand_name:
            raise forms.ValidationError('This field is required')

        for brand in Brand.objects.all():
            if brand.brand_name == brand_name:
                raise forms.ValidationError(brand_name + ' is already created')
        return brand_name


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name',]

    def clean_category_name(self):
        category_name = self.cleaned_data.get('category_name')
        if not category_name:
            raise forms.ValidationError('This field is required')

        for category in Category.objects.all():
            if category.category_name == category_name:
                raise forms.ValidationError(category_name + ' is already created')
        return category_name
        

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Item_name', 'category', 'brand', 'quantity', 'batch_no', 'unit', 'price', 'reorder_level', 'status']

    def clean_Item_name(self):
        Item_name = self.cleaned_data.get('Item_name')
        if not Item_name:
            raise forms.ValidationError('This field is required')

        for product in Product.objects.all():
            if product.Item_name == Item_name:
                raise forms.ValidationError(Item_name + ' is already created')
        return Item_name

class SaleForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [ 'mode_of_sales', 'amount', 'quantity_sold',]

class CountForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['count',]

class RestockForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [ 'quantity_restocked', 'price',]

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('Item_name', 'category', 'brand', 'quantity', 'batch_no', 'unit', 'price', 'status')

class ReorderLevelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['reorder_level']

class ProductSearchForm(forms.ModelForm):
    download_csv = forms.BooleanField(required=False)
    class Meta:
        model = Product
        fields = ['Item_name',]

class ProductReportSearchForm(forms.ModelForm):
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)
    download_csv = forms.BooleanField(required=False)
    class Meta:
        model = Product
        fields = ['start_date', 'end_date',]