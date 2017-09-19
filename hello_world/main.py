from sanic import Sanic
from sanic.response import text
from sanic.response import json

app = Sanic(__name__)

@app.route("/")
async def test(request):
    return text("hello friend!")

@app.route("/tag/<tag>",methods=["GET"]) #You can add:  so like, tag:int/number/[A-z0-9]{0,4}
async def tag_handler(request, tag):
    return text("Tag = {}".format(str(tag)))


@app.post("/testpost")
async def post_handler(request):
    return text('POST request {}'.format(str(request.json)))

@app.get("/testget")
async def get_handler(request):
    return text("GET request - {}".format(request.args))


async def random_handler(request,name):
    return text("random handler: {}".format(name))

app.add_route(random_handler,'/randomhandler/<name:[A-z]{0,20}>',methods=['GET'])





#URLFOR





app.run(host="0.0.0.0", port=8000, debug=True)
