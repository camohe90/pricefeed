from brownie import FundMe, MockV3Aggregator, network, config
from scripts.funciones_utiles import (
    get_account, 
    deploy_mocks, 
    LOCAL_BLOCKCHAIN_ENVIRONMENTS
    )



def main():
    account = get_account()
    deploy_details = {
        'from': account
    }

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        print(f"Mock deployed at {price_feed_address}")

    fundme = FundMe.deploy(
        price_feed_address, 
        deploy_details, 
        publish_source= config["networks"][network.show_active()].get("verify")) #para publicar el codigo en etherscan
    return fundme

