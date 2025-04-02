from django.shortcuts import render, redirect 
from .forms import ContractUploadForm
from .models import Contract
from .utils import extract_text_from_file
import os

def upload_contract(request):
    if request.method == "POST":
        form = ContractUploadForm(request.POST, request.FILES)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.raw_text = extract_text_from_file(request.FILES['file'])
            contract.save()
            return redirect('view_contract', pk=contract.pk)
        else:
            form = ContractUploadForm()
        return render(request, 'anaylzer/upload.html', {'form': form})
    
def view_contract(request, pk):
    contract = Contract.objects.get(pk=pk)
    return render(request, 'analyzer/result.html', {'contract': contract})

