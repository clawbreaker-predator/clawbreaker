import time
from clawbreaker.scanners.token_scanner import detect_new_tokens
from clawbreaker.intelligence.risk_analyzer import score_rug_risk
from clawbreaker.alerts.alert_system import send_alert

def start_engine():
    iteration = 1
    while True:
        print(f'--- Scan Iteration {iteration} ---')
        tokens = detect_new_tokens()
        for token in tokens:
            risk = score_rug_risk(token)
            print(f'[SCAN] {token} detected, rug risk: {risk}')
            if risk > 0.7:
                send_alert(token, risk)
        iteration += 1
        time.sleep(3)
