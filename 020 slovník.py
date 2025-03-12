vek = {"Janko" : 16, "Ferko" : 17, "Anicka" : 15}
print(f"Jankov vek je {vek['Janko']}")
print("Janko" in vek) #zisti ci sa nachadza medzi klucmi
print(15 in vek) # nespravne
print(vek)
for kluc in vek:
    print(kluc, vek[kluc])
#zvacsi kazdemu vek o 1
for kluc in vek:
    vek[kluc] += 1
print(vek)
if "Adam" in vek:
    vek["Adam"] += 1
else:
    vek["Adam"] = 19
print(vek)
print(vek.keys(), type(vek.keys()))
zoznam_klucov = list(vek.keys())
print(zoznam_klucov)
zoznam_hodnot = list(vek.values())
print(zoznam_hodnot)
zoznam_poloziek = list(vek.items())
print(zoznam_poloziek)
for v in vek.values():
    print(v)
for kluc in sorted(vek):
    print(kluc, vek[kluc])
print("počet dvojíc v slovníku:",len(vek))
#zrusenie jednej dvojice v slovniku
del vek["Janko"]
print(vek)
print(vek.get("Ferko"))
print(vek.get("Janko"))
print(vek.get("Janko", 19))


