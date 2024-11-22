import websocket
import threading
import time
from datetime import datetime

# Function to simulate a single WebSocket client
def simulate_connection(user_id, call_id, duration):
    url = f"ws://localhost:8765/{user_id}/{call_id}"
    print(f"Connecting to {url}")
    
    # Connect to the WebSocket server
    ws = websocket.WebSocket()
    ws.connect(url)
    
    start_time = time.time()
    while time.time() - start_time < duration:
        # Current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # User A sends a message
        user_a_message = f"Hello from User A at {timestamp} on channel /{user_id}/{call_id}"
        ws.send(user_a_message)
        print(f"User A sent a message at {timestamp} on channel /{user_id}/{call_id}")
        
        # User B replies
        user_b_reply = ws.recv()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"User B replied with '{user_b_reply}' at {timestamp} on channel /{user_id}/{call_id}")
        
        # Wait for 10 seconds
        time.sleep(10)
    
    # Close the WebSocket connection
    ws.close()
    print(f"Connection {url} closed")

# Function to spawn multiple WebSocket connections
def simulate_multiple_connections(num_connections, duration):
    threads = []
    user_id = "abc"  # Example user ID
    
    for call_id in range(1, num_connections + 1):
        # Create a thread for each WebSocket connection
        thread = threading.Thread(target=simulate_connection, args=(user_id, call_id, duration))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Main function
if __name__ == "__main__":
    # Number of WebSocket connections to simulate
    num_connections = 10
    # Duration for each connection (in seconds)
    duration = 60
    
    # Simulate multiple WebSocket conversations
    simulate_multiple_connections(num_connections, duration)
