"""Tests for plugin."""

import pytest

from wsgirouter3 import PathRouter, WsgiApp

from wsgirouter3_weasyprint import Pdf, PdfConfig, _disable_url_fetching, install, pdf_generator


def test__disable_url_fetching():
    with pytest.raises(NotImplementedError):
        _disable_url_fetching('http://localhost')


def test_pdf_generator():
    used_pdf_id = 'used_pdf_id'
    used_ctx = {'parameter': 'junk'}

    def _gen(pdf_id, ctx):
        assert pdf_id is used_pdf_id
        assert ctx is used_ctx
        return """<html><head></head><body></body></html>"""

    config = PdfConfig(html_generator=_gen, default_headers={'X-Def': 'Value'})

    headers = {}
    result = pdf_generator(
        config,
        Pdf(used_pdf_id, used_ctx, headers={'X-Loc': 'V2'}).write_pdf_with(stylesheets=None),
        headers
    )

    assert isinstance(result, tuple) and len(result) == 1
    assert headers['Content-Type'] == 'application/pdf'
    assert headers['Content-Length'] == str(len(result[0]))
    assert headers['X-Def'] == 'Value'
    assert headers['X-Loc'] == 'V2'

    headers = {}
    result = pdf_generator(config, Pdf(used_pdf_id, used_ctx, headers={'Content-Type': 'application/pdf2'}), headers)

    assert headers['Content-Type'] == 'application/pdf2'
    assert headers['Content-Length'] == str(len(result[0]))
    assert headers['X-Def'] == 'Value'


def test_install():
    router = PathRouter()
    app = WsgiApp(router)
    assert len(app.config.result_converters) == 0

    install(app, PdfConfig(html_generator=None))

    assert len(app.config.result_converters) == 1
