
from django.shortcuts import render
from .models import Contract


def archive(request):
    contracts = Contract.objects.select_related(
        'client',
        'agent',
        'branch',
        'insurance_type'
    ).all()

    return render(request, 'archive.html', {
        'contracts': contracts
    })
