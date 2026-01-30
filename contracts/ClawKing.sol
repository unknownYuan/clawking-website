// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ClawKing is ERC20, Ownable {
    constructor() ERC20("ClawKing", "KING") Ownable(msg.sender) {
        // Total supply: 1 billion (1,000,000,000)
        _mint(msg.sender, 1_000_000_000 * 10**decimals());
    }

    // Function to burn tokens (anyone can burn their own)
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }
}
