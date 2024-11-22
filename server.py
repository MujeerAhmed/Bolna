import asyncio
import websockets

# WebSocket server handler
async def handle_connection(websocket, path):
    print(f"New connection established on channel {path}")
    try:
        async for message in websocket:
            print(f"Received: {message} on channel {path}")
            # Echo the message back to simulate a reply
            reply = f"Received '{message}'"
            await websocket.send(reply)
            print(f"Replied: {reply}")
    except websockets.exceptions.ConnectionClosed:
        print(f"Connection closed on channel {path}")

# Start the WebSocket server
async def start_server():
    server = await websockets.serve(handle_connection, "localhost", 8765)
    print("WebSocket server started on ws://localhost:8765")
    await server.wait_closed()

# Run the server
if __name__ == "__main__":
    asyncio.run(start_server())
