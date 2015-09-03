# GAURAV MOHANTY 
# 201225090

from mininet.net import Mininet
from mininet.node import OVSController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
import sys

X=int(sys.argv[1])
Y=int(sys.argv[2])


def getNet():

	net= Mininet( controller=OVSController , link= TCLink)

	info( '*** Adding controller\n' )

	net.addController('c0')


	even_ip='10.0.0.'
	odd_ip='10.0.1.'
	host_list=[]
	switch_list=[]
	ev=1
	odd=1	
	bandwidth=0
	A=X*Y

	info( '*** Adding hosts\n' )
	
	for x in range(0,A):
		if x%2!=0:
			host_list.append(net.addHost('h'+str(x+1), ip=odd_ip+str(odd)+'/24'))
			odd+=1
		else:
			host_list.append(net.addHost('h'+str(x+1), ip=even_ip+str(ev)+'/24'))
			ev+=1
		print "Added h"+str(x+1)
	info( '*** Adding switch\n' )
	
	for m in range(0,Y):
		switch_list.append(net.addSwitch('s'+str(m+1)))
		print "Added s"+str(m+1)

	info( '*** Creating links\n' )

	for x in range(0,Y):
		for y in range(0,X):
			net.addLink( host_list[X*x+y], switch_list[x],bw=bandwidth+1)
			bandwidth=(bandwidth+1)%2
			print "h"+str(X*x+y+1)+"-------s"+str(x)

	for x in range(0,Y-1):
		net.addLink(switch_list[x],switch_list[x+1],bw=2)
		print "s"+str(x)+"-----s"+str(x+1)

	info( '*** Starting network\n')
	net.start()
	
	info( '*** Running CLI\n' )
	CLI( net )

	info( '*** Stopping network' )
	net.stop()







if __name__ == '__main__':
    setLogLevel( 'info' )
    getNet()
