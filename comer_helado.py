

apetece_helado_input=input("Te apetece un helado?: (si/no)").upper()
tienes_dinero_input=input("Tienes dinero?(si/no)").upper()
esta_el_señor_helados_input= input("esta el señor de los helados?").upper()
esta_tu_tia_input = input("esta tu tia?").upper()

if apetece_helado_input=="SI":
    aprtece_helado= True

elif apetece_helado_input=="NO":
    apetece_helado=False

else:
    print("te he dicho que dijeras SI o NO, no se lo que has puesto,pero lo tomare como no ")
    apetece_helado=False


apetece_helado= apetece_helado_input="SI"
puede_permitirselo=tienes_dinero_input =="SI" or esta_tu_tia_input=="SI"
esta_el_señor_helados=esta_el_señor_helados_input=="SI"

if apetece_helado and puede_permitirselo and esta_el_señor_helados :
    print("pues come helado")

else:
    print("pues nada")
