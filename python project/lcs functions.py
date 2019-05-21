import glob

class Longestcommonstring():

	def string_to_char(self,st):                    #for converting string to char and storing in a list

		st1=""
		l=[]
		for i in range(len(st)):
			st1=""
			for j in range(i,len(st)):
				st1=st1+st[j]
				l.append(st1)
		print(l)
		return l

	def substring(self,k1,k2):                      #appending all common in to one list
		l1=[]
		for i in k1:
			if i in k2:
				l1.append(i)
		return l1

	def longest_length(self,k3):                    #finding the longest length in the list
		j=0
		p=0
		try:
			for i in range(0,len(k3)):
				if(len(k3[i])>p):
					p=len(k3[i])
					j=i
			return (p,k3[j])
		except IndexError:
			print('Lists are empty')
		#return (p,k3[j])

	def lcs_percentage(self,matchedlength,twostrings_sum):          #for finding the percentage of lcs
		lcs=((matchedlength*2)/(twostrings_sum))*100
		return lcs



flist=glob.glob("Newfolder\\*")
print(flist)


mainmat=[]
try:
	for z in range(len(flist)):
		submat=[]
	
		for p in range(len(flist)):
			lcs=Longestcommonstring()
			ty1=open(flist[z])
			ty1=ty1.read()
			k1=lcs.string_to_char(ty1)
			ty2=open(flist[p])
			ty2=ty2.read()
			k2=lcs.string_to_char(ty2)
			k3=lcs.substring(k1,k2)
			k4=lcs.longest_length(k3)
			st2=k4[1].strip()
			print(st2);
			matchedlength=len(st2)
			twostrings_sum=len(ty1)+len(ty2)
			k=lcs.lcs_percentage(matchedlength,twostrings_sum)
			k=round(k,2)
			print(k);
			submat.append(str(k))

		mainmat.append(submat)

	
except:
	print("lists are empty")
print(mainmat)
for i in mainmat:
	a="   ".join(i)
	print(a)
		
