# Clase práctica I: Juego que adivina un número generado de manera random

#Bucle del juego
while True: 
    
    # Configuración
    import random
    numero_secreto = random.randint(50,100)
    minimo, maximo = 50, 100
    intentos = 0
    max_intentos = 5

    # Comienzo
    print(f"\nBienvenido al juego: Adiviná el número entre {minimo} y {maximo}.\n")
    print(f"Tenés hasta {max_intentos} intentos para lograrlo\n")

    # Bucle de intentos
    while intentos < max_intentos:
        entrada = input("Ingresá tu número: ")

        # Validación
        if not entrada.isdigit():
            print("\nPor favor, escriba solo números enteros.\n")
            continue

        intento = int(entrada)
        if not minimo <= intento <= maximo:
            print(f"\nEl número debe estar entre {minimo} y {maximo}.\n")
            continue

        # Intento válido
        intentos += 1

        if intento == numero_secreto: # Adivinó
            palabra = "intento" if intentos == 1 else "intentos"
            print(f"\n¡Felicidades! Adivinaste el número en {intentos} {palabra}.\n")
            break

        if intentos < max_intentos:
            if intento < numero_secreto:
                print("\nEl número secreto es mayor.\n")
            else:
                print("\nEl número secreto es menor.\n")

            resto_int = max_intentos - intentos
            palabra2 = "intento" if resto_int == 1 else "intentos"
            palabra3 = "queda" if resto_int == 1 else "quedan"
            print(f"Te {palabra3} {resto_int} {palabra2}.\n\n")

        else:
            print(f"\nPerdiste. El número secreto era {numero_secreto}.\n")

# Reinicio del juego                    
    while True:
        reiniciar = input("\n¿Querés jugar de nuevo? (si/no): ").strip().lower()
        if reiniciar == "si":
            break
        elif reiniciar == "no":
            print("\nGracias por jugar. ¡Hasta la próxima!\n")
            exit() 
        else:
            print("\nPor favor respondé 'si' o 'no'.\n")