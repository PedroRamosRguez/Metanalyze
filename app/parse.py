import tarfile,re
import numpy as np
def parseFiles(tar,i,dicAlg,member,getConfiguration):
	print 'entre... y esto es member'
	print member
	for j,file in enumerate(member):
		print j
		print file
		f = tar.extractfile(file)
		print f
		print f.name
		dicAlg[str(i)][str(j)] = dict()	#crea el diccionario por ejecuciones dentro del algoritmo actual
		print dicAlg.keys()
		print dicAlg
		for k,line in enumerate(f.readlines()):
			print 'esto es line:'
			print line
			if re.search('^[#]?\s*\w+\s*\d+\n+',line):
				step = re.sub('^[#]?\s*[a-zA-Z]+\s*','',str(line)).rstrip()
				if not step in dicAlg[str(i)][str(j)].keys():
					print 'la clave del paso no existe...'
					print 'esto es step:%s'%step
					#print 'claves:'
					#print dicAlg[str(i)][str(j)].keys()
					dicAlg[str(i)][str(j)][step]=[]
				#se detecta que el paso venga dado de la manera 200(200)\n,200 (200)\n y se elimina la parte del parentesis
			elif re.search('^\d+\s*\(\d+\)\n+',line):
				print 'esto lee el paso...'
				step = re.sub('\(\d+\)\n+','',str(line))
				if not step in dicAlg[str(i)][str(j)].keys():
					dicAlg[str(i)][str(j)][step]=[]
				#aqui lee las soluciones..
			else:
				print 'aqui lee las soluciones'
				Data =np.fromstring(line, dtype=float, sep=' ')
				print Data
				indexObjectives = -int(getConfiguration.nObjectives)
#=============================================================================================================================
			#SI EL PASO ESTA ENTRE LAS CLAVES DEL DICCIONARIO, SE CREA UN ARRAY ON LAS SOLUCIONES Y SOLO SE COGE
			#LAS SOLUCIONES DE LOS OBJETIVOS DEPENDIENDO DEL NUMERO DE OBJETIVOS QUE SE HAYA INSERTADO.
#=============================================================================================================================
				if Data[0] == -1.0:
					print 'no debe leer esto..'
				if step in dicAlg[str(i)][str(j)].keys() and Data[0]!= -1.0:
					print 'esto lee las soluciones'
					solution = []
					print dicAlg[str(i)][str(j)][step]
					#print 'esto es index objetivos %s'%str(indexObjectives)
					#print Data
					#print type(Data)
					#print Data[0]
					while indexObjectives < 0:
						print 'esto es el file...'
						print file
						#print 'estoy en el while...'
						#print solution
						#print Data
						#print Data[indexObjectives]
						solution.append(Data[indexObjectives])
						indexObjectives +=1
					print 'sali del while...'
					dicAlg[str(i)][str(j)][step].append(solution)
	#print dicAlg
	return dicAlg