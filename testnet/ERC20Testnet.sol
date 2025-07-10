// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title ERC20 Testnet Token
/// @author OCOS Team
/// @notice This contract is for testnet purposes only!
/// @dev Use on Goerli, Sepolia, BSC Testnet, Polygon Mumbai, etc.

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ERC20Testnet is ERC20, Ownable {
    uint256 public constant INITIAL_SUPPLY = 100_000_000 * 1e18; // 100 million tokens

    /// @notice Deploys a testnet ERC20 token and mints full supply to deployer (owner)
    constructor() ERC20("OCOS Test Token", "OCOS-T") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /// @notice Mint more tokens (for testnet faucet usage)
    /// @param to The address to receive minted tokens
    /// @param amount The amount to mint (in wei)
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }
}
