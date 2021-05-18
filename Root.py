import os,sys
import math
from matplotlib.pyplot import *
from sage.plot.line import Line
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

def pgcd(a,b) :  
   while a%b != 0 : 
      a, b = b, a%b 
   return (b)



#########for graphic frmat
plt.rcParams['savefig.facecolor'] = "0.8"
#plt.xlim(40, 160)
#plt.ylim(0, 0.03)
#plt.grid(True)
#plt.show()

def example_plot(ax, fontsize=12):
    ax.plot([1, 2])

    ax.locator_params(nbins=3)
    
                                    ######################## draw christoffels #########################
                                    
                     ###NW####               
    
def drawchrfromnw(a,b,c,d):     #plot christoffel word de (b,a)----> (d,c)
	n=c-a+d-b
	dd=pgcd(c-a,n)
	l=1
	for i in range (n):
		if ((c-a)*i-n+dd)%n==0:
			l= i
			break
	r_1=[0 for k in range (n)]
	if dd==1:
		s = [ (i+1)*l%n for i in range((c-a)/dd)]
		r_1 = [ 1 if k in s else 0 for k in range(n) ]
	else:
		j=1
		s=[(i+1)*l%n for i in range((c-a)/dd)]
		kk=len(s)
		while j<=dd:
			for i in range(kk):
				s.append(s[i]+j*(n/dd))
			j+=1
		r_1 = [ 1 if k in s else 0 for k in range(n) ]
		
	dep=(b,a)
	pt=[dep]                                  #pour afficher les points
	kll=line([dep,(d,c)],rgbcolor=hue(0.6))   # le segment de (b,a) to (d,c) de pente c-a/d-b
	coll=[]
	for i in range (n):
		if r_1[i]==0:
			h=(dep[0]+1,dep[1])
			coll.append(line([dep,h],rgbcolor=hue(1.0)))  #etape horizontale
			pt.append(h)
			dep=h
		if r_1[i]==1:
			v=(dep[0],dep[1]+1)
			coll.append(line([dep,v],rgbcolor=hue(1.0)))  #etape verticale
			pt.append(v)
			dep=v
	for i in range(len(coll)):
		kll+=coll[i]
	mn=[]
	mn.append(r_1) #Chr word
	mn.append(kll)  #graph
	mn.append(pt)  #points
	return (mn)
	
	
def graphchnw(l,x,y):   #l=une liste des pentes [a,b,c,d,e,f]  a/b,c/d, e/f pour dessiner  
	r=len(l)
	p=[]
	pt=[]
	s=[l[0]]
	m=[l[1]]
	i=0
	h=l[0]
	hh=l[1]
	while i < r-2:    
		h+=l[i+2]
		hh+=l[i+3]
		s.append(h)
		m.append(hh)
		i+=2
	d0=-h+y
	d1=x
	d2=d0+l[0]
	d3=-hh+l[1]
	i=0
	pt.append(drawchrfromnw(d0,-d1,d0+l[0],-d1+l[1])[2])   #points on ch
	p.append(drawchrfromnw(d0,-d1,d0+l[0],-d1+l[1])[1])    #the path of ch
	j=0
	f=1
	k=[l[0]]
	t=[l[1]]
	while j < r-2:    # pour obtenir les points sur chaque chr
		k.append(l[j+2])
		j+=2
	while f < r-2:
		t.append(l[f+2])
		f+=2	
	
	while i < r-2:   
		d0=d2
		d1=d3
		d2+=l[i+2]
		d3+=l[i+3]
		p.append(drawchrfromnw(d0,d1,d2,d3)[1])
		pt.append(drawchrfromnw(d0,d1,d2,d3)[2])
		i+=2
	
	
	#############################################################################
	G=sum(p[i]+points(pt[i]) for i in range (len(p))) #+text(str(k[i])+"/"+str(t[i]),(-hh+m[i]-1,s[i]))
	
	return (G) 
	
	
	############# NE  #########
