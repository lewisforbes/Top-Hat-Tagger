def mk_folder_output(conf, base_template):
    # construct output
    folder = ""
    for i, q_count in enumerate([int(x) for x in conf["questions"].split(" ")]):
        base_loop = base_template
        if q_count==0:
            continue
        
        if i%2==0: # pink 
            conf["pink_tab"] = "{Tab}"
        else: # grey
            conf["pink_tab"] = ""
        
        conf["q_count"] = q_count
        for var, val in conf.items():
            base_loop = base_loop.replace("*{}*".format(var), str(val))
        assert not "*" in base_loop # if false some var is missed
        folder += base_loop + "\n"
        conf["q_offset"] = int(conf["q_offset"])+q_count

    return folder

def main():
    # read config
    f = open("config.txt", "r")
    conf = {}
    for line in f:
        if line.strip()=="":
            continue
        splt = line.split(":=")
        conf[splt[0].strip()] = splt[1].strip()
    f.close()

    conf["tabs"] = "{Tab}"*int(conf["tabs"])
    conf["folder"] = conf["prefix"]+str(conf["number"])

    # get base loop
    f = open("base_loop.txt", "r")
    base_loop = f.read()
    f.close()

    output = ""
    for qs in conf["all_questions"].split("//"):
        conf["questions"] = qs
        output += "\n" + mk_folder_output(conf, base_loop)
        output += "\nSend, {Down}\nSleep, 200\nSend, {Enter}\nSleep, 1000\n" # move to next folder
        conf["q_offset"] = 0 # start from 0 after first iter
        conf["number"] = int(conf["number"])+1
        conf["folder"] = conf["prefix"]+str(conf["number"])


    # write output
    f = open("tagger.ahk", "w")
    f.write("Sleep, 1000\n\n" + output + "\n\nExitApp\nEsc::ExitApp")
    f.close()
        
try:
    main()
    print("finished.")
except:
    input("failed")