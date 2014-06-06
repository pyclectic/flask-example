#   flask-hello-world
#   Copyright 2012-2013 Michael Gruber, Alexander Metzner
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
    A simple flask application tested using pyassert and pyfix and
    built with pybuilder.
"""

from pybuilder.core import use_plugin, init, Author

use_plugin('filter_resources')

use_plugin('python.core')
use_plugin('python.coverage')
use_plugin('python.pyfix_unittest')
use_plugin('python.integrationtest')
use_plugin('python.install_dependencies')
use_plugin('python.flake8')
use_plugin('python.pydev')

name = 'flask-example'
authors = [Author('Michael Gruber', 'aelgru@gmail.com'),
           Author('Alexander Metzner', 'halimath.wilanthaou@gmail.com')]
license = 'Apache License, Version 2.0'
summary = 'Hello world application for flask.'
url = 'https://github.com/pycletic/flask-example'
version = '0.1.2'


default_task = ['install_dependencies', 'analyze', 'publish']


@init
def set_properties (project):
    project.build_depends_on('coverage')
    project.build_depends_on('pyassert')
    project.build_depends_on('pyfix')
    
    project.depends_on('flask')
    
    project.set_property('coverage_break_build', True)
    project.set_property('flake8_break_build', True)

    project.get_property('filter_resources_glob').append('**/helloworld/__init__.py')