def drawchrfromne(a,b,c,d):     #plot christoffel word de (b,a)----> (d,c)
	lol=abs(c-a)
	loll=abs(d-b)
	n=lol+loll
	dd=pgcd(c-a,n) 
	l=1
	for i in range (n):
		if (lol*i-n+dd)%n==0:
			l= i
			break
	if loll==0:
		r_1=[3 for k in range (dd)]
	else:	
		r_1=[3]
		kk1=1
		if dd==1:
			s = [ (i+1)*l%n  for i in range(lol/dd)]
			if s==[]:
				r_1=[0]	
			else:
				s=sorted(s)
				if s[0]==1:
					r_1=[0 for k in range (n)]
					if dd==1:
						s = [ (i+1)*l%n for i in range(lol/dd)]
						r_1 = [ 3 if k in s else 0 for k in range(n) ]
					else:
						j=1
						s=[(i+1)*l%n for i in range(lol/dd)]
						kk=len(s)
						while j<=dd:
							for i in range(kk):
								s.append(s[i]+j*(n/dd))
							j+=1
						r_1 = [ 3 if k in s else 0 for k in range(n) ]
					r_1=r_1[::-1]
			
				else:
					r_1 = [ 3 if k in s else 0 for k in range(n) ]
					r_1.reverse()
		else:
			j=1
			s=[(i+1)*l%n  for i in range(lol/dd)]
			#print s
			if s==[]:
				r_1=[0]	
				for i in range (dd):
					r_1.append(0)
			else:
				s=sorted(s)
		
				kk=len(s)
				while j<=dd:
					for i in range(kk):
						s.append(s[i]+j*(n/dd))
					j+=1
				
				for i in range( s[0]):
					r_1.append(0)
				for j in range (len(s[1:])):
					r_1.append(3)
					for i in range(s[j+1]-s[j]):
						r_1.append(0)
	dep=(b,a)
	pt=[dep]                                  #pour afficher les points
	kll=line([dep,(d,c)],rgbcolor=hue(0.6))   # le segment de (b,a) to (d,c) de pente c-a/d-b
	coll=[]
	for i in range (n):
		if r_1[i]==0:
			h=(dep[0]+1,dep[1])
			coll.append(line([dep,h],rgbcolor=hue(1.0)))  #etape horizontale
			pt.append(h)
			dep=h
		if r_1[i]==3:
			v=(dep[0],dep[1]-1)
			coll.append(line([dep,v],rgbcolor=hue(1.0)))  #etape verticale
			pt.append(v)
			dep=v
	for i in range(len(coll)):
		kll+=coll[i]
	mn=[]
	mn.append(r_1) #Chr word
	mn.append(kll)  #graph
	mn.append(pt)  #points
	return (mn)
	
	
def graphchne(l,v):   #l=une liste des pentes [a,b,c,d,e,f]  a/b,c/d, e/f pour dessiner v=sum yi de NW
	r=len(l)
	p=[]
	pt=[]
	if r==1:
		pt.append(drawchrfromne(v,0,v,l[0])[2])   #points on ch
		p.append(drawchrfromne(v,0,v,l[0])[1])    #the path of ch	



	elif r>1:
		s=[l[0]]
		m=[l[1]]
		i=0
		h=l[0]
		hh=l[1]
		while i < r-2:    
			h+=l[i+2]
			s.append(h)
			i+=2
		th=0
		while th< r-3:
			hh+=l[th+3]	
			m.append(hh)
			th+=2
		m.append(hh)	
			
			
		j=1
		f=2
		sy=[l[1]]
		sx=[l[2]]
		while j < r-2:    # pour obtenir les points sur chaque chr
			sy.append(l[j+2])
			j+=2
		while f < r-2:
			sx.append(l[f+2])
			f+=2	
		d0=0             
		d1=0
		d2=v
		d3=l[0]
		tol=len(sx)
		i=0
		pt.append(drawchrfromne(v,d0,v,d3)[2])   #points on ch
		p.append(drawchrfromne(v,d0,v,d3)[1])    #the path of ch
	
		while i < tol:   #-1
			d0=d2
			d1=d3
			d2-=sy[i]
			d3+=sx[i]
			p.append(drawchrfromne(d0,d1,d2,d3)[1])
			pt.append(drawchrfromne(d0,d1,d2,d3)[2])
			i+=1
	ptss=[]
	for i in range (len(pt)):
		for j in range (len(pt[i])):
			ptss.append(pt[i][j])
	ptss1=tuple(ptss)
		
	G=sum(p[i]+points(pt[i]) for i in range (len(p))) 
	return (G)    

	################################ ES  #####################"
