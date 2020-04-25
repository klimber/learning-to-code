#!/usr/bin/env python

from flask import Flask, request, jsonify
from loguru import logger

from statsapi import data_store, operation

app = Flask(__name__)


@app.route("/data", methods=["POST"])
def save_data():
    logger.info("Saving data...")
    content = request.get_json()
    uuid = data_store.save(content["data"])
    logger.info(f"Data saved with UUID '{uuid}' successfully")
    return jsonify(
        {"status": "success", "message": "data saved sucessfully", "uuid": uuid}
    )

@app.route("/data/<uuid>", methods=["GET"])
def retrieve_data(uuid):
    logger.info(f"Retrieving data assiciated with UUID '{uuid}'...")
    try:
        data = data_store.get(uuid)
    except (KeyError, ValueError) as e:
        logger.warning(f"Cannot retrieve data associated with UUID '{uuid}'")
        return jsonify({"status":"failed", "message":"data cannot be retrieved", "data":[]})
    
    logger.info(f"Data associated with UUID '{uuid}' retrieved successfully")
    return jsonify({"status":"success", "message":"data retrieved successfully", "data":data})

@app.route("/data/<uuid>/<operation>", methods=["GET"])
def process_operation(uuid, operation):
    logger.info(f"Processing Operation '{operation}' on data associated with UUID '{uuid}'...")
    try:
        data = data_store.get(uuid)
        operation_func = get_operation(operation)
        result = operation_func(data)
    except KeyError as e:
        logger.warning(f"Cannot retrieve data associated with UUID '{uuid}'")
        return jsonify({"status":"failed", "message":"data cannot be retrieved", "result": None})
    except NoSuchOperationError:
        logger.warning(f"Cannot find operation '{operation}'")
        return jsonify({"status":"failed", "message":"No such operation", "result": None})
    
    logger.info(f"Operation '{operation}' on data associated with UUID '{uuid}' finished successfully")
    return jsonify({"status":"success", "message":"result completed", "result":result})

def get_operation(operation_name):
    if operation_name == "max":
        return operation.op_max
    elif operation_name == "min":
        return operation.op_min
    elif operation_name == "mean":
        return operation.op_mean
    else:
        raise NoSuchOperationError

class NoSuchOperationError(Exception):
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)