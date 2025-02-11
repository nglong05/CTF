import web
from web import form
web.config.debug = False
urls = (
  '/', 'index'
)
app = web.application(urls, locals())
render = web.template.render('templates/')
FLAG = open("flag.txt").read()
TEST = "test"
temptation_Form = form.Form(
    form.Password("temptation", description="What is your temptation?"),
    form.Button("submit", type="submit", description="Submit")
)

class index:
    def GET(self):
        try:
            i = web.input()
            if i.source:
                return open(__file__).read()
        except Exception as e:
            pass
        f = temptation_Form()
        return render.index(f)

    def POST(self):
        f = temptation_Form()
        if not f.validates():
            return render.index(f)
        i = web.input()
        temptation = i.temptation
        # if 'flag' in temptation.lower():
        #     return "Too tempted!1"
        # try:
        #     temptation = web.template.Template(f"Your temptation is: {temptation}")()
        # except Exception as  e:
        #     return "Too tempted!2"
        # if str(temptation) == "FLAG":
        #     return FLAG
        # else:
        #     return "Too tempted!3"
        temptation = web.template.Template(f"Your temptation is: {temptation}")()
        print(temptation)
        print(str(temptation) == "FLAG")

application = app.wsgifunc()
if __name__ == "__main__":
    app.run()