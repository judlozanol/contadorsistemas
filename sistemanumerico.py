class SistemaNumerico():
    def __init__(self):
        self.valor=0
        self.sistema=0
        self.cuenta=0
    def convertir_sistema(self):
        #Adaptado de https://gist.github.com/martinandersson82/a33d10a9fe511c4a543dc9f2394666dc#file-convert_number_system-py
        input_number=self.cuenta
        output_base=self.sistema
        input_base=10
        remainder_list = []
        sum_base_10 = 0

        if output_base == 2:
            self.valor=(bin(input_number)[2:])
        else:
            if input_base == 10:
                sum_base_10 = int(input_number)


            while sum_base_10 > 0:
                divided = sum_base_10// int(output_base)
                remainder_list.append(str(sum_base_10 % int(output_base)))
                sum_base_10 = divided

            if int(output_base) == 16:
                hex_dict = {'10' : 'a' , '11' : 'b' , '12' : 'c' , '13' : 'd' , '14' : 'e' , '15' : 'f'}
                for index, each in enumerate(remainder_list):
                    for key, value in hex_dict.items():
                        if each == key:
                            remainder_list[index] = value

            self.valor= ''.join(remainder_list[::-1])
        
    def avanzar(self):
         self.cuenta+=1
         self.convertir_sistema()

if __name__=="__main__":
        p=SistemaNumerico()
        p.cuenta=113
        p.sistema=8
    
        p.avanzar()
        print(p.valor)
        print(p.cuenta)