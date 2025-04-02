import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def call_llm(prompt, model='gpt-4-turbo'):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a vital legal assistant that summarizes, analyzes and extracts key information for non-lawyers."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response['choices'][0]['message']['content'].strip()

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
    prompt = f"""Analyze the following contract and highlight any suspicious, vague, 
    risky, out-of-the-ordinary, potentially harmful details or clauses that might be 
    concerning for the average person. Be specific, explain why, and provide insight:\n\n{contract_text}"""
    return call_llm(prompt)