import math

def subnetcal():

    while 1:
        ip = raw_input("Enter network id: ")
        sp = ip.split('.')
        #print sp

        #CHECK IP CLASS WHETHER A,B,C
        #remove loopback address(127)
        #The 169.254.x.x range of IP addresses is reserved by Microsoft for private network addressing.
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
typeof = raw_input("Select Type of subnetting\n 1.FLSM\n 2.VLSM\n select number for type\n")
if int(typeof) == 1:
    flsmipnum = raw_input("Number of ips for one network: ")
    flsmipnum = int(flsmipnum)
    numb = math.log(flsmipnum, 2)
    numb = int(numb)
    numberofhosts = numb+1
    numberofnets = 32-numberofhosts
    netportions = numberofnets//8
    hostportions = 4-netportions
    convertedhost = numberofhosts

    print netportions
    print hostportions

    

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





