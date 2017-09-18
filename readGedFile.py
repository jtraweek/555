file = open("test.ged", "r")

validTags = {"NAME": 1, "SEX": 1, "BIRT": 1, "DEAT": 1, "FAMC": 1, "FAMS": 1, "MARR": 1, "HUSB": 1,
             "WIFE": 1, "CHIL": 1, "DIV": 1, "DATE": 2, "HEAD": 0, "TRLR": 0, "NOTE": 0}

for line in file:
    line = line.strip()
    print("--> {}".format(line))
    words = line.split(" ")

    if len(words) < 2:
        print("<-- {}|{}".format(line, "N"))
        continue

    level = words[0]
    tag = ""
    valid = "N"
    args = ""

    if level.isdigit():
        level = int(level)
        if len(words) == 3 and words[2] in ["INDI", "FAM"] and level == 0:
            tag = words[2]
            args = words[1]
            valid = "Y"
        else:
            tag = words[1]
            if level == validTags.get(tag):
                valid = "Y"

            for i in range(2, len(words)):
                args += words[i] + " "
            args = args[:-1]

        if len(args) > 0:
            print("<-- {}|{}|{}|{}".format(level, tag, valid, args))
        else:
            print("<-- {}|{}|{}".format(level, tag, valid))
