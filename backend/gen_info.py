import json
import math

proposal = {
    "company" : "EmpowerEnergy",
    "village" : "Nairobi",
    "longitude" : -17.91782,
    "latitude" : 30.90988,
    "start_date" : "January 7, 2025",
    "duration" : 10,
    "capex" : 10,
    "opex" : 10,
    "sus_plan" : "Here is my sustainability plan",
    "total_cost" : 8,
    "num_houses" : 1000,
    "co2" : 1000,
    "pue" : "There will be many productive uses of energy",
    "ppl" : 500
}

criteria = {
    "duration" : 150,
    "capex" : 400,
    "opex" : 400,
    "total_cost" : 900,
    "num_houses" : 70,
    "co2" : 500,
    "ppl" : 250
}

weights = {
    "duration" : .10,
    "capex" : 0,
    "opex" : 0,
    "total_cost" : .40,
    "num_houses" : .20,
    "co2" : .10,
    "ppl" : .20
}

feedback = {
    "duration" : "the duration of your project exceeds the requirement for our funding.",
    "capex" : "the capital expenditures for your project are too high",
    "opex" : "the operational expenditures for your project are too high",
    "total_cost" : "the total requested funds for your project are too high",
    "num_houses" : "the number of connections for your project is too low",
    "co2" : "the avoided co2 emissions projected for your project are too low",
    "ppl" : "the number of people impacted by your project is too low"
}

def get_prop(bool, response, basic_prop):
    if bool == True:
        llm_info = json.loads(response)
        return llm_info
    else:
        return basic_prop

def scoring(proposal, criteria, weights):
    # missing the qualitative description comparisons
    score = 0
    count = 0
    prop_crit = []
    null_crit = []
    num_metric = len(criteria)    
    for key in criteria.keys(): 
        count += 1
        if proposal[key] == None:
            score -= weights[key] * num_metric
            null_crit.append(f"Proposal is missing information regarding the {key}")
        elif count <= 4:
            if proposal[key] <= criteria[key]:
                score += weights[key] * num_metric
            else: 
                prop_crit.append(feedback[key])
        else: 
            if proposal[key] >= criteria[key]:
                score += weights[key] * num_metric
            else: 
                prop_crit.append(feedback[key])
    end_score = (score/num_metric) * 100
    return math.trunc(end_score), prop_crit, null_crit


if __name__ == "__main__":
    scoring(proposal, criteria, weights)
