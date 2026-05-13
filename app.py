def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    html = """
    <html>
    <head><title>Cloud App</title></head>
    <body>
        <h1>Application deployee sur Render 🚀</h1>
        <p>Serveur Python sans Flask fonctionne correctement.</p>
    </body>
    </html>
    """

    return [html.encode("utf-8")]