import asyncio

'''
UPStracking1 = '1ZV349V10491445786'
UPStracking2 = '1ZV349V10493147596'
UPStracking3 = '1ZV349V10494130002'
UPStracking4 = '1ZV349V10496072072'
UPStracking5 = '1ZV349V10498271102'
UPStracking6 = '1ZV349V10496991089'
UPStracking7 = '1ZV349V10499524097'
UPStracking8 = '1ZV349V10492949016'
UPStracking9 = '1ZV349V10123456789'
UPStracking10 = '1ZV349V10123456789'
'''

USPStracking1 = '4209453692612927005139000003195321' #20101612125137
USPStracking2 = '4201206592612927005139000003185346' #20101606583621
USPStracking3 = '4206060192612927005139000003190326' #20101608280546
USPStracking4 = '4207738692612927005139000003215449' #20101703023368
'''
USPStracking5 = '1ZV349V10498271102'
USPStracking6 = '1ZV349V10496991089'
USPStracking7 = '1ZV349V10499524097'
USPStracking8 = '1ZV349V10492949016'
'''

NorthAmericanUPS1 = 'https://www.ups.com/track?loc=en_US&tracknum='
NorthAmericanUPS2 = '&requester=WT/trackdetails'

AustraliaUPS1 = 'https://www.ups.com/track?loc=en_AU&tracknum='
AustraliaUPS2 = '&requester=WT/trackdetails'

USPS1 = 'https://tools.usps.com/go/TrackConfirmAction?tRef=fullpage&tLc=2&text28777=&tLabels='
USPS2 = '%2C&tABt=false'

SF = 'https://www.sf-express.com/cn/sc/dynamic_function/waybill/#search/bill-number/' 

SFtracking = 'SF1041533871234'


#print(NorthAmericanUPS1+UPStracking1+NorthAmericanUPS2)

async def main():

    '''
    await asyncio.sleep(1)
    print(NorthAmericanUPS1+UPStracking2+NorthAmericanUPS2)
        
    await asyncio.sleep(1)    
    print(NorthAmericanUPS1+UPStracking3+NorthAmericanUPS2)

    await asyncio.sleep(2)
    print(NorthAmericanUPS1+UPStracking4+NorthAmericanUPS2)

    await asyncio.sleep(2)
    print(NorthAmericanUPS1+UPStracking5+NorthAmericanUPS2)

    await asyncio.sleep(3)
    print(NorthAmericanUPS1+UPStracking6+NorthAmericanUPS2)

    await asyncio.sleep(3)
    print(NorthAmericanUPS1+UPStracking7+NorthAmericanUPS2)

    await asyncio.sleep(4)
    print(NorthAmericanUPS1+UPStracking8+NorthAmericanUPS2)

print(NorthAmericanUPS1+UPStracking9+NorthAmericanUPS2)
print(NorthAmericanUPS1+UPStracking10+NorthAmericanUPS2)
print(SF+SFtracking)
    '''

    await asyncio.sleep(1)
    print(USPS1+USPStracking1+USPS2) #20101612125137
        
    await asyncio.sleep(1)    
    print(USPS1+USPStracking2+USPS2) #20101606583621

    await asyncio.sleep(2)
    print(USPS1+USPStracking3+USPS2) #20101608280546

    await asyncio.sleep(2)
    print(USPS1+USPStracking4+USPS2) #20101703023368
'''
    await asyncio.sleep(3)
    print(USPS1+USPStracking5+USPS2)

    await asyncio.sleep(3)
    print(USPS1+USPStracking6+USPS2)

    await asyncio.sleep(4)
    print(USPS1+USPStracking7+USPS2)
'''

asyncio.run(main())
