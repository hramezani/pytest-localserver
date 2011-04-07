import py

from pytest_localserver import http, smtp

def pytest_funcarg__httpserver(request):
    """The returned ``httpserver`` funcarg provides these
    helper methods to...
    """
    server = http.Server()
    server.start()
    request.addfinalizer(server.stop)
    return server

def pytest_funcarg__smtpserver(request):
    """The returned ``smtpserver`` funcarg provides these
    helper methods to...
    """
    # next few line are borrowed from tmpdir plugin
    name = request._pyfuncitem.name
    name = py.std.re.sub("[\W]", "_", name)
    tmp = request.config._tmpdirhandler.mktemp(name, numbered=True).strpath
    server = smtp.Server(rootdir=tmp)
    server.start()
    request.addfinalizer(server.stop)
    return server