#Author : SampathKumar Medam
with open('input.txt','r') as input_file:
        a = dict()
        for sentence in input_file:
            sentence = sentence.strip()
            sentence = sentence.lower()
            words = sentence.split(" ")
            for word in words:
                if word in a:
                    a[word] = a[word] + 1
                else:
                    a[word] = 1
        with open('Output.txt','w') as output_file:            
            for key in list(a.keys()):
                print(key,":",a[key],file = output_file)
        


