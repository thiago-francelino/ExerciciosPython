def exercicio1():
    inteiros=[]
    for i in range(5):
        inteiros.append(int(input('Digite um número: ')))
    for i in range(5):
        print(inteiros[i])


def exercicio2():
    a=[]
    for i in range (0,10):
        a.append(int(input('Digite um numero: ')))
    a.reverse()
    for j in range (0,10):
        print(a[j])


def exercicio3():
    notas=[]
    for i in range(4):
        notas.append(float(input(f'Digite a {i+1}° nota: ')))
    for i in range(4):
        print(notas[i])
    print(f'A média é: {sum(notas)/4}')


def exercicio4():
    caracter=[]
    temp=''
    for i in range(10):
        temp=str(input('Digite um caracter: '))
        if temp!='a' and temp!='e' and temp!= 'i' and temp!= 'o' and temp!= 'u':
            caracter.append(temp)
    for i in range(len(caracter)):
        print(f'A letra: {caracter[i]} é consoante')


def exercicio5():
    par=[]
    impar=[]
    numeros=[]
    verifica=0
    for i in range(10):
        verifica=(int(input("Digite um numero: ")))
        numeros.append(verifica)
        if verifica%2==0:
            par.append(verifica)
        else:
            impar.append(verifica)
    print('Os numeros digitados foram:')
    print(numeros)
    print('Os numeros pares são:')
    for i in range(len(par)):
        print(par[i])
    print('Os numeros impares são:')
    for i in range(len(impar)):
        print(impar[i])


def exercicio6():
    notas=[]
    media=[]
    melhores=[]
    q=0
    for i in range(0,10):
        for j in range (0,4):
            notas.append(float(input('Digite a nota: ')))
        media.append(sum(notas)/4)
        notas.clear()
    print('Essas são as medias: {} '.format(media))
    for k in range (0,10):
        if media[k]>6:
            q+=1
    print('São {} com media igual ou superior a 7'.format(q))


def exercicio7():
    vetor=[]
    add=0
    mul=1
    for i in range (0,5):
        vetor.append(int(input('Digite um valor: ')))
    add=sum(vetor)
    for k in range (0,5):
        mul=mul*vetor[k]
    print('A soma dos numeros eh: {} e a multiplicação eh: {}'.format(add, mul))


def exercicio8():
    idade=[]
    altura=[]
    k=2
    for i in range (0,2):
        idade.append(int(input('Digite a sua idade: ')))
        altura.append(float(input('Digite a sua altura: ')))
        idade.sort(reverse=True)
        altura.sort(reverse=True)
    print('idades ao conjtrario: {}'.format(idade))
    print('alturas ao contrario: {}'.format(altura))


def exercicio9():
    a=[]
    for i in range (0,3):
        a.append(pow(int(input('Digite um valor: ')),2))
    print('Estes são os valores digitados ao quadrado: {}'.format(a))


def exercicio10():
    vetor1=[]
    vetor2=[]
    vetor3=[]
    for i in range(10):
        vetor1.append(int(input('Digite um valor: ')))
        vetor2.append(int(input('Digite um valor: ')))
    for i in range(0,10):
        vetor3.append(vetor1[i])
        vetor3.append(vetor2[i])
    print(vetor3)


def exercicio11():
    a=[]
    b=[]
    d=[]
    c=[]
    for i in range(0,2):
        a.append(int(input(f'Digite o valor {i+1}: ')))
        c.append(a[i])
        b.append(int(input(f'Digite o valor {i+2}: ')))
        c.append(b[i])
        d.append(int(input(f'Digite o valor {i+3}: ')))
        c.append(d[i])
    print(c)


def exercicio12():
    altura=[]
    media=0
    abaixo=0
    menores=[]
    for i in range (0,5):
        altura.append(float(input('Digite a sua altura: ')))
    media=sum(altura)/len(altura)
    if altura[i]<media:
        abaixo+=1
        menores.append(altura[i])
    print(f'{abaixo} alunos estão abaixo da media, e os menores tem as respectivas alturas: {menores}')


def exercicio13():
    mes=[
        'Janeiro',
        'Fevereiro',
        'Março',
        'Abril',
        'Maio',
        'Junho',
        'Julho',
        'Agosto',
        'Setembro',
        'Outubro',
        'Novembro',
        'Dezembro'
    ]
    temp=[]
    media=0
    maiores=0
    local=[]
    for i in range(12):
        temp.append(float(input(f'Digite a temperatura em C°do mes {mes[i]} : ')))
    media=sum(temp)/12
    for i in range(12):
        if temp[i]>media:
            local.append(i)
            maiores+=1
    for i in range(0,len(local)):
        print(f'A temperatura acima da media foi {temp[local[i]]}, no mes {mes[local[i]]}')


