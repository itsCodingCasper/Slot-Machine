import sys

original_stdout = sys.stdout
sys.stdout = open('nul', 'w',encoding='utf-8')

from slot import payout, spin, main

def simulate_rtp():

    spins=500000
    balance=10_00_000
    bet=10
    total_returned=0
    total_bet=0

    for i in range(spins):
        before=balance
        balance-=bet
        total_bet+=bet

        roll=spin()
        balance=payout(balance,bet,roll)
        if balance > before:
            total_returned+=(balance-before)
    outcome_count = {
    "double_slash": 0,
    "triple_normal": 0,
    "triple_star": 0,
    "triple_7": 0,
    "double_bomb": 0,
    "triple_bomb": 0
    }

    outcome_return = {
        "double_slash": 0,
        "triple_normal": 0,
        "triple_star": 0,
        "triple_7": 0,
        "double_bomb": 0,
        "triple_bomb": 0
    }
   
    sys.stdout = original_stdout
    print("OUTCOME COUNTS")
    for k, v in outcome_count.items():
        print(k, ":", v)

    print("\nRTP CONTRIBUTION")
    for k, v in outcome_return.items():
        print(k, ":", round((v / total_bet) * 100, 2), "%")

    rtp = (total_returned / total_bet) *100
    print("===== RTP SIMULATION =====")
    print("Spins:", spins)
    print("Total Bet:", total_bet)
    print("Total Returned:", total_returned)
    print(f"RTP: {rtp:.2f}%")


if __name__ == '__main__':
    simulate_rtp()