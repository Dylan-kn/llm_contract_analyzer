from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContractUploadForm, QuestionForm
from .models import Contract
from .utils import extract_text_from_file
from .llm import summarize, extract_key_info, red_flags, generate_title, answer_question
from django.template.loader import render_to_string
from django.http import HttpResponse
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
    contract = get_object_or_404(Contract, pk=pk)
    form = QuestionForm()
    return render(request, 'analyzer/view_contract.html', {
        'contract': contract,
        'form': form
    })

def contract_list(request):
    contracts = Contract.objects.all().order_by('-uploaded_at')
    return render(request, 'analyzer/contract_list.html', {'contracts': contracts}) 

def delete_contract(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == "POST":
        contract.delete()
        return redirect('contract_list')
    return render(request, 'analyzer/delete_confirmation.html', {'contract': contract})

def ask_question(request, pk):
    contract = get_object_or_404(Contract, pk=pk)

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            answer = answer_question(contract.raw_text, question)

            html = render_to_string('analyzer/partials/answer.html', {'answer': answer})
            return HttpResponse(html)
        
    return HttpResponse("error", status=400)

def landing_page(request):
    return render(request, 'analyzer/landing_page.html')

