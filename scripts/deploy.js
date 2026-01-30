async function main() {
  // Get private key from environment
  const privateKey = process.env.PRIVATE_KEY;
  
  if (!privateKey) {
    console.error("❌ 请设置 PRIVATE_KEY 环境变量");
    console.log("示例: PRIVATE_KEY=0x123...456 npx hardhat run scripts/deploy.js --network bsc");
    process.exit(1);
  }

  console.log("🚀 开始部署 ClawKing...");
  
  const ClawKing = await ethers.getContractFactory("ClawKing");
  const token = await ClawKing.deploy();
  
  await token.deployed();
  
  console.log("✅ ClawKing 部署成功!");
  console.log(`📝 合约地址: ${token.address}`);
  console.log(`🔗 BSCScan: https://bscscan.com/address/${token.address}`);
  
  // 保存地址到文件
  const fs = require('fs');
  fs.writeFileSync('./deployed-address.txt', token.address);
  console.log("📁 地址已保存到 deployed-address.txt");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ 部署失败:", error);
    process.exit(1);
  });
