# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Profitable path: tokenB->tokenA->tokenC->tokenE->tokenD->tokenC->tokenB
> Final reward: 22.592156380192314
> | token_in | amount_in | token_out | amount_out |
> | -------- | -------- | -------- | -------- |
> |  tokenB  | 5.000000 |  tokenA  | 5.666667 |
> |  tokenA  | 5.666667 |  tokenC  | 2.380000 |
> |  tokenC  | 2.380000 |  tokenE  | 1.537964 |
> |  tokenE  | 1.537964 |  tokenD  | 3.477202 |
> |  tokenD  | 3.477202 |  tokenC  | 6.739982 |
> |  tokenC  | 6.739982 |  tokenB  | 22.59216 |
> 
> *Those amount are approximation



## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> When a trade is placed in an AMM, especially for larger orders, the actual execution price may deviate. Slippage in AMM refers to this condition that expected price of a trade differs from the actual executed price. Though slippage is unavoidable, it can be minimize by setting a "slippage tolerance" in Uniswap V2. If the actual price does not fall within the tolerance, the trade will be reverted.
> Let ($x$, $y$) be the initial amount of tokenA and tokenB in a pool
> If we want to swap $dx$ to tokenB, we will get $dy=y-\frac{x\times y}{x+dx}=\frac{y\times dx}{x+dx}<\frac{y\times dx}{x}$
> This function takes into account the increase in the token A amount ($dx$), calculates the new token amounts maintaining the constant product, and derives the output amount ($dy$) considering the implied slippage.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Subtracting a minimum liquidity when initially minting liquidity in the Uniswap V2 Pair contract ensures that the pool cannot be completely drained, which prevents manipulations and zero-liquidity scenarios. This approach also helps maintain the integrity and stability of the pool by avoiding division by zero errors in smart contract computations.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> The specific formula used in the Uniswap V2 Pair contract for minting liquidity tokens after the initial deposit ensures that the liquidity tokens issued are proportional to the smallest increase in relative supply of the two tokens in the pool. This design promotes fairness and maintains the value of existing liquidity shares by preventing disproportionate token additions that could dilute the pool’s value for other liquidity providers.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> A sandwich attack is a type of front-running in decentralized finance where an attacker places transactions before and after a pending swap to profit from the resultant price slippage. This can lead to you paying more or receiving less than expected for your trade, as the attacker manipulates market prices by artificially inflating or deflating them around your transaction.

