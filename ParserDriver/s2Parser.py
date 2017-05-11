
def s2parser(replay):
    import subprocess
    replaypath = "../Replays/"+replay
    out = subprocess.Popen(["python.exe", "../s2protocol/s2protocol.py", replaypath,
                            "--trackerevents"], stdout=subprocess.PIPE)
    output_list = out.stdout.readlines()
    # for i in output_list:
    #     if i != '\n':
    #         print i,
    concat_list = ''.join(output_list).split("{")
    bornList = []
    buildList = []
    for str in concat_list:
        if "SUnitBornEvent" in str:
            bornList.append(str)
    for str in concat_list:
        if "SUnitInitEvent" in str:
            buildList.append(str)
    return [bornList, buildList]