def drawchrfromse(a,b,c,d):     #plot christoffel word de (b,a)----> (d,c)
	lol=abs(c-a)
	loll=abs(d-b)
	n=lol+loll
	dd=pgcd(c-a,n)
	l=1
	for i in range (n):
		if (lol*i-n+dd)%n==0:
			l= i
	r_1=[2 for k in range (n)]
	if dd==1:
		s = [ (i+1)*l%n for i in range(lol/dd)]
		r_1 = [ 3 if k in s else 2 for k in range(n) ]
		#print (s)
	else:
		j=1
		s=[(i+1)*l%n for i in range(lol/dd)]
		#print(s)
		kk=len(s)
		while j<=dd:
			for i in range(kk):
				s.append(s[i]+j*(n/dd))
			j+=1
		#print s
		r_1 = [ 3 if k in s else 2 for k in range(n) ]
	#print(r_1)
	dep=(b,a)
	pt=[dep]                                  #pour afficher les points
	kll=line([dep,(d,c)],rgbcolor=hue(0.6))   # le segment de (b,a) to (d,c) de pente c-a/d-b
	coll=[]
	for i in range (n):
		if r_1[i]==2:
			h=(dep[0]-1,dep[1])
			coll.append(line([dep,h],rgbcolor=hue(1.0)))  #etape horizontale
			pt.append(h)
			dep=h
		if r_1[i]==3:
			v=(dep[0],dep[1]-1)
			coll.append(line([dep,v],rgbcolor=hue(1.0)))  #etape verticale
			pt.append(v)
			dep=v
	for i in range(len(coll)):
		kll+=coll[i]
	mn=[]
	mn.append(r_1) #Chr word
	mn.append(kll)  #graph
	mn.append(pt)  #points
	return (mn)
	
	
def graphchse(l,x,y):   #l=une liste des pentes [a,b,c,d,e,f]  a/b,c/d, e/f pour dessiner x=sum xi NE y=sum yi NE
	r=len(l)
	p=[]
	pt=[]
	s=[l[0]]
	m=[l[1]]
	i=0
	h=l[0]
	hh=l[1]
	while i < r-2:    
		h+=l[i+2]
		hh+=l[i+3]
		s.append(h)
		m.append(hh)
		i+=2
	d0=0
	d1=0
	d2=y-s[0]
	d3=x-m[0]
	i=0
	pt.append(drawchrfromse(y,x,y-s[0],x-m[0])[2])   #points on ch
	p.append(drawchrfromse(y,x,y-s[0],x-m[0])[1])    #the path of ch
	j=0
	f=1
	k=[l[0]]
	t=[l[1]]
	while j < r-2:    # pour obtenir les points sur chaque chr
		k.append(l[j+2])
		j+=2
	while f < r-2:
		t.append(l[f+2])
		f+=2	
	while i < r-2:   
		d0=d2
		d1=d3
		d2-=l[i+2]
		d3-=l[i+3]
		p.append(drawchrfromse(d0,d1,d2,d3)[1])
		pt.append(drawchrfromse(d0,d1,d2,d3)[2])
		i+=2
	ptss=[]
	for i in range (len(pt)):
		for j in range (len(pt[i])):
			ptss.append(pt[i][j])
	ptss1=tuple(ptss)
	G=sum(p[i]+points(pt[i])for i in range (len(p))) 
	return (G)
	
	
	
	########################### SW #################
	
def drawchrfromsw(a,b,c,d):     #plot christoffel word de (b,a)----> (d,c)
	lol=abs(c-a)
	loll=abs(d-b)
	n=lol+loll
	dd=pgcd(lol,n)
	l=1
	for i in range (n):
		if (lol*i-n+dd)%n==0:
			l= i
			break
