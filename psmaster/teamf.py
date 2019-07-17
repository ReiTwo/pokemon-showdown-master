# Team Converter


def team_converter(team_lst):
    result = ""

    for pokemon in team_lst:
        # NICKNAME, SPECIES, ITEM, ABILITY, MOVES, NATURE, EVS, GENDER, IVS, SHINY, LEVEL
        pokemon_info = ["", "", "", "", "", "", "", "", "", "", ""]

        for entry in pokemon:
            if entry == pokemon[0]:
                info_entry = entry
                at_index = info_entry.find("@")

                if at_index == -1:
                    if "(M)" in info_entry:
                        pokemon_info[7] = "M"
                        info_entry = info_entry.replace("(M)", " ")
                    elif "(F)" in info_entry:
                        pokemon_info[7] = "F"
                        info_entry = info_entry.replace("(F)", " ")

                    if ("(" not in info_entry) and (")" not in info_entry):
                        pokemon_info[0] = info_entry.strip()
                    else:
                        l_index = info_entry.find("(")
                        r_index = info_entry.find(")")
                        pokemon_info[0] = info_entry[l_index + 1:r_index].strip()
                else:
                    pokemon_info[2] = string_format(info_entry[at_index + 1:])
                    info_entry = info_entry[:at_index].rstrip()

                    if "(M)" in info_entry:
                        pokemon_info[7] = "M"
                        info_entry = info_entry.replace("(M)", " ")
                    elif "(F)" in info_entry:
                        pokemon_info[7] = "F"
                        info_entry = info_entry.replace("(F)", " ")

                    if ("(" not in info_entry) and (")" not in info_entry):
                        pokemon_info[0] = info_entry.strip()
                    else:
                        l_index = info_entry.find("(")
                        r_index = info_entry.find(")")
                        pokemon_info[0] = info_entry[l_index + 1:r_index].strip()
            elif "Ability:" in entry:
                pokemon_info[3] = string_format(entry[8:])
            elif "- " == entry[:2]:
                pokemon_info[4] = pokemon_info[4] + string_format(entry[2:]) + ","
            elif "Nature" in entry:
                pokemon_info[5] = string_format(entry[:-6])
            elif "EVs:" in entry:
                pokemon_info[6] = ev_iv_calc(entry[4:])
            elif "IVs:" in entry:
                pokemon_info[8] = ev_iv_calc(entry[4:])
            elif entry == "Shiny: Yes":
                pokemon_info[9] = "S"
            elif "Level:" in entry:
                pokemon_info[10] = string_format(entry[6:])
            else:
                continue

        for element in pokemon_info:
            if element == pokemon_info[4]:
                result = result + element[:-1] + "|"
            else:
                result = result + element + "|"

        result = result + "]"

    amend_result = result.rstrip("]")
    return amend_result


def ev_iv_calc(stats):
    # HP, Atk, Def, SpA, SpD, Spe
    stats_info = ["", "", "", "", "", ""]

    stripped = stats.strip()
    format_stats = "   " + stripped.replace("/", "   ")

    if "HP" in format_stats:
        index = format_stats.find("HP")
        stats_info[0] = format_stats[index - 4:index].strip()
    if "Atk" in format_stats:
        index = format_stats.find("Atk")
        stats_info[1] = format_stats[index - 4:index].strip()
    if "Def" in format_stats:
        index = format_stats.find("Def")
        stats_info[2] = format_stats[index - 4:index].strip()
    if "SpA" in format_stats:
        index = format_stats.find("SpA")
        stats_info[3] = format_stats[index - 4:index].strip()
    if "SpD" in format_stats:
        index = format_stats.find("SpD")
        stats_info[4] = format_stats[index - 4:index].strip()
    if "Spe" in format_stats:
        index = format_stats.find("Spe")
        stats_info[5] = format_stats[index - 4:index].strip()

    result = ""
    for stat in stats_info:
        result = result + stat + ","

    amend_result = result[:-1]
    return amend_result


def string_format(str_value):
    str_temp = ""
    valid = ["a", "b", "c", "d", "e", "f", "g",
             "h", "i", "j", "k", "l", "m", "n",
             "o", "p", "q", "r", "s", "t",
             "u", "v", "w", "x", "y", "z",
             "A", "B", "C", "D", "E", "F", "G",
             "H", "I", "J", "K", "L", "M", "N",
             "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z",
             "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for c in str_value:
        if c in valid:
            str_temp = str_temp + c

    str_final = str_temp.lower()
    return str_final
