# JaamoCoin - simple Python blockchain example

This is a very simple blockchain example written in Python.

Based on this tutorial:
https://medium.com/coinmonks/python-tutorial-build-a-blockchain-713c706f6531

I modified the code to support proof of work calculation.

You can test this in Python console:

```
python3 -i jaamocoin.py
```

And then you can start playing around:

```
jcn.new_transaction("thebank", "jaamo", 5)
jcn.new_transaction("jaamo", "valo", 1)
jcn.new_transaction("jaamo", "mattiteppo", 1)
```

You can debug what's going on in the chain anytime:

```
jcn.print()
```

And you can always check the current balance of an user by calling:

```
jcn.get_balance("jaamo")
```
