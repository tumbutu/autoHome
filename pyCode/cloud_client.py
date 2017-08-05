import socket
#import pymongo
#import json
#from pymongo import MongoClient
#client = MongoClient('localhost',27017)
#db = client.pi_sensor_data
#col = db.year2017

srvsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#create a socket object
host = socket.gethostbyname('aaronichie')	#get local machines's name
srvsock.bind((host,23000))					#reserve a port for the service and bind the host to the port
srvsock.listen(5) 		# Wait for client connection(listens to accept 5 connections at a time)

msg = True

while 1:
	clisock,(remhost, remport) = srvsock.accept()	#establish connection with client
	str = clisock.recv(100)							#receives TCP message(Max 100 characters can be received @ a time)	
	#data = json.loads(str)
	#col.insert_one(data)
	#if msg:
	#	print "*** data is being delivered to MongoDB *** "
	#	msg = False
	print str
	#clisock.close()								#close connection