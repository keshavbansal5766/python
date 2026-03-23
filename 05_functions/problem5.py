def func_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


func_kwargs(name = "keshav", surname = "Bansal", stream = "Computing")