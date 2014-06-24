import os
from flask import Flask, render_template, request, redirect, url_for, abort, session,send_from_directory ##Se importan las librerias
from werkzeug import secure_filename
app = Flask("Verificacion") 
##################

@app.route('/')
def Verificacion():
    return render_template('Verificacion.html')


############################################################
@app.route('/Pagina')
def Pagina():
    return render_template('Pagina.html')  

@app.route('/Opciones', methods=['POST'])
def Opciones():
    titulo = request.form['titulo']
    descripcion = request.form['descripcion']
    Luz = request.form['Luz']
    Agua = request.form['Agua']
    Cable = request.form['Cable']
    Internet = request.form['Internet']
    Amueblado = request.form['Amueblado']
    cocina = request.form['cocina']
    lavado = request.form['lavado']
    Otros = request.form['Otros']
    numeropisos = request.form['numeropisos']
    numerodormitorios = request.form['numerodormitorios']
    numerobanos = request.form['numerobanos']
    numeroestacionamientos = request.form['numeroestacionamientos']
    pilas = request.form['pilas']
    Jardin = request.form['Jardin']
    Balcon = request.form['Balcon']
    ubicacion = request.form['ubicacion']
    precio = request.form['precio']
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    correo = request.form['correo']
    if Luz == "Si":
	z = True
    else:
	z=False
    if Agua == "Si":
	x = True
    else:
	x=False
    if Cable == "Si":
	c = True
    else:
	c=False
    if Internet == "Si":
	v = True
    else:
	v=False
    if Amueblado == "Si":
	b = True
    else:
	b=False
    if cocina == "Si":
	n = True
    else:
	n=False
    if lavado == "Si":
	m = True
    else:
	m=False
    if Otros == "Si":
	a = True
    else:
	a=False
    if pilas == "Si":
	s = True
    else:
	s=False
    if Jardin == "Si":
	d = True
    else:
	d=False
    if Balcon == "Si":
	f = True
    else:
	f=False
    Apartas.agregar_Aparta(titulo,descripcion,[z,x,c,v,b,n,m,a],[numeropisos,numerodormitorios,numerobanos,numeroestacionamientos,s,d,f],ubicacion,precio,[nombre,telefono,correo])
    return render_template('Opciones.html')  

@app.route('/Ingreso', methods=['POST'])
def Ingreso():
    return render_template('Ingreso.html')

###########################################################
class Aparta:
    def __init__(self,titulo,descripcion,facilidades,caracteristicas,ubicacion,precio,contacto):
        self.tit=titulo
        self.desc=descripcion
        self.facil=facilidades
        self.carac=caracteristicas
        self.ubic=ubicacion
        self.prec=precio
        self.cont=contacto
        self.next=None
    def  __str__(self):
        return str(self.tit, self.desc,self.facil,self.carac,self.ubic,self.prec,self.cont)
#...............................................................................................
class ListaApartas(Aparta):
    def __init__(self):
        self.PrimerAparta = None
        self.UltimoAparta = None
        
    def agregar_Aparta(self, tit,desc,facil,carac,ubica,prec,cont):
        NuevoAparta = Aparta(tit,desc,facil,carac,ubica,prec,cont)
        if self.PrimerAparta == None:
            self.PrimerAparta = NuevoAparta
        if self.UltimoAparta != None:
            self.UltimoAparta.next = NuevoAparta
        self.UltimoAparta = NuevoAparta

    def imprimir (self):
        
        Lista=[]
        Actual = self.PrimerAparta
        if Actual == None:
            return render_template('Vacia.html')  
        else:
            
            while Actual != None:
                T=Actual.tit
                Lista.append(T)
                D=Actual.desc
                Lista.append("Descripcion:" + D)
                Fac=Actual.facil
                F=[]
                if Fac[0]:
                    F.append("Luz")
                if Fac[1]:
                    F.append("Agua")
                if Fac[2]:
                    F.append("TV_Cable")
                if Fac[3]:
                    F.append("Internet")
                if Fac[4]:
                    F.append("Amueblado")
                if Fac[5]:
                    F.append("Equipamento_de_Cocina")
                if Fac[6]:
                    F.append("Equipamento_de_Lavado")
                if Fac[7]:
                    F.append("Otros")
                Lista.append("Facilidades: "+str(F))
                Car=Actual.carac
                C=[]
                C.append("Pisos: "+Car[0])
		C[0].replace("u","")
                C.append("Dormitorios: "+Car[1])
                C.append("Banos " + Car[2])
                if Car[3]!= "0":		    
                    C.append("Estacionamientos:" +Car[3])
                if Car[4]:
                    C.append("Cuarto_de_Pilas")
	
                if Car[5]:
                    C.append("Jardin")    
                if Car[6]:
                    C.append("Balcon")
                Lista.append("Caracteristicas: " + str(C))
                U=Actual.ubic
                Lista.append("Ubicacion: " +U)
                P=Actual.prec
                Lista.append("Precio: " +P)
                K=Actual.cont
                Lista.append("Contacto: "+str(K))
                Actual = Actual.next
      
                return Lista
