import sys

def main():
    """
    Script simples para somar dois números fornecidos como argumentos.
    """
    if len(sys.argv) != 3:
        print("Uso: python exemplo.py <num1> <num2>")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        soma = num1 + num2
        print(f"Resultado: {soma}")
    except ValueError:
        print("Erro: Forneça números válidos.")
        sys.exit(1)

if __name__ == "__main__":
    main()