##########################
	if lol==0:
		r_1=[2 for k in range (dd)]
		
	else:			
		r_1=[1]
		kk1=1
		s = [ (i+1)*l%n  for i in range(lol/dd)]
		if s==[]:
			r_1=[2]	
		else:
			s=sorted(s)
			if s[0]==1:
				r_1=[2 for k in range (n)]
				if dd==1:
					s = [ (i+1)*l%n for i in range(lol/dd)]
					r_1 = [ 1 if k in s else 2 for k in range(n) ]
				else:
					j=1
					s=[(i+1)*l%n for i in range(lol/dd)]
					kk=len(s)
					while j<=dd:
						for i in range(kk):
							s.append(s[i]+j*(n/dd))
						j+=1
					r_1 = [ 1 if k in s else 2 for k in range(n) ]
				r_1=r_1[::-1]
			else:
				r_1 = [ 1 if k in s else 2 for k in range(n) ]
				r_1.reverse()
			if dd!=1:
				r=[]
				for i in range (dd):
					r+=r_1
				r_1=r			
	#######################################################
	dep=(b,a)
	pt=[dep]                                  #pour afficher les points
	kll=line([dep,(d,c)],rgbcolor=hue(0.6))   # le segment de (b,a) to (d,c) de pente c-a/d-b
	coll=[]
	for i in range (n):
		if r_1[i]==2:
			h=(dep[0]-1,dep[1])
			coll.append(line([dep,h],rgbcolor=hue(1.0)))  #etape horizontale
			pt.append(h)
			dep=h
		if r_1[i]==1:
			v=(dep[0],dep[1]+1)
			coll.append(line([dep,v],rgbcolor=hue(1.0)))  #etape verticale
			pt.append(v)
			dep=v
	for i in range(len(coll)):
		kll+=coll[i]
	mn=[]
	mn.append(r_1) #Chr word
	mn.append(kll)  #graph
	mn.append(pt)  #points
	return (mn)
	
	
def graphchsw(l,x,y):   #l=une liste des pentes [a,b,c,d,e,f]  a/b,c/d, e/f pour dessiner 
	r=len(l)
	p=[]
	pt=[]
	if r==1:
		pt.append(drawchrfromsw(-y,x,-y,x-l[0])[2])   #points on ch
		p.append(drawchrfromsw(-y,x,-y,x-l[0])[1])    #the path of ch	
	elif r>1:
		s=[l[0]]
		m=[l[1]]
		i=0
		h=l[0]
		hh=l[1]
		while i < r-2:    
			h+=l[i+2]
			s.append(h)
			i+=2
		th=1
		while th< r-2:
			hh+=l[th+2]	
			m.append(hh)
			th+=2
		h+=0
		hh+=0
		s.append(h)
		m.append(hh)
		j=1
		f=2
		sy=[l[1]]
		sx=[l[2]]
		while j < r-2:    # pour obtenir les points sur chaque chr
			sy.append(l[j+2])
			j+=2
		while f < r-2:
			sx.append(l[f+2])
			f+=2
		d0=0
		d1=0
		d2=-y
		d3=x-l[0]
		i=0
		pt.append(drawchrfromsw(-y,x,-y,x-l[0])[2])   #points on ch
		p.append(drawchrfromsw(-y,x,-y,x-l[0])[1])    #the path of ch
		tol=len(sx)
		while i < tol:    #-1   
			d0=d2
			d1=d3
			d2+=sy[i]
			d3-=sx[i]
			p.append(drawchrfromsw(d0,d1,d2,d3)[1])
			pt.append(drawchrfromsw(d0,d1,d2,d3)[2])
			i+=1	
		
	ptss=[]
	for i in range (len(pt)):
		for j in range (len(pt[i])):
			ptss.append(pt[i][j])
	ptss1=tuple(ptss)
	G=sum(p[i]+points(pt[i]) for i in range (len(p)))
	return (G)
	
	
	
	                         ##########################posit, conv , convtest, facop, ######################
	     ################### NW ########################
	     
def positnw (w):     

	n=len(w) 
	r=[]
	for i in range (n):
		if w[i]==1:
			r.append(i)
	return(r)


