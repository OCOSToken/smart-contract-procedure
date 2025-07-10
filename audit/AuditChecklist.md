# Smart Contract Audit Checklist

_A comprehensive checklist to ensure security and quality for all deployed smart contracts._

---

## General

- [ ] Contract uses SPDX license identifier and correct Solidity version.
- [ ] All external libraries (OpenZeppelin, SafeMath, etc.) are properly imported.
- [ ] Natspec documentation is present for all functions and contracts.
- [ ] Only necessary public/external functions are exposed.

---

## Functional Security

- [ ] No backdoors, hidden minting, or transfer functions.
- [ ] Ownership and administrative functions are properly restricted (`onlyOwner`, `AccessControl`).
- [ ] Token supply and balances are correctly initialized and immutable if required.
- [ ] All arithmetic uses safe math (built-in or library).
- [ ] All contract dependencies are up to date.

---

## Core Features

- [ ] Minting, burning, and pausing mechanisms are tested.
- [ ] ERC-20, ERC-721, or custom standard compliance verified.
- [ ] Modifiers (`whenNotPaused`, `onlyOwner`, etc.) are properly applied.

---

## Upgradeability

- [ ] Proxy patterns or upgradeable contracts reviewed (if used).
- [ ] Initializer functions protected against re-execution.

---

## Testing

- [ ] 100% test coverage with automated scripts (Truffle, Hardhat, Foundry, etc.)
- [ ] Manual test results documented.
- [ ] Fuzz testing and edge cases covered.

---

## Deployment

- [ ] Deployment scripts reviewed and secured.
- [ ] Mainnet contract addresses published and verified.
- [ ] Admin/owner keys securely stored and access-restricted.

---

## Documentation & Reporting

- [ ] All code and audit documents published on GitHub.
- [ ] Audit findings are tracked and resolved.
- [ ] Final public report uploaded.
