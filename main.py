import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import app_identity
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.api import mail
import cloudstorage
import mimetypes
import json
import os
import jinja2

from models import Empresa
from models import Team
from models import Factura
from models import Usuarios
from models import Ticket

jinja_env = jinja2.Environment(
 loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class DemoClass(object):
 pass

def MyClass(obj):
 return obj.__dict__


########################################### CRON ########################################################################
class CronHandler(webapp2.RequestHandler):

    def get(self):
     self.response.headers.add_header('Access-Control-Allow-Origin', '*')
     self.response.headers['Content-Type'] = 'application/json'
     # [START send_message]
     message = mail.EmailMessage(
         sender= "admin@helloworld-158821.appspotmail.com".format(app_identity.get_application_id()),
         subject="Your account has been approved")

     message.to = "Estimado usuario <rhd@getnada.com>"
     message.body = """El fin de semana estaremos realizando tareas de mantenimiento por lo cual nuestro servicio no estara disponible de 10:00 am a 1:00 pm
     Cualquier duda aueddamos a sus servicios.
    """
     message.send()
     # [END send_message]

     self.response.write(message.body)

###############################################  TASK ####################################################################

def send_approved_mail(sender_address, name, email, content):
    # [START send_message]
    message = mail.EmailMessage(
        sender=sender_address,
        subject="Message by " + name + " from " + email)

    message.to = "Ricardo Dorame <rhdorame@gmail.com>"
    message.body = content
    message.send()
    # [END send_message]

class SendTaskMail(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('name')
        email = self.request.get('email')
        content = self.request.get('content')
        sender =self.request.get('sender_address')
        send_approved_mail(sender, name, email, content)

class SendMessageHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.headers['Content-Type'] = 'application/json'

        name = self.request.get('name')
        email = self.request.get('email')
        content = self.request.get('message')
        sender = "admin@minimalist-161601.appspotmail.com".format(app_identity.get_application_id())
        taskqueue.add(url='/sendtask',
                     params={'sender_address': sender, 'name': name, 'email': email, 'content': content})
        json_string = json.dumps("true", default=MyClass)
        self.response.write(json_string)



 ########################### Capa de servicios web tipo get (sin seguridad)###############################################


class GetTeamHandler(webapp2.RequestHandler):

    def get(self):
     self.response.headers.add_header('Access-Control-Allow-Origin', '*')
     self.response.headers['Content-Type'] = 'application/json'

     id_empresa = self.request.get('codigo_empresa')
     objemp = Empresa.query(Empresa.codigo_empresa == id_empresa).get()
     strKey = objemp.key.urlsafe()
     myEmpKey = ndb.Key(urlsafe=strKey)
     myTeam = Team.query(Team.empresa_key == myEmpKey)

     myList = []
     for i in myTeam:
      myObj = DemoClass()
      myObj.nombre = i.nombre
      myObj.puesto = i.puesto
      myObj.urlImage = i.urlImage
      myList.append(myObj)

     json_string = json.dumps(myList, default=MyClass)
     self.response.write(json_string)

class GetTicketHandler(webapp2.RequestHandler):

    def get(self):
     self.response.headers.add_header('Access-Control-Allow-Origin', '*')
     self.response.headers['Content-Type'] = 'application/json'

     id_empresa = self.request.get('codigo_empresa')
     objemp = Empresa.query(Empresa.codigo_empresa == id_empresa).get()
     strKey = objemp.key.urlsafe()
     myEmpKey = ndb.Key(urlsafe=strKey)
     myTeam = Ticket.query(Ticket.empresa_key == myEmpKey)

     myList = []
     for i in myTeam:
      myObj = DemoClass()
      myObj.folio = i.folio
      myObj.fecha = i.fecha
      myObj.total = i.total
      myList.append(myObj)

     json_string = json.dumps(myList, default=MyClass)
     self.response.write(json_string)

class GetUsuarioHandler(webapp2.RequestHandler):

    def get(self):
     self.response.headers.add_header('Access-Control-Allow-Origin', '*')
     self.response.headers['Content-Type'] = 'application/json'

     id_empresa = self.request.get('codigo_empresa')
     objemp = Empresa.query(Empresa.codigo_empresa == id_empresa).get()
     strKey = objemp.key.urlsafe()
     myEmpKey = ndb.Key(urlsafe=strKey)
     myTeam = Usuarios.query(Usuarios.empresa_key == myEmpKey)

     myList = []
     for i in myTeam:
      myObj = DemoClass()
      myObj.email = i.email
      myList.append(myObj)

     json_string = json.dumps(myList, default=MyClass)
     self.response.write(json_string)

class GetFacturaHandler(webapp2.RequestHandler):

    def get(self):
     self.response.headers.add_header('Access-Control-Allow-Origin', '*')
     self.response.headers['Content-Type'] = 'application/json'

     id_empresa = self.request.get('codigo_empresa')
     objemp = Empresa.query(Empresa.codigo_empresa == id_empresa).get()
     strKey = objemp.key.urlsafe()
     myEmpKey = ndb.Key(urlsafe=strKey)
     myTeam = Factura.query(Factura.empresa_key == myEmpKey)

     myList = []
     for i in myTeam:
      myObj = DemoClass()
      myObj.tipoDePersona = i.tipoDePersona
      myObj.nombre = i.nombre
      myObj.rfc = i.rfc
      myObj.pais = i.pais
      myObj.estado = i.estado
      myObj.municipio = i.municipio
      myObj.colonia = i.colonia
      myObj.cp = i.cp
      myObj.calle = i.calle
      myObj.numExt = i.numExt
      myObj.numInt = i.numInt
      myObj.email = i.email
      myObj.numFolio = i.numFolio
      myObj.fecha = i.fecha
      myObj.idTicket = i.idTicket
      myList.append(myObj)

     json_string = json.dumps(myList, default=MyClass)
     self.response.write(json_string)

###########################################################################
class UpHandler(webapp2.RequestHandler):
    def _get_urls_for(self, file_name):

     bucket_name = app_identity.get_default_gcs_bucket_name()
     path = os.path.join('/', bucket_name, file_name)
     real_path = '/gs' + path
     key = blobstore.create_gs_key(real_path)
     try:
      url = images.get_serving_url(key, size=0)
     except images.TransformationError, images.NotImageError:
      url = "http://storage.googleapis.com{}".format(path)

     return url


    def post(self):
     self.response.headers.add_header('Access-Control-Allow-Origin', '*')
     self.response.headers['Content-Type'] = 'application/json'

     bucket_name = app_identity.get_default_gcs_bucket_name()
     uploaded_file = self.request.POST.get('uploaded_file')
     file_name = getattr(uploaded_file, 'filename', None)
     file_content = getattr(uploaded_file, 'file', None)
     real_path = ''

     if file_name and file_content:
      content_t = mimetypes.guess_type(file_name)[0]
      real_path = os.path.join('/', bucket_name, file_name)

      with cloudstorage.open(real_path, 'w', content_type=content_t,
       options={'x-goog-acl': 'public-read'}) as f:
       f.write(file_content.read())

      key = self._get_urls_for(file_name)
      self.response.write(key)


############################# EMPRESAS #########################################
class EmpresaHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('empresa.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

############################# ADMIN #########################################
class AdminHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('admin.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

############################# FACTURAS #########################################
class FacturaHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('factura.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)


############################# TICKETS #########################################
class TicketHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('ticket.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

############################# USUARIOS #########################################
class UsersHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('usuarios.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

class LoginHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('login.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

############################# MAIN #########################################
class MainHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('index.html', template_context))


   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LoginHandler),
    ('/facturacion', FacturaHandler),
    ('/tickets', TicketHandler),
    ('/admin', AdminHandler),
    ('/empresa', EmpresaHandler),
    ('/usuarios', UsersHandler),
    ('/up', UpHandler),
    ('/getteam', GetTeamHandler),
    ('/getticket', GetTicketHandler),
    ('/getusuario', GetUsuarioHandler),
    ('/getfactura', GetFacturaHandler),
    ('/send_message', SendMessageHandler),
    ('/cron', CronHandler),
], debug = True)
