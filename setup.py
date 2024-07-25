"""Setup script."""

import pathlib

from setuptools import setup


readme = (pathlib.Path(__file__).parent / 'README.md').read_text(encoding='utf-8')
install_requires = (pathlib.Path(__file__).parent / 'requirements.txt').read_text(encoding='utf-8').splitlines()

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
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    keywords='web services',
    author='Andrus Kütt',
    author_email='andrus.kuett@gmail.com',
    url='https://github.com/andruskutt/wsgirouter3-weasyprint',
    license='MIT',
    py_modules=['wsgirouter3_weasyprint'],
    python_requires='>=3.8',
    install_requires=install_requires,
)
