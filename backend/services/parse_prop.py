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

async def api_call(file):
    key = os.getenv("OPEN_API_KEY")
    text = extract_text(file)
    file_dir = os.path.dirname(__file__)
    response_path = os.path.join(file_dir, "json/full_template.json")
    with open(response_path, "r") as f:
        template = f.read()
    desired_dir = os.path.dirname(__file__)
    desired_path = os.path.join(desired_dir, "json/example.json")
    with open(desired_path, "r") as d:
        example = d.read()
    # start requests
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
    }
    prompt = f"""

You are given a rural electrification project proposal. Your task is to extract specific information and return it as a valid JSON object.

Below is a **reference template** that describes what each key means and what type of value it should contain. Do **not** include this template in your output — it is for reference only.

---
TEMPLATE:
{template}
---

### Extraction Rules:

1. Return a **flat JSON object** using only the keys described in the template (e.g. general.company, impact.connections).
2. **Do not** include `"instruction"` or `"type"` fields in the output.
3. Use **double quotes** around all string values.
4. Use **lowercase true/false** for boolean values.
5. Use `null` for missing, unspecified, or unextractable values.
6. Do **not** include extra text, headings, markdown (e.g., ```), or comments.
7. Your response must be strictly and fully valid JSON.

---
Here is an example of the desired JSON format **(for formatting guidance only):**
{example}

---
Now, using the rules above, extract the information from the following project proposal:

{text}

Return a valid JSON object only. Do not include any introductory text, explanations, or formatting like markdown. Your output will be passed directly to json.loads(), so it must start with open brackets and end with closed brackets — nothing before or after.
""" 
    data = {
        "model" : "meta-llama/llama-3-8b-instruct",
        "messages" : [ {
            "role" : "system",
            "content" : 
            """
"You are a strict JSON formatter. Always return only a JSON object with no explanation or extra text."
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
    print(response)
    response = json.loads(response)

    return response
    
if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    filepath = os.path.join(dir, "MVP Mock Proposal #1.pdf")
    print(api_call(filepath))