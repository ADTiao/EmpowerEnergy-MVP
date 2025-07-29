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
    "people" : 500
}

criteria = {
    "duration" : 150,
    "capex" : 400,
    "opex" : 400,
    "total_cost" : 900,
    "num_houses" : 70,
    "co2" : 500,
    "people" : 250
}

weights = {
    "duration" : .10,
    "capex" : 0,
    "opex" : 0,
    "total_cost" : .40,
    "num_houses" : .20,
    "co2" : .10,
    "people" : .20
}

feedback = {
    "duration" : "the duration of your project exceeds the expected cost of this type of project.",
    "capex" : "the capital expenditures exceeds the expected cost of this type of project",
    "opex" : "the operational expenditures exceeds the expected cost of this type of project",
    "total_cost" : "the total requested funds exceeds the expected cost of this type of project",
    "num_houses" : "the number of connections underperform for a typical project of this magnitude",
    "co2" : "the avoided co2 emissions underperform for a typical project of this magnitude",
    "people" : "the number of people underperform for a typical project of this magnitude"
}

def get_prop(bool, response, basic_prop):
    if bool == True:
        if response == None or response == "":
            raise ValueError("LLM response is empty — cannot parse JSON.")
        else:   
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
    (scoring(proposal, criteria, weights))
