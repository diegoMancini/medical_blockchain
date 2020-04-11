from src.blockchain_structure.medical_blockchain import MedicalBlockChain

if __name__ == '__main__':

    test_blockchain = MedicalBlockChain()

    test_blockchain.auto_fill_chain_for_tests()
    test_blockchain.get_chain_information()
