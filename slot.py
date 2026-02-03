import random
def spin():
    opt=["🍒", "🫐", "🔔", "⭐", "7️⃣" , "💣"]
    roll=[]
    for i in range(3):
        sym=random.choice(opt)
        roll.append(sym)
    return roll
def show(roll):
    print("\nSpinning..")
    print("*****************")
    print('  |  '.join(roll))
    print("*****************")

def payout(balance,bet,roll):
    if roll[0]==roll[1]==roll[2]=="💣":
        print("💥💥Uh Oh, BOMBED!💥💥")
        amt=bet*10
        print(f"You lost ${amt}, and balance is {balance-amt}")
        return balance-amt  

    elif roll[0]==roll[1]==roll[2]:
        if roll[0] in["🍒", "🫐", "🔔"]:
            print("JACKPOT!")
            amt=bet*16
        elif roll[0]=="⭐":
            print("✨ SPARKLY JACKPOT!✨")
            amt=bet*20
        elif roll[0]=="7️⃣":
            print("💲💲 ULTIMATE JACKPOT!💲💲")
            amt=bet*25
        print(f"You won ${amt}, and balance is now ${balance+amt}")
        return balance+amt

    elif roll.count("💣")==2:
        print("💥Uh Oh, BOMBED!💥")
        amt=bet*2
        print(f"You lost ${amt}, and balance is {balance-amt}")
        return balance-amt

    elif (roll[0]==roll[1]) or (roll[0]==roll[2]) or (roll[2]==roll[1]):
        print("🔪 DOUBLE SLASH!🔪")
        amt=bet*2.5
        print(f"You won ${amt}, and balance is {balance+amt}")
        balance+=amt   
        return balance
    else:
        print("Sorry you lost this round")
        return balance






def main():
    x="*******************************************"
    balance=100
    print("*********************")
    print("     Slot Machine    ")
    print("*********************")
    print("Symbols:🍒 🔔 🫐  ⭐ 7️⃣   [💣💥]")
    
    while balance>0:    
        print("Your balance: $",balance)
        bet=int(input("\nEnter your bet amount: " ))
        if bet<=0:
            print("Bet amount should be greater than zero.\n\n")
            continue
        elif bet>balance:
            print("Insufficient funds.\n\n")
            continue
        else:
            roll=spin()
            show(roll)
            balance-=bet
            balance=payout(balance,bet,roll)
        
  
        again=input("Would you like to play again? (Y/N): ").upper()
        if again!="Y":
            if balance>0:
                print(f"\n{x}")
                print(f"  Game over! Your final balance is ${balance}")
                print(x)
                print("\nThankyou for playing the slot game!")
            break
    if balance<=0:
        print(f"\n{x}")
        print(f"Game over! Balance exhausted, you're broke.")
        print(x)
        print("\nThankyou for playing the slot game!")
    
if __name__ == '__main__':
    main()