
from core import Block, BlockChain


blockchain = BlockChain.BlockChain(difficulty=3)

block1 = Block.Block(["Franck pay 20$ to John", "John pay 10$ for Game"])

blockchain.push_block(block1)

block2 = Block.Block(["Luc pay 50$ to Franck", "Marc pay 18$ for food"], block1.get_hash())

blockchain.push_block(block2)

block3 = Block.Block(["Luc pay 50$ to Franck", "Marc pay 18$ for food"], block2.get_hash())

blockchain.push_block(block3)

print("=====")
blockchain.get_clain()
