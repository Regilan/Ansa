'''
------------Defined Functions Indeces------------
For encrypting: doen(string)		return string
For derypting : dode(string)		return string
-------------------------------------------------
'''

#importing the required packages
import numpy as np

#hash key used in the crypto process
key=[77, 97, 114, 105, 97, 95, 73, 114, 117, 100, 97, 121, 97, 95, 82, 101, 103, 105, 108, 97, 110, 95, 108, 111, 118, 101, 115, 95, 78, 97, 110, 99, 121, 95, 83, 97, 98, 97, 116, 116, 105, 110, 105, 95, 115, 111, 95, 109, 117, 99, 104]

#formatting the hash input to the list
def getbest(ips):
	cvdips=list(ips)
	ips=[]
	for i in cvdips:
		ips.append(ord(i) if not str(i).isdigit() else i)
	return ips

#returns the string from the np-array paramater
def as_text(nparray):
	arr=list(nparray)
	t=''
	for i in arr:
		t=t+chr(i)
	return t

#hash function algorithm to encrypt the given text
def doen(ips):
	ips=getbest(ips)
	if len(ips) == len(key):
		return as_text(np.array(ips)+np.array(key))
	elif len(ips)>len(key):
		return as_text(np.array(ips[:len(key)])+np.array(key))+doen(ips[len(key):])
	else:
		return as_text(np.array(ips)+np.array(key[:len(ips)]))

#hash function algorithm to decrypt the given text
def dode(ips):
	ips=getbest(ips)
	if len(ips) == len(key):
		return as_text(np.array(ips)-np.array(key))
	elif len(ips)>len(key):
		return as_text(np.array(ips[:len(key)])-np.array(key))+dode(ips[len(key):])
	else:
		return as_text(np.array(ips)-np.array(key[:len(ips)]))