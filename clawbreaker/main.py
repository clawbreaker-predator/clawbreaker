import time
from clawbreaker.core.engine import start_engine

def dashboard():
    print("="*50)
    print("🚀 CLAWBREAKER TERMINAL DASHBOARD 🚀")
    print("="*50)
    print("Status: Initializing modules...")
    time.sleep(1)
    print("Scanners: ONLINE")
    print("Intelligence: ONLINE")
    print("Strategies: ONLINE")
    print("Execution: STANDBY")
    print("Alerts: ONLINE")
    print("="*50)
    print("Press Ctrl+C to exit")
    print("\nLaunching live monitoring...\n")
    time.sleep(1)
    start_engine()

if __name__ == "__main__":
    dashboard()
