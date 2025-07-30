# ----------- HELPERS --------------

# function to evaluate if the metric is greater than the criteria and provide feedback
def lesser(dict, categ, sub, metric, criteria, feed):
        val = metric <= criteria
        dict[categ][sub] = val
        if val == False:
            feed[categ][sub] == f"Your {sub} is too high"

def greater(dict, categ, sub, metric, criteria, feed):
        val = metric >= criteria
        dict[categ][sub] = val
        if val == False:
            feed[categ][sub] == f"Your {sub} underperforms expectations"

def range(dict, categ, sub, metric, low, high, feed):
    val = (metric > low and metric < high)
    dict[categ][sub] = val
    if val == False:
        feed[categ][sub] == f"Your {sub} is outside of the expected range"

def bool_string(dict, categ, sub, metric, criteria, feed):
    val = metric == criteria
    dict[categ][sub] = val
    if val == False:
        feed[categ][sub] == f"Your {sub} should not be used for this type of project"


# will likely add more -- maybe some that have an api call


# ------- MAIN -------

#function will populate a dictionary with True or False depending on if the provided metrics fulfill the criteria
# inputs: metrics dictionary from LLM, category to evaluate, criteria dictionary determined by funder
# output: dictionary with True or False values

def evaluate_category(metrics, category, criteria, feed, final):
    help_dict = {
    "carbon": "range",
    "connections": "greater",
    "women_consideration": "bool",
    "track_women": "greater",
    "w_comm_prog": "greater",
    "pue": "greater",
    "econ_focus": "greater",
    "capex": "range",
    "opex": "range",
    "cpc": "range",
    "lev_ratio": "greater",
    "tariff": "range",
    "lcoe": "range",
    "requested_funds": "range",
    "per_local_tech": "greater",
    "scalable": "bool",
    "solution": "bool_string",
    "monitering": "bool",
    "backup": "bool",
    "dur": "range"
}
    # impact criteria
    d1 = metrics[category]
    # loop through dictionary keys
    for key in d1:
        metric = d1[key]
        if key not in help_dict:
            continue
        elif metric == None:
            final[category][key] = None
            feed[category][key] = f"The {key} is not included in your proposal"
        elif help_dict[key] == "range":
            range(final, category, key, metric, criteria[key][0], criteria[key][1])
        elif help_dict[key] == "greater":
            greater(final, category, key, metric, criteria[key])
        elif help_dict[key] == "lesser":
            lesser(final, category, key, metric, criteria[key])
        elif help_dict[key] == "bool_string":
             bool_string(final, category, key, metric, criteria[key])
        elif help_dict[key] == "bool":
            final[category][key] = metric
            if metric == False:
                feed[category][key] = f"Your proposal does not seem to be {key}"

# Input: final dictionary with True or Falses, Weighting dictionary
# Output: Final score and dictionary of scores per category
def evaluate_whole(final):
    sub_weights = {
        "carbon": 1,
        "connections": 1,
        "women_consideration": 1,
        "track_women": 1,
        "w_comm_prog": 1,
        "pue": 1,
        "econ_focus": 1,
        "capex": 1,
        "opex": 1,
        "cpc": 1,
        "lev_ratio": 1,
        "tariff": 1,
        "lcoe": 1,
        "requested_funds": 1,
        "per_local_tech": 1,
        "scalable": 1,
        "solution": 1,
        "monitering": 1,
        "backup": 1,
        "dur": 1
    }
    cat_weights = {
        "impact" : .20,
        "finance" : .20,
        "dev" : .20,
        "tech" : .20,
        "timeline" : .20 
    }
    cat_scores = {}
    score = 0
    for category in final: 
        for key in category:
            if category[key]:
                cat_scores[category] += sub_weights[key]
    for category in cat_weights:
        score += cat_scores[category] * cat_weights[category]
    return score, cat_scores

