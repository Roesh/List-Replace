import sys

print("FYI: make sure src and rep lists are mutually exclusive, otherwise you could modify a value twice. Use my chkList.py script or a diff tool")

src = [] # Place you comma delimited source and replace lists here
rep = []
try:
    with open("List1.txt",'r') as f:
        content = f.readlines()
    # Remove whitespace characters like `\n` at the end of each line
    src = [x.strip() for x in content]
    print("Found List1.txt for source list")
except:
    pass
try:
    with open("List2.txt",'r') as f:
        content = f.readlines()
    # Remove whitespace characters like `\n` at the end of each line
    rep = [x.strip() for x in content]
    print("Found List2.txt for replace list")
except:
    pass

# Replace function
def replace(fname,src,rep,noPrompt=0):
    try:
      inputf = open(fname,'r')
    except:
      print("Could not open input file."+fname)
      quit()

    def inputList(listName):
      tmp = input("Input " + listName + ". <Enter> to use Found/stored list: ")
      tmp = tmp.strip()
      if(len(tmp) == 0):
        return None
      tmplist = []
      while(len(tmp)!=0):
        tmplist.append(tmp)
        tmp = input("Next value? ")
        tmp = tmp.strip()
      return tmplist

    tmplist = None
    if noPrompt is 0:
        tmplist = inputList("source list")
    if tmplist is not None:
      src = tmplist
    print("Source")
    print(src)

    if noPrompt is 0:
        tmplist = inputList("replacement list")
    if tmplist is not None:
      rep = tmplist
    print("Source")
    print(rep)

    s = inputf.read() #String of text to be modified

    repLen = len(rep)
    # quit if list lengths don't match
    if(repLen != len(src)):
      print("Source and replacement lists' length must match, exiting...")
      quit()

    i = 0 #index
    for x in src:
      y = rep[i]
      s = s.replace(str(x),str(y))
      i=i+1
    print(s)

    try:
      outputf = open("mod_"+fname,'w')
    except:
      print("Could not open output file.")
      quit()

    outputf.write(s)

if len(sys.argv) > 1:
    for fname in sys.argv[1:]:
        replace(fname,src,rep,1)
else:
    #Get input file name if file path arguments weren't passed in
    fname = input("Input file path? ")
    replace(fname,src,rep)
