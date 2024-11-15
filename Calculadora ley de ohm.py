while True:
   Calculo = input("""
   1: Calculo de Resistencia
   2: Calculo de Intensidad
   3: Calculo de Voltaje
   4: Cálculo de potencia
   5: Calculo de Intensidad a partir de Potencia

   Elige una opción: """)


   if Calculo == "1":
      Voltaje = float(input("Introduzca Voltaje (V): "))
      Intensidad = float(input("Introduzca Intensidad (A): "))
      Intensidad = float(Intensidad)
      Voltaje = float(Voltaje)
      Resistencia = Voltaje / Intensidad
      print(f"Resistencia = {Resistencia}Ω")
   else:
      print("Error")

   if Calculo == "2":
      Voltaje = float(input("Introduzca Voltaje (V): "))
      Resistencia = float(input("Introduzca Resistenica (Ω): "))
      Voltaje = float(Voltaje)
      Resistencia = float(Resistencia)
      Intensidad = Voltaje / Resistencia
      print(f"Intensidad = {Intensidad}A ")

   if Calculo == "3":
      Intensidad = float(input("Introduzca Intensidad (A): "))
      Resistencia = float(input("Introduzca Resistencia (Ω): "))
      Intensidad = float(Intensidad)
      Resistencia = float(Resistencia)
      Voltaje = Intensidad * Resistencia
      print(f"Voltaje = {Voltaje}V")
   
   if Calculo == "4":
      Voltaje = float(input("Introduzca Voltaje (V): "))
      Intensidad = float(input("Introduzca Intensidad (A): "))
      Voltaje = float(Voltaje)
      Intensidad = float(Intensidad)
      Potencia = Voltaje * Intensidad
      print(f"Potencia = {Potencia}W")

   if Calculo == "5":
      Potencia = float(input("Introduzca Potencia (W): "))
      Voltaje = float(input("Introduzca Voltaje (V): "))
      Potencia = float(Potencia)
      Voltaje = float(Voltaje)
      Intensidad = Potencia / Voltaje
      print(f"Intensidad = {Intensidad}A")
