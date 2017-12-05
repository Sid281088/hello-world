# -*- coding: cp1252 -*-
#Original code from:
#http://ankitvad.github.io/blog/visualizingwhatsappchathistory.html
##


# Define inputs
whatsappfile="WhatsApp Chat with Anastasia Senina.txt" #Whatsapp text file as made by whatsapp.
myname="Siddharth" #Exactly as it is in the Whatsapp file
yourname="Anastasia Senina" #Exactly as it is in the Whatsapp file

#Note that the input text file might have to be manually cleansed depending on what is there.
##
#dates.py
x = open(whatsappfile,"r")
#loading data
me = myname+":"
you = yourname+":"

my_date = open(myname+"_date"+".txt","w")
your_date = open(yourname+"_date"+".txt","w")


y = x.readline().decode('utf-8-sig').encode('utf-8')
while y:
	if (me in y):
		temp = y.split(" ",1)
		my_date.write(temp[0]+"\n")
	elif (you in y):
		temp = y.split(" ",1)
		your_date.write(temp[0]+"\n")
	y = x.readline().decode('utf-8-sig').encode('utf-8')
my_date.close();
your_date.close();

	
print('Data loaded and split');

#Cleaning data
#cal_msg.py :
import re
b = open(whatsappfile,"r")
a = open("messages_"+yourname+".txt","w")
y = b.readline().decode('utf-8-sig').encode('utf-8')
while y:
	if(y != '\r\n'):
		temp = y.split(": ",2)
		
		x = temp[1] #SIDS
		x = re.sub('([\:\;][\)\|\\\/dDOoPp\(\'\"][\(\)DOo]?)','',x)
		x = re.sub('[?\.#_]','',x)
		x = re.sub('[\s]+',' ',x)
		a.write(x+"\n")
	y = b.readline()
a.close();

print('Data cleansed and raw messages saved to '+"messages_"+yourname+".txt")

#count dates and Export dates to csv
x = open(myname+"_date"+".txt",'r')
y = x.read()

from collections import Counter
counted= Counter(y.split('\n'))
outfileme="counted_"+myname+".csv"
with open(outfileme,'w') as f:
    for k,v in  counted.most_common():
        f.write( "{} {}\n".format(k,v) )
f.close()
#

#count dates and Export dates to csv
x = open(yourname+"_date"+".txt",'r')
y = x.read()
from collections import Counter
counted= Counter(y.split('\n'))
outfileyou="counted_"+yourname+".csv"
with open(outfileyou,'w') as f:
    for k,v in  counted.most_common():
        f.write( "{} {}\n".format(k,v) )
f.close()
#print Counter(y.split('\n'))
print('Counts saved to: '+outfileyou +' And ' + outfileme) 
##
