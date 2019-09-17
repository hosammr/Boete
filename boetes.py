MIN_SPEED = 60
MAX_SPEED = 100

def hoogteBoete(snelheid):
    
    if snelheid < (MIN_SPEED + 5):
        return "OK"
    elif snelheid > MAX_SPEED:
        return "Rijbewijs ingenomen"
    else:
        snelheid -= MIN_SPEED
        boete = int(snelheid / 5)
        boete = boete * 10
        return boete
        