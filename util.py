import ConfigParser

def ConfigSectionMap(Config, section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

def EnforceSelectionFeasibility(budget,selected):
    numSelected = len(selected)
    if (numSelected > budget):
        for i in range(0,numSelected - budget):
            selected.pop()

    return selected
