import models

def main():
    if not any(alg['Nume'] == 'AES' for alg in models.get_algorithms()):
        models.add_algorithm("AES", "Symmetric", "Advanced Encryption Standard")
        print("Added AES algorithm to the database.")

    if not any(alg['Nume'] == 'RSA' for alg in models.get_algorithms()):
        models.add_algorithm("RSA", "Asymmetric", "Rivest–Shamir–Adleman")
        print("Added RSA algorithm to the database.")

if __name__ == "__main__":
    main()
