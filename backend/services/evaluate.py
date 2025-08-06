# ----------- HELPERS --------------
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
    "duration": "range"
}
label_dict = {
    "carbon": "carbon emissions avoided",
    "connections": "connections",
    "women_consideration": "women considered in project development",
    "track_women": "mechanisms to moniter women's progress",
    "w_comm_prog": "female community programs",
    "pue": "PUEs",
    "econ_focus": "economic partnerships",
    "capex": "CAPEX",
    "opex": "OPEX",
    "cpc": "CPC",
    "lev_ratio": "leverage ratio",
    "tariff": "tariff cost",
    "lcoe": "lcoe",
    "requested_funds": "requested funds",
    "per_local_tech": "percent of local technicians",
    "scalable": "a scalable project",
    "solution": "energy solution",
    "monitering": "a remote monitering system",
    "backup": "backup generation",
    "duration": "duration"
    }
example_metrics = {
    "general": {
      "company": "BrightPower Solutions Ltd",
      "village": "Kakuma",
      "start": "2024-01-15",
      "longitude": 34.8917,
      "latitude": 3.7072,
      "energy_generated": 1250000
    },
  
    "impact": {
      "carbon": 850,
      "connections": 350,
      "women_consideration": True,
      "track_women": 2,
      "w_comm_prog": 3,
      "pue": 4,
      "econ_focus": 15
    },
  
    "finance": {
      "capex": 175000,
      "opex": 55000,
      "cpc": 3.5,
      "lev_ratio": 1.5,
      "tariff_type": "tiered",
      "tariff": 0.25,
      "lcoe": 0.184,
      "requested_funds" : 109200
    },
  
    "dev": {
      "per_local_tech": 0.6
    },
  
    "tech": {
      "scalable": False,
      "solution": "mini grid",
      "monitering" : True,
      "backup" : False
    },
  
    "timeline": {
      "duration": 365
    }
}

# function to evaluate if the metric is greater than the criteria and provide feedback
def lesser(final : dict, categ : str, sub : str, metric, criteria, feed : dict):
    val = metric <= criteria
    final.setdefault(categ, {})[sub] = val
    if val == False:
        feed.setdefault(categ, {})[sub] = f"Your {label_dict[sub]} is too high"
def greater(final : dict, categ : str, sub : str, metric, criteria, feed : dict):
    val = metric >= criteria
    final.setdefault(categ, {})[sub] = val
    if val == False:
        feed.setdefault(categ, {})[sub] = f"Your {label_dict[sub]} underperforms expectations"
def range(final : dict, categ : str, sub : str, metric, low, high, feed : dict):
    val = (metric > low and metric < high)
    final.setdefault(categ, {})[sub] = val
    if val == False:
        feed.setdefault(categ, {})[sub] = f"Your {label_dict[sub]} does not lie inside of the expected range"
def bool_string(final : dict, categ : str, sub : str, metric, criteria, feed : dict):
    val = metric == criteria
    final.setdefault(categ, {})[sub] = val
    if val == False:
        feed.setdefault(categ, {})[sub] = f"Your {label_dict[sub]} should not be used for this type of project"

# will likely add more -- maybe some that have an api call

# ------- MAIN FUNCTIONS -------

#function will populate a dictionary with True or False depending on if the provided metrics fulfill the criteria
# inputs: metrics dictionary from LLM, category to evaluate, criteria dictionary determined by funder
# output: dictionary with True or False values

def evaluate_category(metrics : dict, category: str, criteria : dict, feed : dict, final : dict):
    # proposal values
    prop_info = metrics[category]
    # loop through dictionary keys
    for key in prop_info:
        metric = prop_info[key]
        if key in help_dict:
            label = label_dict[key]
        else:
            continue
        if metric == None:
            final.setdefault(category, {})[key] = None
            final[category][key] = None
            feed.setdefault(category, {})[key] = f"The {label} is not included in your proposal"
        elif help_dict[key] == "range":
            range(final, category, key, metric, criteria[key][0], criteria[key][1], feed)
        elif help_dict[key] == "greater":
            greater(final, category, key, metric, criteria[key], feed)
        elif help_dict[key] == "lesser":
            lesser(final, category, key, metric, criteria[key], feed)
        elif help_dict[key] == "bool_string":
             bool_string(final, category, key, metric, criteria[key], feed)
        elif help_dict[key] == "bool":
            final.setdefault(category, {})[key] = metric
            if metric == False:
                feed.setdefault(category, {})[key] = f"Your proposal does not seem to be {label}"

# Input: final dictionary with True or Falses, Weighting dictionary
# Output: Final score and dictionary of scores per category

