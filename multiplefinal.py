import os
for root, dirs ,files in os.walk('/root/tk2'):
    print(files)
    for file in files:
        if file.endswith('.py'):
             os.ststem("docker container run -dit  -p 2222:80 --name  myhtmlcode -v
                        /root/tk2:/var/www/html vimal13/apache-webserver-php")
        elif file.endswith('.html'):
             os.ststem("docker container run -dit  -p 1111:80 --name  mypythoncode mypython:v1")
        

        
