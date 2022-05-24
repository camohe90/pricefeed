
from brownie import network, accounts, exceptions
from scripts.funciones_utiles import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_contract
import pytest


""" def test_deploy():
    # Arrange
    account = get_account()
    deploy_details = {
        'from': account
    }
    # Act
    fundme = fund_me = deploy_contract()
    starting_value = fundme.getVersion()
    expected = 0 # si es en local la versión es 0 si es en la red de pruebas deberia ser 4
    # Assert
    assert starting_value == expected  """

""" def test_can_fund():
    account = get_account()
    fund_me = deploy_contract()
    entrace_fee = fund_me.getEntranceFee()
    tx = fund_me.fund({"from":account, "value":entrace_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address)==entrace_fee
    tx2 = fund_me.withdraw({"from":account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address)== 0 """

def test_only_owner():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    fund_me = deploy_contract()
    bad_actor = accounts.add()
    print(bad_actor)
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})



