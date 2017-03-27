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
    lat_empresa = messages.FloatField(4)
    long_empresa = messages.FloatField(5)

class EmpresaUpdate(messages.Message):
    token = messages.StringField(1, required=True)
    entityKey = messages.StringField(2, required=True)
    codigo_empresa = messages.StringField(3)
    nombre_empresa = messages.StringField(4)
    lat_empresa = messages.FloatField(5)
    long_empresa = messages.FloatField(6)



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
class FacturaInput(messages.Message):
    token = messages.StringField(1, required=True)
    idTicket = messages.IntegerField(2, required=True)
    tipoDePersona = messages.StringField(3, required=True)
    nombre = messages.StringField(4, required=True)
    rfc = messages.StringField(5, required=True)
    pais = messages.StringField(6, required=True)
    estado = messages.StringField(7, required=True)
    municipio = messages.StringField(8, required=True)
    colonia = messages.StringField(9, required=True)
    cp = messages.IntegerField(10, required=True)
    calle = messages.StringField(11, required=True)
    numExt = messages.IntegerField(12, required=True)
    numInt = messages.IntegerField(13)
    email = messages.StringField(14, required=True)
    numFolio = messages.IntegerField(15, required=True)
    fecha = messages.StringField(16, required=True)


class FacturaUpdate(messages.Message):
    token = messages.StringField(1, required=True)
    #empresa_key = messages.StringField(2, required=True)
    entityKey = messages.StringField(2, required=True)
    tipoDePersona = messages.StringField(3, required=True)
    nombre = messages.StringField(4, required=True)
    rfc = messages.StringField(5, required=True)
    pais = messages.StringField(6, required=True)
    estado = messages.StringField(7, required=True)
    municipio = messages.StringField(8, required=True)
    colonia = messages.StringField(9, required=True)
    cp = messages.IntegerField(10, required=True)
    calle = messages.StringField(11, required=True)
    numExt = messages.IntegerField(12, required=True)
    numInt = messages.IntegerField(13)
    email = messages.StringField(14, required=True)
    numFolio = messages.IntegerField(15, required=True)
    fecha = messages.StringField(16, required=True)
    idTicket = messages.IntegerField(17, required=True)

class FacturaList(messages.Message):
    code = messages.IntegerField(1)
    data = messages.MessageField(FacturaUpdate, 2, repeated=True)

######  Ticket ########
class TicketInput(messages.Message):
    token = messages.StringField(1, required=True)
    folio = messages.IntegerField(3, required=True)
    fecha = messages.StringField(4, required=True)
    total = messages.FloatField(5, required=True)
    items = messages.StringField(6, required=True)
    qty = messages.IntegerField(7, required=True)
    facturado = messages.StringField(8, required=True)


class TicketUpdate(messages.Message):
    #entityKey = messages.StringField(2, required=True)
    token = messages.StringField(1, required=True)
    entityKey = messages.StringField(2, required=True)
    folio = messages.IntegerField(3, required=True)
    fecha = messages.StringField(4, required=True)
    total = messages.FloatField(5, required=True)
    items = messages.StringField(6, required=True)
    qty = messages.IntegerField(7, required=True)
    facturado = messages.StringField(8, required=True)

class TicketList(messages.Message):
    code = messages.IntegerField(1)
    data = messages.MessageField(TicketUpdate, 2, repeated=True)
