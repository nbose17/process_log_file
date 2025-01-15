import re

def process_log_file(log_content):
    # Regular expression to capture log entries with level ERROR
    error_pattern = r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] ERROR: (.+)"
    
    # Find all error messages
    error_messages = re.findall(error_pattern, log_content)

    # Get unique error messages sorted alphabetically
    unique_errors = sorted(set(error_messages))

    # Return the result as a dictionary
    return {
        'total_errors': len(error_messages),
        'unique_error_messages': unique_errors
    }

    
def lambda_handler(event, context):
    try:
        #check if log_content is empty
        if not event['log_content'].strip():
            raise ValueError("Log content is empty.")

        result = process_log_file(event['log_content'])

        return {
            'statusCode': 200,
            'body': {
                "candidate_id": event['candidate_id'],
                "result": result
            }
        }

    except KeyError as e:
        return {
            'statusCode': 400,
            'body': {
                'message': f'Missing parameter: {str(e)}'
            }
        }

    except ValueError as v:
        return {
            'statusCode': 400,
            'body': {
                'message': f'{v}'
            }
        }

