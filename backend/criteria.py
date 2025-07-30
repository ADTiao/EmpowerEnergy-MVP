
# NOTE: FOR RANGE STUFF, HAVE LOW BE THE FIRST AND HIGH BE THE SECOND

def impact_dict(c02, conn, w_consider, w_track, w_comm_prog, pue, econ_partner):
    impact = {
        "carbon" : c02,
        "connections" : conn,
        "women_consideration" : w_consider,
        "track_women" : w_track,
        "w_comm_prog" : w_comm_prog,
        "pue" : pue,
        "econ_focus" : econ_partner
    }
    return impact

def finance_dict(capex, opex, cpc, lev_ratio, tarrif_type, tarrif, lcoe, funding):
    finance = {
        "capex" : capex,
        "opex": opex,
        "cpc" : cpc,
        "lev_ratio" : lev_ratio,
        "tarrif_type" : tarrif_type,
        "tarrif" : tarrif,
        "lcoe" : lcoe,
        "requested_funds" : funding
    }
    return finance

def dev_dict(per_local):
    dev = {
        "per_local_tech" : per_local
    }
    return dev

def tech_dict(scalable, match, monitering, backup):
    tech = {
        "scalable" : scalable,
        "solution" : match,
        "monitering" : monitering,
        "backup" : backup
    }
    return tech

def timeline_dict(start, dur): 
    timeline = {
        "start" : start,
        "dur" : dur
    }
    return timeline

if __name__ == "__main__":
    print("Worked")