def weights_helper(category, impact_weights, finance_weights, dev_weights, tech_weights, timeline_weights):
    if category == "impact":
        return impact_weights
    if category == "finance":
        return finance_weights
    if category == "dev":
        return dev_weights
    if category == "tech":
        return tech_weights
    if category == "timeline":
        return timeline_weights

def evaluate_whole(final : dict, impact_weights : dict, finance_weights : dict, 
                   dev_weights : dict, tech_weights : dict, timeline_weights : dict, 
                   categ_weights : dict, feed):
    cat_scores = {}
    score = 0
    for categ in final: 
        category = final[categ]
        for metric in category:
            cat_scores.setdefault(categ, 0)
            if category[metric]:
                weights = weights_helper(categ, impact_weights, finance_weights, dev_weights, tech_weights, timeline_weights)
                cat_scores[categ] += weights[metric]
    for category in categ_weights:
        score += cat_scores[category] * categ_weights[category]
    score = score * 100
    for key in cat_scores:
        cat_scores[key] *= 100
    return score, cat_scores, feed

def main(metrics, impact_crit, finance_crit, dev_crit, tech_crit, timeline_crit, impact_weight,
         finance_weight, dev_weight, tech_weight, timeline_weight, categ_weight):
    feed = {}
    final = {}
    evaluate_category(metrics, "impact", impact_crit, feed, final)
    evaluate_category(metrics, "finance", finance_crit, feed, final)
    evaluate_category(metrics, "dev", dev_crit, feed, final)
    evaluate_category(metrics, "tech", tech_crit, feed, final)
    evaluate_category(metrics, "timeline", timeline_crit, feed, final)
    # print(final, feed)
    return evaluate_whole(final, impact_weight, finance_weight, dev_weight, tech_weight,
                          timeline_weight, categ_weight, feed)

if __name__ == "__main__":

        # ----------- MOCK CRITERIA ----------
    mock_impact = {'carbon': [230, 300], 'connections': 150, 'women_consideration': True, 
              'track_women': 3, 'w_comm_prog': 2, 'pue': 5, 'econ_focus': 4}  
    mock_finance = {'capex': [50000, 300000], 'opex': [15000, 30000], 'cpc': [0.5, 4.0], 
               'lev_ratio': 2, 'tariff': 'mixed_tier', 'tariff': [0, 3.5], 'lcoe': [0.2, 0.4], 
               'requested_funds': [0, 190000]} 
    mock_dev = {'per_local_tech': 75.0} 
    mock_tech = {'scalable': True, 'solution': 'mini grid', 'monitering': True, 'backup': True} 
    mock_timeline = {'duration': [100, 366]}
    
    # ------------ MOCK WEIGHTS ------------
    mock_categ_weights = {
        "impact" : .2,
        "finance" : .2,
        "dev" : .2,
        "tech" : .2,
        "timeline" : .2
    }
    mock_impact_weights = {
            "carbon": .4,
            "connections": .1,
            "women_consideration": .1,
            "track_women": .1,
            "w_comm_prog": .1,
            "pue": .1,
            "econ_focus": .1,
        }
    mock_finance_weights = {
            "capex": .3,
            "opex": .2,
            "cpc": .1,
            "lev_ratio": .1,
            "tariff": .1,
            "lcoe": .1,
            "requested_funds": .1,
        }
    mock_dev_weights = {
        "per_local_tech": 1
    }
    mock_tech_weights = {
        "scalable": .3,
        "solution": .5,
        "monitering" : .1,
        "backup" : .1
    }
    mock_timeline_weights = {
        "duration": 1
    }

    eval = main(example_metrics, mock_impact, mock_finance, mock_dev, mock_tech, mock_timeline, mock_impact_weights,
         mock_finance_weights, mock_dev_weights, mock_tech_weights, mock_timeline_weights, mock_categ_weights)

    print(eval)



    
    


# sub_weights = {
    #     "impact": {
    #         "carbon": 1,
    #         "connections": 1,
    #         "women_consideration": 1,
    #         "track_women": 1,
    #         "w_comm_prog": 1,
    #         "pue": 1,
    #         "econ_focus": 1,
    #     },
    #     "finance" : {
    #         "capex": 1,
    #         "opex": 1,
    #         "cpc": 1,
    #         "lev_ratio": 1,
    #         "tariff": 1,
    #         "lcoe": 1,
    #         "requested_funds": 1,
    #     },
    #     "dev" : {
    #         "per_local_tech": 1,
    #     },
    #     "tech" : {
    #         "scalable": 1,
    #     "solution": 1,
    #         "monitering": 1,
    #         "backup": 1,
    #     },
    #     "timeline" : {
    #         "dur": 1
    #     }
    # }
    # cat_weights = {
    #     "impact" : .20,
    #     "finance" : .20,
    #     "dev" : .20,
    #     "tech" : .20,
    #     "timeline" : .20 
    # }