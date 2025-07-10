// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title ERC20Burnable Extension
/// @notice Enables token holders to burn their tokens, reducing total supply.
/// @dev Use as an abstract extension for ERC-20 contracts.

import "../interfaces/IERC20.sol";

abstract contract ERC20Burnable is IERC20 {
    /**
     * @notice Destroys a specific amount of tokens from the caller's account.
     * @param amount The amount of token to be burned.
     */
    function burn(uint256 amount) public virtual {
        _burn(msg.sender, amount);
    }

    /**
     * @notice Destroys a specific amount of tokens from another account, deducting from the caller’s allowance.
     * @param account The account whose tokens will be burned.
     * @param amount The amount of token to be burned.
     */
    function burnFrom(address account, uint256 amount) public virtual {
        uint256 currentAllowance = allowance(account, msg.sender);
        require(currentAllowance >= amount, "ERC20: burn amount exceeds allowance");
        _approve(account, msg.sender, currentAllowance - amount);
        _burn(account, amount);
    }

    function _burn(address account, uint256 amount) internal virtual;
    function allowance(address owner, address spender) public view virtual returns (uint256);
    function _approve(address owner, address spender, uint256 amount) internal virtual;
}
