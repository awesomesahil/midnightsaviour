from flask import Flask, session, jsonify, request
from flask.ext.cors import CORS
from flask_mail import Mail, Message
from database import NewOrder, OrderUpdation, FetchOrders
import gc
import json

<<<<<<< HEAD
def MongoDBconnection(database, collection):
  connection = pymongo.MongoClient("mongodb://localhost")
  db = connection[database]
  cursor = db[collection]
  return connection, db, cursor
=======
app = Flask(__name__)
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~Xsa!jmN]LWX/,?RT'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'themidnightsaviour'
app.config['MAIL_PASSWORD'] = 'tmsadmin123'

mail = Mail(app)
CORS(app)
>>>>>>> 1defd22088fa0901d56efa4868cf13c7991823dd

def allowed_file(filename):
  return filename.rsplit('.', 1)[-1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def home():
  #print sendmail('sahilsehgal1995@gmail.com', 'Trying hard', 'Trying')
  return 'TMS'
    #return app.send_static_file("index.html")

def sendmail(email, message, subject):
  try:
    msg = Message(subject,sender="No-Reply@lenme.in",recipients=[email])
    msg.body = "Lenme"
    msg.html = '<b>'+message+'</b>'
    mail.send(msg)
    return 'Mail Sent'
  except Exception as e:
    print str(e)
    return 'Unable to send'

@app.route('/api/orderUpdation/', methods=['GET', 'POST'])
def orderUpdation():
  if request.method=='POST' and request.args.get('secretKey') == 'TMSHERE':
    return OrderUpdation(request.args.get('Order'))
  return 'Invalid Request'

@app.route('/api/Fetchorders/', methods=['GET', 'POST'])
def Fetchorders():
  if request.method=='POST' and request.args.get('secretKey') == 'TMSHERE':
    return FetchOrders()
  return 'Invalid Request'

@app.route('/api/newOrder/', methods=['GET', 'POST'])
def neworder():
  try:
<<<<<<< HEAD
    now = datetime.datetime.now()
    starttime = now.replace(hour=21, minute=30, second=0, microsecond=0)
    endtime = starttime + datetime.timedelta(hours=5)
    if now<starttime or now>endtime:
      return 'Order Not Allowed', '{}'
    return ''
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
=======
    if request.method=='POST':
      reply, order = NewOrder(request.args.get('Order'))
      if reply == 'Order Placed':
	message = 'New order<br>'+ str(order)
	sendmail('themidnightsaviour@gmail.com',message, 'New order')
	sendmail('deliveryboy31@gmail.com',message, 'New order')
      return reply
    return 'Invalid Request'
>>>>>>> 1defd22088fa0901d56efa4868cf13c7991823dd
  except Exception as e:
    return str(e)

<<<<<<< HEAD
if __name__ == "__main__":
  #print comparedatetime()
  #print FetchOrders()
  #print OrderUpdation('O_6')
  print NewOrder('{"Name":"Sahil Sehgal", "Products":[{"product_name":"MALAI KOFTA","Actual_Price": "50", "TMS_Price": "60", "Shop_Name" : "NFS1"}, {"product_name":"Paneer Thaliii","Actual_Price": "50", "TMS_Price": "60", "Shop_Name" : "NFS2"}, {"product_name":"Paneer Thali22","Actual_Price": "50", "TMS_Price": "60", "Shop_Name" : "NFS2"}]}')
=======
if __name__ == '__main__':
  app.run(host='0.0.0.0')
>>>>>>> 1defd22088fa0901d56efa4868cf13c7991823dd
