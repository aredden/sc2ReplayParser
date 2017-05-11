def listconverter(list, gamespeed):
    import s2TimeFinder
    convertedList = []
    for elem in list:
        if "CommandCenter" in elem:
            time = s2TimeFinder.findtime(elem, 75.0/gamespeed)
            convertedList.append(["CommandCenter", time])
            continue
        if "SCV" in elem:
            time = s2TimeFinder.findtime(elem, 17.0/gamespeed)
            convertedList.append(["SCV", time])
            continue
        if "MULE" in elem:
            time = s2TimeFinder.findtime(elem, 0/gamespeed)
            convertedList.append(["MULE", time])
            continue
        if "Reaper" in elem:
            time = s2TimeFinder.findtime(elem, 45.0/gamespeed)
            convertedList.append(["Reaper", time])
            continue
        if "Marine" in elem:
            time = s2TimeFinder.findtime(elem, 25.0/gamespeed)
            convertedList.append(["Marine", time])
            continue
        if "WidowMine" in elem:
            time = s2TimeFinder.findtime(elem, 40.0/gamespeed)
            convertedList.append(["WidowMine", time])
            continue
        if "Medivac" in elem:
            time = s2TimeFinder.findtime(elem, 42.0/gamespeed)
            convertedList.append(["Medivac", time])
            continue
        if "Marauder" in elem:
            time = s2TimeFinder.findtime(elem, 30.0/gamespeed)
            convertedList.append(["Marauder", time])
            continue
        if "HellionTank" in elem:
            time = s2TimeFinder.findtime(elem, 30.0/gamespeed)
            convertedList.append(["HellionTank", time])
            continue
        if "SupplyDepot" in elem:
            time = s2TimeFinder.findtime(elem, 21.0/gamespeed)
            convertedList.append(["SupplyDepot", time])
            continue
        if "Barracks" in elem:
            time = s2TimeFinder.findtime(elem, 46.0/gamespeed)
            convertedList.append(["Barracks", time])
            continue
        if "Refinery" in elem:
            time = s2TimeFinder.findtime(elem, 21.0/gamespeed)
            convertedList.append(["Refinery", time])
            continue
        if "BarracksReactor" in elem:
            time = s2TimeFinder.findtime(elem, 36.0/gamespeed)
            convertedList.append(["BarracksReactor", time])
            continue
        if "BarracksTechLab" in elem:
            time = s2TimeFinder.findtime(elem, 25.0/gamespeed)
            convertedList.append(["BarracksTechLab", time])
            continue
        if "Bunker" in elem:
            time = s2TimeFinder.findtime(elem, 29.0/gamespeed)
            convertedList.append(["Bunker", time])
            continue
        if "EngineeringBay" in elem:
            time = s2TimeFinder.findtime(elem, 25.0/gamespeed)
            convertedList.append(["EngineeringBay", time])
            continue
        if "FactoryReactor" in elem:
            time = s2TimeFinder.findtime(elem, 36.0/gamespeed)
            convertedList.append(["FactoryReactor", time])
            continue
        if "StarPort" in elem:
            time = s2TimeFinder.findtime(elem, 36.0/gamespeed)
            convertedList.append(["StarPort", time])
            continue
        if "MissileTurret" in elem:
            time = s2TimeFinder.findtime(elem, 18.0/gamespeed)
            convertedList.append(["MissileTurret", time])
            continue
        if "Armory" in elem:
            time = s2TimeFinder.findtime(elem, 46.0/gamespeed)
            convertedList.append(["Armory", time])
            continue
        if "FactoryTechLab" in elem:
            time = s2TimeFinder.findtime(elem, 25.0/gamespeed)
            convertedList.append(["FactoryTechLab", time])
            continue
    return convertedList
