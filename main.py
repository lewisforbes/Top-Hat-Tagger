tab = ""

while(True):
    prefix = input("Enter prefix (for example F1S, F etc.): ").upper()

    if not "F" in prefix:
        print("invalid format")
        continue

    if "S" in prefix:
        tab="{Tab}"
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
    if fst_f<1:
        print("invalid format")
        continue
    f_offset = fst_f-1
    break





while(True):
    f_n = input("How many {}folders to tag? ".format(sub))
    if f_n.isdigit():
        f_n = int(f_n)
        break
    print("invalid format")

f_qs = []
for f_i in range(1, f_n+1):
    while(True):
        f_q = input("How many questions in {}{} to tag? ".format(prefix, f_i+f_offset))
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
    main += loop.replace("*q count*", str(q_count)).replace("*(sub)folder*", str(i+1+f_offset)).replace("*extra tab*", tab).replace("*prefix*", prefix).replace("*q offset*", q_offset) + "\n"
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