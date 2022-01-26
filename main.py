garums = float(input("Kāds ir nepieciešamais podestu garums cm? "))
platums = float(input("Kāds ir nepieciešamais podestu platums cm? "))
augstums = float(input("Kāds ir nepieciešamais podestu augstums cm? "))
skaits = int(input("Kāds ir nepieciešamo podestu skaits? "))

def materialuAprekins(garums, platums, augstums, skaits):
  print("Ja vajadzīgi podesti, kas ir {:.1f} cm gari, {:.1f} cm plati un {:.1f} cm augsti un kopā jāpasūta {:.1f}.".format(garums, platums, augstums, skaits))

materialuAprekins(garums ,platums, augstums, skaits)
a = skaits * 6 #finieri
b = skaits * 8 #stūri
c = skaits * 12 #līstes
print("Tad būs nepieciešamas " + str(a) + " finieru plāksnes, " + str(b) + " stūri un " + str(c) + " līstes.")
