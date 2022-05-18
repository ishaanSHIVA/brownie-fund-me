from brownie import FundMe, config, network, MockV3Aggregator
from scripts.helpful_script import (
    get_account,
    deployMocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_funds():

    account = get_account()

    print(network.show_active())

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        priceFeed = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deployMocks()
        priceFeed = MockV3Aggregator[-1].address

        print(f"Mocks deployed at {MockV3Aggregator[-1].address}")

    fundMe = FundMe.deploy(
        priceFeed,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    return fundMe 

    print(f"Contract deployed at {fundMe.address}")


def main():
    deploy_funds()
