from re import findall

class Tagger_Gen:
    def __init__(self):
        self.config     = "config.txt"
        data_dir        = "data/"
        self.base_loop  = data_dir+"base_loop.txt"
        self.warnings   = data_dir+"warnings.txt"
        self.welcome    = data_dir+"welcome.txt"
        self.tagger     = "tagger.ahk" # output

        self.save_time  = 6000
        self.new_q_time = 1000

        self.tabs_override = None
        self.tabs = 5
        self.sub = None

        self.print_welcome()

        self.read_config()
        self.prefix     = self.get_prefix()
        self.fst_f      = self.get_fst_f()
        self.q_offset   = self.get_q_offset()
        self.f_n        = self.get_f_n()
        self.f_qs       = self.get_f_qs()

        self.replacements   = None
        self.write_tagger(self.mk_tagger())

        input("Complete, press enter to exit.")

    def print_welcome(self):
        f = open(self.welcome, "r")
        longest = 0
        msg=""
        for line in f:
            msg+=line
            if len(line)>longest:
                longest=len(line)
        
        bar = "-"*longest
        print(bar, msg, bar, sep="\n", end="\n\n")
        f.close()

    def read_config(self):        
        default = "default"
        comment = "#"
        equals = ":="

        f = open(self.config, "r")
        for line in f:
            if (comment in line) or (not (equals in line)):
                continue

            line_value = line.split(equals)[1].strip()
            if line_value!=default and not line_value.isdigit():
                input("Invalid value in {}: {}.\nConsider resetting config.\nPress enter to exit.".format(self.config, line_value))
                raise Exception()
                
            if "tabs" in line:
                if line_value==default:
                    self.tabs_override = False
                else:
                    self.tabs_override = True
                    self.tabs = int(line_value)
                    print("Using tabs provided in {}".format(self.config))

            if ("save_time" in line) and (line_value!=default):
                self.save_time = int(line_value)
            if ("new_q_time" in line) and (line_value!=default):
                self.new_q_time = int(line_value)
        f.close()

    def get_prefix(self):
        def folder_is_zero(prefix):
            try:
                if int(prefix[1:-1])==0:
                    return True
            except:
                return False
            
        def is_FnS(prefix):
            return len(findall("F[0-9]S", prefix))==1 # n can't be 0
            
        print("Prefixes are the same for every question.\nExamples are F or F1S.")
        while(True):
            prefix = input("Enter the prefix: ").upper()

            if prefix=="F":
                self.sub = ""
                return prefix
            
            if not is_FnS(prefix):
                print("Invalid format.")
                continue

            if folder_is_zero(prefix):
                print("Invalid format: folder cannot be 0 if there are subfolders.")
                continue

            # prefix is valid FnS          
            if not self.tabs_override:
                self.tabs+=1
            
            self.sub = ""
            return prefix

    def get_q_offset(self):
        while(True):
            fst_q = input("Enter number of first question: ")
            if not fst_q.isdigit():
                print("invalid format")
                continue
            fst_q = int(fst_q)
            if fst_q<1:
                print("invalid format")
                continue
            
            return fst_q-1
    
    def get_fst_f(self):
        while(True):
            fst_f = input("Enter number of first {}folder: ".format(self.sub))
            if not fst_f.isdigit():
                print("invalid format")
                continue
            fst_f = int(fst_f)
            if fst_f<0:
                print("invalid format")
                continue
            if fst_f==0:
                if "S" in self.prefix:
                    input("\nError: first folder is 0 and there are subfolders.\nPress enter to exit.")
                    raise Exception()
                if not self.tabs_override:
                    self.tabs=4
            return fst_f

    def get_f_n(self):
        while(True):
            if self.fst_f==0:
                print("Tagging F0 only.")
                return 1

            f_n = input("How many {}folders to tag? ".format(self.sub))
            if f_n.isdigit():
                return int(f_n)
            print("invalid format")

    def get_f_qs(self):
        f_qs = []
        for f_i in range(0, self.f_n):
            while(True):
                f_q = input("How many questions in {}{} to tag? ".format(self.prefix, f_i+self.fst_f))
                if f_q.isdigit():
                    f_q = int(f_q)
                    break
                print("invalid format")
            f_qs.append(f_q)
        return f_qs

    def get_replacements(self, i, q_count):
        if self.replacements==None:
            self.replacements = {"*tabs*"        : "{Tab}"*self.tabs,
                                 "*prefix*"      : self.prefix,
                                 "*q offset*"    : self.q_offset,
                                 "*save time*"   : self.save_time,
                                 "*new q time*"  : self.new_q_time}

        self.replacements["*q count*"]      = q_count
        self.replacements["*(sub)folder*"] = i+self.fst_f
        return self.replacements

    def mk_tagger(self):
        f = open(self.base_loop, "r")
        loop = f.read()
        f.close()

        script = ""
        for i, q_count in enumerate(self.f_qs):
            current = loop
            for old,new in self.get_replacements(i, q_count).items():
                current = current.replace(old, str(new))
            script += current + "\n"
            if i==0:
                self.q_offset=0

        f = open(self.warnings, "r")
        warnings = f.read()
        f.close()

        print("\n" + warnings.replace("; ", ""))
        print("\nUSE AT YOUR OWN RISK! PRESS [ESC] TO TERMINATE MACRO!")

        return warnings + "\nSleep, 3000\n" + script + "\n\nExitApp\nEsc::ExitApp"

    def write_tagger(self, script):
        f = open(self.tagger, "w")
        f.write(script)
        f.close()

Tagger_Gen()