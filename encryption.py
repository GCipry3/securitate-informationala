import subprocess
import os

def encrypt_file(input_file, output_file, algorithm, key, iv):
    command = f"openssl enc -{algorithm} -in {input_file} -out {output_file} -K {key} -iv {iv} -e"
    subprocess.run(command, shell=True, check=True)

def decrypt_file(input_file, output_file, algorithm, key, iv):
    command = f"openssl enc -{algorithm} -in {input_file} -out {output_file} -K {key} -iv {iv} -d"
    subprocess.run(command, shell=True, check=True)
