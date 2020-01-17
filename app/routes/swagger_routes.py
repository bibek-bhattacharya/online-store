
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/v1/swagger'
API_URL = '/static/swagger_product.json'
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Product API"
    }
)