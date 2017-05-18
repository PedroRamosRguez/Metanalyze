import tarfile,re
import numpy as np
def parseFiles(tar,i,dicAlg,member,getConfiguration):
	for j,file in enumerate(member):
		f = tar.extractfile(file)
		dicAlg[str(i)][str(j)] = dict()	#crea el diccionario por ejecuciones dentro del algoritmo actual
		for k,line in enumerate(f.readlines()):
			if re.search('^[#]?\s*\w+\s*\d+\n+',line):
				step = re.sub('^[#]?\s*[a-zA-Z]+\s*','',str(line)).rstrip()
				if not step in dicAlg[str(i)][str(j)].keys():
					#print 'claves:'
					#print dicAlg[str(i)][str(j)].keys()
					dicAlg[str(i)][str(j)][step]=[]
				#se detecta que el paso venga dado de la manera 200(200)\n,200 (200)\n y se elimina la parte del parentesis
			elif re.search('^\d+\s*\(\d+\)\n+',line):
				step = re.sub('\(\d+\)\n+','',str(line))
				if not step in dicAlg[str(i)][str(j)].keys():
					dicAlg[str(i)][str(j)][step]=[]
				#aqui lee las soluciones..
			else:
				Data =np.fromstring(line, dtype=float, sep=' ')
				#print Data
				indexObjectives = -int(getConfiguration.nObjectives)
#=============================================================================================================================
			#SI EL PASO ESTA ENTRE LAS CLAVES DEL DICCIONARIO, SE CREA UN ARRAY ON LAS SOLUCIONES Y SOLO SE COGE
			#LAS SOLUCIONES DE LOS OBJETIVOS DEPENDIENDO DEL NUMERO DE OBJETIVOS QUE SE HAYA INSERTADO.
#=============================================================================================================================
				if Data[0] == -1.0:
					print 'white line'
					pass
				if step in dicAlg[str(i)][str(j)].keys() and Data[0]!= -1.0:
					solution = []
					print dicAlg[str(i)][str(j)][step]
					#print 'esto es index objetivos %s'%str(indexObjectives)
					#print Data
					#print type(Data)
					#print Data[0]
					while indexObjectives < 0:
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

def parseZipFiles(zf,i,dicAlg,fileList,getConfiguration):
	for j,filename in enumerate(fileList):
		print 'entre aqui...'
		print zf
		#f = tar.extractfile(file)
		dicAlg[str(i)][str(j)] = dict()	#crea el diccionario por ejecuciones dentro del algoritmo actual
		#data = zf.readlines(filename)
		with zf.open(filename) as f:
			for line in f:
				if re.search('^[#]?\s*\w+\s*\d+\n+',line):
					step = re.sub('^[#]?\s*[a-zA-Z]+\s*','',str(line)).rstrip()

					if not step in dicAlg[str(i)][str(j)].keys():
						#print 'claves:'
						#print dicAlg[str(i)][str(j)].keys()
						dicAlg[str(i)][str(j)][step]=[]
					#se detecta que el paso venga dado de la manera 200(200)\n,200 (200)\n y se elimina la parte del parentesis
				elif re.search('^\d+\s*\(\d+\)\n+',line):
					step = re.sub('\(\d+\)\n+','',str(line))
					if not step in dicAlg[str(i)][str(j)].keys():
						dicAlg[str(i)][str(j)][step]=[]
					#aqui lee las soluciones..
				else:
					Data =np.fromstring(line, dtype=float, sep=' ')
					#print Data
					indexObjectives = -int(getConfiguration.nObjectives)
		#=============================================================================================================================
				#SI EL PASO ESTA ENTRE LAS CLAVES DEL DICCIONARIO, SE CREA UN ARRAY ON LAS SOLUCIONES Y SOLO SE COGE
				#LAS SOLUCIONES DE LOS OBJETIVOS DEPENDIENDO DEL NUMERO DE OBJETIVOS QUE SE HAYA INSERTADO.
		#=============================================================================================================================
					if Data[0] == -1.0:
						print 'white line'
					if step in dicAlg[str(i)][str(j)].keys() and Data[0]!= -1.0:
						solution = []
						print dicAlg[str(i)][str(j)][step]
						#print 'esto es index objetivos %s'%str(indexObjectives)
						#print Data
						#print type(Data)
						#print Data[0]
						while indexObjectives < 0:
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