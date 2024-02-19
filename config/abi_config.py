# -*- coding: utf-8 -*-
# Time     :2024/1/20 23:28
# Author   :ym
# File     :abi_config.py
bex_abi = [
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "pool",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "receiver",
                "type": "address"
            },
            {
                "internalType": "address[]",
                "name": "assetsIn",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "amountsIn",
                "type": "uint256[]"
            }
        ],
        "name": "addLiquidity",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "shares",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "shareAmounts",
                "type": "uint256[]"
            },
            {
                "internalType": "address[]",
                "name": "liquidity",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "liquidityAmounts",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "enum IERC20DexModule.SwapKind",
                "name": "kind",
                "type": "uint8"
            },
            {
                "components": [
                    {
                        "internalType": "address",
                        "name": "poolId",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "assetIn",
                        "type": "address"
                    },
                    {
                        "internalType": "uint256",
                        "name": "amountIn",
                        "type": "uint256"
                    },
                    {
                        "internalType": "address",
                        "name": "assetOut",
                        "type": "address"
                    },
                    {
                        "internalType": "uint256",
                        "name": "amountOut",
                        "type": "uint256"
                    },
                    {
                        "internalType": "bytes",
                        "name": "userData",
                        "type": "bytes"
                    }
                ],
                "internalType": "struct IERC20DexModule.BatchSwapStep[]",
                "name": "swaps",
                "type": "tuple[]"
            },
            {
                "internalType": "uint256",
                "name": "deadline",
                "type": "uint256"
            }
        ],
        "name": "batchSwap",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "assets",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "amounts",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "name",
                "type": "string"
            },
            {
                "internalType": "address[]",
                "name": "assetsIn",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "amountsIn",
                "type": "uint256[]"
            },
            {
                "internalType": "string",
                "name": "poolType",
                "type": "string"
            },
            {
                "components": [
                    {
                        "components": [
                            {
                                "internalType": "address",
                                "name": "asset",
                                "type": "address"
                            },
                            {
                                "internalType": "uint256",
                                "name": "weight",
                                "type": "uint256"
                            }
                        ],
                        "internalType": "struct IERC20DexModule.AssetWeight[]",
                        "name": "weights",
                        "type": "tuple[]"
                    },
                    {
                        "internalType": "uint256",
                        "name": "swapFee",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct IERC20DexModule.PoolOptions",
                "name": "options",
                "type": "tuple"
            }
        ],
        "name": "createPool",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "pool",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "baseAsset",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "quoteAsset",
                "type": "address"
            }
        ],
        "name": "getExchangeRate",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "pool",
                "type": "address"
            }
        ],
        "name": "getLiquidity",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "asset",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "amounts",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "pool",
                "type": "address"
            }
        ],
        "name": "getPoolName",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "pool",
                "type": "address"
            }
        ],
        "name": "getPoolOptions",
        "outputs": [
            {
                "components": [
                    {
                        "components": [
                            {
                                "internalType": "address",
                                "name": "asset",
                                "type": "address"
                            },
                            {
                                "internalType": "uint256",
                                "name": "weight",
                                "type": "uint256"
                            }
                        ],
                        "internalType": "struct IERC20DexModule.AssetWeight[]",
                        "name": "weights",
                        "type": "tuple[]"
                    },
                    {
                        "internalType": "uint256",
                        "name": "swapFee",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct IERC20DexModule.PoolOptions",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "pool",
                "type": "address"
            },
            {
                "internalType": "address[]",
                "name": "assets",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "amounts",
                "type": "uint256[]"
            }
        ],
        "name": "getPreviewAddLiquidityNoSwap",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "shares",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "shareAmounts",
                "type": "uint256[]"
            },
            {
                "internalType": "address[]",
                "name": "liqOut",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "liquidityAmounts",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "pool",
                "type": "address"
            },
            {
                "internalType": "address[]",
                "name": "liquidity",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "amounts",
                "type": "uint256[]"
            }
        ],
        "name": "getPreviewAddLiquidityStaticPrice",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "shares",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "shareAmounts",
                "type": "uint256[]"
            },
            {
                "internalType": "address[]",
                "name": "liqOut",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "liquidityAmounts",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "enum IERC20DexModule.SwapKind",
                "name": "kind",
                "type": "uint8"
            },
            {
                "components": [
                    {
                        "internalType": "address",
                        "name": "poolId",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "assetIn",
                        "type": "address"
                    },
                    {
                        "internalType": "uint256",
                        "name": "amountIn",
                        "type": "uint256"
                    },
                    {
                        "internalType": "address",
                        "name": "assetOut",
                        "type": "address"
                    },
                    {
                        "internalType": "uint256",
                        "name": "amountOut",
                        "type": "uint256"
                    },
                    {
                        "internalType": "bytes",
                        "name": "userData",
                        "type": "bytes"
                    }
                ],
                "internalType": "struct IERC20DexModule.BatchSwapStep[]",
                "name": "swaps",
                "type": "tuple[]"
            }
        ],
        "name": "getPreviewBatchSwap",
        "outputs": [
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "pool",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "getPreviewBurnShares",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "assets",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "amounts",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "pool",
                "type": "address"
            },
            {
                "internalType": "address[]",
                "name": "assets",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "amounts",
                "type": "uint256[]"
            }
        ],
        "name": "getPreviewSharesForLiquidity",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "shares",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "shareAmounts",
                "type": "uint256[]"
            },
            {
                "internalType": "address[]",
                "name": "liquidity",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "liquidityAmounts",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "pool",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "getPreviewSharesForSingleSidedLiquidityRequest",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "assets",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "amounts",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "enum IERC20DexModule.SwapKind",
                "name": "kind",
                "type": "uint8"
            },
            {
                "internalType": "address",
                "name": "pool",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "baseAsset",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "baseAssetAmount",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "quoteAsset",
                "type": "address"
            }
        ],
        "name": "getPreviewSwapExact",
        "outputs": [
            {
                "internalType": "address",
                "name": "asset",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "pool",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "assetIn",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "assetAmount",
                "type": "uint256"
            }
        ],
        "name": "getRemoveLiquidityExactAmountOut",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "assets",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "amounts",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "pool",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "assetOut",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "sharesIn",
                "type": "uint256"
            }
        ],
        "name": "getRemoveLiquidityOneSideOut",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "assets",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "amounts",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "pool",
                "type": "address"
            }
        ],
        "name": "getTotalShares",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "assets",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "amounts",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "pool",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "withdrawAddress",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "assetIn",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amountIn",
                "type": "uint256"
            }
        ],
        "name": "removeLiquidityBurningShares",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "liquidity",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "liquidityAmounts",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "pool",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "withdrawAddress",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "assetOut",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amountOut",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "sharesIn",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "maxSharesIn",
                "type": "uint256"
            }
        ],
        "name": "removeLiquidityExactAmount",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "shares",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "shareAmounts",
                "type": "uint256[]"
            },
            {
                "internalType": "address[]",
                "name": "liquidity",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "liquidityAmounts",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "enum IERC20DexModule.SwapKind",
                "name": "kind",
                "type": "uint8"
            },
            {
                "internalType": "address",
                "name": "poolId",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "assetIn",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amountIn",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "assetOut",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amountOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "deadline",
                "type": "uint256"
            }
        ],
        "name": "swap",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "assets",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "amounts",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "payable",
        "type": "function"
    }
]

