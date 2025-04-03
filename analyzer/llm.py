import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv()
client = OpenAI()


def call_llm(prompt, model='gpt-3.5-turbo'):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a vital legal assistant that summarizes, analyzes and extracts key information for non-lawyers."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

def summarize(contract_text):
    prompt = f"Summarize the following contract in plain english:\n\n{contract_text}"
    return call_llm(prompt)

def extract_key_info(contract_text):
    prompt = f"""From the following contract, extract key details in bullet point format, including info like:
    - Names of all parties involved
    - Important dates
    - Payment terms or monetary values
    - Any special clauses (termination, renewal, indemnity, etc.)
    - Jurisdiction or governing law
    - Any other relevant information

    Use simple, clear, concise language:\n\n{contract_text}"""
    return call_llm(prompt)

def red_flags(contract_text):
    prompt = f"""Analyze the following contract. If it contains any suspicious, vague, 
    risky, out-of-the-ordinary, potentially harmful details or clauses that might be 
    concerning for the average person, highlight them. Be specific, explain why, and provide insight. If 
    the contract seems fair and contains no major red flags, say so clearly. Do not invent issues, but
    flag them if they exist:\n\n{contract_text}"""
    return call_llm(prompt)

def generate_title(contract_text):
    prompt = f"""Generate a title for the following contract based on its content. 
    Should be short, descriptive and no more than 8 words:\n\n{contract_text}"""
    return call_llm(prompt)

def answer_question(contract_text, user_question):
    prompt = f"""Answer the following question based on the provided 
    contract text:
    {contract_text}

    Question: "{user_question}"

    Answer in plain english, clearly and directly"""

    return call_llm(prompt)

