const ethers = require('ethers');
const fs = require('fs');

function generateAccounts(numAccounts) {
  const accounts = [];
  const keys = [];

  for (let i = 0; i < numAccounts; i++) {
    const wallet = ethers.Wallet.createRandom();
	console.log(i,wallet.address)
    const account = [
      wallet.privateKey,
      wallet.mnemonic.phrase,
      wallet.address
    ];
    accounts.push(account)
  }

  return accounts;
}

const numAccounts = 10; // 要生成的账号数量
const accounts = generateAccounts(numAccounts);
const output = accounts.map(account => account.join(',')).join('\n');
const time = Math.round(new Date() / 1000)
fs.writeFileSync('wallet/bera_private_keys_hcy_auto_'+time+'.txt', output);
