## goal is to receive a pdf and then extract the information
import pdfplumber # type: ignore
import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()

# turns file to JSON
def extract_text(filepath):
    # eventually store text
    extracted_text = " "
    # open pdf and extract text
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                extracted_text += text
        dict = {
        "message" : extracted_text
        }
        final_form = json.dumps(dict)
    return final_form

def api_call(file):
    key = os.getenv("OPEN_API_KEY")
    text = extract_text(file)
    with open("response.json", "r") as f:
        template = f.read()
    # start requests
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
    }
    prompt = f"""

Here is the proposal you will be analyzing: {text}

In this proposal, you must idenitfy the following components described here : {template}

Please return the following filled-in template **as valid JSON**, enclosed in curly braces and using double quotes. 
Use `null` instead of `None`. Do not include 'value :'. For example, for the location, I want the template to be populated as such:

If there is no information to populate a certain key, put the value as null. Do not put the value as None. 

Return **ONLY** the populated template -- nothing else. Even at the begginnning, do not put "here is the populated template. 
I only want the JSON template.   

Thank you.

""" 
    data = {
        "model" : "meta-llama/llama-3-8b-instruct",
        "messages" : [ {
            "role" : "system",
            "content" : 
            """
You are acting on the behalf of a rural electrification financier. In this role, you will be 
identifying various aspects of a rural energy access project proposal to aid them in their work.
            """
            },
            {
            "role " : "user", 
            "content" : prompt
            }
        ]
    }
    answer = requests.post(url, headers=headers, json=data)
    
    response = answer.json()["choices"][0]["message"]["content"]
    return response
    
def main():
    file = "sampledoc.pdf"
    answer = api_call(file)
    return answer

if __name__ == "__main__":
   print(main())