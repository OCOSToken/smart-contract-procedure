// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title Deutsche EUR (dEUR) Token Contract
/// @author OCOS Team
/// @notice Official OCOS Deutsche EUR (dEUR) token, fixed supply.

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DEURToken is ERC20, Ownable {
    uint256 public constant INITIAL_SUPPLY = 28_000_000_000 * 1e18; // 28 billion dEUR

    constructor(address owner_) ERC20("Deutsche EUR", "dEUR") {
        _mint(owner_, INITIAL_SUPPLY);
        transferOwnership(owner_);
    }
}
