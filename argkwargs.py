def check(*args, **kwargs):
    print(args,type(args))
    print(kwargs,type(kwargs))

check(1,2,3,a=1,b=3)
def ghar(*pariwar):
    print(pariwar)

pariwar = ("baba", "mummy", "chhora/chhori")