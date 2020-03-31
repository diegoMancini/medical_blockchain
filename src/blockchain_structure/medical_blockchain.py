import datetime
from src.blockchain_structure.block import Block


class MedicalBlockChain:

    genesis_block = Block.create_genesis_block()
    medical_block_chain = []
    #Para pruebas
    MAX_CHAIN_SIZE = 10

    def __init__(self):
        self.medical_block_chain.append(self.genesis_block)
        print(f"\n\nGenesis Block has been created!"
              f"\n\tData --> {self.medical_block_chain[0].data}"
              f"\n\tTimestamp --> {self.medical_block_chain[0].timestamp}"
              f"\n\tPrevious Hash --> {self.medical_block_chain[0].previous_block_hash}"
              f"\n\tHash --> {self.medical_block_chain[0].hash}")
        print("\n\nMedical BlockChain started.\n")

    def auto_fill_chain_for_tests(self):
        print("\n\n\n\n\n\t\t\t\t\t\t\tCreacion de blockchain para prueba de datos\n\n")
        for i in range(1, self.MAX_CHAIN_SIZE + 1):
            aux_block = Block(self.medical_block_chain[-1].hash, f"TEST DATA {i}", datetime.datetime.now())
            self.medical_block_chain.append(aux_block)
            print(f"\nBlock {i} has been created!"
                  f"\n\tData --> {self.medical_block_chain[i].data}"
                  f"\n\tTimestamp --> {self.medical_block_chain[i].timestamp}"
                  f"\n\tPrevious Hash --> {self.medical_block_chain[i].previous_block_hash}"
                  f"\n\tHash --> {self.medical_block_chain[i].hash}")

    def get_chain_information(self):
        print("\n\n\n\n\n\t\t\t\t\t\t\tRevelacion de datos de la blockchain\n\n")
        counter = 0
        aux_block = self.medical_block_chain[0]
        for block in self.medical_block_chain:
            if counter == 0:
                block_type = 'GENESIS'
                block_validation = "VALIDO"
            else:
                block_type = counter
                block_validation = block.validate_data(aux_block)

            print(f"\nBlock {block_type} information: "
                  f"\n\tData --> {block.data}"
                  f"\n\tTimestamp --> {block.timestamp}"
                  f"\n\tPrevious Hash --> {block.previous_block_hash}"
                  f"\n\tHash anterior valido --> {block_validation}"
                  f"\n\tHash --> {block.hash}")
            counter += 1
            aux_block = block