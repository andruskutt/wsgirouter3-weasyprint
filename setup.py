"""Setup script."""

import os

from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='wsgirouter3_weasyprint',
    version='0.1.2',
    description='WSGI routing library weasyprint plugin',
    long_description=readme,
    long_description_content_type='text/markdown',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    keywords='web services',
    author='Andrus Kütt',
    author_email='andrus.kuett@gmail.com',
    url='https://github.com/andruskutt/wsgirouter3-weasyprint',
    license='MIT',
    py_modules=['wsgirouter3_weasyprint'],
    python_requires='>=3.7',
)
