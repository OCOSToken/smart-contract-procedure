// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title SafeMath Library for uint256
/// @notice Provides safe mathematical operations with overflow checks for uint256
/// @dev Since Solidity 0.8+, overflows revert by default, but custom math libraries may be required for explicit handling.

library SafeMath {
    /// @notice Returns the addition of two unsigned integers, reverts on overflow.
    /// @param a First operand
    /// @param b Second operand
    /// @return uint256 Result of a + b
    function add(uint256 a, uint256 b) internal pure returns (uint256) {
        unchecked {
            uint256 c = a + b;
            require(c >= a, "SafeMath: addition overflow");
            return c;
        }
    }

    /// @notice Returns the subtraction of two unsigned integers, reverts on underflow (when the result is negative).
    /// @param a First operand
    /// @param b Second operand
    /// @return uint256 Result of a - b
    function sub(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b <= a, "SafeMath: subtraction underflow");
        unchecked {
            return a - b;
        }
    }

    /// @notice Returns the multiplication of two unsigned integers, reverts on overflow.
    /// @param a First operand
    /// @param b Second operand
    /// @return uint256 Result of a * b
    function mul(uint256 a, uint256 b) internal pure returns (uint256) {
        if (a == 0) return 0;
        unchecked {
            uint256 c = a * b;
            require(c / a == b, "SafeMath: multiplication overflow");
            return c;
        }
    }

    /// @notice Returns the integer division of two unsigned integers, reverts on division by zero.
    /// @param a First operand
    /// @param b Second operand
    /// @return uint256 Result of a / b
    function div(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b > 0, "SafeMath: division by zero");
        unchecked {
            return a / b;
        }
    }

    /// @notice Returns the remainder of dividing two unsigned integers, reverts when dividing by zero.
    /// @param a First operand
    /// @param b Second operand
    /// @return uint256 Result of a % b
    function mod(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b > 0, "SafeMath: modulo by zero");
        unchecked {
            return a % b;
        }
    }
}
