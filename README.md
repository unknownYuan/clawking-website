# 🦞 ClawKing 部署指南

## 准备

1. **新钱包**: 创建只装少量 BNB 的新钱包
2. **私钥**: 获取该钱包的私钥（用完即销毁）

## 部署步骤

```bash
cd /Users/guohaodong/.openclaw/workspace/meme-deploy

# 1. 安装依赖
npm install

# 2. 设置私钥并部署
PRIVATE_KEY=你的私钥 npx hardhat run scripts/deploy.js --network bsc
```

## 部署后

- 合约地址会显示在屏幕上
- 也会保存到 `deployed-address.txt`
- 在 BSCScan 上验证合约
- 在 PancakeSwap 创建交易对

## ⚠️ 重要

- 私钥用完立即销毁
- 只用新钱包操作
- 小额测试后再加大投入
