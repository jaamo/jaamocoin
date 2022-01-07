import hashlib
import json
from time import time


#
# Very simple example of a cryptocurrency based on blockchain technology.
# 
# Based on this tutorial:
# https://medium.com/coinmonks/python-tutorial-build-a-blockchain-713c706f6531
#
class JaamoCoin(object):


    #
    # Initialize the blockchain.
    #
    def __init__(self):

        # This is the actual blockchain! 
        # Let's add a genesis block with some initial content. 
        # Also init the chain with 10 coins.
        self.chain = [
            {
                "index": 1,
                "timestamp": time(),
                "sender": "god",
                "recipient": "thebank",
                "amount": 10,
                "proof": 0,
                "previous_hash": "A single JaamoCoin is worth of 500 000 Cinelli Supercorsa bicycles.",

            }
        ]


    #
    # Adds new transaction and creates a block to the blockchain.
    #
    def new_transaction(self, sender, recipient, amount):

        if self.get_balance(sender) < amount:
            print("Can't transfer %s JCN from an account '%s'. Balance is %s." % (amount, sender, self.get_balance(sender)))
            return False

        # Create new block.
        block = {
            # Running index.
            "index": len(self.chain) + 1,
            # Add timestamp.
            "timestamp": time(),
            # Transaction details.
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
            # This is the chain part of blockchain. Calculate has from previous block.
            # If the previous block is ever altered this hash changes and the
            # whole chain will change.
            "previous_hash": self.hash(self.chain[-1]),
        }

        # Mine a proof to this block.
        block["proof"] = self.mine_proof(block)

        # Finally add our fresh new block to our blockchain!
        self.chain.append(block)


    #
    # Calculate a verification hash for a block.
    #
    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()
        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        return hex_hash


    #
    # This is the actual mining part. Try different kind of proofs
    # to find a block hash that starts with four zeros.
    #
    # This takes time to calculate (proof of work) but is also very cheap
    # to verify.
    #
    # Four zeros is not very complex to calculate 
    # but this is just an example.
    #
    def mine_proof(self, block):

        # Just run through candidates for proof.
        for x in range(10000):

            block["proof"] = x

            # Calculate block hash.
            hex_hash = self.hash(block)

            # Create binary representation of the hash 
            # and remove Python's "0b" prefix.
            bin_hash = bin(int(hex_hash, 16))[2:]

            # Leading zeros are omitted so we need to first pad the 
            # binary string with leading zeros. Then we take only
            # the first four bits from the list.
            hash_slice = bin_hash.zfill(256)[:4]

            # Check if we found what we are looking for.
            if hash_slice == "0000":
                return x

        # WTF?!! No proof found. Just return something.
        # In reality this would fuck up things in real life.
        return -1
    
    #
    # Get balance for given account. There's actually no concept 
    # of "account" in blockchain so the account balance needs to
    # be calculated by looping through the whole blockchain.
    #
    def get_balance(self, account):
        balance = 0
        for block in self.chain:
            if block["sender"] == account:
                balance = balance - block["amount"]
            if block["recipient"] == account:
                balance = balance + block["amount"]
        return balance

    #
    # Debug output.
    #
    def print(self):
        print(json.dumps(self.chain, indent=2))


# Init an object
jcn = JaamoCoin()