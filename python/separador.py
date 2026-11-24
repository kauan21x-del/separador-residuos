print("=========================================")
print("   SEPARADOR DE RESÍDUOS - ODS 12")
print("=========================================")
print("Tipos aceitos: papel, plastico, vidro, metal, organico, eletronico")

# .strip() remove espaços extras e .lower() deixa tudo em minúsculo
residuo = input("\nInforme o resíduo que deseja descartar: ").strip().lower()

if residuo == "papel":
    print("\n[LIXEIRA AZUL - PAPEL]")
    print("Orientação: Descarte limpo e seco (caixas, folhas, jornais). Não misture papel engordurado.")
elif residuo == "plastico" or residuo == "plástico":
    print("\n[LIXEIRA VERMELHA - PLÁSTICO]")
    print("Orientação: Lave embalagens para tirar restos de alimentos antes de descartar.")
elif residuo == "vidro":
    print("\n[LIXEIRA VERDE - VIDRO]")
    print("Orientação: Descarte garrafas e potes limpos. Se estiver quebrado, embale bem para evitar acidentes.")
elif residuo == "metal":
    print("\n[LIXEIRA AMARELA - METAL]")
    print("Orientação: Latinhas e embalagens metálicas devem estar limpas e, se possível, amassadas.")
elif residuo == "organico" or residuo == "orgânico":
    print("\n[LIXEIRA MARROM - ORGÂNICO]")
    print("Orientação: Restos de alimentos e cascas podem ir para compostagem ou lixo orgânico comum.")
elif residuo == "eletronico" or residuo == "eletrônico":
    print("\n[PONTO DE COLETA ESPECIAL - ELETRÔNICO]")
    print("Orientação: Pilhas, baterias, cabos e celulares NÃO vão no lixo comum. Leve a um ecoponto.")
else:
    print("\n[ATENÇÃO]")
    print("Tipo de resíduo não reconhecido. Tente digitar: papel, plastico, vidro, metal, organico ou eletronico.")