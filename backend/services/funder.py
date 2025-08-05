
def impact_dict(c02_l: int, c02_h: int, conn: int, w_consider: bool, w_track: int, 
                w_comm_prog: int, pue: int, econ_partner: int):
    impact = {
        "carbon" : [c02_l, c02_h],
        "connections" : conn,
        "women_consideration" : w_consider,
        "track_women" : w_track,
        "w_comm_prog" : w_comm_prog,
        "pue" : pue,
        "econ_focus" : econ_partner
    }
    return impact

def finance_dict(capex_l: int, capex_h: int, opex_l: int, opex_h: int, cpc_l: 
                 float, cpc_h: float, lev_ratio: float, tarrif_type: str, 
                 tarrif: float, lcoe_l: float, lcoe_h: float, fund_l: int, fund_h: int):
    finance = {
        "capex" : [capex_l, capex_h],
        "opex": [opex_l, opex_h],
        "cpc" : [cpc_l, cpc_h],
        "lev_ratio" : lev_ratio,
        "tarrif_type" : tarrif_type,
        "tarrif" : tarrif,
        "lcoe" : [lcoe_l, lcoe_h],
        "requested_funds" : [fund_l, fund_h]
    }
    return finance

def dev_dict(per_local: float):
    dev = {
        "per_local_tech" : per_local
    }
    return dev

def tech_dict(scalable: bool, solution: str, monitering: bool, backup: bool):
    tech = {
        "scalable" : scalable,
        "solution" : solution,
        "monitering" : monitering,
        "backup" : backup
    }
    return tech

def timeline_dict(dur_l: int, dur_h: int): 
    timeline = {
        # "start" : start,
        "dur" : [dur_l, dur_h]
    }
    return timeline

def category_weights(impact : float, finance : float, dev : float, tech : float, timeline : float):
    weights = {
        "impact" : impact,
        "finance" : finance,
        "dev" : dev,
        "tech" : tech,
        "timeline" : timeline
    }
    total = impact + finance + dev + tech + timeline
    if total != 1:
        raise ValueError("Weights do not add up to 1")
    return weights

def impact_weights(carbon : float, connections : float, women_consideration : float, track_women : float, 
                   w_comm_prog : float, pue : float, econ_focus : float):
    weights = {
            "carbon": carbon,
            "connections": connections,
            "women_consideration": women_consideration,
            "track_women": track_women,
            "w_comm_prog": w_comm_prog,
            "pue": pue,
            "econ_focus": econ_focus,
            },
    total = carbon + connections + women_consideration + track_women + w_comm_prog + pue + econ_focus
    if total != 1:
        raise ValueError("Weights do not add up to 1")
    return weights

    
def finance_weights(capex : float, opex : float, cpc : float, lev_ratio : float, tarrif : float, 
                    lcoe : float, funds : float):
    weights =  {
            "capex": capex,
            "opex": opex,
            "cpc": cpc,
            "lev_ratio": lev_ratio,
            "tariff": tarrif,
            "lcoe": lcoe,
            "requested_funds": funds,
        },
    total = capex + opex + cpc + lev_ratio + tarrif + lcoe + funds
    if total != 1:
        raise ValueError("Weights do not add up to 1")
    return weights
    
    
def dev_weights(per_local_tech):
    weights = {
        "per_local_tech": per_local_tech
        }
    if per_local_tech != 1:
        raise ValueError("Weights must add up to 1")
    return weights
    
def tech_weights(scalable, solution, monitering, backup):
    weights = {
            "scalable": scalable,
            "solution": solution,
            "monitering": monitering,
            "backup": backup,
        }
    total = scalable + solution + monitering + backup
    if total != 1:
        raise ValueError("Weights do not add up to 1")
    return weights
    
def timeline_weights(duration):
    weights = {
        "duration" : duration
    }
    if duration != 1:
        raise ValueError("Weights must add up to 1")
    return weights


def main():
    impact = impact_dict(c02_l=230, c02_h=300, conn=150, w_consider=True, w_track=3, w_comm_prog=2, 
                         pue=5, econ_partner=4)
    finance = finance_dict(capex_l=50000, capex_h=300000, opex_l=15000, opex_h=30000, 
                           cpc_l=0.5, cpc_h=4.0, lev_ratio=2, tarrif_type="mixed_tier", tarrif=1.5, 
                           lcoe_l=.2, lcoe_h=.4, fund_l=0, fund_h=190000)
    dev = dev_dict(per_local=75.0)
    tech = tech_dict(scalable=True, solution="mini grid", monitering=True, backup=True)
    timeline = timeline_dict(dur_l=100, dur_h=366)
    return impact, finance, dev, tech, timeline



if __name__ == "__main__":
    main()
    print(main)
