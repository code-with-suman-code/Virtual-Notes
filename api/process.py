
import json

def handler(request):
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Backend will extract text & generate MCQs here"})
    }
