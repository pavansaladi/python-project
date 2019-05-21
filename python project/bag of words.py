import os
import glob
flist=[]

flist=glob.glob("Newfolder\\*")
print(flist)

def readfile_split(fo):      #for spliting the words and store to a list
	f1=open(fo)
	str=f1.read()
	str=str.lower()
	st1=""
	for i in str:
		if(97<=ord(i)<=122 or 48<=ord(i)<=57):
			st1=st1+i
		else:
			st1=st1+' '

	data = st1.split()
	print(data)
	return data

def frequency(k):                #for finding the frequency of each word
	dict={}
	for i in k:
		if i not in dict:
			dict[i]=1
		else:
			dict[i]=dict[i]+1
	print(dict)
	return dict

def dotproduct(r,h):             #dot product of two common words
	l=[]
	for i in r:
		for j in h:
			if(i==j):
				l.append(r[i]*h[j])
	print(l)
	return l

def euclidian_form(r):              #square root of all the values
	sum=0
	for i in r.values():
		sum=sum+i**2
	v=sum**(1/2)
	return v

def sum_of_dotproduct(l):               #for finding the sum of common words
	tot=0
	for i in l:
		tot=tot+i
	print(tot)
	return tot
i=0
l=[]
for z in range(len(flist)-1):                   #for multiples files
	
	ty=readfile_split(flist[z])

	f1=frequency(ty)

	f2=euclidian_form(f1)
	for p in range(z+1,len(flist)):
		ty1=frequency(readfile_split(flist[p]))
		ty2=euclidian_form(ty1)
		ty3=dotproduct(f1,ty1)
		ty4=sum_of_dotproduct(ty3)

		cos=((ty4)/(f2*ty2))*100
		l.append(cos)

		print("the percentage of copy from file",os.path.basename(flist[z]),"and",os.path.basename(flist[p]),cos)
