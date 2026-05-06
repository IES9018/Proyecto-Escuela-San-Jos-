# =============================================================================
# RUTINA LÓGICA DE EJERCICIOS
# Implementación en Python del pseudocódigo en Pseint
# Objetivo: Enseñar algoritmos, decisiones, bucles y subprocesos
# =============================================================================

def subproceso_abdominales(series: int, reps_objetivo: int):
    print("\n---- Abdominales (Crunch Básico) ----")
    posicion = input("Posición inicial (boca_arriba / boca_abajo / costado): ").strip().lower()
    
    if posicion in ["boca_abajo", "costado"]:
        print("Corrección: girar hasta quedar boca arriba.")
    
    print("Acostarse boca arriba, rodillas flexionadas, pies apoyados.")
    print("Manos en pecho o detrás de orejas (sin tirar del cuello).")
    
    dolor_lumbar = input("¿Dolor lumbar ahora? (si/no): ").strip().lower()
    if dolor_lumbar == "si":
        print("Ajuste: subir menos y apretar abdomen.")
        dolor_persiste = input("¿Sigue el dolor? (si/no): ").strip().lower()
        if dolor_persiste == "si":
            print("Detener abdominales. Recomendación: cambiar por plancha suave.")
            return
    
    for s in range(1, series + 1):
        print(f"\nSerie {s} de {series}")
        for r in range(1, reps_objetivo + 1):
            print(f"  Repetición {r} de {reps_objetivo}")
            dolor_cuello = input("  ¿Dolor de cuello o empujas con el cuello? (si/no): ").strip().lower()
            if dolor_cuello == "si":
                print("  Corrección: relajar cuello, mirar al techo, mentón separado del pecho.")
            print("  Acción: exhalar, contraer abdomen, elevar hombros, pausar 1s y bajar lento.")

def subproceso_espinales(series: int, reps_objetivo: int):
    print("\n---- Espinales (Extensión Lumbar) ----")
    posicion = input("Posición inicial (boca_abajo / boca_arriba): ").strip().lower()
    
    if posicion == "boca_arriba":
        print("Corrección: girar hasta quedar boca abajo.")
    
    print("Acostarse boca abajo, cuello neutral.")
    print("Abdomen activo suave.")
    
    dolor_lumbar = input("¿Dolor lumbar ahora? (si/no): ").strip().lower()
    if dolor_lumbar == "si":
        print("Ajuste: levantar menos (solo un poco el pecho).")
        dolor_persiste = input("¿Sigue el dolor? (si/no): ").strip().lower()
        if dolor_persiste == "si":
            print("Detener espinales.")
            return
    
    for s in range(1, series + 1):
        print(f"\nSerie {s} de {series}")
        for r in range(1, reps_objetivo + 1):
            print(f"  Repetición {r} de {reps_objetivo}")
            print("  Acción: elevar pecho, pausar 1s y bajar lento.")

def subproceso_sentadillas(series: int, reps_objetivo: int):
    print("\n---- Sentadillas ----")
    print("De pie, pies al ancho de hombros, espalda recta.")
    
    for s in range(1, series + 1):
        print(f"\nSerie {s} de {series}")
        for r in range(1, reps_objetivo + 1):
            print(f"  Repetición {r} de {reps_objetivo}")
            
            talones = input("  ¿Se levantan los talones? (si/no): ").strip().lower()
            if talones == "si":
                print("  Corrección: separar pies o bajar menos profundo.")
            
            print("  Acción: bajar cadera como sentarse, rodillas siguen pies, subir controlado.")
            
            rodillas = input("  ¿Rodillas hacia adentro? (si/no): ").strip().lower()
            if rodillas == "si":
                print("  Corrección: abrir rodillas y bajar menos.")
            
            dolor_rodilla = input("  ¿Dolor de rodilla? (si/no): ").strip().lower()
            if dolor_rodilla == "si":
                print("  Ajuste: reducir profundidad.")
                persiste = input("  ¿Sigue el dolor? (si/no): ").strip().lower()
                if persiste == "si":
                    print("  Detener sentadillas por seguridad.")
                    return

def rutina_principal():
    print("🏋️‍♂️ **RUTINA LÓGICA DE EJERCICIOS** 🏋️‍♂️\n")
    
    tiempo = int(input("Tiempo disponible (minutos): "))
    energia = input("Energía (alta/media/baja): ").strip().lower()
    dolor = input("¿Tenés dolor fuerte o lesión? (si/no): ").strip().lower()
    
    if dolor == "si":
        print("🔴 Hacer movilidad suave 5-10 min y terminar.")
        print("¡Cuidá tu cuerpo!")
        return
    
    print("🔥 Calentamiento 3 min (movilidad + caminar en el lugar).")
    
    # Decisión de modo
    if tiempo >= 20:
        modo = "completa"
        print("✅ Modo: Rutina completa")
    else:
        modo = "corta"
        print("✅ Modo: Rutina corta")
    
    # Decisión de intensidad
    if energia == "alta":
        series = 3
        reps_sent = 15
        reps_abd = 15
        reps_esp = 12
    else:
        series = 2
        reps_sent = 10
        reps_abd = 10
        reps_esp = 8
    
    print(f"📊 Series: {series} | Reps aproximadas: {reps_sent}")
    
    # Ejecutar rutina
    if modo == "completa":
        print("\n🌟 **RUTINA COMPLETA**")
    else:
        print("\n⚡ **RUTINA CORTA**")
    
    subproceso_sentadillas(series, reps_sent)
    subproceso_abdominales(series, reps_abd)
    subproceso_espinales(series, reps_esp)
    
    print("\n🧘 Enfriamiento 2 min (respirar profundo + estiramientos suaves).")
    print("\n✅ ¡Rutina completada! Recordá escuchar a tu cuerpo.")

if __name__ == "__main__":
    rutina_principal()
