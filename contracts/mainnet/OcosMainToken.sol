// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title OCOS Main Token Contract
/// @author OCOS Team
/// @notice This is the official OCOS mainnet token contract. Supply is fixed, no mint or burn after deployment. Full audit-compliance.
/// @custom:audit OpenZeppelin standard, reviewed for security, mainnet deployment only.

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "../extensions/Pausable.sol"; //

contract OcosMainToken is ERC20, Ownable, Pausable {
    uint256 public constant INITIAL_SUPPLY = 1_000_000_000 * 1e18; //

    /// @notice Deploys the OCOS token with full supply to the owner (deployer)
    constructor(address owner_) ERC20("OCOS Token", "OCOS") {
        _mint(owner_, INITIAL_SUPPLY);
        transferOwnership(owner_);
    }

    /// @notice Transfers tokens, but only if contract is not paused
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);
        require(!paused(), "OCOS: token transfer while paused");
    }

    // Fallback: No mint or burn after deployment!
}
