from clawbreaker.scanners.launch_detector import detect_new_tokens
from clawbreaker.intelligence.rug_classifier import score_rug_risk

def start_engine():
    print('Scanning for token activity...')
    tokens = detect_new_tokens()
    for token in tokens:
        risk = score_rug_risk(token)
        print(f'{token} rug risk score: {risk}')
