// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title Interface for OtherToken with custom features
/// @notice Extends IERC20 with burn and freeze capabilities
interface IOtherToken /* is IERC20 */ {
    /// @notice Burns `amount` tokens from caller's balance
    function burn(uint256 amount) external;

    /// @notice Freezes `account` so it cannot transfer tokens
    function freeze(address account) external;

    /// @notice Checks if an account is frozen
    function isFrozen(address account) external view returns (bool);

    /// @dev Emitted when an account is frozen or unfrozen
    event Frozen(address indexed account, bool frozen);
}
