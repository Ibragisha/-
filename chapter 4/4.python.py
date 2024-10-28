def get_resistor_value(mac):
    if len(mac)<=3:  return [None,None]
    cok=["bk","br","rd",'or','yl','gr','bl','vi','gy','wh','au','ag',' ']
    znah=[0,1,2,3,4,5,6,7,8,9,0,0]
    mnog=[1,10,100,10**4,10**5,10**6,10**7,10**8,10**9,0,0,0]
    otkl=[0,1,2,0,5,0.5,0.25,0.1,0.05,0,5,10]
    if mac[0] not in cok or mac[1] not in cok or mac[2] not in cok or mac[3] not in cok :
        return [None,None]
    a=znah[cok.index(mac[0])]
    b=znah[cok.index(mac[1])]
    c=mnog[cok.index(mac[2])]
    d=otkl[cok.index(mac[3])]
    return [int(str(a)+str(b))*c,d]

# In
print(get_resistor_value(['br', 'bk', 'yl', 'ag']))
print(get_resistor_value(['yl', 'vi', 'rd', 'au']))
print(get_resistor_value(['vi', 'yl', 'rd', 'gr']))
print(get_resistor_value(['ws', 'yl', 'rd', 'rd']))
print(get_resistor_value(['vi', 'yl', 'rd']))