import os
import pytest
import base64


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
  pytest_html = item.config.pluginmanager.getplugin('html')
  outcome = yield
  report = outcome.get_result()
  extra = getattr(report, 'extra', [])

  # encoded = base64.b64encode(open("screenshots/helloworld.png", "rb").read())
  # extra.append(pytest_html.extras.image(encoded, ''))
  # image_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x05\x00\x00\x00\x05\x08\x06\x00\x00\x00\x8do&\xe5\x00\x00\x00\x1cIDAT\x08\xd7c\xf8\xff\xff?\xc3\x7f\x06 \x05\xc3 \x12\x84\xd01\xf1\x82X\xcd\x04\x00\x0e\xf55\xcb\xd1\x8e\x0e\x1f\x00\x00\x00\x00IEND\xaeB`\x82'

  html='<div><img src='+'assets/helloworld.png'+' alt="screenshot" style="width:304px;height:228px;" ' \


  extra.append(pytest_html.extras.html(html))



  report.extra = extra
