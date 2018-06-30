'''
---------------------Defined Functions Indeces---------------------
For hashing: doen(string, True => encryption/ False => decryption)		
			 return string
-------------------------------------------------------------------
'''

#importing the required packages
import numpy as np

#hash key used in the crypto process
key=[77, 97, 114, 105, 97, 95, 73, 114, 117, 100, 97, 121, 97, 95, 82, 101, 103, 105, 108, 97, 110, 95, 108, 111, 118, 101, 115, 95, 78, 97, 110, 99, 121, 95, 83, 97, 98, 97, 116, 116, 105, 110, 105, 95, 115, 111, 95, 109, 117, 99, 104]

#formatting the hash input to the list
def getbest(cvdips):
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
def doen(ips,state):
	ips=getbest(list(ips))
	if len(ips) == len(key):
		return as_text(np.array(ips)+np.array(key) if state else np.array(ips)-np.array(key))
	elif len(ips)>len(key):
		return as_text(np.array(ips[:len(key)])+np.array(key) if state else np.array(ips[:len(key)])-np.array(key))+doen(ips[len(key):],state)
	else:
		return as_text(np.array(ips)+np.array(key[:len(ips)]) if state else np.array(ips)-np.array(key[:len(ips)]))
