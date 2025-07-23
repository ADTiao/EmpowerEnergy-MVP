## goal is to receive a pdf and then extract the information
import pdfplumber # type: ignore
import json
import requests

# turns python dictionary to JSON
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
        "message" : extracted_text[:100]
        }
        final_form = json.dumps(dict)
    return final_form

def api_call(file):
    with open("response.json", "r") as f:
        template = f.read()
    # start requests
    url = "http://localhost:11434/api/generate"
    prompt = f"""

You are acting on the behalf of a rural electrification financier. In this role, you will be 
identifying various aspects of a rural energy access project proposal to aid them in their work. 
In this proposal, you must idenitfy the following components: 
- company name, village name, longitude and latitude coordinates, the technical solution(s) used to 
provide renewable energy 
- project completion date, start date, and the project duration, 
- the capital expenditures (capex), operational expenditures (opex), financing structure, 
longterm sustainability plan, and the total funding required of the financier you work for. 
- # of households affected, carbon emission avoided (co2), proposed productive uses of energy (pue) as 
a result of the project, and the number of people estimated to be impacted.

Please present this information according to the following schema {template}

"""
    
    
if __name__ == "__main__":
    # load pdf
    filepath = "sampledoc.pdf"
    # convert pdf to json form
    pre_api = extract_text(filepath)

