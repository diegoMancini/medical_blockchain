import datetime
from tester.block import Block

block_chain = [Block.create_genesis_block()]
print(f"\nGenesis Block has been created!"
      f"\n\tData --> {block_chain[0].data}"
      f"\n\tTimestamp --> {block_chain[0].timestamp}"
      f"\n\tHash --> {block_chain[0].hash}")

num_blocks_to_add = 10

for i in range(1, num_blocks_to_add+1):
    block_chain.append(Block(block_chain[-1], f"DATA "+str(i), datetime.datetime.now()))
    print(f"\nBlock {i} has been created!"
          f"\n\tData --> {block_chain[i].data}"
          f"\n\tTimestamp --> {block_chain[i].timestamp}"
          f"\n\tHash --> {block_chain[i].hash}")
