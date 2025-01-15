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


def main(event_log):
    try:
        #check if log_content is empty
        if not event_log.strip():
            raise ValueError("Log content is empty.")

        result = process_log_file(event_log)

        return result

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

main('''[2024-01-07 10:15:30] ERROR: Database connection failed
[2024-01-07 10:15:35] INFO: Retry attempt 1
[2024-01-07 10:15:40] ERROR: Authentication failed''')

main('')