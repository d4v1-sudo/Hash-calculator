import argparse
import hashlib

def calcular_sha256(mensagem):
    sha256 = hashlib.sha256()
    sha256.update(mensagem.encode('utf-8'))
    return sha256.hexdigest()

def calcular_blake512(mensagem):
    blake512 = hashlib.blake512()
    blake512.update(mensagem.encode('utf-8'))
    return blake512.hexdigest()

def calcular_blake2b(mensagem):
    blake2b = hashlib.blake2b()
    blake2b.update(mensagem.encode('utf-8'))
    return blake2b.hexdigest()

def verificar_hash(algoritmo, mensagem, hash_esperado):
    if algoritmo == 'sha256':
        hash_calculado = calcular_sha256(mensagem)
    elif algoritmo == 'blake512':
        hash_calculado = calcular_blake512(mensagem)
    elif algoritmo == 'blake2b':
        hash_calculado = calcular_blake2b(mensagem)
    else:
        raise ValueError("Algoritmo não suportado")

    return hash_calculado == hash_esperado

def main():
    parser = argparse.ArgumentParser(description="Calcula ou verifica hashes SHA-256, BLAKE-512 e BLAKE2b de uma mensagem.")
    parser.add_argument('-e', '--encrypt', action='store_true', help='Calcular o hash da mensagem')
    parser.add_argument('-v', '--verify', action='store_true', help='Verificar se o hash corresponde à mensagem')
    parser.add_argument('--sha256', action='store_const', dest='algoritmo', const='sha256', help='Usar SHA-256')
    parser.add_argument('--blake512', action='store_const', dest='algoritmo', const='blake512', help='Usar BLAKE-512')
    parser.add_argument('--blake2b', action='store_const', dest='algoritmo', const='blake2b', help='Usar BLAKE2b')
    parser.add_argument('mensagem', type=str, help='A mensagem para calcular ou verificar')
    parser.add_argument('hash', nargs='?', type=str, help='O hash esperado (para verificação)')

    args = parser.parse_args()

    if not args.algoritmo:
        args.algoritmo = 'sha256'
        print(f"Usando SHA-256 como algoritmo padrão.")

    if args.encrypt:
        if args.algoritmo == 'sha256':
            hash_calculado = calcular_sha256(args.mensagem)
        elif args.algoritmo == 'blake512':
            hash_calculado = calcular_blake512(args.mensagem)
        elif args.algoritmo == 'blake2b':
            hash_calculado = calcular_blake2b(args.mensagem)
        else:
            raise ValueError("Algoritmo não suportado")

        print(f"Hash {args.algoritmo.upper()} da mensagem:", hash_calculado)
    elif args.verify:
        if args.hash:
            if verificar_hash(args.algoritmo, args.mensagem, args.hash):
                print(f"O hash {args.algoritmo.upper()} corresponde à mensagem.")
            else:
                print(f"O hash {args.algoritmo.upper()} não corresponde à mensagem.")
        else:
            print("Verificação requer o hash esperado como segundo argumento.")
    else:
        print("Escolha uma opção: -e para calcular ou -v para verificar o hash.")

if __name__ == "__main__":
    main()
