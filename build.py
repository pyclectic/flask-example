
import sys
from pythonbuilder.core import use_plugin, init, Author

use_plugin('filter_resources')

use_plugin('python.core')
use_plugin('python.coverage')
use_plugin('python.unittest')
use_plugin('python.integrationtest')
use_plugin('python.install_dependencies')
use_plugin('python.pychecker')
use_plugin('python.pydev')

name    = 'flask-hello-world'
authors = [Author('Michael Gruber', 'aelgru@gmail.com')]
license = 'GNU GPL v3'
summary = 'Hello world application for flask.'
url     = 'https://github.com/aelgru/flask-hello-world'
version = '0.0.3'

default_task = ['install_dependencies', 'analyze', 'publish']


@init
def set_properties (project):
    project.build_depends_on('coverage')
    project.build_depends_on('pyassert')
    
    project.depends_on('flask')
    
    project.set_property('coverage_break_build', True)
    project.set_property('pychecker_break_build', False)
    project.set_property('pychecker_args', ['-Q', '-b', 'unittest'])

    project.get_property('filter_resources_glob').append('**/helloworld/__init__.py')