def exercicio14():
    cont=0
    respostas=[]
    respostas.append(str(input('Voçê telefonou para a vítima? responda com S ou N ')))
    respostas.append(str(input('Esteve no local do crime? responda com S ou N ')))
    respostas.append(str(input('Mora perto da vítima? responda com S ou N ')))
    respostas.append(str(input('Devia para a vítima? responda com S ou N ')))
    respostas.append(str(input('Já trabalhou com a vítima? responda com S ou N ')))
    for i in range (0,5):
        if respostas[i]=='s':
            cont+=1
    if cont== 0:
        print('inocente')
        print(cont)
    elif cont== 5:
        print('Assassino')
        print(cont)
    elif cont==1:
        print('OK, esta liberado')
        print(cont)
    elif cont==2:
        print('Suspeito')
        print(cont)
    elif cont== 3 or 4:
        print('Cumplice')
        print(cont)


def exercicio15():
    veri=0
    vetor=[]
    for i in range (3):
        veri=(float(input('Digite um valor: ')))
        if veri<0:
            print('Valor nãi aceito, Digite um valor positivo: ')
        else:
            vetor.append(veri)
    print(f'Foram informados {len(vetor)} valores')
    print(f'Segue os valores informados: {vetor}')
    vetor.reverse()
    print('Segue o vetor invertido:')
    for i in range(3):
        #print(f'Segue o vetor invertido {vetor[i]}\n')
        print(vetor[i])
    print(f'a soma dos valores do vetor é: {sum(vetor)}')
    media=sum(vetor)/len(vetor)
    print(f'a media dos valores eh: {media}')
    a=0
    b=0
    acima=[]
    menores=[]
    for i in range(3):
        if vetor[i]>media:
            a+=1
            acima.append(vetor[i])
            #print(f'São {a} os valores acima da media, segue a lista: {vetor[i]}')
        if vetor[i]<7:
            b+=1
            menores.append(vetor[i])
    print(f'São {a} valores acima da media, segue os valores: {acima}')
    print(f'São {b} valores abaixo de 7, segue os valores: {menores}')
    print('O programa chegou ao fim')


def exercicio16():
    inferior=[200,300,400,500,600,700,800,900,1000]
    superior=[299,399,499,599,699,799,899,999,1099]
    salario=[]
    salariosu=[]
    for i in range(0,9):
        salario.append(200+(inferior[i]/100)*9)
    for i in range(0,9):
        salariosu.append(200+(superior[i]/100)*9)
    for i in range(0, 9):
        print(f'O vendedor que vender de R${inferior[i]} à R${superior[i]} por semana, recebera de R${salario[i]} à R${salariosu[i]} na semana respectivamente.')


def exercicio17():

    teste=[]
    me=[]
    salto=['Primeiro','Segundo','Terceiro','Quarto','Quinto']
    a=0
    print('\nAo indicar o tamanho do salto digite somente o numero sem o m pra indicar a unidade\n')
    for i in range (3):
        me.append(str(input('Digite o nome do atleta: ')))
        for j in range (1,6):
            me.append(float(input(f'Digite a distancia do {j}° salto: ')))
        teste.append(me[:])
        me.clear()
    for i in range(3):
        a=0
        for j in range(1,6):
            a=a+teste[i][j]
        teste[i].append((a/5))
    print(('-=') * 30)
    for i in range(3):
        print(f'\nAtleta: {teste[i][0]}\n')
        for j in range(0,5):
            print(f'{salto[j]} salto: {teste[i][j+1]}')
        print('\nResultado final: ')
        print('Saltos: ',end=" ")
        for j in range(1,6):
            print(teste[i][j], end=" - ")
        print(f'\nMédia dos saltos: {teste[i][6]} m\n')
        print(('-=') * 30)


