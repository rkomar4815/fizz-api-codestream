from flask_restx import Namespace, Resource
from flask.wrappers import Response


api = Namespace("Traffic", description="A modular namespace within Other API")  # noqa


@api.route("/")
class GenerateResource(Resource):
    """Releases"""

    def get(self):
        """Return 200"""
        print('Inside Generate Traffic')
        return 200