def facopnw(w):     #donne la suite des fractions sous forme de 1/k
	s=positnw(w)
	n=len(w)
	if n==0:
		k=[1]
	else:
		k=[]
		a=0
		for i in s:
			k.append(w[a:i+1].count(1))
			k.append(w[a:i+1].count(0))
			a=i+1
		if s[-1]!=n-1:
			k.append(0)
			k.append(n-s[-1]-1)
	return (k)
	
	
def factonw(k):   # premiere iteration pour concatenation
	#k=facopnw(w)	    
	p=[0]
	l=0
	m=[0,0]
	if len (k)==4:
		if k[0]*k[3]-k[1]*k[2]==-1:
			m[-2]=k[0]+k[2]
			m[-1]=k[1]+k[3]
		else:
			m=k
	elif len (k)==2:
		m=k
		
	else:
		while len(k[l:])>2:
			if k[l+0]*k[l+3]-k[l+1]*k[l+2]==-1:
				if p[-1]==1:
					m.append(k[l+0]+k[l+2])
					m.append(k[l+1]+k[l+3])
					l+=4
					p.append(1)
				else: 
					m[-2]=k[l+0]+k[l+2]
					m[-1]=k[l+1]+k[l+3]
					l+=4
					p.append(1)
					
			
			else:
				if p[-1]==1:
					m.append(k[l+0])
					m.append(k[l+1])
					m.append(k[l+2])
					m.append(k[l+3])	
					l+=2
					p.append(0)
				else:
					m[-2]=k[l+0]
					m[-1]=k[l+1]
					m.append(k[l+2])
					m.append(k[l+3])	
					l+=2
					p.append(0)
		if len(k[l:])==2:
			if p[-1]==1:
				m.append(k[-2])
				m.append(k[-1])
			else:
				m[-2]=k[-2]
				m[-1]=k[-1]		
	return (m)






def convnw(w):                        #forme la plus simplifiee de la suite des fractions
	k=facopnw(w)
	m=factonw(k)
	for i in range (len(m)):
		t=factonw(m)
		while t!=m:
			m=t
	return (m)
	
	
	
	
	
def convtestnw(w):        # teste l'ordre des pentes pour decider si c'est DC ou pas.
	u=convnw(w)
	print (u)
	if len(u)==2:
		print ("Digitally convex")
	else:
		c=[]
		i=0
		while i < len(u)-3:
			c.append(u[i]*u[i+3]-u[i+1]*u[i+2])
			i+=2
		
		if min(c)>=0:
			print ("Digitally convex")
		else:
			print ("Non Digitally convex")
	     ################################## NE ##########################""""*
def positne (w):     

	n=len(w) 
	r=[]
	for i in range (n):
		if w[i]==3:
			r.append(i)
	return(r)
	


def facopne(w):     #donne la suite des fractions sous forme de 1/k
	s=positne(w)
	t=len(s)
	#if s==[]:
	#	k=[1]
	#else:
	n=len(w)
	if t==0:
		k=[n]
	elif t>0:
		k=[s[0]]
		a=0
		c1=1
		for i in range(t-1):
			l=s[i+1]-s[i]-1
			if l!=0:
				if c1==1:
					k.append(1)
					k.append(l)
				else:
					if l==1:
						k.append(c1)
						k.append(1)
						c1=1
					else:
						k.append(c1)
						k.append(1)
						k.append(0)
						k.append(l-1)
						c1=1
				
			else:
				c1+=1
		if w.count(3)>len(k)/2:
			k.append(c1)
			k.append(n-s[-1]-1)
	return (k)
	
	

	
	
