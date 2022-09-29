rock = []
country = []

# Dopracowane przez mua
# Do zapisywania tytułów piosenek tak naprawdę to nie wiem na chuj to robiłem xD
def collect_songs():
  ask = "Naciśnij klawisz r(ock), c(ountry) albo q(uit) żeby wyjść."

  while True:
    song = "Wpisz tytuł piosenki"
    qenre = input(ask)
    if qenre == "q":
      break

    if qenre == "r":
      song += " rockowej: \n"
      rk = input(song)
      rock.append(rk)
    elif qenre == "c":
      song += " country: \n"
      ct = input(song)
      country.append(ct)
    else:
      print("Nieprawidłowy klawisz spróbuj r, c lub q aby wyjść")

  print("Piosenki rockowe \n" + ", ".join(rock))
  print("Piosenki country \n" + ", ".join(country))

collect_songs()