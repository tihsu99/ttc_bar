#==============
# Last used: python crab_submission_preparation.py on/off
#==============
import sys
import os

def join_l(l, sep):
    li = iter(l)
    string = "/"+str(next(li))
    for i in li:
        string += str(sep) + str(i)
    return string

def perform_operation(action="on"):
    # Replace this with the operation you want to perform
    if action=="on":
        print("moving .git folder to before CMSSW dir...")
        l = os.environ["CMSSW_BASE"].split("/")[1:-1]
        location = join_l(l, "/")
        print ("\033[1;33mmv ../.git "+location+"/\033[0;m")
        if not os.path.isdir("../.git"):
            print ("Already moved to "+location+"/"+"  -> go ahead with crab submission")
        else:
            os.system("mv ../.git "+location+"/") 
    elif action=="off":
        print ("moving .git folder back to analysis dir")
        l = os.environ["CMSSW_BASE"].split("/")[1:-1]
        location = join_l(l, "/")
        print ("\033[1;33mmv "+location+"/.git "+"../\033[0;m")
        if not os.path.isdir(location+"/.git"):
           print ("Already moved to Analysis dir")
        else:
            os.system("mv "+location+"/.git "+"../")
 
# Main function
if len(sys.argv) == 2 and sys.argv[1] == "on":
    perform_operation("on")
elif len(sys.argv) == 2 and sys.argv[1] == "off":
    perform_operation("off")
else:
    print("Usage: python crab_submission_preparation.py on/off")
