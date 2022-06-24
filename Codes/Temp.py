from breezypythongui import EasyFrame

class TemperatureConverter(EasyFrame):

    def __init__(self):

        EasyFrame.__init__(self,title="Temperature Converter")

        # add celsius label and field of one floating point precision
        self.addLabel(text = "Celsius",row = 1, column = 0)

        self.celsius = self.addFloatField(value=0.0,row=2,column=0,precision=1)

        # add fahrenheit label and field of one floating point precision

        self.addLabel(text = "Fahrenheit",row = 1, column = 1)
        self.fahrenheit = self.addFloatField(value=32.0,row=2,column=1,precision=1)

        # add button for celius to fahrenheit with command computefahr

        self.addButton(text=">>>>",row=3,column=0,command=self.computeFahr)

        # add button for fahrenheit to celius with command computeCelsius
        self.addButton(text="<<<<",row=3,column=1,command=self.computeCelsius)

    def computeFahr(self):

        # get celsius value and compute fahrenheit and set to fahrenheit field

        c = self.celsius.getNumber()

        f = (c*9/5)+32

        self.fahrenheit.setNumber(f)

    def computeCelsius(self):

        # get fahrenheit value and compute celsius and set to celsius field

        f = self.fahrenheit.getNumber()

        c = (f-32.0)*(5/9)

        self.celsius.setNumber(c)

def main():

    t = TemperatureConverter()

    t.mainloop()

if __name__=="__main__":

    main()