// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title Pausable Extension
/// @notice Adds emergency stop mechanism to smart contracts.
/// @dev Use as an abstract extension for ERC-20 or any contract.

abstract contract Pausable {
    event Paused(address account);
    event Unpaused(address account);

    bool private _paused;

    /**
     * @notice Returns true if the contract is paused, and false otherwise.
     */
    function paused() public view virtual returns (bool) {
        return _paused;
    }

    /**
     * @notice Triggers stopped state.
     * Only contract owner should call in actual implementation.
     */
    function _pause() internal virtual {
        require(!_paused, "Pausable: already paused");
        _paused = true;
        emit Paused(msg.sender);
    }

    /**
     * @notice Returns to normal state.
     * Only contract owner should call in actual implementation.
     */
    function _unpause() internal virtual {
        require(_paused, "Pausable: not paused");
        _paused = false;
        emit Unpaused(msg.sender);
    }

    /**
     * @dev Modifier to make a function callable only when the contract is not paused.
     */
    modifier whenNotPaused() {
        require(!_paused, "Pausable: paused");
        _;
    }

    /**
     * @dev Modifier to make a function callable only when the contract is paused.
     */
    modifier whenPaused() {
        require(_paused, "Pausable: not paused");
        _;
    }
}
