import random

fake_tokens = ['TOKEN_ALPHA','TOKEN_BETA','TOKEN_GAMMA','MEMECOIN_X','FOMO_COIN','DOGE_CLONE']

def detect_new_tokens():
    count = random.randint(1,3)
    return random.sample(fake_tokens, count)
