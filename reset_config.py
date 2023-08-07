from time import sleep
def reset():
    f = open("data/default_config.txt", "r")
    config = f.read()
    f.close()

    f = open("config.txt", "w")
    f.write(config)
    f.close()
    
    end("config reset")

def end(msg):
    print("\n"+msg)
    sleep(1)

yes = "r"
tmp = input("Enter {} to reset config. Enter anything else to cancel.".format(yes))

if tmp==yes:
    reset()
else:
    end("cancelled")