from brownie import Contract

def main():
    #playingfundmenumber = FundMe[-1]
    playingfundmenumber= Contract('0x66342a62e5F17523b0bF5112e1Ed36be915EFCd5')
    print(f"La versión es {playingfundmenumber.getVersion()}")
    print(f"La versión es {playingfundmenumber.getPrice()}")