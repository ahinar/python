print('Argumentos variables')

def superheroe(alias, alter_ego,*args):    #los args corresponden a los superpoderes
	print(f'SuperHeroe: {alias}, Alter Ego: {alter_ego}, Superpoderes: {args}')
	
superheroe('Spiderman', 'Peter Parker', 'Sentido aracnido','Superfuerza')