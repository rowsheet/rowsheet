from django.template.loader import render_to_string
from django.conf import settings
from django.core import serializers
from django.http import JsonResponse, HttpResponse

def ajax(request):
    start = int(request.GET.get("start"))
    length = int(request.GET.get("length"))
    draw = request.GET.get("draw")
    print("START:   %s" % start)
    print("LENGTH:  %s" % length)
    from storefront.models import Product
    total = len(Product.objects.all())
    result = Product.objects.all().order_by("-id")[start:(start+length)]
    response = {
    "draw": draw,
    "recordsTotal": total,
    "recordsFiltered": total,
    "data": [
        [
        item.id,
        item.parent_product_id,
        item.visible,
        item.for_sale,
        item.discontinued,
        item.vendor,
        item.name,
        item.upc,
        item.vendor_code,
        item.details_kv,
        item.base_price,
        item.price,
        item.uofm,
        item.inventory,
        item.bin_date,
        item.weight,
        item.category,
        item.description,
        item.creation_timestamp,
        item.last_changed_timestamp,
        item.job_timestamp,
        item.adilas_active,
        item.adilas_import_timestamp,
        item.adilas_import_error
    ] for item in result]}
    return JsonResponse(response)

def test(request):
    return HttpResponse("""
<div class="col-md-12">
<table id="example" class="display nowrap" style="width:100%">
    <thead>
        <tr>
            <th>NAME</th>
            <th>DESCRIPTION</th>
            <th>ADILAS ACTIVE</th>
            <th>ADILAS IMPORT TIMESTAMP</th>
            <th>ADILAS IMPORT ERROR</th>
            <th>VISIBLE</th>
            <th>FOR_SALE</th>
            <th>DISCONTINUED</th>
            <th>VENDOR</th>
            <th>UPC</th>
            <th>VENDOR CODE</th>
            <th>BASE PRICE</th>
            <th>PRICE</th>
            <th>IMAGE</th>
            <th>UOFM</th>
            <th>INVENTORY</th>
            <th>DATE CREATED</th>
            <th>WEIGHT</th>
            <th>CATEGORY</th>
            <th>CREATION TIMESTAMP</th>
            <th>LAST CHANGED TIMESTAMP</th>
            <th>JOB TIMESTAMP</th>
        </tr>
    </thead>
    <tfoot>
        <tr>
            <th>NAME</th>
            <th>DESCRIPTION</th>
            <th>ADILAS ACTIVE</th>
            <th>ADILAS IMPORT TIMESTAMP</th>
            <th>ADILAS IMPORT ERROR</th>
            <th>VISIBLE</th>
            <th>FOR_SALE</th>
            <th>DISCONTINUED</th>
            <th>VENDOR</th>
            <th>UPC</th>
            <th>VENDOR CODE</th>
            <th>BASE PRICE</th>
            <th>PRICE</th>
            <th>IMAGE</th>
            <th>UOFM</th>
            <th>INVENTORY</th>
            <th>DATE CREATED</th>
            <th>WEIGHT</th>
            <th>CATEGORY</th>
            <th>CREATION TIMESTAMP</th>
            <th>LAST CHANGED TIMESTAMP</th>
            <th>JOB TIMESTAMP</th>
        </tr>
    </tfoot>
</table>
</div>
<script>
$(document).ready(function() {
    $('#example').DataTable( {
        "scrollY": 500,
        "scrollX": true,
        "processing": true,
        "serverSide": true,
        "ajax": "/tests/ajax/",
    } );
} );
console.log("TEST");
</script>
    """)
