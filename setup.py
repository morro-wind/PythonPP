import os
from setuptools import setup, find_packages

def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basepath, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''

setup(
        name='guestbook',
        version='1.0.0',
        description='A guestbook web application.',
        long_description=read_file('README.rst'),
        author='<you name>',
        author_email='<you e-mail addreass>',
        url='htts://github.com/<you account>/guestbook/',
        classifiers=[
            'Development Status :: 4 - Beat',
            'Framework :: Flask',
            'License :: OSI Approved :: BSD License,',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            ],
        packages=find_packages(),
        include_package_data=True,
        keywords=['web', 'guestbook'],
        license='BSD License',
        install_requires=[
            'Flask',
        ],
        entry_points="""
            [console_scripts]
            guestbook = guestbook:main
        """,
)

