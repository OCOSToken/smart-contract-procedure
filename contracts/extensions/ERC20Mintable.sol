// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title ERC20Mintable Extension
/// @notice Enables the contract owner (or other authorized minters) to create new tokens.
/// @dev Use as an abstract extension for ERC-20 contracts.

import "../interfaces/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

abstract contract ERC20Mintable is IERC20, Ownable {
    /**
     * @notice Mints new tokens to the specified account.
     * @param account The address that will receive the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address account, uint256 amount) public virtual onlyOwner {
        _mint(account, amount);
    }

    function _mint(address account, uint256 amount) internal virtual;
}
