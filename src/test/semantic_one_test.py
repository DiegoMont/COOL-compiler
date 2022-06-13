import pytest

from main import compile
from util.exceptions import *

def test_anattributenamedself():
    with pytest.raises(anattributenamedself):
        # Relativo a main
        #compile('src/resources/semantic/input/anattributenamedself.cool')
        #Relativo al root
        compile('src/resources/semantic/input/anattributenamedself.cool')

def test_badredefineint():
    with pytest.raises(badredefineint):
        compile('src/resources/semantic/input/badredefineint.cool')

def test_inheritsbool():
    with pytest.raises(inheritsbool):
        compile('src/resources/semantic/input/inheritsbool.cool')

def test_inheritsselftype():
    with pytest.raises(inheritsselftype):
        compile('src/resources/semantic/input/inheritsselftype.cool')

def test_inheritsstring():
    with pytest.raises(inheritsstring):
        compile('src/resources/semantic/input/inheritsstring.cool')

def test_letself():
    with pytest.raises(letself):
        compile('src/resources/semantic/input/letself.cool')

def test_nomain():
    with pytest.raises(nomain):
        compile('src/resources/semantic/input/nomain.cool')

def test_redefinedobject():
    with pytest.raises(redefinedobject):
        compile('src/resources/semantic/input/redefinedobject.cool')

def test_selfassignment():
    with pytest.raises(selfassignment):
        compile('src/resources/semantic/input/self-assignment.cool')

def test_selfinformalparameter():
    with pytest.raises(selfinformalparameter):
        compile('src/resources/semantic/input/selfinformalparameter.cool')

def test_selftypeparameterposition():
    with pytest.raises(selftypeparameterposition):
        compile('src/resources/semantic/input/selftypeparameterposition.cool')

def test_selftyperedeclared():
    with pytest.raises(selftyperedeclared):
        compile('src/resources/semantic/input/selftyperedeclared.cool')

