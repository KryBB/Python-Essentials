#-------------------------------------------------------
# Connection Error Troubleshooting Guide (Interactive)
#-------------------------------------------------------

import socket
import requests
import traceback
from urllib.request import urlopen

def connection_refused_demo():
    """
    ConnectionRefusedError: Target actively rejected connection
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for:
    - Closed ports
    - Wrong IP/port combinations
    - Services not running
    
    Resolution:
    - Retry logic with backoff
    - Service verification
    - Timeout parameters
    """
    print("\n=== DEMO: ConnectionRefusedError ===")
    try:
        s = socket.socket()
        s.connect(('localhost', 9999))  # Intentional bad port
    except ConnectionRefusedError as e:
        print("🔥 RAW TRACEBACK:")
        traceback.print_exc()

def connection_aborted_demo():
    """
    ConnectionAbortedError: Remote host terminated connection
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for:
    - Network interruptions
    - Server-side closures
    - Firewall interference
    
    Resolution:
    - Chunked transfers
    - Connection verification
    - Heartbeat mechanisms
    """
    print("\n=== DEMO: ConnectionAbortedError ===")
    try:
        s = socket.socket()
        s.connect(('httpbin.org', 80))
        s.sendall(b"GET /delay/2 HTTP/1.1\r\nHost: httpbin.org\r\nConnection: close\r\n\r\n")
        s.settimeout(1.0)
        s.recv(1024)
    except (ConnectionAbortedError, socket.timeout) as e:
        print("🔥 RAW TRACEBACK:")
        traceback.print_exc()

def connection_reset_demo():
    """
    ConnectionResetError: Connection forcibly reset by peer
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for:
    - Remote host crashes
    - Network equipment issues
    - Protocol violations
    
    Resolution:
    - Reconnection logic
    - Protocol validation
    - Higher-level libraries
    """
    print("\n=== DEMO: ConnectionResetError ===")
    try:
        conn = urlopen('http://httpbin.org/bytes/1024')
        conn.close()
        conn.read()  # Intentional error
    except ConnectionResetError as e:
        print("🔥 RAW TRACEBACK:")
        traceback.print_exc()

#-------------------------------------------------------
# Trigger Functions (For Error Mode)
#-------------------------------------------------------

def trigger_connection_refused():
    """Raw error trigger for menu option"""
    s = socket.socket()
    s.connect(('localhost', 9999))

def trigger_connection_aborted():
    """Raw error trigger for menu option"""
    s = socket.socket()
    s.connect(('httpbin.org', 80))
    s.sendall(b"GET / HTTP/1.1\r\nHost: httpbin.org\r\n\r\n")
    s.close()
    s.recv(1024)

def trigger_connection_reset():
    """Raw error trigger for menu option"""
    conn = urlopen('http://httpbin.org/bytes/1024')
    conn.close()
    conn.read()

#-------------------------------------------------------
# Main Menu System
#-------------------------------------------------------

def show_demo_mode():
    """Run all educational demonstrations"""
    print("\n" + "="*50)
    print("RUNNING DEMONSTRATION MODE".center(50))
    print("="*50)
    connection_refused_demo()
    connection_aborted_demo()
    connection_reset_demo()

def show_trigger_mode():
    """Let user select specific errors to trigger"""
    print("\n" + "="*50)
    print("TRIGGER ERROR MODE".center(50))
    print("="*50)
    print("Select error to trigger:")
    print("1. ConnectionRefusedError")
    print("2. ConnectionAbortedError")
    print("3. ConnectionResetError")
    
    choice = input("Enter number (1-3): ")
    
    triggers = {
        '1': trigger_connection_refused,
        '2': trigger_connection_aborted,
        '3': trigger_connection_reset
    }
    
    if choice in triggers:
        try:
            triggers[choice]()
        except Exception:
            print("\n💥 RAW TRACEBACK:")
            traceback.print_exc()
    else:
        print("Invalid selection")

def main():
    print("\n" + "="*50)
    print("CONNECTION ERROR TROUBLESHOOTING GUIDE".center(50))
    print("="*50)
    
    while True:
        print("\nMain Menu:")
        print("1. Demonstration Mode (Learn with examples)")
        print("2. Trigger Error Mode (Generate raw errors)")
        print("3. Exit")
        
        mode = input("Select mode (1-3): ")
        
        if mode == '1':
            show_demo_mode()
        elif mode == '2':
            show_trigger_mode()
        elif mode == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid selection")

if __name__ == "__main__":
    main()
