import json


# The process_request function takes in a request string (contains a JSON object)
# and outputs a list contains ALL possible choices of that request.

def process_request(req_str):
    req_obj = req_str[len("|request|"):].strip()
    json_obj = json.loads(req_obj)
    req_id = str(json_obj["rqid"])

    choice = [[], ""]
    choice[1] = "|" + req_id

    if "wait" in json_obj:
        if json_obj["wait"]:
            return choice
    elif "teamPreview" in json_obj:
        if json_obj["teamPreview"]:
            if len(json_obj["side"]["pokemon"]) == 6:
                choice[0].append("choose team 123456")
                choice[0].append("choose team 213456")
                choice[0].append("choose team 312456")
                choice[0].append("choose team 412356")
                choice[0].append("choose team 512346")
                choice[0].append("choose team 612345")
            else:
                choice[0].append("choose default")
            return choice
    elif "forceSwitch" in json_obj:
        if json_obj["forceSwitch"] == [True]:
            try:
                switch_choice = json_obj["side"]["pokemon"]

                for i in range(len(switch_choice)):
                    if (not switch_choice[i]["active"]) and (switch_choice[i]["condition"] != "0 fnt"):
                        choice[0].append("choose switch " + switch_choice[i]["ident"][4:].strip())

                return choice
            except Exception:
                choice[0].append("choose default")
                return choice
    elif "active" in json_obj:
        try:
            move_choice = json_obj["active"][0]["moves"]

            for i in range(len(move_choice)):
                if "disabled" in move_choice[i]:
                    if not move_choice[i]["disabled"]:
                        choice[0].append("choose move " + move_choice[i]["id"])
                else:
                    choice[0].append("choose move " + move_choice[i]["id"])

            if "canMegaEvo" in json_obj["active"][0]:
                if json_obj["active"][0]["canMegaEvo"]:
                    for i in range(len(move_choice)):
                        if not move_choice[i]["disabled"]:
                            choice[0].append("choose move " + move_choice[i]["id"] + " mega")
            elif "canZMove" in json_obj["active"][0]:
                zmove_lst = json_obj["active"][0]["canZMove"]

                for i in range(len(zmove_lst)):
                    if zmove_lst[i] is not None:
                        choice[0].append("choose move " + move_choice[i]["id"] + " zmove")
            elif "canUltraBurst" in json_obj["active"][0]:
                if json_obj["active"][0]["canUltraBurst"]:
                    for i in range(len(move_choice)):
                        if not move_choice[i]["disabled"]:
                            choice[0].append("choose move " + move_choice[i]["id"] + " ultra")

            if "trapped" in json_obj["active"][0]:
                if json_obj["active"][0]["trapped"]:
                    return choice

            switch_choice = json_obj["side"]["pokemon"]

            for i in range(len(switch_choice)):
                if (not switch_choice[i]["active"]) and (switch_choice[i]["condition"] != "0 fnt"):
                    choice[0].append("choose switch " + switch_choice[i]["ident"][4:].strip())

            return choice
        except Exception:
            choice[0].append("choose default")
            return choice
    else:
        choice[0].append("choose default")
        return choice
