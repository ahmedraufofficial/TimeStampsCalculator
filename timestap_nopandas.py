from datetime import datetime 
from datetime import timedelta
from random import randint
from random import sample

start = datetime.now()
end = start + timedelta(days = 60)
result = []

while start < end:
    result.append(start.strftime('%Y-%m-%d %H:%M:%S'))
    high_rand = randint(24, 72)
    low_rand = randint(5, 18)
    value = randint(low_rand, high_rand)
    step = timedelta(hours=value)
    start += step

res = sample(result,len(result))


resdt = []
for i in res:
    new = datetime.strptime(i ,'%Y-%m-%d %H:%M:%S')
    start_date = new.date()
    resdt.append(start_date)

resdt.sort()
mylist = list(dict.fromkeys(resdt))


result = []
consec = 1


for i in range(len(mylist)):
    start_date = mylist[i]
    next_date = mylist[i] + timedelta(days=1)
    try:
        if next_date == mylist[i+1]:
            consec += 1
        else:
            end_date = start_date - timedelta(days=consec-1)
            result.append((str(end_date),str(start_date),consec))
            consec = 1
    except IndexError:
        end_date = start_date - timedelta(days=consec-1)
        result.append((str(end_date),str(start_date), consec))
        consec = 1

r = sorted(result, key=lambda x: x[2],reverse=True)

print ("START         END        LENGTH")
for ele1,ele2,ele3 in r:
    print ("{:<14}{:<11}{}".format(ele1,ele2,ele3))


