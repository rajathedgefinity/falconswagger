import falcon
from falcon_swagger_ui import register_swaggerui_app

app = falcon.API()

SWAGGER_URL = '/swagger'
SCHEMA_URL = 'http://petstore.swagger.io/v2/swagger.json'

page_title = 'Falcon Swagger Doc'
favicon_url = 'https://faconframework.org/favicon-32x32.png'

register_swaggerui_app(
    app, SWAGGER_URL, SCHEMA_URL,
    page_title=page_title,
    favicon_url = favicon_url,
    config = {'supportSubmitMethods':['get'],}
)
