class BlockChain:
    """
    The BlockChain class
    """
    def __init__(self, difficulty=5):
        self.chain = []
        self.difficulty = difficulty

    def get_last_block(self):
        return self.chain[0]

    def push_block(self, block):
        if len(self.chain) > 1:
            if block.get_preview_hash() is None:
                raise TypeError("Cannot put the next block without preview block hash information")
            if block.get_preview_hash() != self.chain[-1].get_hash():
                raise TypeError("Cannot put the next block the preview hash is valid")
        block.mine(self.difficulty)
        self.chain.append(block)
        return block

    def get_clain(self):
        for block in self.chain:
            if block is not None:
                block.analytics()
