
import functions_framework


@functions_framework.http
def {{ cookiecutter.function_name }}(request):
    """HTTP Cloud Function.
    Args:
      request (flask.Request): The request object.
      <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
      The response text, or any set of values that can be turned into a
      Response object using `make_response`
      <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """

    # Log that the file was written to the bucket
    return 'It\'s working!!'
