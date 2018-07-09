# Tournament-App
1. set up vm, Using the terminal, change directory to fullstack/vagrant (cd fullstack/vagrant), then type vagrant up to launch your virtual machine. 

2. Once it is up and running, type vagrant ssh to log into it. 3.type psql in prompt to access psql program  

[in psql cmd prompt]: 

3. create data base by typing "CREATE DATABASE tournament;" 

4. connect with "\c tournament;"  

5. then create tables with \i tournament.sql if that does not work copy and past the text from inside tournament.sql into your psql prompt. or use (run psql -f tournament.sql) if the above option do not work for you.  

[in file system] 

6.finaly run tournament_test.py
