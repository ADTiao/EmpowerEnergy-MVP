import llm_reply
import json

# going to take in inputs from llm_reply and turn to python dictionary

response = llm_reply.main()
proposal = json.loads(response)
score = 0
thresholds = {
    "duration" : 150,
    "capex" : 400,
    "opex" : 400,
    "total_cost" : 900,
    "num_houses" : 70,
    "co2" : 500,
    "ppl" : 250
}


# output the basic details and do initial scoring
def summarize_v1(proposed, thresholds):
    # have AI do another summary based on the proposed
    # score card
    if proposed["duration"] != "null" and thresholds["duration"] > proposed["duration"]:
        print(proposed["duration"])
        score += 10
    if proposed["finance"]["capex"] != "null" and thresholds["duration"] > proposed["finance"]["capex"]:
        score += 10
    if proposed["finance"]["opex"] != "null" and thresholds["duration"] > proposed["finance"]["opex"]:
        score += 10
    if proposed["finance"]["total_cost"] != "null" and thresholds["duration"] > proposed["finance"]["total_cost"]:
        score += 10
    if proposed["impact"]["num_houses"] != "null" and thresholds["num_houses"] > proposed["impact"]["num_houses"]:
        score += 10
    if proposed["impact"]["co2"] != "null" and thresholds["co2"] > proposed["impact"]["co2"]:
        score += 10
    if proposed["impact"]["ppl"] != "null" and thresholds["ppl"] > proposed["impact"]["ppl"]:
        score += 10

    return score

print(score)
            
    

    

