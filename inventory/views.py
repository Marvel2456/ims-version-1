import csv, io
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    form = ProductSearchForm(request.POST or None)
    product = Product.objects.all()

    context = {
        'product' : product,
        'form' : form,

    }

    if request.method == 'POST':
        product = Product.objects.filter(Item_name__icontains=form['Item_name'].value(),
                                        )
        
        if form['download_csv'].value() ==True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=" Product List.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
            product = product
            for product in product:
                writer.writerow([product.category, product.Item_name, product.quantity])
            return response

    context = {
        'product' : product,
        'form' : form,
    }

    return render(request, 'inventory/index.html', context)

@login_required
def brand(request):
    brand = Brand.objects.all()

    context = {
        'brand' : brand,

    }
    return render(request, 'inventory/brand.html', context)

@login_required
def category(request):
    category = Category.objects.all()

    context = {
        'category' : category,

    }
    return render(request, 'inventory/category.html', context)

@login_required
def product(request):
    form = ProductSearchForm(request.POST or None)
    product = Product.objects.all()

    
    if request.method == 'POST':
        product = Product.objects.filter(Item_name__icontains=form['Item_name'].value(),
                                        )

    context = {
        'product' : product,
        'form' : form,
    }

    return render(request, 'inventory/product.html', context)

@login_required
def reports(request):
    form = ProductReportSearchForm(request.POST or None)
    product = Product.objects.all()
    if request.method == 'POST':
        product = Product.objects.filter(last_updated__range=[  form['start_date'].value(),
                                                                form['end_date'].value(),
                                                            ]
                                        )
        if form['download_csv'].value() ==True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=" Report.csv"'
            writer = csv.writer(response)
            writer.writerow(['ITEM', 'RESTOCKED', 'IN STORE', 'SALES', 'AVAILABLE', 'COUNT', 'VARIANCE', 'DATE'])
            product = product
            for product in product:
                writer.writerow([product.Item_name, product.quantity_restocked, product.quantity, product.quantity_sold, product.available, product.count, product.variance, product.last_updated])
            return response

    context = {
        'product' : product,
        'form' : form
    
    }
    return render(request, 'inventory/reports.html', context)



def add_category(request):
    form = CategoryForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Added')
        return redirect('category')

    context = {
            'form' : form
        }
    return render(request, 'inventory/add_new.html', context)


def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('category')
    return render(request, 'inventory/delete_items.html')

def add_brand(request):
    form = BrandForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Added')
        return redirect('brand')

    context = {
            'form' : form
        }
    return render(request, 'inventory/add_new.html', context)

def delete_brand(request, pk):
    brand = Brand.objects.get(id=pk)
    if request.method == 'POST':
        brand.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('brand')
    return render(request, 'inventory/delete_items.html')


def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Added')
        return redirect('product')

    context = {
            'form' : form
        }
    return render(request, 'inventory/add_new.html', context)

def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('product')
    return render(request, 'inventory/delete_items.html')

def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductUpdateForm(instance=product)
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated')
            return redirect('product')
    context = {
        'form' : form
    }
    return render(request, 'inventory/add_new.html', context)

def product_details(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product' : product
    }
    return render(request, 'inventory/product_details.html', context)

def add_sale(request, pk):
    queryset = Product.objects.get(id=pk)
    form = SaleForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantity -= instance.quantity_sold
        instance.available = instance.quantity
        #instance.quantity_restocked = 0
        messages.success(request, 'Update Successful, ' + str(instance.quantity) +  "  "  + (instance.Item_name) + " now left in store")
        instance.save()
        sale_report = ProductReport(
            id = instance.id,
            last_updated = instance.last_updated,
            Item_name = instance.Item_name,
            quantity_sold = instance.quantity_sold,
            count = instance.count,
            quantity_restocked = instance.quantity_restocked,
            available = instance.available,
            variance = instance.variance,
            
        )
        sale_report.save()
        return redirect('/product_details/'+str(instance.id))

    context = {
        'product' : product,
        'form' : form
    }
    return render(request, 'inventory/add_new.html', context)

def product_upload(request):

    prompt = {
        'order' : 'Order of the CSV should be Item_name, category, brand, quantity, price'
    }
    if request.method == "GET":
        return render(request, 'inventory/csv_upload.html', prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set =csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=','):
        _, updated = Product.objects.update_or_create(
            Item_name = column[0],
            category = column[1],
            brand = column[2],
            quantity = column[3],
            price = column[4]
            )


    context = {
        'product' : product,
    }
    return redirect('product', context)

def add_stock(request, pk):
    product = Product.objects.get(id=pk)
    form = RestockForm(request.POST or None, instance=product)
    if form.is_valid():
        product = form.save(commit=False)
        product.quantity += product.quantity_restocked
        product.available = product.quantity
        #product.quantity_sold = 0
        messages.success(request, "Update Successful, " + str(product.quantity) + "  " + (product.Item_name) + " now left in store")
        product.save()
        stock_report = ProductReport(
            id = product.id,
            last_updated = product.last_updated,
            Item_name = product.Item_name,
            quantity_sold = product.quantity_sold,
            count = product.count,
            quantity_restocked = product.quantity_restocked,
            available = product.available,
            variance = product.variance,
            
        )
        stock_report.save()
        return redirect('/product_details/'+str(product.id))

    context = {
        'product' : product,
        'form' : form
    }
    return render(request, 'inventory/add_new.html', context)

"""def (request, pk):
    product = Product.objects.get(id=pk)
    form = RestockForm(request.POST or None, instance=product)
    
    if add_stock or add_sale in RestockForm():
        
        
        


        print(report)"""

def add_count(request, pk):
    product = Product.objects.get(id=pk)
    form = CountForm(request.POST or None, instance=product)

    if form.is_valid():
        product = form.save(commit=False)
        product.variance = product.count-product.available
        messages.success(request, 'Successfully Added')
        product.save()
        return redirect('/product_details/'+str(product.id))
        
    else:
        form = CountForm()

        context = {
            'product' : product,
            'form' : form
        }
        return render(request, 'inventory/add_new.html', context)

def reorder_level(request, pk):
    product = Product.objects.get(id=pk)
    form = ReorderLevelForm(request.POST or None, instance=product)
    if form.is_valid():
        product = form.save(commit=False)
        product.save()
        messages.success(request, 'Successfully Updated')

        return redirect('/product_details/'+str(product.id))
    
    context = {
        'product' : product,
        'form' : form
    }
    return render(request, 'inventory/add_new.html', context)







