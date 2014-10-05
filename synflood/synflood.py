import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        self.render("input_config.html")

    def post(self):
	zone = self.request.get("zone")
	attack_threshold = self.request.get("attack_threshold")
	alarm_threshold = self.request.get("alarm_threshold")
	source_threshold = self.request.get("source_threshold")
	destination_threshold = self.request.get("destination_threshold")
	timeout = self.request.get("timeout")
    	PingOfDeath = self.request.get("PingOfDeath")
    	TearDrop = self.request.get("TearDrop")
    	SourceRoute = self.request.get("SourceRoute")
    	LandAttack = self.request.get("LandAttack")
	params = dict(zone = zone,
			attack_threshold = attack_threshold,
			alarm_threshold = alarm_threshold,
			source_threshold = source_threshold,
			destination_threshold = destination_threshold,
    			timeout = timeout,
    			PingOfDeath = PingOfDeath,
    			TearDrop = TearDrop,
    			SourceRoute = SourceRoute,
    			LandAttack = LandAttack)

	if not (zone and attack_threshold and timeout):
        	self.render("input_config.html",**params)
	else:
        	self.render("output_config.html",**params)

app = webapp2.WSGIApplication([('/',MainPage),
                              ],
                              debug=True)
