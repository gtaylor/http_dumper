from bottle import run, request, response, route, default_app

@route('/')
def emit_request_details():
    """
    This view just dumbly dumps a bunch of details about the HTTP request.
    """
    print('== HEADERS ==')
    for key, val in request.headers.items():
        print("  %s: %s" % (key, val))

    return """<html>
    <head>
        <title>HTTP Dumper</title>
    </head>
    <body>
        <h1>HTTP Dumped</h1>
        <p>Consider it dumped! Here's a kitten.</p>
        <img src='http://placekitten.com/g/200/300'>
    </body>
    </html>"""

