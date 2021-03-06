import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

def numIslands(arr):
    count = 0
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == "1" : #or arr[i][j] == "0"
                DFS(arr, len(arr), len(arr[0]), i,j)
                count += 1
    return count

def DFS(arr, row, col, i, j):
    if arr[i][j] == "*":
        return
    arr[i][j] = "*"

    if i != 0:
        DFS(arr, row, col, i-1,j)

    if i != row -1:
        DFS(arr, row, col, i+1,j)

    if j != 0:
        DFS(arr, row, col, i,j-1)
    
    if j != col-1:
        DFS(arr, row, col, i,j+1)
    
    if i!=0 and j!=0:
        DFS(arr, row, col, i-1,j-1)
    
    if i!=0 and j!=col-1:
        DFS(arr, row, col, i-1,j+1)

    if i!=row-1 and j!=0:
        DFS(arr, row, col, i+1,j-1)
    
    if i!=row-1 and j!=col-1:
        DFS(arr, row, col, i+1,j+1)


@app.route('/cluster', methods=['POST'])
def evaluateC():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    arr = data
    count = numIslands(arr)
    result = {"answer": count}
    logging.info("My result :{}".format(result))
    return json.dumps(result)
