from flask import Flask, session, jsonify, request
from flask.ext.cors import CORS
from flask_mail import Mail, Message
from database import NewOrder, OrderUpdation, FetchOrders
import gc
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~Xsa!jmN]LWX/,?RT'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'themidnightsaviour'
app.config['MAIL_PASSWORD'] = 'tmsadmin123'

mail = Mail(app)
CORS(app)

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
    if request.method=='POST':
      reply, order = NewOrder(request.args.get('Order'))
      if reply == 'Order Placed':
	message = 'New order<br>'+ str(order)
	sendmail('themidnightsaviour@gmail.com',message, 'New order')
	sendmail('deliveryboy31@gmail.com',message, 'New order')
      return reply
    return 'Invalid Request'
  except Exception as e:
    return str(e)

if __name__ == '__main__':
  app.run(host='0.0.0.0')