erc_20_abi = [{"type": "event", "name": "Approval", "inputs": [{"indexed": True, "name": "owner", "type": "address"},
                                                               {"indexed": True, "name": "spender", "type": "address"},
                                                               {"indexed": False, "name": "value", "type": "uint256"}]},
              {"type": "event", "name": "Transfer", "inputs": [{"indexed": True, "name": "from", "type": "address"},
                                                               {"indexed": True, "name": "to", "type": "address"},
                                                               {"indexed": False, "name": "value", "type": "uint256"}]},
              {"type": "function", "name": "allowance", "stateMutability": "view",
               "inputs": [{"name": "owner", "type": "address"}, {"name": "spender", "type": "address"}],
               "outputs": [{"name": "", "type": "uint256"}]},
              {"type": "function", "name": "approve", "stateMutability": "nonpayable",
               "inputs": [{"name": "spender", "type": "address"}, {"name": "amount", "type": "uint256"}],
               "outputs": [{"name": "", "type": "bool"}]},
              {"type": "function", "name": "balanceOf", "stateMutability": "view",
               "inputs": [{"name": "account", "type": "address"}], "outputs": [{"name": "", "type": "uint256"}]},
              {"type": "function", "name": "decimals", "stateMutability": "view", "inputs": [],
               "outputs": [{"name": "", "type": "uint8"}]},
              {"type": "function", "name": "name", "stateMutability": "view", "inputs": [],
               "outputs": [{"name": "", "type": "bytes32"}]},
              {"type": "function", "name": "symbol", "stateMutability": "view", "inputs": [],
               "outputs": [{"name": "", "type": "bytes32"}]},
              {"type": "function", "name": "totalSupply", "stateMutability": "view", "inputs": [],
               "outputs": [{"name": "", "type": "uint256"}]},
              {"type": "function", "name": "transfer", "stateMutability": "nonpayable",
               "inputs": [{"name": "recipient", "type": "address"}, {"name": "amount", "type": "uint256"}],
               "outputs": [{"name": "", "type": "bool"}]},
              {"type": "function", "name": "transferFrom", "stateMutability": "nonpayable",
               "inputs": [{"name": "sender", "type": "address"}, {"name": "recipient", "type": "address"},
                          {"name": "amount", "type": "uint256"}], "outputs": [{"name": "", "type": "bool"}]}]

