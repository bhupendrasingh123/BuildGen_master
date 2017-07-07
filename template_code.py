from bottle import get, post, request, run, route, template

def main():
    @route('/build-gen')
    def index():
        msg = 'hello bhpi'
        return template ('index')

    run(host='localhost', port=8080, debug=True)
main()