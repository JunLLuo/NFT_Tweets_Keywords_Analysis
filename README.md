# NFT_tweets_keywords_analysis

Code for the paper [[arxiv](https://arxiv.org/abs/2209.07706), inproceedings]:  

Understanding NFT Price Moves through Tweets Keywords Analysis, accepted at ACM 3rd International Conference on Information Technology for Social Good (GoodIT 2023) 06-08 September 2023, Lisbon, Portugal.


# Data

To get the datasets:

Twitter data (Tweets):  Please refer to the Twitter API / Tutorials: [link](https://developer.twitter.com/en/docs/tutorials/getting-historical-tweets-using-the-full-archive-search-endpoint).

NFT transaction data:  Use Google BigQuery, put the address of the contract, for example, to get the transactions of BAYC:
```
SELECT contracts.address, contracts.is_erc721, contracts.is_erc20,
token_trs.from_address, token_trs.to_address, token_trs.value, token_trs.transaction_hash, transactions.value as transaction_value, transactions.hash, token_trs.log_index, token_trs.block_timestamp
FROM `bigquery-public-data.crypto_ethereum.contracts` AS contracts
JOIN `bigquery-public-data.crypto_ethereum.token_transfers` AS token_trs ON (token_trs.token_address = contracts.address)
JOIN `bigquery-public-data.crypto_ethereum.transactions` AS transactions ON (transactions.hash = token_trs.transaction_hash)
where contracts.address = '0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d'
ORDER BY token_trs.block_timestamp DESC
```

# Run

*The code is demonstrated by some synthetic data.

Every .py file has a runnable main function.


# Citation

Will be happy if this work is useful for your research. 
```
@inproceedings{luo_nft_goodit23,
author = {Luo, Junliang and Jia, Yongzheng and Liu, Xue},
title = {Understanding NFT Price Moves through Tweets Keywords Analysis},
year = {2023},
isbn = {9798400701160},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3582515.3609562},
doi = {10.1145/3582515.3609562},
pages = {410–418},
numpages = {9},
keywords = {NFT market analysis, Social media keywords analysis},
location = {Lisbon, Portugal},
series = {GoodIT '23}
}

```

