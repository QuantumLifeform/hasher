import requests

def get_block_hash(block_number):
    url = f"https://blockchain.info/block-height/{block_number}?format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["blocks"][0]["hash"]
    else:
        return None

def save_hashes_to_file(start_block, end_block, file_path):
    with open(file_path, "w") as file:
        for block_number in range(start_block, end_block + 1):
            block_hash = get_block_hash(block_number)
            if block_hash:
                file.write(block_hash + "\n")
            else:
                print(f"Failed to retrieve hash for block number {block_number}")

start_block = int(input("Enter start block number: "))
end_block = int(input("Enter end block number: "))
file_path = "/home/zbigniew/hashes.txt"

save_hashes_to_file(start_block, end_block, file_path)
