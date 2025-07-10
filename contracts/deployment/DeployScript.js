// SPDX-License-Identifier: MIT
/**
 * @file DeployScript.js
 * @description Script for deploying the OCOS Main Token contract to any network using Hardhat.
 * @author OCOS Team
 */

const { ethers } = require("hardhat");

async function main() {
  // Retrieve the deployer account
  const [deployer] = await ethers.getSigners();
  console.log("Deploying contract with account:", deployer.address);

  // Compile and get contract factory
  const OcosMainToken = await ethers.getContractFactory("OcosMainToken");

  // Deploy the contract, passing the owner address (deployer)
  const token = await OcosMainToken.deploy(deployer.address);

  // Wait for deployment to finish
  await token.deployed();

  // Output the deployed contract address
  console.log("OCOS Main Token deployed to:", token.address);
}

// Run the deployment script
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
