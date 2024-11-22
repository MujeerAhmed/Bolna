# Bolna

## server.py
- This script is responsible for managing the websocket connections created by different users ('abc' in this case) 
- replies to the client when it sends a message
- closes a connection after 60 seconds of it's inception.

## client.py
- This script passes a UserID 'abc' and spwans 10 connections
- sends a message to the server every 2 seconds as long as the connection is intact.
