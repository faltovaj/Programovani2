def fceVne():
    p = "out"
    def fceUvnitr():
        nonlocal p       # p z fceVne, bez tohoto radku bere p jako lokalni promennou
        p = "in"
        print("In:", p)
    fceUvnitr()
    print("Out:", p)

fceVne()