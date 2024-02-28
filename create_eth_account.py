from eth_account import Account
from mnemonic import Mnemonic
import os
import time

# 启用未经审核的HD钱包功能
Account.enable_unaudited_hdwallet_features()


def generate_accounts(_num_accounts):
    _accounts = []
    mnemo = Mnemonic("english")

    for i in range(_num_accounts):
        mnemonic = mnemo.generate(strength=128)
        wallet = Account.from_mnemonic(mnemonic)
        print(i, wallet.address)
        _accounts.append((
            wallet.key.hex(),  # 注意这里使用 `key` 而不是 `privateKey`
            mnemonic,
            wallet.address,
        ))

    return _accounts


def main_generate_accounts(_num_accounts):
    accounts = generate_accounts(_num_accounts)
    output = '\n'.join([','.join(account) for account in accounts])
    # 确保存储文件的文件夹存在
    os.makedirs('wallet', exist_ok=True)
    time_stamp = int(time.time())
    filename = f'wallet/bera_private_keys_hcy_auto_{time_stamp}.txt'
    with open(filename, 'w') as f:
        f.write(output)


if __name__ == '__main__':
    _num_accounts = 1500
    main_generate_accounts(_num_accounts)
