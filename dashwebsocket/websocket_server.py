import asyncio
import datetime
import random
import websockets
import json
from datetime import datetime

CLIENTS = set()

stocks = ["MSFT", "AAPL", "NVDA","AMZN"]
prices = [100, 155, 66, 88]

def gen_data():
    idx = random.randrange(0,4)
    stock = stocks[idx]
    org_price = prices[idx]
    price = org_price + random.randrange(-1000,1000)/100
    diff = (price - org_price)/org_price

    #create a new data point
    point_data = {
    	'stock': stock,
    	'price' : round(price,2),
    	'diff': "{:.2%}".format(diff),
    	'time': datetime.now().strftime("%H:%M:%S")
    }
    return point_data

async def broadcast():
    while True:
        data = gen_data()
        for ws in CLIENTS:
            await ws.send(json.dumps(data))
        await asyncio.sleep(random.random())

async def publisher(websocket, path):
    CLIENTS.add(websocket)
    try:
        async for msg in websocket:
            pass
    finally:
        CLIENTS.remove(websocket)
        

start_server = websockets.serve(publisher, "127.0.0.1", 5656)
asyncio.get_event_loop().create_task(broadcast())
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()