# 1. TCP Communication
`tcpclient.py`
 - Connects to a server on port `41111`
 - Sends the numbers to the server, waits for a response, and prints the server’s reply, which includes the sum of the two numbers along with the current time.

`tcpserver.py`
 - Binds to the server’s hostname on port `41111` and waits for client connections.
 - When a client connects, it receives the numbers, calculates the sum, and sends it back to the client.
 - Logs the message it received from the client and the reply it sends.

# 2. UDP Communication
`udpclient.py`
-   Asks the user to enter a single number.
-   Sends that number to the server at port `2233`.
-   Receives the server’s response (the sum if multiple numbers were sent) and displays it along with a timestamp.

`udpserver.py`
-   Receives a number (or multiple numbers if entered) from the client, calculates the sum, and sends it back.
-   Logs the client’s message and the response it sends.

# Requirements
Python 3.x

# How to Run the Code
-   Start the Server:
    -   For TCP:
        `python3 tcpserver.py` 
        
    -   For UDP:
        `python3 udpserver.py` 
        
-   Start the Client:
    -   For TCP:
        `python3 tcpclient.py` 
        
    -   For UDP:
        `python3 udpclient.py` 
        
-   **Example Usage**:
    
    -   For TCP: Enter two numbers separated by a space (e.g., `3 5`).
    -   For UDP: Enter a single number (e.g., `10`).
    
    The server will calculate the sum and send it back with a timestamp, which the client will then display.
## Sample Output

### TCP Example

-   **Client Input**: `3 5`
-   **Server Output**: `6388118: server received: 3 5`
-   **Client Output**: `6388118: <timestamp> 8`

### UDP Example

-   **Client Input**: `10 20`
-   **Server Output**: `6388118: server received from: <client_address> with data 10 20`
-   **Client Output**: `6388118: <timestamp> 30`

## Important Notes

-   **Port Numbers**:
    -   TCP communication happens on port `41111`.
    -   UDP communication happens on port `2233`.
-   **Error Handling**: This is a simple example, so there’s minimal error handling. For instance, it assumes that the user will enter valid numbers.
-   **Timestamp**: The timestamp is generated using `time.asctime()` and added to the server’s response.
