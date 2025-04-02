from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContractUploadForm
from .models import Contract
from .utils import extract_text_from_file
from .llm import summarize, extract_key_info, red_flags, generate_title
import os

def upload_contract(request):
    if request.method == "POST":
        form = ContractUploadForm(request.POST, request.FILES)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.raw_text = extract_text_from_file(request.FILES['file'])
            contract.title = generate_title(contract.raw_text)
            contract.summary = summarize(contract.raw_text)
            contract.key_info = extract_key_info(contract.raw_text)
            contract.red_flags = red_flags(contract.raw_text)

            contract.save()
            return redirect('view_contract', pk=contract.pk)
    else:
        form = ContractUploadForm()
    return render(request, 'analyzer/upload_contract.html', {'form': form})
    
def view_contract(request, pk):
    contract = Contract.objects.get(pk=pk)
    return render(request, 'analyzer/view_contract.html', {'contract': contract})

def contract_list(request):
    contracts = Contract.objects.all().order_by('-uploaded_at')
    return render(request, 'analyzer/contract_list.html', {'contracts': contracts}) 

def delete_contract(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == "POST":
        contract.delete()
        return redirect('contract_list')
    return render(request, 'analyzer/delete_confirmation.html', {'contract': contract})
