import sys
with open('dbname.txt','a') as out:
    out.write(sys.argv[1] + '\n')
    