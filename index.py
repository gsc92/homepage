from bottle import route, run, static_file


@route('/static/<path_to:path>/<file_name>')
def serve_file(path_to, file_name):
    return static_file(file_name, root="./static/" + path_to)


@route('/')
def serve_index():
    return static_file("index.html", root=".")


run(host='localhost', port=8080)
