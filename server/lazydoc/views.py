# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import LazyDoc

# A welcome page to allow insecure https
def hi(request):
    response = render_to_response('hi.html')
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Headers'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = '1800'
    return response

# Record building api
def new_record(request):
    print 'date:', request.POST.get('date')
    print 'recorder:', request.POST.get('recorder')
    print 'title:', request.POST.get('title')

    ld = LazyDoc()
    res_data = {}

    ld.create_rst(
        raw=request.POST.get('rstText'),
        filename=request.POST.get('title') + '.rst'
    )
    pdf_file = ld.create_pdf(
        rst_filename=request.POST.get('title') + '.rst',
        pdf_filename=request.POST.get('title') + '.pdf'
    )

    if not pdf_file:
        response = HttpResponse(json.dumps({'code': 400, 'msg': 'Parameter error'}), status=400, content_type='application/json')
    else:
        res_data['rst'] = request.POST.get('title') + '.rst'
        res_data['pdf'] = request.POST.get('title') + '.pdf'
        response = HttpResponse(json.dumps(res_data), content_type='application/json')

    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Headers'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = '1800'
    return response
