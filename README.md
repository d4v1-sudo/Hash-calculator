# Hash Calculator and Verifier

## Description

This Python script allows you to calculate or verify hashes using different algorithms, including SHA-256, BLAKE-512, and BLAKE2b. It provides options to calculate the hash of a message or verify if a given hash matches a message.

## Features

- **Multiple Algorithms**: Supports SHA-256, BLAKE-512, and BLAKE2b hash algorithms.
- **Hash Calculation**: Calculate the hash of a message using your chosen algorithm.
- **Hash Verification**: Verify if a hash matches a specific message.
- **Command-Line Interface**: Easy-to-use command-line interface for quick hash operations.

## Usage

You can use this script in the following ways:

- **Calculate Hash**:

python script.py -e --algorithm sha256 "Your message here"

- **Verify Hash**:

python script.py -v --algorithm sha256 "Your message here" "Expected hash"

- **Choose Algorithm**:

You can choose from the following algorithms:

- `--sha256`: SHA-256 (Default)
- `--blake512`: BLAKE-512
- `--blake2b`: BLAKE2b

## Requirements

Ensure you have the required library installed:

```bash
pip install pycryptodome==3.11.0