honey_abi = [{"inputs": [{"internalType": "contract IERC20", "name": "_honey", "type": "address"}],
              "stateMutability": "nonpayable", "type": "constructor"}, {"inputs": [], "name": "erc20Module",
                                                                        "outputs": [
                                                                            {"internalType": "contract IERC20Module",
                                                                             "name": "", "type": "address"}],
                                                                        "stateMutability": "view", "type": "function"},
             {"inputs": [], "name": "getExchangable", "outputs": [{"components": [
                 {"internalType": "contract IERC20", "name": "collateral", "type": "address"},
                 {"internalType": "bool", "name": "enabled", "type": "bool"},
                 {"internalType": "uint256", "name": "mintRate", "type": "uint256"},
                 {"internalType": "uint256", "name": "redemptionRate", "type": "uint256"}],
                 "internalType": "struct ERC20Honey.ERC20Exchangable[]",
                 "name": "", "type": "tuple[]"}],
              "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "honey", "outputs": [
        {"internalType": "contract IERC20", "name": "", "type": "address"}], "stateMutability": "view",
                                                                     "type": "function"},
             {"inputs": [], "name": "honeyModule",
              "outputs": [{"internalType": "contract IHoneyModule", "name": "", "type": "address"}],
              "stateMutability": "view", "type": "function"}, {
                 "inputs": [{"internalType": "address", "name": "to", "type": "address"},
                            {"internalType": "contract IERC20", "name": "collateral", "type": "address"},
                            {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "mint",
                 "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                 "stateMutability": "nonpayable", "type": "function"}, {
                 "inputs": [{"internalType": "contract IERC20", "name": "collateral", "type": "address"},
                            {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "previewMint",
                 "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
                 "type": "function"}, {
                 "inputs": [{"internalType": "contract IERC20", "name": "collateral", "type": "address"},
                            {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "previewRedeem",
                 "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
                 "type": "function"}, {"inputs": [{"internalType": "address", "name": "to", "type": "address"},
                                                  {"internalType": "uint256", "name": "amount", "type": "uint256"},
                                                  {"internalType": "contract IERC20", "name": "collateral",
                                                   "type": "address"}], "name": "redeem",
                                       "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                                       "stateMutability": "nonpayable", "type": "function"}]

bend_abi = [{"inputs": [{"internalType": "contract IPoolAddressesProvider", "name": "provider", "type": "address"}],
             "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": False, "inputs": [
    {"indexed": True, "internalType": "address", "name": "reserve", "type": "address"},
    {"indexed": True, "internalType": "address", "name": "backer", "type": "address"},
    {"indexed": False, "internalType": "uint256", "name": "amount", "type": "uint256"},
    {"indexed": False, "internalType": "uint256", "name": "fee", "type": "uint256"}], "name": "BackUnbacked",
                                                                       "type": "event"}, {"anonymous": False,
                                                                                          "inputs": [{"indexed": True,
                                                                                                      "internalType": "address",
                                                                                                      "name": "reserve",
                                                                                                      "type": "address"},
                                                                                                     {"indexed": False,
                                                                                                      "internalType": "address",
                                                                                                      "name": "user",
                                                                                                      "type": "address"},
                                                                                                     {"indexed": True,
                                                                                                      "internalType": "address",
                                                                                                      "name": "onBehalfOf",
                                                                                                      "type": "address"},
                                                                                                     {"indexed": False,
                                                                                                      "internalType": "uint256",
                                                                                                      "name": "amount",
                                                                                                      "type": "uint256"},
                                                                                                     {"indexed": False,
                                                                                                      "internalType": "enum DataTypes.InterestRateMode",
                                                                                                      "name": "interestRateMode",
                                                                                                      "type": "uint8"},
                                                                                                     {"indexed": False,
                                                                                                      "internalType": "uint256",
                                                                                                      "name": "borrowRate",
                                                                                                      "type": "uint256"},
                                                                                                     {"indexed": True,
                                                                                                      "internalType": "uint16",
                                                                                                      "name": "referralCode",
                                                                                                      "type": "uint16"}],
                                                                                          "name": "Borrow",
                                                                                          "type": "event"},
            {"anonymous": False,
             "inputs": [{"indexed": True, "internalType": "address", "name": "target", "type": "address"},
                        {"indexed": False, "internalType": "address", "name": "initiator", "type": "address"},
                        {"indexed": True, "internalType": "address", "name": "asset", "type": "address"},
                        {"indexed": False, "internalType": "uint256", "name": "amount", "type": "uint256"},
                        {"indexed": False, "internalType": "enum DataTypes.InterestRateMode",
                         "name": "interestRateMode", "type": "uint8"},
                        {"indexed": False, "internalType": "uint256", "name": "premium", "type": "uint256"},
                        {"indexed": True, "internalType": "uint16", "name": "referralCode", "type": "uint16"}],
             "name": "FlashLoan", "type": "event"}, {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "asset", "type": "address"},
        {"indexed": False, "internalType": "uint256", "name": "totalDebt", "type": "uint256"}],
                                                     "name": "IsolationModeTotalDebtUpdated", "type": "event"},
            {"anonymous": False,
             "inputs": [{"indexed": True, "internalType": "address", "name": "collateralAsset", "type": "address"},
                        {"indexed": True, "internalType": "address", "name": "debtAsset", "type": "address"},
                        {"indexed": True, "internalType": "address", "name": "user", "type": "address"},
                        {"indexed": False, "internalType": "uint256", "name": "debtToCover", "type": "uint256"},
                        {"indexed": False, "internalType": "uint256", "name": "liquidatedCollateralAmount",
                         "type": "uint256"},
                        {"indexed": False, "internalType": "address", "name": "liquidator", "type": "address"},
                        {"indexed": False, "internalType": "bool", "name": "receiveAToken", "type": "bool"}],
             "name": "LiquidationCall", "type": "event"}, {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "reserve", "type": "address"},
        {"indexed": False, "internalType": "address", "name": "user", "type": "address"},
        {"indexed": True, "internalType": "address", "name": "onBehalfOf", "type": "address"},
        {"indexed": False, "internalType": "uint256", "name": "amount", "type": "uint256"},
        {"indexed": True, "internalType": "uint16", "name": "referralCode", "type": "uint16"}], "name": "MintUnbacked",
                                                           "type": "event"}, {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "reserve", "type": "address"},
        {"indexed": False, "internalType": "uint256", "name": "amountMinted", "type": "uint256"}],
                                                                              "name": "MintedToTreasury",
                                                                              "type": "event"}, {"anonymous": False,
                                                                                                 "inputs": [
                                                                                                     {"indexed": True,
                                                                                                      "internalType": "address",
                                                                                                      "name": "reserve",
                                                                                                      "type": "address"},
                                                                                                     {"indexed": True,
                                                                                                      "internalType": "address",
                                                                                                      "name": "user",
                                                                                                      "type": "address"}],
                                                                                                 "name": "RebalanceStableBorrowRate",
                                                                                                 "type": "event"},
            {"anonymous": False,
             "inputs": [{"indexed": True, "internalType": "address", "name": "reserve", "type": "address"},
                        {"indexed": True, "internalType": "address", "name": "user", "type": "address"},
                        {"indexed": True, "internalType": "address", "name": "repayer", "type": "address"},
                        {"indexed": False, "internalType": "uint256", "name": "amount", "type": "uint256"},
                        {"indexed": False, "internalType": "bool", "name": "useATokens", "type": "bool"}],
             "name": "Repay", "type": "event"}, {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "reserve", "type": "address"},
        {"indexed": False, "internalType": "uint256", "name": "liquidityRate", "type": "uint256"},
        {"indexed": False, "internalType": "uint256", "name": "stableBorrowRate", "type": "uint256"},
        {"indexed": False, "internalType": "uint256", "name": "variableBorrowRate", "type": "uint256"},
        {"indexed": False, "internalType": "uint256", "name": "liquidityIndex", "type": "uint256"},
        {"indexed": False, "internalType": "uint256", "name": "variableBorrowIndex", "type": "uint256"}],
                                                 "name": "ReserveDataUpdated", "type": "event"}, {"anonymous": False,
                                                                                                  "inputs": [
                                                                                                      {"indexed": True,
                                                                                                       "internalType": "address",
                                                                                                       "name": "reserve",
                                                                                                       "type": "address"},
                                                                                                      {"indexed": True,
                                                                                                       "internalType": "address",
                                                                                                       "name": "user",
                                                                                                       "type": "address"}],
                                                                                                  "name": "ReserveUsedAsCollateralDisabled",
                                                                                                  "type": "event"},
            {"anonymous": False,
             "inputs": [{"indexed": True, "internalType": "address", "name": "reserve", "type": "address"},
                        {"indexed": True, "internalType": "address", "name": "user", "type": "address"}],
             "name": "ReserveUsedAsCollateralEnabled", "type": "event"}, {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "reserve", "type": "address"},
        {"indexed": False, "internalType": "address", "name": "user", "type": "address"},
        {"indexed": True, "internalType": "address", "name": "onBehalfOf", "type": "address"},
        {"indexed": False, "internalType": "uint256", "name": "amount", "type": "uint256"},
        {"indexed": True, "internalType": "uint16", "name": "referralCode", "type": "uint16"}], "name": "Supply",
                                                                          "type": "event"}, {"anonymous": False,
                                                                                             "inputs": [
                                                                                                 {"indexed": True,
                                                                                                  "internalType": "address",
                                                                                                  "name": "reserve",
                                                                                                  "type": "address"},
                                                                                                 {"indexed": True,
                                                                                                  "internalType": "address",
                                                                                                  "name": "user",
                                                                                                  "type": "address"},
                                                                                                 {"indexed": False,
                                                                                                  "internalType": "enum DataTypes.InterestRateMode",
                                                                                                  "name": "interestRateMode",
                                                                                                  "type": "uint8"}],
                                                                                             "name": "SwapBorrowRateMode",
                                                                                             "type": "event"},
            {"anonymous": False,
             "inputs": [{"indexed": True, "internalType": "address", "name": "user", "type": "address"},
                        {"indexed": False, "internalType": "uint8", "name": "categoryId", "type": "uint8"}],
             "name": "UserEModeSet", "type": "event"}, {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "reserve", "type": "address"},
        {"indexed": True, "internalType": "address", "name": "user", "type": "address"},
        {"indexed": True, "internalType": "address", "name": "to", "type": "address"},
        {"indexed": False, "internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "Withdraw",
                                                        "type": "event"}, {"inputs": [], "name": "ADDRESSES_PROVIDER",
                                                                           "outputs": [{
                                                                               "internalType": "contract IPoolAddressesProvider",
                                                                               "name": "",
                                                                               "type": "address"}],
                                                                           "stateMutability": "view",
                                                                           "type": "function"},
            {"inputs": [], "name": "BRIDGE_PROTOCOL_FEE",
             "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
             "type": "function"}, {"inputs": [], "name": "FLASHLOAN_PREMIUM_TOTAL",
                                   "outputs": [{"internalType": "uint128", "name": "", "type": "uint128"}],
                                   "stateMutability": "view", "type": "function"},
            {"inputs": [], "name": "FLASHLOAN_PREMIUM_TO_PROTOCOL",
             "outputs": [{"internalType": "uint128", "name": "", "type": "uint128"}], "stateMutability": "view",
             "type": "function"}, {"inputs": [], "name": "MAX_NUMBER_RESERVES",
                                   "outputs": [{"internalType": "uint16", "name": "", "type": "uint16"}],
                                   "stateMutability": "view", "type": "function"},
            {"inputs": [], "name": "MAX_STABLE_RATE_BORROW_SIZE_PERCENT",
             "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
             "type": "function"}, {"inputs": [], "name": "POOL_REVISION",
                                   "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                                   "stateMutability": "view", "type": "function"}, {
                "inputs": [{"internalType": "address", "name": "asset", "type": "address"},
                           {"internalType": "uint256", "name": "amount", "type": "uint256"},
                           {"internalType": "uint256", "name": "fee", "type": "uint256"}], "name": "backUnbacked",
                "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                "stateMutability": "nonpayable", "type": "function"}, {
                "inputs": [{"internalType": "address", "name": "asset", "type": "address"},
                           {"internalType": "uint256", "name": "amount", "type": "uint256"},
                           {"internalType": "uint256", "name": "interestRateMode", "type": "uint256"},
                           {"internalType": "uint16", "name": "referralCode", "type": "uint16"},
                           {"internalType": "address", "name": "onBehalfOf", "type": "address"}], "name": "borrow",
                "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {
                "inputs": [{"internalType": "uint8", "name": "id", "type": "uint8"}, {
                    "components": [{"internalType": "uint16", "name": "ltv", "type": "uint16"},
                                   {"internalType": "uint16", "name": "liquidationThreshold", "type": "uint16"},
                                   {"internalType": "uint16", "name": "liquidationBonus", "type": "uint16"},
                                   {"internalType": "address", "name": "priceSource", "type": "address"},
                                   {"internalType": "string", "name": "label", "type": "string"}],
                    "internalType": "struct DataTypes.EModeCategory", "name": "category", "type": "tuple"}],
                "name": "configureEModeCategory", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {
                "inputs": [{"internalType": "address", "name": "asset", "type": "address"},
                           {"internalType": "uint256", "name": "amount", "type": "uint256"},
                           {"internalType": "address", "name": "onBehalfOf", "type": "address"},
                           {"internalType": "uint16", "name": "referralCode", "type": "uint16"}], "name": "deposit",
                "outputs": [], "stateMutability": "nonpayable", "type": "function"},
            {"inputs": [{"internalType": "address", "name": "asset", "type": "address"}], "name": "dropReserve",
             "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {
                "inputs": [{"internalType": "address", "name": "asset", "type": "address"},
                           {"internalType": "address", "name": "from", "type": "address"},
                           {"internalType": "address", "name": "to", "type": "address"},
                           {"internalType": "uint256", "name": "amount", "type": "uint256"},
                           {"internalType": "uint256", "name": "balanceFromBefore", "type": "uint256"},
                           {"internalType": "uint256", "name": "balanceToBefore", "type": "uint256"}],
                "name": "finalizeTransfer", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {
                "inputs": [{"internalType": "address", "name": "receiverAddress", "type": "address"},
                           {"internalType": "address[]", "name": "assets", "type": "address[]"},
                           {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"},
                           {"internalType": "uint256[]", "name": "interestRateModes", "type": "uint256[]"},
                           {"internalType": "address", "name": "onBehalfOf", "type": "address"},
                           {"internalType": "bytes", "name": "params", "type": "bytes"},
                           {"internalType": "uint16", "name": "referralCode", "type": "uint16"}], "name": "flashLoan",
                "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {
                "inputs": [{"internalType": "address", "name": "receiverAddress", "type": "address"},
                           {"internalType": "address", "name": "asset", "type": "address"},
                           {"internalType": "uint256", "name": "amount", "type": "uint256"},
                           {"internalType": "bytes", "name": "params", "type": "bytes"},
                           {"internalType": "uint16", "name": "referralCode", "type": "uint16"}],
                "name": "flashLoanSimple", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
            {"inputs": [{"internalType": "address", "name": "asset", "type": "address"}], "name": "getConfiguration",
             "outputs": [{"components": [{"internalType": "uint256", "name": "data", "type": "uint256"}],
                          "internalType": "struct DataTypes.ReserveConfigurationMap", "name": "", "type": "tuple"}],
             "stateMutability": "view", "type": "function"},
            {"inputs": [{"internalType": "uint8", "name": "id", "type": "uint8"}], "name": "getEModeCategoryData",
             "outputs": [{"components": [{"internalType": "uint16", "name": "ltv", "type": "uint16"},
                                         {"internalType": "uint16", "name": "liquidationThreshold", "type": "uint16"},
                                         {"internalType": "uint16", "name": "liquidationBonus", "type": "uint16"},
                                         {"internalType": "address", "name": "priceSource", "type": "address"},
                                         {"internalType": "string", "name": "label", "type": "string"}],
                          "internalType": "struct DataTypes.EModeCategory", "name": "", "type": "tuple"}],
             "stateMutability": "view", "type": "function"},
            {"inputs": [{"internalType": "uint16", "name": "id", "type": "uint16"}], "name": "getReserveAddressById",
             "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view",
             "type": "function"},
            {"inputs": [{"internalType": "address", "name": "asset", "type": "address"}], "name": "getReserveData",
             "outputs": [{"components": [
                 {"components": [{"internalType": "uint256", "name": "data", "type": "uint256"}],
                  "internalType": "struct DataTypes.ReserveConfigurationMap", "name": "configuration", "type": "tuple"},
                 {"internalType": "uint128", "name": "liquidityIndex", "type": "uint128"},
                 {"internalType": "uint128", "name": "currentLiquidityRate", "type": "uint128"},
                 {"internalType": "uint128", "name": "variableBorrowIndex", "type": "uint128"},
                 {"internalType": "uint128", "name": "currentVariableBorrowRate", "type": "uint128"},
                 {"internalType": "uint128", "name": "currentStableBorrowRate", "type": "uint128"},
                 {"internalType": "uint40", "name": "lastUpdateTimestamp", "type": "uint40"},
                 {"internalType": "uint16", "name": "id", "type": "uint16"},
                 {"internalType": "address", "name": "aTokenAddress", "type": "address"},
                 {"internalType": "address", "name": "stableDebtTokenAddress", "type": "address"},
                 {"internalType": "address", "name": "variableDebtTokenAddress", "type": "address"},
                 {"internalType": "address", "name": "interestRateStrategyAddress", "type": "address"},
                 {"internalType": "uint128", "name": "accruedToTreasury", "type": "uint128"},
                 {"internalType": "uint128", "name": "unbacked", "type": "uint128"},
                 {"internalType": "uint128", "name": "isolationModeTotalDebt", "type": "uint128"}],
                 "internalType": "struct DataTypes.ReserveData", "name": "", "type": "tuple"}],
             "stateMutability": "view", "type": "function"},
            {"inputs": [{"internalType": "address", "name": "asset", "type": "address"}],
             "name": "getReserveNormalizedIncome",
             "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
             "type": "function"}, {"inputs": [{"internalType": "address", "name": "asset", "type": "address"}],
                                   "name": "getReserveNormalizedVariableDebt",
                                   "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                                   "stateMutability": "view", "type": "function"},
            {"inputs": [], "name": "getReservesList",
             "outputs": [{"internalType": "address[]", "name": "", "type": "address[]"}], "stateMutability": "view",
             "type": "function"},
            {"inputs": [{"internalType": "address", "name": "user", "type": "address"}], "name": "getUserAccountData",
             "outputs": [{"internalType": "uint256", "name": "totalCollateralBase", "type": "uint256"},
                         {"internalType": "uint256", "name": "totalDebtBase", "type": "uint256"},
                         {"internalType": "uint256", "name": "availableBorrowsBase", "type": "uint256"},
                         {"internalType": "uint256", "name": "currentLiquidationThreshold", "type": "uint256"},
                         {"internalType": "uint256", "name": "ltv", "type": "uint256"},
                         {"internalType": "uint256", "name": "healthFactor", "type": "uint256"}],
             "stateMutability": "view", "type": "function"},
            {"inputs": [{"internalType": "address", "name": "user", "type": "address"}], "name": "getUserConfiguration",
             "outputs": [{"components": [{"internalType": "uint256", "name": "data", "type": "uint256"}],
                          "internalType": "struct DataTypes.UserConfigurationMap", "name": "", "type": "tuple"}],
             "stateMutability": "view", "type": "function"},
            {"inputs": [{"internalType": "address", "name": "user", "type": "address"}], "name": "getUserEMode",
             "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
             "type": "function"}, {"inputs": [{"internalType": "address", "name": "asset", "type": "address"},
                                              {"internalType": "address", "name": "aTokenAddress", "type": "address"},
                                              {"internalType": "address", "name": "stableDebtAddress",
                                               "type": "address"},
                                              {"internalType": "address", "name": "variableDebtAddress",
                                               "type": "address"},
                                              {"internalType": "address", "name": "interestRateStrategyAddress",
                                               "type": "address"}], "name": "initReserve", "outputs": [],
                                   "stateMutability": "nonpayable", "type": "function"},
            {"inputs": [{"internalType": "contract IPoolAddressesProvider", "name": "provider", "type": "address"}],
             "name": "initialize", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {
                "inputs": [{"internalType": "address", "name": "collateralAsset", "type": "address"},
                           {"internalType": "address", "name": "debtAsset", "type": "address"},
                           {"internalType": "address", "name": "user", "type": "address"},
                           {"internalType": "uint256", "name": "debtToCover", "type": "uint256"},
                           {"internalType": "bool", "name": "receiveAToken", "type": "bool"}],
                "name": "liquidationCall", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
            {"inputs": [{"internalType": "address[]", "name": "assets", "type": "address[]"}], "name": "mintToTreasury",
             "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {
                "inputs": [{"internalType": "address", "name": "asset", "type": "address"},
                           {"internalType": "uint256", "name": "amount", "type": "uint256"},
                           {"internalType": "address", "name": "onBehalfOf", "type": "address"},
                           {"internalType": "uint16", "name": "referralCode", "type": "uint16"}],
                "name": "mintUnbacked", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {
                "inputs": [{"internalType": "address", "name": "asset", "type": "address"},
                           {"internalType": "address", "name": "user", "type": "address"}],
                "name": "rebalanceStableBorrowRate", "outputs": [], "stateMutability": "nonpayable",
                "type": "function"}, {"inputs": [{"internalType": "address", "name": "asset", "type": "address"},
                                                 {"internalType": "uint256", "name": "amount", "type": "uint256"},
                                                 {"internalType": "uint256", "name": "interestRateMode",
                                                  "type": "uint256"},
                                                 {"internalType": "address", "name": "onBehalfOf", "type": "address"}],
                                      "name": "repay",
                                      "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                                      "stateMutability": "nonpayable", "type": "function"}, {
                "inputs": [{"internalType": "address", "name": "asset", "type": "address"},
                           {"internalType": "uint256", "name": "amount", "type": "uint256"},
                           {"internalType": "uint256", "name": "interestRateMode", "type": "uint256"}],
                "name": "repayWithATokens", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                "stateMutability": "nonpayable", "type": "function"}, {
                "inputs": [{"internalType": "address", "name": "asset", "type": "address"},
                           {"internalType": "uint256", "name": "amount", "type": "uint256"},
                           {"internalType": "uint256", "name": "interestRateMode", "type": "uint256"},
                           {"internalType": "address", "name": "onBehalfOf", "type": "address"},
                           {"internalType": "uint256", "name": "deadline", "type": "uint256"},
                           {"internalType": "uint8", "name": "permitV", "type": "uint8"},
                           {"internalType": "bytes32", "name": "permitR", "type": "bytes32"},
                           {"internalType": "bytes32", "name": "permitS", "type": "bytes32"}],
                "name": "repayWithPermit", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                "stateMutability": "nonpayable", "type": "function"}, {
                "inputs": [{"internalType": "address", "name": "token", "type": "address"},
                           {"internalType": "address", "name": "to", "type": "address"},
                           {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "rescueTokens",
                "outputs": [], "stateMutability": "nonpayable", "type": "function"},
            {"inputs": [{"internalType": "address", "name": "asset", "type": "address"}],
             "name": "resetIsolationModeTotalDebt", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
            {"inputs": [{"internalType": "address", "name": "asset", "type": "address"},
                        {"components": [{"internalType": "uint256", "name": "data", "type": "uint256"}],
                         "internalType": "struct DataTypes.ReserveConfigurationMap", "name": "configuration",
                         "type": "tuple"}], "name": "setConfiguration", "outputs": [], "stateMutability": "nonpayable",
             "type": "function"}, {"inputs": [{"internalType": "address", "name": "asset", "type": "address"},
                                              {"internalType": "address", "name": "rateStrategyAddress",
                                               "type": "address"}], "name": "setReserveInterestRateStrategyAddress",
                                   "outputs": [], "stateMutability": "nonpayable", "type": "function"},
            {"inputs": [{"internalType": "uint8", "name": "categoryId", "type": "uint8"}], "name": "setUserEMode",
             "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {
                "inputs": [{"internalType": "address", "name": "asset", "type": "address"},
                           {"internalType": "bool", "name": "useAsCollateral", "type": "bool"}],
                "name": "setUserUseReserveAsCollateral", "outputs": [], "stateMutability": "nonpayable",
                "type": "function"}, {"inputs": [{"internalType": "address", "name": "asset", "type": "address"},
                                                 {"internalType": "uint256", "name": "amount", "type": "uint256"},
                                                 {"internalType": "address", "name": "onBehalfOf", "type": "address"},
                                                 {"internalType": "uint16", "name": "referralCode", "type": "uint16"}],
                                      "name": "supply", "outputs": [], "stateMutability": "nonpayable",
                                      "type": "function"}, {
                "inputs": [{"internalType": "address", "name": "asset", "type": "address"},
                           {"internalType": "uint256", "name": "amount", "type": "uint256"},
                           {"internalType": "address", "name": "onBehalfOf", "type": "address"},
                           {"internalType": "uint16", "name": "referralCode", "type": "uint16"},
                           {"internalType": "uint256", "name": "deadline", "type": "uint256"},
                           {"internalType": "uint8", "name": "permitV", "type": "uint8"},
                           {"internalType": "bytes32", "name": "permitR", "type": "bytes32"},
                           {"internalType": "bytes32", "name": "permitS", "type": "bytes32"}],
                "name": "supplyWithPermit", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {
                "inputs": [{"internalType": "address", "name": "asset", "type": "address"},
                           {"internalType": "uint256", "name": "interestRateMode", "type": "uint256"}],
                "name": "swapBorrowRateMode", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
            {"inputs": [{"internalType": "uint256", "name": "protocolFee", "type": "uint256"}],
             "name": "updateBridgeProtocolFee", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {
                "inputs": [{"internalType": "uint128", "name": "flashLoanPremiumTotal", "type": "uint128"},
                           {"internalType": "uint128", "name": "flashLoanPremiumToProtocol", "type": "uint128"}],
                "name": "updateFlashloanPremiums", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
            {"inputs": [{"internalType": "address", "name": "asset", "type": "address"},
                        {"internalType": "uint256", "name": "amount", "type": "uint256"},
                        {"internalType": "address", "name": "to", "type": "address"}], "name": "withdraw",
             "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "nonpayable",
             "type": "function"}]

bend_borrows_abi = [{"inputs": [
    {"internalType": "contract IEACAggregatorProxy", "name": "_networkBaseTokenPriceInUsdProxyAggregator",
     "type": "address"},
    {"internalType": "contract IEACAggregatorProxy", "name": "_marketReferenceCurrencyPriceInUsdProxyAggregator",
     "type": "address"}], "stateMutability": "nonpayable", "type": "constructor"},
    {"inputs": [], "name": "ETH_CURRENCY_UNIT",
     "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
     "type": "function"}, {"inputs": [], "name": "MKR_ADDRESS",
                           "outputs": [{"internalType": "address", "name": "", "type": "address"}],
                           "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "bytes32", "name": "_bytes32", "type": "bytes32"}],
     "name": "bytes32ToString", "outputs": [{"internalType": "string", "name": "", "type": "string"}],
     "stateMutability": "pure", "type": "function"}, {"inputs": [
        {"internalType": "contract IPoolAddressesProvider", "name": "provider", "type": "address"}],
        "name": "getReservesData", "outputs": [{
            "components": [
                {
                    "internalType": "address",
                    "name": "underlyingAsset",
                    "type": "address"},
                {
                    "internalType": "string",
                    "name": "name",
                    "type": "string"},
                {
                    "internalType": "string",
                    "name": "symbol",
                    "type": "string"},
                {
                    "internalType": "uint256",
                    "name": "decimals",
                    "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "baseLTVasCollateral",
                    "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "reserveLiquidationThreshold",
                    "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "reserveLiquidationBonus",
                    "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "reserveFactor",
                    "type": "uint256"},
                {
                    "internalType": "bool",
                    "name": "usageAsCollateralEnabled",
                    "type": "bool"},
                {
                    "internalType": "bool",
                    "name": "borrowingEnabled",
                    "type": "bool"},
                {
                    "internalType": "bool",
                    "name": "stableBorrowRateEnabled",
                    "type": "bool"},
                {
                    "internalType": "bool",
                    "name": "isActive",
                    "type": "bool"},
                {
                    "internalType": "bool",
                    "name": "isFrozen",
                    "type": "bool"},
                {
                    "internalType": "uint128",
                    "name": "liquidityIndex",
                    "type": "uint128"},
                {
                    "internalType": "uint128",
                    "name": "variableBorrowIndex",
                    "type": "uint128"},
                {
                    "internalType": "uint128",
                    "name": "liquidityRate",
                    "type": "uint128"},
                {
                    "internalType": "uint128",
                    "name": "variableBorrowRate",
                    "type": "uint128"},
                {
                    "internalType": "uint128",
                    "name": "stableBorrowRate",
                    "type": "uint128"},
                {
                    "internalType": "uint40",
                    "name": "lastUpdateTimestamp",
                    "type": "uint40"},
                {
                    "internalType": "address",
                    "name": "aTokenAddress",
                    "type": "address"},
                {
                    "internalType": "address",
                    "name": "stableDebtTokenAddress",
                    "type": "address"},
                {
                    "internalType": "address",
                    "name": "variableDebtTokenAddress",
                    "type": "address"},
                {
                    "internalType": "address",
                    "name": "interestRateStrategyAddress",
                    "type": "address"},
                {
                    "internalType": "uint256",
                    "name": "availableLiquidity",
                    "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "totalPrincipalStableDebt",
                    "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "averageStableRate",
                    "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "stableDebtLastUpdateTimestamp",
                    "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "totalScaledVariableDebt",
                    "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "priceInMarketReferenceCurrency",
                    "type": "uint256"},
                {
                    "internalType": "address",
                    "name": "priceOracle",
                    "type": "address"},
                {
                    "internalType": "uint256",
                    "name": "variableRateSlope1",
                    "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "variableRateSlope2",
                    "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "stableRateSlope1",
                    "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "stableRateSlope2",
                    "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "baseStableBorrowRate",
                    "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "baseVariableBorrowRate",
                    "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "optimalUsageRatio",
                    "type": "uint256"},
                {
                    "internalType": "bool",
                    "name": "isPaused",
                    "type": "bool"},
                {
                    "internalType": "bool",
                    "name": "isSiloedBorrowing",
                    "type": "bool"},
                {
                    "internalType": "uint128",
                    "name": "accruedToTreasury",
                    "type": "uint128"},
                {
                    "internalType": "uint128",
                    "name": "unbacked",
                    "type": "uint128"},
                {
                    "internalType": "uint128",
                    "name": "isolationModeTotalDebt",
                    "type": "uint128"},
                {
                    "internalType": "bool",
                    "name": "flashLoanEnabled",
                    "type": "bool"},
                {
                    "internalType": "uint256",
                    "name": "debtCeiling",
                    "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "debtCeilingDecimals",
                    "type": "uint256"},
                {
                    "internalType": "uint8",
                    "name": "eModeCategoryId",
                    "type": "uint8"},
                {
                    "internalType": "uint256",
                    "name": "borrowCap",
                    "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "supplyCap",
                    "type": "uint256"},
                {
                    "internalType": "uint16",
                    "name": "eModeLtv",
                    "type": "uint16"},
                {
                    "internalType": "uint16",
                    "name": "eModeLiquidationThreshold",
                    "type": "uint16"},
                {
                    "internalType": "uint16",
                    "name": "eModeLiquidationBonus",
                    "type": "uint16"},
                {
                    "internalType": "address",
                    "name": "eModePriceSource",
                    "type": "address"},
                {
                    "internalType": "string",
                    "name": "eModeLabel",
                    "type": "string"},
                {
                    "internalType": "bool",
                    "name": "borrowableInIsolation",
                    "type": "bool"}],
            "internalType": "struct IUiPoolDataProviderV3.AggregatedReserveData[]",
            "name": "",
            "type": "tuple[]"},
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "marketReferenceCurrencyUnit",
                        "type": "uint256"},
                    {
                        "internalType": "int256",
                        "name": "marketReferenceCurrencyPriceInUsd",
                        "type": "int256"},
                    {
                        "internalType": "int256",
                        "name": "networkBaseTokenPriceInUsd",
                        "type": "int256"},
                    {
                        "internalType": "uint8",
                        "name": "networkBaseTokenPriceDecimals",
                        "type": "uint8"}],
                "internalType": "struct IUiPoolDataProviderV3.BaseCurrencyInfo",
                "name": "",
                "type": "tuple"}],
        "stateMutability": "view", "type": "function"}, {
        "inputs": [
            {"internalType": "contract IPoolAddressesProvider", "name": "provider", "type": "address"}],
        "name": "getReservesList",
        "outputs": [{"internalType": "address[]", "name": "", "type": "address[]"}],
        "stateMutability": "view", "type": "function"}, {"inputs": [
        {"internalType": "contract IPoolAddressesProvider", "name": "provider", "type": "address"},
        {"internalType": "address", "name": "user", "type": "address"}], "name": "getUserReservesData", "outputs": [{
        "components": [
            {
                "internalType": "address",
                "name": "underlyingAsset",
                "type": "address"},
            {
                "internalType": "uint256",
                "name": "scaledATokenBalance",
                "type": "uint256"},
            {
                "internalType": "bool",
                "name": "usageAsCollateralEnabledOnUser",
                "type": "bool"},
            {
                "internalType": "uint256",
                "name": "stableBorrowRate",
                "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "scaledVariableDebt",
                "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "principalStableDebt",
                "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "stableBorrowLastUpdateTimestamp",
                "type": "uint256"}],
        "internalType": "struct IUiPoolDataProviderV3.UserReserveData[]",
        "name": "",
        "type": "tuple[]"},
        {
            "internalType": "uint8",
            "name": "",
            "type": "uint8"}],
        "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "marketReferenceCurrencyPriceInUsdProxyAggregator",
     "outputs": [{"internalType": "contract IEACAggregatorProxy", "name": "", "type": "address"}],
     "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "networkBaseTokenPriceInUsdProxyAggregator",
     "outputs": [{"internalType": "contract IEACAggregatorProxy", "name": "", "type": "address"}],
     "stateMutability": "view", "type": "function"}]

ooga_booga_abi = [
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "allowlist_",
                "type": "bytes32"
            },
            {
                "internalType": "string",
                "name": "name_",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "symbol_",
                "type": "string"
            },
            {
                "internalType": "contract IERC20",
                "name": "paymentToken_",
                "type": "address"
            },
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "native",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "erc20",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct Ticket.MintCost",
                "name": "mintCost_",
                "type": "tuple"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [],
        "name": "AccountBalanceOverflow",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "AlreadyClaimed",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "BalanceQueryForZeroAddress",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidProof",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "NotOwnerNorApproved",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "OwnableInvalidOwner",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "OwnableUnauthorizedAccount",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "TokenAlreadyExists",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "TokenDoesNotExist",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "TransferFromIncorrectOwner",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "TransferToNonERC721ReceiverImplementer",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "TransferToZeroAddress",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "URIQueryForNonexistentToken",
        "type": "error"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "account",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "operator",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "bool",
                "name": "isApproved",
                "type": "bool"
            }
        ],
        "name": "ApprovalForAll",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "string",
                "name": "uri",
                "type": "string"
            }
        ],
        "name": "BaseURISet",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "bytes32",
                "name": "root",
                "type": "bytes32"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "index",
                "type": "uint256"
            }
        ],
        "name": "Claimed",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "bool",
                "name": "generated",
                "type": "bool"
            }
        ],
        "name": "SetGenerated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "allowlist",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "result",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "buy",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "index_",
                "type": "uint256"
            },
            {
                "internalType": "bytes32[]",
                "name": "proof_",
                "type": "bytes32[]"
            }
        ],
        "name": "claim",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "claimAmount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "index_",
                "type": "uint256"
            }
        ],
        "name": "claimed",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "getApproved",
        "outputs": [
            {
                "internalType": "address",
                "name": "result",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "name": "hasMinted",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "operator",
                "type": "address"
            }
        ],
        "name": "isApprovedForAll",
        "outputs": [
            {
                "internalType": "bool",
                "name": "result",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "isGenerated",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "mintCost",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "native",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "erc20",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "ownerOf",
        "outputs": [
            {
                "internalType": "address",
                "name": "result",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "paymentToken",
        "outputs": [
            {
                "internalType": "contract IERC20",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "realOwner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "safeTransferFrom",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "safeTransferFrom",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "allowlist_",
                "type": "bytes32"
            }
        ],
        "name": "setAllowList",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "operator",
                "type": "address"
            },
            {
                "internalType": "bool",
                "name": "isApproved",
                "type": "bool"
            }
        ],
        "name": "setApprovalForAll",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "baseURI_",
                "type": "string"
            }
        ],
        "name": "setBaseURI",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "claimAmount_",
                "type": "uint256"
            }
        ],
        "name": "setClaimAmount",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bool",
                "name": "generated_",
                "type": "bool"
            }
        ],
        "name": "setGenerated",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "native",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "erc20",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct Ticket.MintCost",
                "name": "mintCost_",
                "type": "tuple"
            }
        ],
        "name": "setMintCost",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "contract IERC20",
                "name": "paymentToken_",
                "type": "address"
            }
        ],
        "name": "setPaymentToken",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes4",
                "name": "interfaceId",
                "type": "bytes4"
            }
        ],
        "name": "supportsInterface",
        "outputs": [
            {
                "internalType": "bool",
                "name": "result",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "tokenURI",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "transferLowerOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newRealOwner",
                "type": "address"
            }
        ],
        "name": "transferRealOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "withdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "stateMutability": "payable",
        "type": "receive"
    }
]

