def application():
    """Application"""
    while True:
        pass
        
def graceful_exit():
    """keyboard interrupt handled here"""
    print("KeyboardInterrupt, exit(1)")
    exit(1)
    
if __name__ == "__main__":
    try:
        application()
    except KeyboardInterrupt:
        graceful_exit()
        
