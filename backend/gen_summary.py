import json
from dotenv import load_dotenv
import os
import requests
load_dotenv()

# get score and proposal information
# info = gen_info.main()
# score = info[0]
# miss_feed = info[1]
# null_feed = info[2]
# prop_info = info[3]

def dev_feedback(score, null_feed, miss_feed):
   num_null = len(null_feed)
   num_miss = len(miss_feed)
   null_script = ""
   miss_script = ""
   if num_null == 0 and num_miss == 0: 
        feedback = "Great Job!" 
   if num_null != 0:
        null_script = "\nYour proposal did not include key pieces of information: \n"
        for i in range(num_null):
            null_script += f"     {i+1}) {null_feed[i]}"
   if num_miss != 0:
        miss_script = "\nYour proposal did not meet the funding criteria in the following ways: \n"
        for i in range(num_miss):
            miss_script += f"     {i+1}) {miss_feed[i]}"  
   if num_null != 0 or num_miss != 0:     
        feedback = f"Below is some insight as to why your received this score:\n{miss_script}{null_script}" 
   
   script = f"Your proposal received a score of {score}. {feedback}"  
   return script 

def inv_feedback(score, prop_info, null_feed, miss_feed):
    # API info
    url = "https://openrouter.ai/api/v1/chat/completions"
    key = os.getenv("OPEN_API_KEY")
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
        }
    prompt = f"""

Please summarize the energy access proposal using the format and instructions below.
Only use information explicitly provided in {prop_info}, {score}, {null_feed}, and {miss_feed}.
Do not invent missing information. If any detail is unavailable, clearly write: "There is no information regarding [field]".
Do not include this prompt or the template — only return the formatted summary.
"""

    data = {
            "model" : "meta-llama/llama-3-8b-instruct",
            "messages" : [ {
                "role" : "system",
                "content" : 
                """
    You are acting on the behalf of a rural electrification financier. In this role, you will be 
    summarizing a project proposal using the information given to you. 
                """
                },
                {
                "role " : "user", 
                "content" : json.dumps(prompt)
                }
            ]
        }
    answer = requests.post(url, headers=headers, json=data)
    response = answer.json()["choices"][0]["message"]["content"]
    return response










    # f"""

    # Please provide the following summary of an energy access proposal using the following instructions: 

    # Use the following format: 

    # Company Name
    # Village Name
    # Longitude, latitude
    # Score: use the score value inputed here -- {score}
    # (If there is insufficient information -- DO NOT MAKE UP RANDOM INFORMATION. 
    # Simply write that "there is insufficient information.")

    # First Paragraph {prop_info}:
    # One sentence with information about the duration (start date, duration)
    # One sentence with the capital expenditures (capex), operational expenditures (opex), and the total requested funds (total_cost)
    # One sentence summary of the sustainability plan
    # Two-three sentences about the impact. Include information about the carbon emissions avoided (c02), 
    # number of connections (num_houses), number of people impacted (num_ppl), and the productive uses of energy
    # that will be brought about because of the project.
    # --- if there is insufficient information to complete these sentences, write the following: "There is no information 
    # regarding the (variable in which information is missing)"

    # Second Paragraph: 
    # One or two sentences detailing missing information {null_feed}
    # One or two sentences detailing where the project projections do not fulfill the criteria according
    # to {miss_feed}. Do not provide analysis, simply state where it does not match. 
    # (IF miss_feed and null_feed are empty, write: "This project does not have any clear deficiencies")

    # DO NOT PROVIDE YOUR OWN ANALYSIS. Simply state the data in legible form and that is all. Additionally, do not
    # put the template provided in your response. Only the answer.  
    # """