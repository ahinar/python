print('Argumentos variables')

def superheroe(alias, alter_ego,*args):    #los args corresponden a los superpoderes
	print(f'SuperHeroe: {alias}, Alter Ego: {alter_ego}, Superpoderes: {args}')
	for superpoder in args:
		print(f'\tSuperPoder: {superpoder}')
	
superheroe('Spiderman', 'Peter Parker', 'Sentido aracnido','Superfuerza')
superheroe('Ironman', 'Tony Stark', 'Armadura','Inteligencia','Dinero')
superheroe('Hulk', 'Bruce Banner', 'Fuerza','Resistencia','Inmortalidad')