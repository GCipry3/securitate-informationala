import subprocess
import os

def encrypt_file(input_file, output_file, algorithm, key, iv):
    if 'aes' in algorithm.lower():
        command = f"openssl enc -{algorithm} -in {input_file} -out {output_file} -K {key} -iv {iv} -e"
    elif 'rsa' in algorithm.lower():
        command = f"openssl rsautl -encrypt -in {input_file} -out {output_file} -pubin -inkey {key}"
    subprocess.run(command, shell=True, check=True)

def decrypt_file(input_file, output_file, algorithm, key, iv=None):
    if 'aes' in algorithm.lower():
        command = f"openssl enc -{algorithm} -in {input_file} -out {output_file} -K {key} -iv {iv} -d"
    elif 'rsa' in algorithm.lower():
        command = f"openssl rsautl -decrypt -in {input_file} -out {output_file} -inkey {key}"
    subprocess.run(command, shell=True, check=True)
