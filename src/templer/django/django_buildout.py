from templer.buildout.basic_buildout import BasicBuildout
import copy
from templer.core.vars import BooleanVar, EASY, EXPERT, ALL

class DjangoBuildout(BasicBuildout):
    _template_dir = 'templates/django_buildout'
    summary = "A Django buildout skeleton"
    help = """This creates a Django buildout."""

    vars = copy.deepcopy(BasicBuildout.vars)
    vars.insert(1, BooleanVar(
        'wsgi',
        title='WSGI',
        description='Insert a WSGI control script?',
        modes=(EASY, EXPERT),
        default=False,
        structures={'False': None, 'True': 'namespace_profile'},
        help="""
An extra script is generated in the bin folder when this is set to true.
This can be used with mod_wsgi to deploy the project.
The name of the script is control-script.wsgi.
""",
    ))
