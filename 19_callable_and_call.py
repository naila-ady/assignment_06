"""Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies
 an input by the factor. Test it with callable() and by calling the object like a function."""


class Multiplier:                        # Ek class banayi gai jiska naam 'Multiplier' hai
    def __init__(self,factor):          # Jab object banega to yeh constructor chalega
        self.factor=factor              # Factor ko object ke andar save kar liya

    def __call__(self, value):          # Jab object ko function ki tarah call karein to yeh method chalega
        result =(self.factor * value)   # Diya gaya value aur factor multiply kiya gaya
        return result                   # Result wapas return kiya gaya

obj = Multiplier(6)                      # yahan factor ki value/argument pass kya hy
print(callable(obj))                    # Dekhta hai kya object ko call kiya ja sakta hai — hamesha True milega
print(obj(5))                           # jo value de jae gi isko factor sy multiply krky print retun de ga

class Multiplier:                        # Class banayi jo multiple values ko multiply karegi
    def __init__(self, factor):          # Constructor mein factor diya gaya
        self.factor = factor             # Factor object ke andar save kiya gaya

    def __call__(self, *args, **kwargs): # Jab object ko call karte hain, to multiple positional aur keyword arguments support honge
        results = [arg * self.factor for arg in args]  # Har input value ko factor se multiply karke list banayi

        if kwargs.get("return_as") == "sum":  # Agar keyword argument "return_as" diya gaya ho aur woh "sum" ho
            return sum(results)               # To list ka sum return karo
        return results                        # Warna poori list return karo (default)

m = Multiplier(3)                             # Object banaya jisme factor 3 hai

print(m(1, 2, 3))                      # Input values 1, 2, 3 diye gaye — multiply kar ke list return hui: [3, 6, 9]
print(m(1, 2, 3, return_as="sum"))    # Same values diye gaye, lekin return_as="sum" diya gaya — is liye sum return hua: 18
