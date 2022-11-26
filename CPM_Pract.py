fhand = open("input.txt")
tsk={}

for line in fhand:

    element = line.split(',')
    tsk[element[0]]={}
    tsk[element[0]]['Activity']=element[0]
    tsk[element[0]]['Duration']=int(element[1])
    element[-1]=element[-1].split('\n')[0]
    tsk[element[0]]['Predecessor']=element[2:]
    tsk[element[0]]['ES']=0
    tsk[element[0]]['EF']=0
    tsk[element[0]]['LS']=0
    tsk[element[0]]['LF']=0
    tsk[element[0]]['ST']=0


#............forward pass..............#

for tskFB in tsk:
    if '-' in tsk[tskFB]['Predecessor']:
        tsk[tskFB]['EF']=tsk[tskFB]['Duration']
    for key in tsk:
        for dep in tsk[key]['Predecessor']:
            if '-'!=dep and tsk[key]['ES']<tsk[dep]['EF']:
                tsk[key]['ES']=int(tsk[dep]['EF'])
                tsk[key]['EF']=int(tsk[key]['ES'])+int(tsk[key]['Duration'])


listB=[]
for k in reversed(list(tsk.keys())):
    listB.append(k)

#....................backward pass.....................#

for tskBP in listB:
    if listB.index(tskBP)==0:
        tsk[tskBP]['LF']=int(tsk[tskBP]['EF'])
        tsk[tskBP]['LS']=int(tsk[tskBP]['LF'])-int(tsk[tskBP]['Duration'])
        tsk[tskBP]['ST']=int(tsk[tskBP]['LF'])-int(tsk[tskBP]['EF'])
    for dep in tsk[tskBP]['Predecessor']:
        if dep=='-':
            continue
        if tsk[dep]['LF']==0:
            tsk[dep]['LF']=int(tsk[tskBP]['LS'])
            tsk[dep]['LS']=int(tsk[dep]['LF'])-int(tsk[dep]['Duration'])
        elif int(tsk[dep]['LF'])>int(tsk[tskBP]['LS']):
            tsk[dep]['LF']=int(tsk[tskBP]['LS'])
            tsk[dep]['LS']=int(tsk[dep]['LF'])-int(tsk[dep]['Duration'])
        tsk[dep]['ST']=int(tsk[dep]['LF'])-int(tsk[dep]['EF'])

for item in tsk:
    print(item,tsk[item])
            
path=[]

for item in listB:
    if tsk[item]['ST']==0:
        path.append(item)

path= list(reversed(path))
print(path)