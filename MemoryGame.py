# Importando bibliotecas
import random
import math
import numpy as np

# Definição de variáveis e listas
order = ["first", "second", "third", "fourth", "fifth"]
random_list = []
times = 5
times = times + 1 


# Gerando número aleatório
for i in range(1, times):
    random_list.append(random.randint(1,9))

    # FIXME: Verificando muitas repetições (opcional)
    """if i >= 3:
        if random_list[i] == random_list[i-1] and random_list[i-1] == random_list[i-2]:
            random_list[i-1] = random.randint(1,9)"""

    print("Numbers: {0}".format(random_list))

    answer = []


    # Analisando as respostas 
    for j in range(0, i):
        oneAnswer = (int(input("What were the {0} number? ".format(order[j]))))
        answer.append(oneAnswer)
        print(random_list)
        print(answer)

        if oneAnswer == random_list[j]:
            print("Good job!")

        else:
            #TODO: 
            #   - Toda vez que errar, o som fica mais alto, mas por enquanto vamos com isso mesmo
            print("Try again!")
            oneAnswer = (input("What were the {0} number? ".format(order[j-1])))

            if oneAnswer != random_list[j]:
                print("That's not good")
                breakpoint