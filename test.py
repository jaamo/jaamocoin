from jaamocoin import jcn

jcn.new_transaction("thebank", "jaamo", 5)
jcn.new_transaction("jaamo", "valo", 1)
jcn.new_transaction("jaamo", "mattiteppo", 10)
jcn.print()
print(jcn.get_balance("thebank"))
print(jcn.get_balance("valo"))
print(jcn.get_balance("jaamo"))
print(jcn.get_balance("mattiteppo"))