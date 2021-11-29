import hashlib

class EduCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        self.block_data = "-".join(transaction_list) + "_" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

cert1 = "rohit brala. BE"

initial_block= EduCoinBlock("Initial String",[cert1])

print(initial_block.block_data)
print(initial_block.block_hash)

cert2 = "Sujay. Btech"
second_block= EduCoinBlock(initial_block.block_hash,[cert2])

print(second_block.block_data)
print(second_block.block_hash)
