import hashlib


class Block:
    """
    Define block new block on blockchain
    """
    def __init__(self, timestamps, transactions=None, prev_hash=None):
        if transactions is None:
            transactions = []
        if prev_hash is None:
            prev_hash = 'Genesis hash'
        self.timestamps = timestamps
        self.prev_hash = prev_hash
        self.increment = 0
        self.transactions = transactions
        self.hash = self.compute_hash()

    def get_transactions(self):
        return self.transactions

    def compute_hash(self):
        transactions = ''
        for transaction in self.transactions:
            transactions += transaction
        tmp_hash = str(self.timestamps) + self.prev_hash + transactions + str(self.increment)
        return hashlib.sha256(str.encode(tmp_hash)).hexdigest()

    def get_hash(self):
        return self.hash

    def get_preview_hash(self):
        return self.prev_hash

    def analytics(self):
        print('Transaction: ', self.transactions)
        print('Prev hash: ', self.prev_hash)
        print('Hash: ', self.hash)
        print('Timestamps: ', self.timestamps)
        print("=====")

    def mine(self, difficulty=3):
        difficulty += 1
        proof = ''
        for i in range(difficulty):
            proof += '0'

        while self.hash[0:difficulty] != proof:
            self.increment += 1
            self.hash = self.compute_hash()
            print(self.increment, self.hash)

        print("BLOCK IS MINED: ", self.transactions)
