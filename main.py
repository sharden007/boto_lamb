import boto3
import json

# Initialize the Lambda client with error handling
try:
    lambda_client = boto3.client('lambda')  # Create a client for AWS Lambda
except Exception as e:
    print(f"Error initializing Lambda client: {e}")
    raise  # Re-raise the exception to halt execution if initialization fails

# Define the Lambda function name and payload
function_name = 'my-lambda-function'  # Replace with your actual Lambda function name
payload = {"key": "value"}  # Example payload as a Python dictionary

# Convert the payload to bytes for the invocation
try:
    payload_bytes = json.dumps(payload).encode('utf-8')  # Serialize and encode payload to JSON bytes
except Exception as e:
    print(f"Error encoding payload to JSON: {e}")
    raise  # Re-raise the exception if payload conversion fails

# Trigger the Lambda function with error handling
try:
    response = lambda_client.invoke(
        FunctionName=function_name,  # Specify the function name
        InvocationType='Event',  # Async invocation (does not wait for a response)
        Payload=payload_bytes  # Pass the serialized payload
    )
    
    # Check the response status code to confirm successful invocation
    if response['StatusCode'] == 202:  # Status code 202 indicates success for async invocations
        print(f"Lambda function triggered successfully. Status Code: {response['StatusCode']}")
    else:
        print(f"Failed to trigger Lambda function. Status Code: {response['StatusCode']}")
except Exception as e:
    print(f"Error invoking Lambda function: {e}")
    raise  # Re-raise the exception if invocation fails

