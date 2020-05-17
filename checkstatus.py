import os
if(os.system("$(curl -o /dev/null  -s  -w  \"%{http_code}\" 192.168.43.238:2222/*.html)") == "200"):
    pass
elif(os.system("$(curl -o  /dev/null -s -w \"%{http_code}" 192.168.43.238:1111/*.py)") == "200"):
    pass
else:
    with open("/status","w") as a:
        a.write("Not valid code")
               
