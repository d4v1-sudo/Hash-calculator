import argparse
import hashlib
from Crypto.Hash import BLAKE2b, BLAKE2s

def calculate_sha256(message):
    sha256 = hashlib.sha256()
    sha256.update(message.encode('utf-8'))
    return sha256.hexdigest()

def calculate_blake512(message):
    blake512 = BLAKE2b.new(digest_bits=512)
    blake512.update(message.encode('utf-8'))
    return blake512.hexdigest()

def calculate_blake2b(message):
    blake2b = BLAKE2b.new(digest_bits=256)
    blake2b.update(message.encode('utf-8'))
    return blake2b.hexdigest()

def verify_hash(algorithm, message, expected_hash):
    if algorithm == 'sha256':
        calculated_hash = calculate_sha256(message)
    elif algorithm == 'blake512':
        calculated_hash = calculate_blake512(message)
    elif algorithm == 'blake2b':
        calculated_hash = calculate_blake2b(message)
    else:
        raise ValueError("Unsupported algorithm")

    return calculated_hash == expected_hash

def main():
    parser = argparse.ArgumentParser(description="Calculate or verify SHA-256, BLAKE-512, and BLAKE2b hashes of a message.")
    parser.add_argument('-e', '--encrypt', action='store_true', help='Calculate the hash of the message')
    parser.add_argument('-v', '--verify', action='store_true', help='Verify if the hash matches the message')
    parser.add_argument('--sha256', action='store_const', dest='algorithm', const='sha256', help='Use SHA-256')
    parser.add_argument('--blake512', action='store_const', dest='algorithm', const='blake512', help='Use BLAKE-512')
    parser.add_argument('--blake2b', action='store_const', dest='algorithm', const='blake2b', help='Use BLAKE2b')
    parser.add_argument('message', type=str, help='The message to calculate or verify')
    parser.add_argument('hash', nargs='?', type=str, help='The expected hash (for verification)')

    args = parser.parse_args()

    if not args.algorithm:
        print("Choose an algorithm: --sha256, --blake512, or --blake2b")
        return

    if args.encrypt:
        if args.algorithm == 'sha256':
            calculated_hash = calculate_sha256(args.message)
        elif args.algorithm == 'blake512':
            calculated_hash = calculate_blake512(args.message)
        elif args.algorithm == 'blake2b':
            calculated_hash = calculate_blake2b(args.message)
        else:
            raise ValueError("Unsupported algorithm")

        print(f"{args.algorithm.upper()} hash of the message:", calculated_hash)
    elif args.verify:
        if args.hash:
            if verify_hash(args.algorithm, args.message, args.hash):
                print(f"The {args.algorithm.upper()} hash matches the message.")
            else:
                print(f"The {args.algorithm.upper()} hash does not match the message.")
        else:
            print("Verification requires the expected hash as the second argument.")
    else:
        print("Choose an option: -e to calculate or -v to verify the hash.")

if __name__ == "__main__":
    main()