nft_abi = [
    {
        "inputs": [
            {
                "internalType": "contract IERC20",
                "name": "paymentToken_",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "mintCost_",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [],
        "name": "AccountBalanceOverflow",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "AlreadyMinted",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "BalanceQueryForZeroAddress",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ItsOver",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "NotOwnerNorApproved",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "OwnableInvalidOwner",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "OwnableUnauthorizedAccount",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "TokenAlreadyExists",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "TokenDoesNotExist",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "TransferFromIncorrectOwner",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "TransferToNonERC721ReceiverImplementer",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "TransferToZeroAddress",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "URIQueryForNonexistentToken",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "WereSoEarly",
        "type": "error"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "account",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "operator",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "bool",
                "name": "isApproved",
                "type": "bool"
            }
        ],
        "name": "ApprovalForAll",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "string",
                "name": "uri",
                "type": "string"
            }
        ],
        "name": "BaseURISet",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "bool",
                "name": "generated",
                "type": "bool"
            }
        ],
        "name": "SetGenerated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "result",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "buy",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "endTime",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "getApproved",
        "outputs": [
            {
                "internalType": "address",
                "name": "result",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "name": "hasMinted",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "operator",
                "type": "address"
            }
        ],
        "name": "isApprovedForAll",
        "outputs": [
            {
                "internalType": "bool",
                "name": "result",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "isGenerated",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "mintAmount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "mintCost",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "ownerOf",
        "outputs": [
            {
                "internalType": "address",
                "name": "result",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "paymentToken",
        "outputs": [
            {
                "internalType": "contract IERC20",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "realOwner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "safeTransferFrom",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "safeTransferFrom",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "operator",
                "type": "address"
            },
            {
                "internalType": "bool",
                "name": "isApproved",
                "type": "bool"
            }
        ],
        "name": "setApprovalForAll",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "baseURI_",
                "type": "string"
            }
        ],
        "name": "setBaseURI",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "endTime_",
                "type": "uint256"
            }
        ],
        "name": "setEndTime",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bool",
                "name": "generated_",
                "type": "bool"
            }
        ],
        "name": "setGenerated",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "mintAmount_",
                "type": "uint256"
            }
        ],
        "name": "setMintAmount",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "mintCost_",
                "type": "uint256"
            }
        ],
        "name": "setMintCost",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "contract IERC20",
                "name": "paymentToken_",
                "type": "address"
            }
        ],
        "name": "setPaymentToken",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "startTime_",
                "type": "uint256"
            }
        ],
        "name": "setStartTime",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "startTime",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes4",
                "name": "interfaceId",
                "type": "bytes4"
            }
        ],
        "name": "supportsInterface",
        "outputs": [
            {
                "internalType": "bool",
                "name": "result",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "tokenURI",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "transferLowerOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newRealOwner",
                "type": "address"
            }
        ],
        "name": "transferRealOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "withdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "stateMutability": "payable",
        "type": "receive"
    }
]
domain_abi = [
    {
        "inputs": [
            {
                "internalType": "string[]",
                "name": "_strings",
                "type": "string[]"
            },
            {
                "internalType": "uint256",
                "name": "_uint",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "_addr1",
                "type": "address"
            },
            {
                "internalType": "string",
                "name": "_string1",
                "type": "string"
            },
            {
                "internalType": "address",
                "name": "_addr2",
                "type": "address"
            }
        ],
        "name": "mintNative",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {"type": "function", "name": "balanceOf", "stateMutability": "view",
     "inputs": [{"name": "account", "type": "address"}], "outputs": [{"name": "", "type": "uint256"}]}
]
