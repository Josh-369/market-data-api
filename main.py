{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, request, jsonify\
\
app = Flask(__name__)\
\
@app.route('/webhook', methods=['POST'])\
def webhook():\
    data = request.json  # Get incoming JSON data\
\
    if not data:\
        return jsonify(\{'error': 'No data received'\}), 400\
    \
    # Extract relevant information\
    symbol = data.get('symbol')\
    price = data.get('price')\
    timestamp = data.get('time')\
\
    # Print received data (useful for debugging)\
    print(f"Received Webhook: Symbol=\{symbol\}, Price=\{price\}, Time=\{timestamp\}")\
\
    # Respond to TradingView\
    return jsonify(\{'message': 'Webhook received successfully', 'received_data': data\}), 200\
\
if __name__ == '__main__':\
    app.run(host='0.0.0.0', port=8080)\
}