def factone(k):	    # premiere iteration pour concatenation
	#k=facopne(w)
	if len(k)<=3:
		return (k)
	else:  #if k[2]!=k[4]+1: 	
		p=[0]
		l=0
		m=[k[0],0,0]
		if len (k)==5:
			if k[1]*k[4]-k[2]*k[3]==1:  ### changed to==1 car on est dans le sens mirroir
				m[-2]=k[1]+k[3]
				m[-1]=k[2]+k[4]
			else:
				m=k
		elif len (k)==3:
			m=k
		
		else:
			while len(k[l:])>3:
				if k[l+1]*k[l+4]-k[l+2]*k[l+3]==1:
					if p[-1]==3:
						m.append(k[l+1]+k[l+3])
						m.append(k[l+2]+k[l+4])
						l+=4
						p.append(3)
					else: 
						m[-2]=k[l+1]+k[l+3]
						m[-1]=k[l+2]+k[l+4]
						l+=4
						p.append(3)
					
			
				else:
					if p[-1]==3:
						m.append(k[l+1])
						m.append(k[l+2])
						m.append(k[l+3])
						m.append(k[l+4])	
						l+=2
						p.append(0)
					else:
						m[-2]=k[l+1]
						m[-1]=k[l+2]
						m.append(k[l+3])
						m.append(k[l+4])	
						l+=2
						p.append(0)
			if len(k[l:])==3:
				if p[-1]==3:
					m.append(k[-2])
					m.append(k[-1])
				else:
					m[-2]=k[-2]
					m[-1]=k[-1]	
			if m[-4]*m[-1]-m[-2]*m[-3]==1:
				bb=m[:-4]
				bb.append(m[-4]+m[-2])
				bb.append(m[-3]+m[-1])
				m=bb	
		return (m)
	#else:
	#	return (k)






def convne(w):                        #forme la plus simplifiee de la suite des fractions
	k=facopne(w)
	m=factone(k)
	for i in range (len(m)):
		t=factone(m)
		while t!=m:
			m=t
	return (m)
	
	
	
	
	
def convtestne(w):        # teste l'ordre des pentes pour decider si c'est DC ou pas.
	u=convne(w)
	print (u)
	if len(u)==2:
		print ("Digitally convex")
	else:
		c=[]
		i=0
		while i < len(u)-3:
			c.append(u[i]*u[i+3]-u[i+1]*u[i+2])
			i+=2		
		if min(c)>=0:
			print ("Digitally convex")
		else:
			print ("Non Digitally convex")
	     ############################################## ES #########################"    
def positse (w):     

	n=len(w) 
	r=[]
	for i in range (n):
		if w[i]==3:
			r.append(i)
	return(r)
	


def facopse(w):     #donne la suite des fractions sous forme de 1/k
	s=positse(w)
	n=len(w)
	k=[]
	a=0
	for i in s:
		k.append(w[a:i+1].count(3))
		k.append(w[a:i+1].count(2))
		a=i+1
	if s[-1]!=n-1:
		k.append(0)
		k.append(n-s[-1]-1)
	return (k)
	
	
def factose(k):	    # premiere iteration pour concatenation
	#k=facopse(w)
	p=[0]
	l=0
	m=[0,0]
	
	if len (k)==4:
		if k[0]*k[3]-k[1]*k[2]==-1:
			m[-2]=k[0]+k[2]
			m[-1]=k[1]+k[3]
		else:
			m=k
	elif len (k)==2:
		m=k
		
	else:
		while len(k[l:])>2:
			if k[l+0]*k[l+3]-k[l+1]*k[l+2]==-1:
				if p[-1]==3:
					m.append(k[l+0]+k[l+2])
					m.append(k[l+1]+k[l+3])
					l+=4
					p.append(3)
				else: 
					m[-2]=k[l+0]+k[l+2]
					m[-1]=k[l+1]+k[l+3]
					l+=4
					p.append(3)
					
			
			else:
				if p[-1]==3:
					m.append(k[l+0])
					m.append(k[l+1])
					m.append(k[l+2])
					m.append(k[l+3])	
					l+=2
					p.append(2)
				else:
					m[-2]=k[l+0]
					m[-1]=k[l+1]
					m.append(k[l+2])
					m.append(k[l+3])	
					l+=2
					p.append(2)
		if len(k[l:])==2:
			if p[-1]==3:
				m.append(k[-2])
				m.append(k[-1])
			else:
				m[-2]=k[-2]
				m[-1]=k[-1]		
	return (m)







