from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_list(request):
    """ A view that renders the list contents page """

    return render(request, 'list/list.html')

def add_to_list(request, item_id):
    """ Add a quantity of the specified product to the shopping list """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    list = request.session.get('list', {})

    if size:
        if item_id in list(list.keys()):
            if size in list[item_id]['items_by_size'].keys():
                list[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {list[item_id]["items_by_size"][size]}')
            else:
                list[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your list')
        else:
            list[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your list')
    else:
        if item_id in list(list.keys()):
            list[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {list[item_id]}')
        else:
            list[item_id] = quantity
            messages.success(request, f'Added {product.name} to your list')

    request.session['list'] = list
    return redirect(redirect_url)
    

def adjust_list(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    list = request.session.get('list', {})

    if size:
        if quantity > 0:
            list[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {list[item_id]["items_by_size"][size]}')
        else:
            del list[item_id]['items_by_size'][size]
            if not list[item_id]['items_by_size']:
                list.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your list')
    else:
        if quantity > 0:
            list[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {list[item_id]}')
        else:
            list.pop(item_id)
            messages.success(request, f'Removed {product.name} from your list')

    request.session['list'] = list
    return redirect(reverse('view_list'))


def remove_from_list(request, item_id):
    """Remove the item from the shopping list"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        list = request.session.get('list', {})

        if size:
            del list[item_id]['items_by_size'][size]
            if not list[item_id]['items_by_size']:
                list.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your list')
        else:
            list.pop(item_id)
            messages.success(request, f'Removed {product.name} from your list')

        request.session['list'] = list
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)