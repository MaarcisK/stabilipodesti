garums = float(input("Kāds ir nepieciešamais podestu garums cm? "))
platums = float(input("Kāds ir nepieciešamais podestu platums cm? "))
augstums = float(input("Kāds ir nepieciešamais podestu augstums cm? "))
skaits = int(input("Kāds ir nepieciešamo podestu skaits? "))

def materialuAprekins(garums, platums, augstums, skaits):
  print("Ja vajadzīgi podesti, kas ir {:.1f} cm gari, {:.1f} cm plati un {:.1f} cm augsti un kopā jāpasūta {:.1f}.".format(garums, platums, augstums, skaits))

materialuAprekins(garums ,platums, augstums, skaits)
x = skaits * 6 #finieri
y = skaits * 8 #stūri
z = skaits * 12 #līstes
print("Tad būs nepieciešamas " + str(x) + " finieru plāksnes, " + str(y) + " stūri un " + str(z) + " līstes.")
