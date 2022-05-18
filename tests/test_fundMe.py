from scripts.helpful_script import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_funds
from brownie import network, accounts, exceptions
import pytest


def testCanFundAndWithdraw():

    account = get_account()

    fundMe = deploy_funds()

    entranceFee = fundMe.getEntranceFee() + 100

    tx = fundMe.fund({"from": account, "value": entranceFee})
    tx.wait(1)
    assert fundMe.addressToAmountFunded(account.address) == entranceFee

    tx2 = fundMe.withdraw({"from": account})
    tx.wait(1)
    assert fundMe.addressToAmountFunded(account.address) == 0


def test_only_owner():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for ")

    fundMe = deploy_funds()
    badActor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fundMe.withdraw({"from": badActor})
