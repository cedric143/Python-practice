class Magari:
    def __init__(self,make, model, year):
        self.mymake=make
        self.mymodel=model
        self.myyear=year
    def kuanzisah(self):
        print(f"{self.mymake} {self.mymodel} {self.myyear} started")
class Toyota(Magari):
    def __init__(self,make,model,year,num_doors):
        super().__init__(make,model,year)
        self.mynum_doors=num_doors

    def kuanzisah(self):
        print(f"{self.mymake}{self.mymodel} car with {self.mynum_doors} cc started)

Toyota=Toyota("harrier","hybrid","2022","4")
Toyota.kuanzisah()