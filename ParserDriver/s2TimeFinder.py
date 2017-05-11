
def findtime(elem,buildTime):
    import datetime
    sep = ':'
    x = "'_gameloop'"
    elem = elem.split('\n')

    for line in elem:
        if x in line:
            matches = line.split(sep)
            loops = float(matches[1][1:len(matches[1])-1])
            time = 0
            if loops > 0:
                time = int(float(loops)/22.4-buildTime)
    return str(datetime.timedelta(seconds=time))