#.............................................................

    def Buscar_Ubicacion(self,ubicacion):
        Lista=[]
        Actual = self.PrimerAparta
        Bandera = False
        if Actual == None:
            print ("No hay Apartas")
        else:
            while Actual != None:
                print('Entra while ubic')
        	if Actual.ubic==ubicacion:
                    Bandera = True
                    T=Actual.tit
                    Lista.append(T)
                    D=Actual.desc
                    Lista.append("Descripcion:" + D)
                    Fac=Actual.facil
                    F=[]
                    if Fac[0]:
                        F.append("Luz")
                    if Fac[1]:
                        F.append("Agua")
                    if Fac[2]:
                        F.append("TV_Cable")
                    if Fac[3]:
                        F.append("Internet")
                    if Fac[4]:
                        F.append("Amueblado")
                    if Fac[5]:
                        F.append("Equipamento_de_Cocina")
                    if Fac[6]:
                        F.append("Equipamento_de_Lavado")
                    if Fac[7]:
                        F.append("Otros")
                    Lista.append("Facilidades: "+str(F))
                    Car=Actual.carac
                    C=[]
                    C.append("Pisos: "+Car[0])
                    C[0].replace("u","")
                    C.append("Dormitorios: "+Car[1])
                    C.append("Banos " + Car[2])
                    if Car[3]!= "0":		    
                        C.append("Estacionamientos:" +Car[3])
                    if Car[4]:
                        C.append("Cuarto_de_Pilas")
	
                    if Car[5]:
                        C.append("Jardin")    
                    if Car[6]:
                        C.append("Balcon")
                    Lista.append("Caracteristicas: " + str(C))
                    U=Actual.ubic
                    Lista.append("Ubicacion: " +U)
                    P=Actual.prec
                    Lista.append("Precio: " +P)
                    K=Actual.cont
                    Lista.append("Contacto: "+str(K))
                Actual = Actual.next
	    if Bandera == False:
                ##Retorna: No hay apartamentos en esa ubicacion
                return render_template('Ingreso.html')
            else:
        	return Lista


    def Ordenar_Precio(self):
	ListaPrecios=[]
	Aux = self.PrimerAparta
	if Aux == None:
	    print ("No hay Apartas")
	else:
	    while Aux != None:
	        ListaPrecios.append(Aux.prec)
	        Aux = Aux.next
            return sorted(ListaPrecios)
	
    def Buscar_Precio(self):
        Lista=[]
        ListaPrecios=[]
	Aux = self.PrimerAparta
	if Aux == None:
	    print ("No hay Apartas")
	else:
	    while Aux != None:
	        ListaPrecios.append(Aux.prec)
	        Aux = Aux.next
	print(ListaPrecios)
	ListaPrecios=sorted(ListaPrecios)
	print(ListaPrecios)
        for i in ListaPrecios:
            Actual = self.PrimerAparta
            while Actual != None:
                if Actual.prec == i :
        	    Bandera = True
                    T=Actual.tit
                    Lista.append(T)
                    D=Actual.desc
                    Lista.append("Descripcion:" + D)
                    Fac=Actual.facil
                    F=[]
                    if Fac[0]:
                        F.append("Luz")
                    if Fac[1]:
                        F.append("Agua")
                    if Fac[2]:
                        F.append("TV_Cable")
                    if Fac[3]:
                        F.append("Internet")
                    if Fac[4]:
                        F.append("Amueblado")
                    if Fac[5]:
                        F.append("Equipamento_de_Cocina")
                    if Fac[6]:
                        F.append("Equipamento_de_Lavado")
                    if Fac[7]:
                        F.append("Otros")
                    Lista.append("Facilidades: "+str(F))
                    Car=Actual.carac
                    C=[]
                    C.append("Pisos: "+Car[0])
                    C[0].replace("u","")
                    C.append("Dormitorios: "+Car[1])
                    C.append("Banos " + Car[2])
                    if Car[3]!= "0":		    
                        C.append("Estacionamientos:" +Car[3])
                    if Car[4]:
                        C.append("Cuarto_de_Pilas")
	
                    if Car[5]:
                        C.append("Jardin")    
                    if Car[6]:
                        C.append("Balcon")
                    Lista.append("Caracteristicas: " + str(C))
                    U=Actual.ubic
                    Lista.append("Ubicacion: " +U)
                    P=Actual.prec
                    Lista.append("Precio: " +P)
                    K=Actual.cont
                    Lista.append("Contacto: "+str(K))
                Actual = Actual.next
            return Lista
	
    def Buscar_Facilidades(self, luz,agua,cable,internet,amueblado,cocina,lavado,otros):
        Lista=[]
	Actual = self.PrimerAparta
	ListaFacil=[luz,agua,cable,internet,amueblado,cocina,lavado,otros]
	Bandera = False
	while Actual != None:
	    if Actual.facil == ListaFacil:
	        Bandera = True
                T=Actual.tit
                Lista.append(T)
                D=Actual.desc
                Lista.append("Descripcion:" + D)
                Fac=Actual.facil
                F=[]
                if Fac[0]:
                    F.append("Luz")
                if Fac[1]:
                    F.append("Agua")
                if Fac[2]:
                    F.append("TV_Cable")
                if Fac[3]:
                    F.append("Internet")
                if Fac[4]:
                    F.append("Amueblado")
                if Fac[5]:
                    F.append("Equipamento_de_Cocina")
                if Fac[6]:
                    F.append("Equipamento_de_Lavado")
                if Fac[7]:
                    F.append("Otros")
                Lista.append("Facilidades: "+str(F))
                Car=Actual.carac
                C=[]
                C.append("Pisos: "+Car[0])
                C[0].replace("u","")
                C.append("Dormitorios: "+Car[1])
                C.append("Banos " + Car[2])
                if Car[3]!= "0":		    
                    C.append("Estacionamientos:" +Car[3])
                if Car[4]:
                    C.append("Cuarto_de_Pilas")
                if Car[5]:
                    C.append("Jardin")    
                if Car[6]:
                    C.append("Balcon")
                Lista.append("Caracteristicas: " + str(C))
                U=Actual.ubic
                Lista.append("Ubicacion: " +U)
                P=Actual.prec
                Lista.append("Precio: " +P)
                K=Actual.cont
                Lista.append("Contacto: "+str(K))
	    Actual=Actual.next
	if Bandera == False:
            ##Retorna: No hay apartamentos que cumplan con las facilidades
            return render_template('Ingreso.html')
        else:
            return Lista

    def Buscar_Caracteristicas(self, pisos,dormitorios,banos,parqueo,pilas,jardin,balcon):
        Lista=[]
	Actual = self.PrimerAparta
	ListaCaract=[pisos,dormitorios,banos,parqueo,pilas,jardin,balcon]
	Bandera=False
	while Actual != None:
	    if Actual.carac == ListaCaract:
	        Bandera = True
                T=Actual.tit
                Lista.append(T)
                D=Actual.desc
                Lista.append("Descripcion:" + D)
                Fac=Actual.facil
                F=[]
                if Fac[0]:
                    F.append("Luz")
                if Fac[1]:
                    F.append("Agua")
                if Fac[2]:
                    F.append("TV_Cable")
                if Fac[3]:
                    F.append("Internet")
                if Fac[4]:
                    F.append("Amueblado")
                if Fac[5]:
                    F.append("Equipamento_de_Cocina")
                if Fac[6]:
                    F.append("Equipamento_de_Lavado")
                if Fac[7]:
                    F.append("Otros")
                Lista.append("Facilidades: "+str(F))
                Car=Actual.carac
                C=[]
                C.append("Pisos: "+Car[0])
                C[0].replace("u","")
                C.append("Dormitorios: "+Car[1])
                C.append("Banos " + Car[2])
                if Car[3]!= "0":		    
                    C.append("Estacionamientos:" +Car[3])
                if Car[4]:
                    C.append("Cuarto_de_Pilas")
                if Car[5]:
                    C.append("Jardin")    
                if Car[6]:
                    C.append("Balcon")
                Lista.append("Caracteristicas: " + str(C))
                U=Actual.ubic
                Lista.append("Ubicacion: " +U)
                P=Actual.prec
                Lista.append("Precio: " +P)
                K=Actual.cont
                Lista.append("Contacto: "+str(K))
	    Actual=Actual.next
	if Bandera == False:
            ##Retorna: No hay apartamentos que cumplan con las caracteristicas
            return render_template('Ingreso.html')
        else:
            return Lista