def convse(w):                        #forme la plus simplifiee de la suite des fractions
	k=facopse(w)
	m=factose(k)
	for i in range (len(m)):
		t=factose(m)
		while t!=m:
			m=t
	return (m)
	
	
	
	
	
def convtestse(w):        # teste l'ordre des pentes pour decider si c'est DC ou pas.
	u=convse(w)
	print (u)
	if len(u)==2:
		print ("Digitally convex")
	else:
		c=[]
		i=0
		while i < len(u)-3:
			c.append(u[i]*u[i+3]-u[i+1]*u[i+2])
			i+=2
		
		if min(c)>=0:
			print ("Digitally convex")
		else:
			print ("Non Digitally convex")
			
			
			
			################################################# SW ########################
def positsw (w):     

	n=len(w) 
	r=[]
	for i in range (n):
		if w[i]==1:
			r.append(i)
	return(r)


def facopsw(w):     #donne la suite des fractions sous forme de 1/k
	s=positsw(w)
	t=len(s)
	#if t==0:
	#	k=[1]
	#else:
	n=len(w)
	if t==0:
		k=[n]
	elif t>0:
		k=[s[0]]
		a=0
		c1=1
		for i in range(t-1):
			l=s[i+1]-s[i]-1
			if l!=0:
				if c1==1:
					k.append(1)
					k.append(l)
				else:
					k.append(c1)
					k.append(1)
					c1=1
			else:
				c1+=1
		if w.count(1)>len(k)/2:
			k.append(c1)
			k.append(n-s[-1]-1)      ####I added this row
	return (k)

	
	
def factosw(k):
	#k=facopsw(w)
	if len(k)<=3:
		return (k)
	else:  #if k[2]!=k[4]+1:  
		p=[0]
		l=0
		m=[k[0],0,0]
		if len (k)==5:
			if k[1]*k[4]-k[2]*k[3]==1:
				m[-2]=k[1]+k[3]
				m[-1]=k[2]+k[4]       
			else:
				m=k        
		elif len (k)==3:
			m=k					
		else:
			kl=k[-1]
			kl1=k[-2]
			k=k[:-2]
			while len(k[l:])>3:
				if k[l+1]*k[l+4]-k[l+2]*k[l+3]==1:
					if p[-1]==1:
						m.append(k[l+1]+k[l+3])
						m.append(k[l+2]+k[l+4])
						l+=4
						p.append(1)
					else: 
						m[-2]=k[l+1]+k[l+3]
						m[-1]=k[l+2]+k[l+4]
						l+=4
						p.append(1)
				
			
				else:
					if p[-1]==1:
						m.append(k[l+1])
						m.append(k[l+2])
						m.append(k[l+3])
						m.append(k[l+4])	
						l+=2
						p.append(2)
					else:
						m[-2]=k[l+1]
						m[-1]=k[l+2]
						m.append(k[l+3])
						m.append(k[l+4])	
						l+=2
						p.append(2)
			
			if len(k[l:])==3:
				if p[-1]==1:
					m.append(k[-2])
					m.append(k[-1])
				else:
					m[-2]=k[-2]
					m[-1]=k[-1]		

			m.append(kl1)
			m.append(kl)

			if m[-4]*m[-1]-m[-2]*m[-3]==1:
				bb=m[:-4]
				bb.append(m[-4]+m[-2])
				bb.append(m[-3]+m[-1])
				m=bb
		return (m)
	#else:
	#	return (k)






def convsw(w):                        #forme la plus simplifiee de la suite des fractions
	k=facopsw(w)
	m=factosw(k)
	for i in range (len(m)):
		t=factosw(m)
		while t!=m:
			m=t
	return (m)
	
	
	
	
	
def convtestsw(w):        # teste l'ordre des pentes pour decider si c'est DC ou pas.
	u=convsw(w)
	print (u)
	if len(u)==2:
		print ("Digitally convex")
	else:
		c=[]
		i=0
		while i < len(u)-3:
			c.append(u[i]*u[i+3]-u[i+1]*u[i+2])
			i+=2
		if min(c)>=0:
			print ("Digitally convex")
		else:
			print ("Non Digitally convex")
