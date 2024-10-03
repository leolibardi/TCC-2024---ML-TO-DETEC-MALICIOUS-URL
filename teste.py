from pydub import AudioSegment
from pydub.playback import play

print("Calculadora do Rafael - Macaquice ao extremo")
print("1: Soma \n 2: Multiplicação \n 3: Divisão ")
num = input("Insira qual modalidade de conta: ")

match num:
    case "1":
        num1 = int(input("Insira a primeira variavel: "))
        num2 = int(input("Insira a segunda variavel: "))
        soma = num1 + num2
        print(f'A soma é: {soma}')
        if soma == 13:
            print("sai petista do caralho preto")
        
        elif soma == 22:
            print("vota vota e confirma 22 é bolsonaro")
            audio = AudioSegment.from_file('musica.mp3', format='mp3')
            play(audio)
            

    case "2":
        num1 = int(input("Insira a primeira variavel: "))
        num2 = int(input("Insira a segunda variavel: "))
        multi = num1 * num2
        print(f'A multi é: {multi}')


    case "3":
        num1 = int(input("Insira a primeira variavel: "))
        num2 = int(input("Insira a segunda variavel: "))
        div = num1 / num2
        print(f'A div é: {div}')


    case _:
        print("o seu animal, tem que ser um dos tres! pau no cu!")