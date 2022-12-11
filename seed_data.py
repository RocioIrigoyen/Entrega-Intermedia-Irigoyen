from aplicacion.models import Libro, Pelicula, Juegos
Libro(nombre="La casa de ceniza", autor="Abelardo Castillo", año=1968).save()
Libro(nombre="Los peligros de fumar en la cama", autor="Mariana Enriquez", año=2009).save()
Libro(nombre="La casa de los eucaliptus", autor="Luciano Lamberti", año=2017).save()
Libro(nombre="Drácula", autor="Bram Stoker", año=1897).save()
Libro(nombre="It", autor="Stephen King", año=1986).save()
Libro(nombre="Frankenstein o el moderno Prometeo", autor="Mary Shelley", año=1818).save()

Pelicula(nombre="El exorcista", director="William Friedkin", año =1973).save()
Pelicula(nombre="El orfanato", director="Juan Antonio Bayona", año =2007).save()
Pelicula(nombre="La profecía", director="Richard Donner", año =1976).save()
Pelicula(nombre="Alien, el octavo pasajero", director="Ridley Scott", año =1979).save()
Pelicula(nombre="El resplandor", director="Stanley Kubrick", año =1980).save()
Pelicula(nombre="Los otros", director="Alejandro Amenábar", año =2001).save()

Juegos(nombre="Bloodborne", desarrollador="From Software", año=2015).save()
Juegos(nombre="Dead Space", desarrollador="EA Redwood Shores", año=2008).save()
Juegos(nombre="Alien: Isolation", desarrollador="Creative Assembly", año=2014).save()
Juegos(nombre="Eternal Darkness: Sanity’s Requiem", desarrollador="Silicon Knights", año=2002).save()
Juegos(nombre="Resident Evil 2", desarrollador="Capcom", año=1998).save()
Juegos(nombre="Outlast", desarrollador="Red Barrels", año=2013).save()
Juegos(nombre="Silent Hill", desarrollador="Team Silent", año=1999).save()

print("Se cargo con éxito la lista de títulos")