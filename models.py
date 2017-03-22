import base64
import Crypto
from Crypto.Hash import SHA256
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from protorpc import remote
from endpoints_proto_datastore.ndb import EndpointsModel
import endpoints
from google.appengine.api import mail
from google.appengine.ext.webapp import blobstore_handlers

class CustomBaseModel(EndpointsModel):
    def populate(self, data):
        super(self.__class__, self).__init__()
        for attr in self._message_fields_schema:
            if hasattr(data, attr):
                setattr(self, attr, getattr(data, attr))

## empresa
class Empresa(CustomBaseModel):
    _message_fields_schema = ('entityKey', 'codigo_empresa', 'nombre_empresa')
    codigo_empresa = ndb.StringProperty()
    nombre_empresa = ndb.StringProperty()

       ###Empresa####
    def empresa_m(self, data):
        empresa = Empresa()#Crea una variable de tipo Base de datos
        empresa.populate(data)#Llena la variables con los datos dados por el request en main.py
        #empresa.empresa_key=empresakey #inserta el entityKey de la empresa que es un parametro que se manda en main.py
        empresa.put()#inserta o hace un update depende del main.py
        return 0



#####USUARIOS#########

class Usuarios(CustomBaseModel):
    _message_fields_schema = ('entityKey', 'email', 'password', 'salt')

    empresa_key = ndb.KeyProperty(kind=Empresa)
    email = ndb.StringProperty()
    password = ndb.StringProperty()
    salt = ndb.StringProperty(indexed=False)


    def hash_password(self):
        """ Create a cryptographyc random secure salt and hash the password
            using the salt created and store both in the database, the password
            and the salt """
        # Note: It is needed to encode in base64 the salt, otherwise it will
        # cause an exception trying to store non utf-8 characteres
        self.salt = base64.urlsafe_b64encode(
            Crypto.Random.get_random_bytes(16))
        hash_helper = SHA256.new()
        hash_helper.update(self.password + self.salt)
        self.password = hash_helper.hexdigest()

    def verify_password(self, password):
        """ Verify if the password is correct """
        hash_helper = SHA256.new()
        hash_helper.update(password + self.salt)
        return hash_helper.hexdigest() == self.password

       ###Usuarios####
    def usuario_m(self, data, empresakey):
        user = Usuarios()#Crea una variable de tipo Base de datos
        user.populate(data)#Llena la variables con los datos dados por el request en main.py
        user.empresa_key=empresakey
        user.status=1
        user.hash_password()#encripta la contrasena
        user.put()#inserta o hace un update depende del main.py
        return 0




def validarEmail(email):
	emailv = Usuarios.query(Usuarios.email == email)
	if not emailv.get():
		return False
	else:
		return True

if validarEmail("root@kubeet.com") == False:
    empresaAdmin = Empresa(
      codigo_empresa = 'kubeet',
      nombre_empresa="kubeet sa de cv",

    )
    empresaAdmin.put()
    keyadmincol = ndb.Key(urlsafe=empresaAdmin.entityKey)
    admin = Usuarios(
          empresa_key = keyadmincol,
	      email="root@kubeet.com",
          password="docker",

    )
    admin.hash_password()
    admin.put()




######### Team #########

class Team(CustomBaseModel):
    _message_fields_schema = ('entityKey', 'nombre', 'puesto', 'urlImage')
    empresa_key = ndb.KeyProperty(kind=Empresa)
    nombre = ndb.StringProperty()
    puesto = ndb.StringProperty()
    urlImage = ndb.StringProperty()

    ### Team ####
    def team_m(self, data, empresakey):
        team  = Team()#Crea una variable de tipo Base de datos
        team.populate(data)#Llena la variables con los datos dados por el request en main.py
        team.empresa_key=empresakey#inserta el entityKey de la empresa que es un parametro que se manda en main.py
        team.put()#inserta o hace un update depende del main.py
        return 0

######### Factura #########

class Factura(CustomBaseModel):
    _message_fields_schema = ('entityKey', 'tipoDePersona', 'nombre')#, 'rfc', 'pais', 'estado', 'municipio', 'colonia', 'cp', 'calle', 'numExt', 'numInt', 'email', 'numFolio', 'fecha', 'total')
    empresa_key = ndb.KeyProperty(kind=Empresa)
    tipoDePersona = ndb.StringProperty()
    nombre = ndb.StringProperty()
    """rfc = ndb.StringProperty()
    pais = ndb.StringProperty()
    estado = ndb.StringProperty()
    municipio = ndb.StringProperty()
    colonia = ndb.StringProperty()
    cp = ndb.StringProperty()
    calle = ndb.StringProperty()
    numExt = ndb.StringProperty()
    numInt = ndb.StringProperty()
    email = ndb.StringProperty()
    numFolio = ndb.StringProperty()
    fecha = ndb.StringProperty()
    total = ndb.StringProperty()
    """

    ### Factura ####
    def factura_m(self, data, empresakey):
        factura = Factura()#Crea una variable de tipo Base de datos
        factura.populate(data)#Llena la variables con los datos dados por el request en main.py
        factura.empresa_key=empresakey#inserta el entityKey de la empresa que es un parametro que se manda en main.py
        factura.put()#inserta o hace un update depende del main.py
        return 0