def exercicio18():
    princ=[
        ['Jogador', 'Votos', '%'],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    maximo=[]
    a=0
    jogador=0
    cont=0
    maior=0
    ultimo=0
    print('Digite 0 para parar o programa, somente serão aceitos numeros entre 1 a 23')
    while True:
        jogador=(int(input('Digite o numero do jogador: ')))
        if jogador==0:
            break
        else:
            princ[jogador].append(1)
        cont += 1
    for i in range(1,24):
        princ[i].append((100*len(princ[i])/cont))
    print(f"{princ[0][0]: >2} {princ[0][1]: >7} {princ[0][2]: >10}")
    for i in range(1,24):
        ultimo = len(princ[i])
        print(f'{i: >4} {ultimo-1: >7} {princ[i][(ultimo-1)]: >20}')
    maior = len(princ[1])
    b=1
    for i in range(2, 24):
        if len(princ[i])>maior:
            maior=len(princ[i])
            b=i
    print(f'o jogador mais votado foi o: {b} com {len(princ[b])-1} votos que corresponde a {princ[b][len(princ[b])-1]}% dos votos')


def exercicio19():
    soma = 0
    a=1
    so = [['Sistema Operacional', 'Votos', '%'], ['Windows Server'], ['Unix'], ['Linux'], ['Netware'], ['Mac OS'],
          ['Outro']]
    for i in range(1, 7):
        so[i].append(int(input(f'Digite a quantidade de votos do {so[i][0]}: ')))
    for i in range(1, 7):
        soma = soma + so[i][1]
    for i in range(1, 7):
        so[i].append((100 * so[i][1]) / soma)
    print(f'\n{so[0][0]: <20}     {so[0][1]: >5}     {so[0][2]: >7}\n')
    print(('-=')*30)
    #print('\n')
    for i in range(1, 7):
        print(f'{so[i][0]: <20}     {so[i][1]: >4}     {so[i][2]: <7}', end='\n')
    print(('-=')*30)
    print(f'Total: {soma: >22}')
    maior=so[1][2]
    for i in range(2,7):
        if so[i][2]>maior:
            a=i
    print(f'\nO sistema mais votado é o {so[a][0]} com {so[a][2]}% dos votos')


def exercicio20():
    salario=[
        ['Salario','Abono']
    ]
    listaabono=[]
    soma=0
    cont=0
    tamanho=0
    interrupcao=0
    print('Para parar o programa digite 0')
    while True:
        interrupcao=(float(input('Digite o valor do salario: ')))
        if interrupcao==0:
            break
        salario.append([interrupcao])
    tamanho=int(len(salario)-1)
    for i in range(1,tamanho):
        abono=salario[i][0]*20/100
        if abono < 101:
            abono=100
            cont+=1
            listaabono.append(abono)
        else:
            listaabono.append(abono)
        #salario[i].append(abono)
        salario[i].append(abono)
    print(f'\n{salario[0][0]: <10}-{salario[0][1]}\n')
    for i in range (1,tamanho):
        print(f'R$ {salario[i][0]: <7}-R$ {salario[i][1]}')
        soma=salario[i][1]+soma
    print(f'\n{len(salario)-1} salarios foram computados')
    print(f'O valor total gasto em abono foi: {soma}')
    print(f'{cont} pessoas receberam o valor minimo de abono')
    print(f'O maior abono foi {max(listaabono)}')


def exercicio21():
    carros=[
        ['Carro','Km/litro','Litros/1000km','Valor/1000km']
    ]
    menor=0
    contador=0
    for i in range(1,6):
        carros.append([])
        carros[i].append(str(input('Digite o nome do carro: ')))
        carros[i].append(int(input('Digite o Km/Litro do carro: ')))
    for i in range(1,6):
        carros[i].append(int(1000/carros[i][1]))
        carros[i].append(int(carros[i][2]*2.25))
    print('\nRelatorio final:')
    print(f'\n{carros[0][0]: <10}{carros[0][1]: <10}{carros[0][2]: <15}{carros[0][3]: <10}\n')
    for i in range(1,6):
        print(f'{carros[i][0]: <10}{carros[i][1]: <10}Litros {carros[i][2]: <10}R$ {carros[i][3]: <10}')
    menor = carros[1][1]
    for i in range(1,6):
        if carros[i][1]>menor:
            menor=carros[i][1]
            contador=i
        else:
            menor=carros[1][1]
            contador=1
    print(f'O carro com menor consumo é o {carros[contador][0]}')


def exercicio22():
    mouses=[['Situação','Quantidade','Percentual']]
    temp=0
    esfera=0
    limpeza=0
    troca=0
    quebrado=0
    contador=0
    print('Digite 1 para: necessita da esfera')
    print('Digite 2 para: necessita de limpeza')
    print('Digite 3 para: necessita troca do cabo ou conector')
    print('Digite 4 para: quebrado ou inutilizado\n')
    while True:
        mouses.append([])
        mouses[contador].append(int(input('Digite o numero de indentificação do mouse: ')))
        temp=int(input("Digite o tipo de defeito: "))
        if temp==1:
            esfera+=1
        elif temp==2:
            limpeza+=1
        elif temp==3:
            troca+=1
        elif temp==4:
            quebrado+=1
        mouses[contador].append(temp)
        contador+=1
        temp = int(input("Quer parar? Sim=0/Não=1: "))
        if temp==0:
            break
    print(f'\nQuantidade de mouses: {contador}\n')
    print(f'{mouses[0][0]: <28}{mouses[0][1]: <10}   {mouses[0][2]}')
    print(f'1- necessita da esfera         {esfera: <10}{esfera/contador*100}%')
    print(f'2- necessita de limpeza        {limpeza: <10}{limpeza/contador*100}%')
    print(f'3- troca do cabo ou conector   {troca: <10}{troca/contador*100}%')
    print(f'4- quebrado ou inutilizado     {quebrado: <10}{quebrado/contador*100}%')


def kbprambExercicio23(a,b):
    c=a / b
    return(c)


def mediaExercicio23(a,b):
    c=a/b*100
    return(c)


def exercicio23():
    formatacao=''
    formatacao2=''
    texto=[]
    numeros=[[],[],[],[],[],[]]
    letras = [[], [], [], [], [], []]
    with open('usuarios.txt','r') as arquivo:
        mensagem= arquivo.readlines()
    for i in range(len(mensagem)):
        formatacao=mensagem[i].replace(" ","")
        formatacao2=formatacao.replace("\n","")
        texto.append(formatacao2)
    for i in range(len(texto)):
        for j in range(len(texto[i])):
            if texto[i][j]=='1' or texto[i][j]=='2' or texto[i][j]=='3' or texto[i][j]=='4' or texto[i][j]=='5' or texto[i][j]=='6' or texto[i][j]=='7' or texto[i][j]=='8' or texto[i][j]=='9' or texto[i][j]=='0':
                numeros[i].append(texto[i][j])
            else:
                letras[i].append(texto[i][j])
    vetorfinal=[]
    concatenar=''
    for i in range(6):
        vetorfinal.append([])
        for j in range(len(letras[i])):
            concatenar=concatenar+letras[i][j]
        vetorfinal[i].append(str(concatenar))
        concatenar=''
        for j in range(len(numeros[i])):
            concatenar=concatenar+numeros[i][j]
        vetorfinal[i].append(int(concatenar))
        concatenar=''
    soma=0
    for i in range(6):
        soma=soma+vetorfinal[i][1]/1048576
        #vetorfinal[i].append(vetorfinal[i][1]/1048576)
        vetorfinal[i].append(kbprambExercicio23(vetorfinal[i][1],1048576))
    for i in range(6):
        vetorfinal[i].append(mediaExercicio23(vetorfinal[i][2],soma))
    media=soma/6
    print(vetorfinal)
    with open('relatorio.txt', 'w') as saida:
        saida.write("ACME Inc.               Uso do espaco em disco pelos usuarios\n")
        saida.write(('-')*61)
        saida.write('\nNr.  Usuario        Espaco utilizado     % do uso\n')
        for i in range(6):
            saida.write(f'\n{i+1: <5}{vetorfinal[i][0]: <15}{round(vetorfinal[i][2],2): <21}{round(vetorfinal[i][3],2)}%')
        saida.write(f"\n\nEspaco total ocupado: {round(soma,2)}MB\n")
        saida.write(f"Espaco medio ocupado: {round(media,2)}MB")


def exercicio24():
    import random
    resultados=[0,[],[],[],[],[],[]]
    for i in range(100):
        dado = random.randint(1, 6)
        resultados[dado].append(1)
    print(f'O numero 1 caiu {len(resultados[1])} vezes')
    print(f'O numero 2 caiu {len(resultados[2])} vezes')
    print(f'O numero 3 caiu {len(resultados[3])} vezes')
    print(f'O numero 4 caiu {len(resultados[4])} vezes')
    print(f'O numero 5 caiu {len(resultados[5])} vezes')
    print(f'O numero 6 caiu {len(resultados[6])} vezes')