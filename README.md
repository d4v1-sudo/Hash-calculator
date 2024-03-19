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

  ```shell
  python3 script.py -e <algorithm> "<Your message here>"

- **Verify Hash**:

  ```shell
  python3 script.py -v <algorithm> "<Your message here>" "<Expected hash>"

- **Choose Algorithm**:

You can choose from the following algorithms:

- `--sha256`: SHA-256 (Default)
- `--blake512`: BLAKE-512
- `--blake2b`: BLAKE2b

## Requirements

Ensure you have the required library installed:

```bash
pip install pycryptodome==3.11.0
```

## Note

It isn't possible to decipher a hash. The reason is that a hash function is a one-way mathematical function. This means that while it's relatively easy to compute the hash of some data, it's extremely difficult (practically impossible) to reverse the process and obtain the original data from the hash. This property is essential for ensuring the security and integrity of cryptographic systems and digital signatures.

<a href="https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fd4v1-sudo%2FHash-calculator"><img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fd4v1-sudo%2FHash-calculator&label=Thanks%20for%20dropping%20in&labelColor=%23000000&countColor=%23FFFFFF" /></a>
