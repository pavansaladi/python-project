import glob
flist=glob.glob("C:\\Users\\Lenovo\\Desktop\\New folder\\*")
print(flist)
fo=open(flist[0],'r')
f1=open(flist[1],'r')
st1=fo.read()
st2=f1.read()

def remove_spchar(st):
	st1=""
	for i in st:
		if(97<=ord(i)<=122):
			st1=st1+i
	return st1
def ngram(st1,n):
	l=[]
	for i in range(0,len(st1)-n+1):
		l.append(st1[i:i+n])
	sum=0
	l1=[]
	for i in l:
		k=len(i)
		sum=0
		for j in i:
			sum=sum+(2**(k-1))*ord(j)
			k=k-1
		l1.append(sum)
	return(l1)
def common_in_lists(k1,k2):
	l4=[]
	for i in k1:
		if i in k2:
			l4.append(i)
	return l4


st1=remove_spchar(st1)
st2=remove_spchar(st2)

n=int(input('enter any value to slice'))
k1=ngram(st1,n)
k2=ngram(st2,n)
print(k1)
print(k2)
k=common_in_lists(k1,k2)
print((len(k)*2)/(len(k1)+len(k2))*100)
