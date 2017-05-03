import os
def process(BASE_DIR,f):
	with open(os.path.join(BASE_DIR, 'media/')+ str(f),'wb+')as destination:
		for chunk in f.chunks():
	  		destination.write(chunk)