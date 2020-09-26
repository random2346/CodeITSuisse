import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/clean_floor', methods=['POST'])
def evaluateCF():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = {}
    logging.info("My result :{}".format(result))
    return json.dumps(result)
