from protorpc import messages
from protorpc import message_types

class MessageNone(messages.Message):
    inti = messages.StringField(1)
# Input messages
#Recibe el token para validar
class Token(messages.Message):
    tokenint = messages.StringField(1, required=True)
    #entityKey = messages.StringField(2, required=False)
    #fromurl = messages.StringField(3)

#Recibe el token y un entityKey de cualquier base de datos para validar
class TokenKey(messages.Message):
    tokenint = messages.StringField(1, required=True)
    entityKey = messages.StringField(2, required=True)
    #fromurl = messages.StringField(3)


#Recibe el email y contrasena para la creacion de token
class EmailPasswordMessage(messages.Message):
    email = messages.StringField(1, required=True)
    password = messages.StringField(2, required=True)


#USERS
class UserInput(messages.Message):
    token = messages.StringField(1)
    empresa_key = messages.StringField(2)
    email = messages.StringField(3)
    password = messages.StringField(4)



class UserUpdate(messages.Message):
    token = messages.StringField(1)
    email = messages.StringField(2)
    password = messages.StringField(3)
    entityKey = messages.StringField(4, required=True)

class UserList(messages.Message):
    code = messages.IntegerField(1)
    data = messages.MessageField(UserUpdate, 2, repeated=True)


######Empresa########

#Mensaje de Entrada y Salida para la base de datos Empresa
class EmpresaInput(messages.Message):
    token = messages.StringField(1, required=True)
    codigo_empresa = messages.StringField(2)
    nombre_empresa = messages.StringField(3)


class EmpresaUpdate(messages.Message):
    token = messages.StringField(1, required=True)
    entityKey = messages.StringField(2, required=True)
    codigo_empresa = messages.StringField(3)
    nombre_empresa = messages.StringField(4)



#regresa una lista para la base de datos Empresa
class EmpresaList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIELD que regresa una lista de tipo EmpresaUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(EmpresaUpdate, 2, repeated=True)


######Team########

#Mensaje de Entrada y Salida para la base de datos Team
class TeamInput(messages.Message):
    token = messages.StringField(1, required=True)
    nombre = messages.StringField(2)
    puesto = messages.StringField(3)
    urlImage = messages.StringField(5)


class TeamUpdate(messages.Message):
    token = messages.StringField(1, required=True)
    #empresa_key = messages.StringField(2, required=True)
    entityKey = messages.StringField(2, required=True)
    nombre = messages.StringField(3)
    puesto = messages.StringField(4)
    urlImage = messages.StringField(5)

#regresa una lista para la base de datos Empresa
class TeamList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIED que regresa una lista de tipo TeamUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(TeamUpdate, 2, repeated=True)


# Output messages
#regresa un token
class TokenMessage(messages.Message):
    code = messages.IntegerField(1)
    message = messages.StringField(2)
    token = messages.StringField(3)

#regresa mensajes de lo ocurrido
class CodeMessage(messages.Message):
    code = messages.IntegerField(1)
    message = messages.StringField(2)




######  Factura ########

#Mensaje de Entrada y Salida para la base de datos Team
class FacturaInput(messages.Message):
    token = messages.StringField(1, required=True)
    tipoDePersona = messages.StringField(2)
    nombre = messages.StringField(3)
    """rfc = messages.StringField(4)
    pais = messages.StringField(5)
    colonia = messages.StringField(8)
    cp = messages.StringField(9)
    calle = messages.StringField(10)
    numExt = messages.StringField(11)
    numInt = messages.StringField(12)
    email = messages.StringField(13)
    numFolio = messages.StringField(14)
    fecha = messages.StringField(15)
    total = messages.StringField(16)"""


class FacturaUpdate(messages.Message):
    token = messages.StringField(1, required=True)
    #empresa_key = messages.StringField(2, required=True)
    entityKey = messages.StringField(2, required=True)
    tipoDePersona = messages.StringField(3)
    nombre = messages.StringField(4)
    """rfc = messages.StringField(5)
    pais = messages.StringField(6)
    estado = messages.StringField(7)
    municipio = messages.StringField(8)
    colonia = messages.StringField(9)
    cp = messages.StringField(10)
    calle = messages.StringField(11)
    numExt = messages.StringField(12)
    numInt = messages.StringField(13)
    email = messages.StringField(14)
    numFolio = messages.StringField(15)
    fecha = messages.StringField(16)
    total = messages.StringField(17)"""

class FacturaList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIED que regresa una lista de tipo TeamUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(FacturaUpdate, 2, repeated=True)
