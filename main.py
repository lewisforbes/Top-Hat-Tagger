tabs = 5


def folder_is_zero(prefix):
    try:
        if int(prefix[1:-1])==0:
            return True
    except:
        return False
    
def manual_tab_count(tabs_original):
    cancel = "q"
    print("Overwriting tabs, enter {} to cancel.".format(cancel))
    while(True):
        tabs = input("Enter number of tabs: ")
        if tabs==cancel:
            return tabs_original
        
        if not tabs.isdigit():
            print("invalid format")
            continue
        tabs = int(tabs)
        if tabs<0:
            print("invalid format")
            continue
        return tabs




while(True):
    prefix = input("Enter prefix (for example F1S, F etc.): ").upper()

    if not "F" in prefix:
        print("invalid format")
        continue

    if "S" in prefix:
        if folder_is_zero(prefix):
            print("invalid format")
            continue
        tabs=6
    break

sub = ""
if "S" in prefix:
    sub="sub"

q_offset=0
while(True):
    fst_q = input("Enter number of first question: ")
    if not fst_q.isdigit():
        print("invalid format")
        continue
    fst_q = int(fst_q)
    if fst_q<1:
        print("invalid format")
        continue
    q_offset = str(fst_q-1)
    break

f_offset = 0
while(True):
    fst_f = input("Enter number of first {}folder: ".format(sub))
    if not fst_f.isdigit():
        print("invalid format")
        continue
    fst_f = int(fst_f)
    if fst_f<0:
        print("invalid format")
        continue
    if fst_f==0:
        if "S" in prefix:
            input("\nError: first folder is 0 and there are subfolders.\nPress enter to exit.")
            raise Exception()
        tabs=4
    f_offset = fst_f-1
    break


while(True):
    if fst_f==0:
        print("Tagging F0 only.")
        f_n=1
        break

    f_n = input("How many {}folders to tag? ".format(sub))
    if f_n.isdigit():
        f_n = int(f_n)
        break
    print("invalid format")

f_qs = []
for f_i in range(1, f_n+1):
    while(True):
        f_q = input("How many questions in {}{} to tag? ".format(prefix, f_i+f_offset))
        if f_q=="tabstabs":
            tabs = manual_tab_count(tabs_original=tabs)
            continue 
        if f_q.isdigit():
            f_q = int(f_q)
            break
        print("invalid format")
    f_qs.append(f_q)


f = open("base_loop.txt", "r")
loop = f.read()
f.close()

main = ""
for i, q_count in enumerate(f_qs):
    main += loop.replace("*q count*", str(q_count)).replace("*(sub)folder*", str(i+1+f_offset)).replace("*tabs*", "{Tab}"*tabs).replace("*prefix*", prefix).replace("*q offset*", q_offset) + "\n"
    if i==0:
        q_offset="0"

f = open("warnings.txt", "r")
warnings = f.read()
f.close()

output = warnings + "\nSleep, 3000\n" + main
f = open("tagger.ahk", "w")
f.write(output + "\n\nExitApp\n\nEsc::ExitApp")
f.close()

print("\n" + warnings.replace("; ", ""))
input("\nUSE AT YOUR OWN RISK! PRESS [ESC] TO TERMINATE MACRO!" + "\n\n[press enter to exit]")