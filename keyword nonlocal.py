def fun():
    x = "Tony"
    def nestedfun():
        nonlocal x
        x = "Hello"
    nestedfun()
    print(x)
fun()
