from aplicacion.models import Libro
Libro(nombre="La casa de ceniza", autor="Abelardo Castillo", año=1968).save()
Libro(nombre="Los peligros de fumar en la cama", autor="Mariana Enriquez", año=2009).save()
Libro(nombre="La casa de los eucaliptus", autor="Luciano Lamberti", año=2017).save()
Libro(nombre="Drácula", autor="Bram Stoker", año=1897).save()
Libro(nombre="It", autor="Stephen King", año=1986).save()
Libro(nombre="Frankenstein o el moderno Prometeo", autor="Mary Shelley", año=1818).save()
print("Se cargo con éxito la lista de títulos")