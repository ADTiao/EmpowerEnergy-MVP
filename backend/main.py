import llm_reply
import gen_info
import gen_summary

def main():
    basic_prop = gen_info.proposal
    criteria = gen_info.criteria
    weights = gen_info.weights
    file = "sampledoc.pdf"

    response = llm_reply.api_call(file)
    # make bool true to have llm analyze document
    bool = False
    proposal = gen_info.get_prop(bool, response, basic_prop)
    prop_info = gen_info.scoring(proposal, criteria, weights)

    score = prop_info[0]
    miss_feed = prop_info[1]
    null_feed = prop_info[2]

    dev_feed = gen_summary.dev_feedback(score, null_feed, miss_feed)
    inv_feed = gen_summary.inv_feedback(score, proposal, null_feed, miss_feed)

    print("developer feedback:")
    print(dev_feed)
    print("\n\n investor feedback \n\n")
    print(inv_feed)

if __name__ == "__main__":
    main()


