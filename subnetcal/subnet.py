import math
ip = 0
def subnetcal():

    while 1:
        global ip 
        ip = raw_input("Enter network id: ")
        sp = ip.split('.')

        if (len(sp)==4):
            if( 1 <=int(sp[0]) <= 223):
                if(int(sp[0]) != 127):
                    if(int(sp[0]) != 169 or int(sp[1]) !=254):

                        if(0<=int(sp[1])<=255 and 0<=int(sp[2])<=255 and 0<=int(sp[3])<=255 ):
                            break

                        else:
                            print 'Not a valid ip address\n'
                            continue
                            
                    else:
                        print '169.254.x.x range is reserved by Microsoft for private network addressing\n'
                        continue
                else:
                    print '127.x.x.x are reserved for the loopback\n'
                    continue
            else:
                print 'ip address should not be a multicast or class E\n'
                continue

        else:
            print "Your ip address is not valid,it should ipv4 address\n"
            continue

subnetcal()

def subnetmaskcal(flsmipnum):
    numb = math.log(flsmipnum, 2)
    numb = int(numb)
    numberofhosts = numb+1
    bloks = abs(256/2**numberofhosts)
    numberofnets = 32-numberofhosts
    netportions = numberofnets//8
    hostportions = 4-netportions
    value=0
    
    if (numberofhosts<=8):

        ran = 8-numberofhosts
        for x in range(1,ran+1):
            value = value+ 2**(8-x)

    elif (numberofhosts<=16):
        ran = 16-numberofhosts
        for x in range(1,ran+1):
            value = value+ 2**(8-x)
        value = str(value) + '.0'

    elif(numberofhosts<=24):
        ran = 24-numberofhosts
        for x in range(1,ran+1):
            value = value+ 2**(8-x)

        value = str(value) + '.0.0'

    subnet = '255.'*netportions + str(value)
    subn = subnet.split('.')
    return (subn,bloks)


def getwildcard(data):
    newlist = []
    for n in data:
        binaryval = bin(int(n)).split('b')[1]
        
        if (len(binaryval) == 8):
            newlist.append(binaryval)
        elif(len(binaryval)<8):
            newval = binaryval.zfill(8)
            newlist.append(newval)
    fina = "".join(newlist)

    zeros = fina.count('0')
    ones = 32 - zeros
    valid_ips = abs(2**zeros -2)

    wildcard = []
    for x in data:
        wildval = 255 - int(x)
        wildcard.append(str(wildval))

    wildcard_final = ".".join(wildcard)
    
    return (zeros,ones,valid_ips)


def networkandbradcast(ipaddress,zerosinip,onesinip,validips):
    address = ipaddress.split('.')
    ipaddresslist = []
    for n in address:
        binaryval = bin(int(n)).split('b')[1]
        
        if (len(binaryval) == 8):
            ipaddresslist.append(binaryval)
        elif(len(binaryval)<8):
            newval = binaryval.zfill(8)
            ipaddresslist.append(newval)

    ipadbinary = "".join(ipaddresslist)

    network_ip = ipadbinary[:(onesinip)] + '0'*zerosinip
    braodcast_ip = ipadbinary[:(onesinip)] + '1'*zerosinip
    
    networkip = []
    for q in range(0,len(network_ip),8):
        netip = network_ip[q:q+8]
        networkip.append(netip)
    
    networkipdecimal = []
    for l in networkip:
        networkipdecimal.append(str(int(l,2)))

    finalNetworkIp = ".".join(networkipdecimal)

    broadcast = []
    for q in range(0,len(braodcast_ip),8):
        bdip = braodcast_ip[q:q+8]
        broadcast.append(bdip)
    
    bdipdecimal = []
    for l in broadcast:
        bdipdecimal.append(str(int(l,2)))

    finalBroadcastIp = ".".join(bdipdecimal)
    
    return(finalNetworkIp,finalBroadcastIp)


typeof = raw_input("Select Type of subnetting\n 1.FLSM\n 2.VLSM\n select number for type\n")

if int(typeof) == 1:
    flsmipnum = raw_input("Number of ips for one network: ")
    flsmipnum = int(flsmipnum)
    subnetMask = subnetmaskcal(flsmipnum)
    numberofblocks = subnetMask[1]
    submask = subnetMask[0]
    wildcardmask = getwildcard(submask)
    z = wildcardmask[0]
    o = wildcardmask[1]
    vip = wildcardmask[2]
    nandbroad = networkandbradcast(ip,z,o,vip)
    netIp = nandbroad[0]
    boadIp = nandbroad[1]

    print 'Network Address: '+ str(netIp)
    print 'BroadCast Address: '+ str(boadIp)



if int(typeof)==2:
    networks = raw_input("Number of  network: ")
    ll = int(networks)
    iplist = []
    ln=1
    while ll>0:
        ipsforeach= raw_input("Number of ips for  network " + str(ln) + ": ")
        iplist.append(ipsforeach)
        ll-=1
        ln+=1

    for x in iplist:
        x= int(x)
        resu = subnetmaskcal(x)
        print resu






