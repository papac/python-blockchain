from datetime import datetime
from src import Block, BlockChain, Transaction


blockchain = BlockChain.BlockChain(difficulty=4)

block1 = Block.Block(datetime.now(), ["Franck pay 20$ to John", "John pay 10$ for Game"])

blockchain.push_block(block1)

block2 = Block.Block(datetime.now(), ["Luc pay 50$ to Franck", "Marc pay 18$ for food"], block1.get_hash())

blockchain.push_block(block2)

block3 = Block.Block(datetime.now(), ["Luc pay 50$ to Franck", "Marc pay 18$ for food"], block2.get_hash())

blockchain.push_block(block3)

print("=====")
blockchain.get_clain()
