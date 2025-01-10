

plan=[7500, 2500, 3000, 4200, 1800, 4000, 2500, 1500, 3000]
perc=[20, 50, 0, 100, 0, 0, 100, 100, 0]
cr=[3000, 1000, 0, 4000, 0, 0, 2800, 1400, 0]


vp = 0
va = 0
for i in range(len(plan)):
    va += plan[i] * (perc[i]/100)
    if perc[i] != 0:
        vp += plan[i]
        
CR = sum(cr)

ed = va-vp
ec = va-CR

ipc = va/CR
ipd = va/vp
baa = sum(plan)
cfe = baa / ipc

ipap = (baa - va) / (cfe-CR)


print('va',va)
print('vp',vp)
print('CR',CR)
print('BAA',baa)
print('ED',ed)
print('EC',ec)
print('IPC',ipc)
print('IPD',ipd)
print('CfE',cfe)
print('IPAP',ipap)








