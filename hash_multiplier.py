import pandas as pd
import hmac
import hashlib

salt = "0000000000000000000fa3b65e43e4240d71762a5bf397d5304b2596d116859c"
# Function to calculate hash result
def get_result(game_hash):
    hm = hmac.new(str.encode(game_hash), b'', hashlib.sha256)
    hm.update(salt.encode("utf-8"))
    h = hm.hexdigest()
    if (int(h, 16) % 33 == 0):
        return 1
    h = int(h[:13], 16)
    e = 2**52
    return int(((100 * e - h) / (e-h)) // 1)

def main():
    file_csv = "data.csv"

    df = pd.read_csv(file_csv)

    # Set the salt value

    df['hash_result'] = df['serverSeed'].apply(get_result)

    # Convert 'hash_result' to int
    df['hash_result'] = df['hash_result'].astype(int)

    # Calculate the difference between 'ticket' and 'hash_result'
    df['difference'] = df['ticket'] - df['hash_result']

    # Save the updated DataFrame back to the CSV file
    df.to_csv(file_csv, index=False)
