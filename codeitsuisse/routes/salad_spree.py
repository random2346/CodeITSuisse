import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/salad-spree', methods=['POST'])
def evaluateSP():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    n = data.get("number_of_salads")
    arr = data.get("salad_prices_street_map")
    result = str(n) + str(arr)
    logging.info("My result :{}".format(result))
    return json.dumps(result)
