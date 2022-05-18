from brownie import FundMe, config
from scripts.helpful_script import get_account


def deploy_funds():

    account = get_account()

    print(account)

    fundMe = FundMe.deploy({"from": account})

    print(f"Contract deployed at {fundMe.address}")


def main():
    deploy_funds()
