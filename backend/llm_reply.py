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
    text = text[:5000]
    file_dir = os.path.dirname(__file__)
    response_path = os.path.join(file_dir, "response.json")
    with open(response_path, "r") as f:
        template = f.read()
    desired_dir = os.path.dirname(__file__)
    desired_path = os.path.join(desired_dir, "desired_output.json")
    with open(desired_path, "r") as d:
        example = d.read()
    # start requests
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
    }
    prompt = f"""

You are given a project proposal. Your job is to extract the required information and return it as a valid JSON object.

Below is a template that explains **what each key means** and what kind of value it should contain. This is for your reference only — you should NOT return the template itself.

---

KEY DESCRIPTIONS:
{template}

---

Rules:
- Return a **flat JSON object** using only the keys described above.
- Do **not** include `"value"` or `"type"` in the output.
- Use **double quotes** around all strings.
- Use `null` for any missing or unavailable values.
- Do **not** include extra text, headings, or formatting like triple backticks (```).
- Only return the JSON object — nothing else.

Here is an example of a desired JSON output: 
{example}

This is simply an example of how the desired JSON output should be formatted, nothing more. 

Here is the proposal:
{text}

Now return the desired JSON object:


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
            "role" : "user", 
            "content" : prompt
            }
        ]
    }
    answer = requests.post(url, headers=headers, json=data)

    response = answer.json()["choices"][0]["message"]["content"]
    return response
    

if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    filepath = os.path.join(dir, "sampledoc.pdf")
    print(api_call(filepath))