#..................................................................................................
@app.route('/muestra')
def muestra():
    return render_template('muestra.html',Lista=Apartas.imprimir()) 

@app.route('/busqueda')
def busqueda():
    return render_template('busqueda.html') 

@app.route('/busquedaubicacion')
def busquedaubicacion():
    print("ubica")
    return render_template('busquedaubicacion.html') 

@app.route('/muestraporubicacion', methods=['POST'])
def muestraporubicacion():
    print ('muestra')
    ubicacion = request.form['ubicacion']
    Apartas.Buscar_Ubicacion(ubicacion)
    return render_template('muestraporubicacion.html',Lista=Apartas.Buscar_Ubicacion(ubicacion)) 

@app.route('/busquedafac')
def busquedafac():
    return render_template('busquedafac.html') 

@app.route('/busquedacarac')
def busquedacarac():
    return render_template('busquedacarac.html') 

@app.route('/muestraporprecio')
def muestraporprecio():
    return render_template('muestraporprecio.html',precio=Apartas.Buscar_Precio()) 

@app.route('/muestraporfac', methods=['POST'])
def muestraporfac():
    Luz = request.form['Luz']
    Agua = request.form['Agua']
    Cable = request.form['Cable']
    Internet = request.form['Internet']
    Amueblado = request.form['Amueblado']
    cocina = request.form['cocina']
    lavado = request.form['lavado']
    Otros = request.form['Otros']
    if Luz == "Si":
	z = True
    else:
	z=False
    if Agua == "Si":
	x = True
    else:
	x=False
    if Cable == "Si":
	c = True
    else:
	c=False
    if Internet == "Si":
	v = True
    else:
	v=False
    if Amueblado == "Si":
	b = True
    else:
	b=False
    if cocina == "Si":
	n = True
    else:
	n=False
    if lavado == "Si":
	m = True
    else:
	m=False
    if Otros == "Si":
	a = True
    else:
	a=False
    return render_template('muestraporfac.html',fac=Apartas.Buscar_Facilidades(z,x,c,v,b,n,m,a)) 

@app.route('/muestraporcarac', methods=['POST'])
def muestraporcarac():
    numeropisos = request.form['numeropisos']
    numerodormitorios = request.form['numerodormitorios']
    numerobanos = request.form['numerobanos']
    numeroestacionamientos = request.form['numeroestacionamientos']
    pilas = request.form['pilas']
    Jardin = request.form['Jardin']
    Balcon = request.form['Balcon']
    if pilas == "Si":
	s = True
    else:
	s=False
    if Jardin == "Si":
	d = True
    else:
	d=False
    if Balcon == "Si":
	f = True
    else:
	f=False
    return render_template('muestraporcarac.html',carac=Apartas.Buscar_Caracteristicas(numeropisos,numerodormitorios,numerobanos,numeroestacionamientos,s,d,f)) 




if __name__ == '__main__':
    Apartas= ListaApartas()
    app.run()
