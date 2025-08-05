# from backend.services.funder import impact_dict, finance_dict, dev_dict, tech_dict, timeline_dict
# from backend.services.funder import category_weights, impact_weights, finance_weights, dev_weights, tech_weights, timeline_weights
from backend.info import info as final
from backend.services.evaluate import main as evaluate

# will be used after user clicks analyze and info dictionary has been completely filled
def analyze():
    for key in final:
        if key == "proposal":
            proposal = final[key]
        if key == "criteria":
            categories = final[key]
            for category in categories:
                if category == "impact":
                    impact_dict = categories[category]
                if category == "finance":
                    finance_dict = categories[category]
                if category == "dev":
                    dev_dict = categories[category]
                if category == "tech":
                    tech_dict = categories[category]
                if category == "timeline":
                    timeline_dict = categories[category]
        if key == "weights":
            categories = final[key]
            for category in categories:
                if category == "grand":
                    category_weights = categories[category]
                if category == "impact":
                    impact_weights = categories[category]
                if category == "finance":
                    finance_weights = categories[category]
                if category == "dev":
                    dev_weights = categories[category]
                if category == "tech":
                    tech_weights = categories[category]
                if category == "timeline":
                    timeline_weights = categories[category]

    info = evaluate(metrics=proposal, impact_crit=impact_dict, finance_crit=finance_dict,
                          dev_crit=dev_dict, tech_crit=tech_dict, timeline_crit=timeline_dict,
                          impact_weight=impact_weights, finance_weight=finance_weights, 
                          dev_weight=dev_weights, tech_weight=tech_weights, timeline_weight=timeline_weights, 
                          categ_weight=category_weights)
    category_scores = info[1]
    
    score = info[0]
    impact_score = category_scores[0]
    finance_score = category_scores[1]
    dev_score = category_scores[2]
    tech_score = category_scores[3]
    timeline_score = category_scores[4]
    feedback = info[2]

    output = {
        "overall" : score,
        "impact" : impact_score,
        "finance" : finance_score,
        "dev" : dev_score,
        "tech" : tech_score,
        "timeline" : timeline_score,
        "feed" : feedback
    }

    return output

if __name__ == "__main__":
    print("HELLO WORLD")

    
    
    





