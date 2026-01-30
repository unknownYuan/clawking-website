require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  solidity: "0.8.19",
  networks: {
    bsc: {
      url: "https://bsc-dataseed.binance.org/",
      chainId: 56,
    },
  },
};
