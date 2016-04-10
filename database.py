import pymongo
import json
import os
import gc
from os import walk
from random import randint

base='http://www.filterlady.com/'

def MongoDBconnection(database, collection):
  connection = pymongo.MongoClient("mongodb://localhost")
  db = connection[database]
  cursor = db[collection]
  return connection, db, cursor

def OrderUpdation(orderid):
  try:
    connection, db, collection = MongoDBconnection('TMS', 'Orders')
    collection.update({'_id':orderid},{'$set':{"Status":"Delivered"}})
    connection.close()
    gc.collect()
    return 'Order Delivered'
  except Exception as e:
    print str(e)
    return 'Unable to Place order'

def FetchOrders():
  try:
    connection, db, collection = MongoDBconnection('TMS', 'Orders')
    iter = collection.find({'Status':'New Order'})
    orders = list()
    for order in iter:
      orders.append(order)
    connection.close()
    gc.collect()
    return json.dumps(orders)
  except Exception as e:
    print str(e)
    return 'Unable to Place order'

def NewOrder(order):
  try:
    order = json.loads(order)
    i=1
    for product in order['Products']:
      connection, db, collection = MongoDBconnection('TMS', product['Shop_Name'])
      iter = collection.find({"product_name": product['product_name']})
      if iter.count():
	product['TMS_Price']=iter[0]['TMS_Price']
      else:
	order['Products'].remove(product)
      connection.close()
    connection, db, collection = MongoDBconnection('TMS', 'Orders')
    iter = collection.find()
    if not iter.count():
      order['_id']='O_1'
    else:
      order['_id'] = 'O_'+ str(int(iter[iter.count()-1]['_id'].split("_")[-1])+1)
    order['Status'] = 'New Order'
    collection.insert(order)
    connection.close()
    gc.collect()
    return 'Order Placed', json.dumps(order)
  except Exception as e:
    print str(e)
    return 'Unable to Place order', '{}'

if __name__ == "__main__":
  print FetchOrders()
  #print OrderUpdation('O_6')
  #print NewOrder('{"Name":"Sahil Sehgal", "Products":[{"product_name":"MALAI KOFTA","Actual_Price": "50", "TMS_Price": "60", "Shop_Name" : "NFS1"}, {"product_name":"Paneer Thaliii","Actual_Price": "50", "TMS_Price": "60", "Shop_Name" : "NFS2"}, {"product_name":"Paneer Thali22","Actual_Price": "50", "TMS_Price": "60", "Shop_Name" : "NFS2"}]}')
