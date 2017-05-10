def listconverter(list):
    convertedList = []
    for elem in list:
        if "CommandCenter" in elem:
            convertedList.append("CommandCenter")
            continue
        if "SCV" in elem:
            convertedList.append("SCV")
            continue
        if "MULE" in elem:
            convertedList.append("MULE")
            continue
        if "Reaper" in elem:
            convertedList.append("Reaper")
            continue
        if "Marine" in elem:
            convertedList.append("Marine")
            continue
        if "WidowMine" in elem:
            convertedList.append("WidowMine")
            continue
        if "Medivac" in elem:
            convertedList.append("Medivac")
            continue
        if "Marauder" in elem:
            convertedList.append("Marauder")
            continue
        if "HellionTank" in elem:
            convertedList.append("HellionTank")
            continue
        if "SupplyDepot" in elem:
            convertedList.append("SupplyDepot")
            continue
        if "Barracks" in elem:
            convertedList.append("Barracks")
            continue
        if "Refinery" in elem:
            convertedList.append("Refinery")
            continue
        if "BarracksReactor" in elem:
            convertedList.append("BarracksReactor")
            continue
        if "BarracksTechLab" in elem:
            convertedList.append("BarracksTechLab")
            continue
        if "Bunker" in elem:
            convertedList.append("Bunker")
            continue
        if "EngineeringBay" in elem:
            convertedList.append("EngineeringBay")
            continue
        if "FactoryReactor" in elem:
            convertedList.append("FactoryReactor")
            continue
        if "StarPort" in elem:
            convertedList.append("StarPort")
            continue
        if "MissileTurret" in elem:
            convertedList.append("MissileTurret")
            continue
        if "Armory" in elem:
            convertedList.append("Armory")
            continue
        if "FactoryTechLab" in elem:
            convertedList.append("FactoryTechLab")
            continue
    return convertedList
