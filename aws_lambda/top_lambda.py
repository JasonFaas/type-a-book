import json

qsp = 'queryStringParameters'

print('Loading Function top lambda function')

def lambda_handler(event, context):
    # 1. Parse out query string params
    id = 'transactionId'
    transactionId = event[qsp][id]
    transactionType = event[qsp]['type']
    transactionAmount = event[qsp]['amount']

    # 2. Construct the body of the response object
    transactionResponse = {}
    transactionResponse[id] = transactionId
    transactionResponse['type'] = transactionType
    transactionResponse['amount'] = transactionAmount
    transactionResponse['message'] = 'Hello World! Jason'

    # 3. Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    respnnseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)

    return responseObject
