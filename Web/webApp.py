class application:
    def __init__(self, environ, strt_response):
        self.environ = environ
        sel.start = start_response

    def __iter__(self):
        path = self.environ['PATH_INFO']
        if path == '/':
            return self.GET_index()
        elif path == "/hello":
            return self.GET_hello()
        else:
            return self.notfound()
    def GET_index():
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield "Welcome!\n"
    def GET_hello():
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield "Hello world!\n"
    def notfound():
        status = '404 Not Found'
        response_header = [('Content-type', 'text/plain')]
        yield "Not Found\n"

