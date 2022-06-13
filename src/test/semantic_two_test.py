import pytest

from main import compile
from util.exceptions import *

def test_badarith():
    with pytest.raises(badarith):
        compile('src/resources/semantic/input/badarith.cool')

def test_baddispatch():
    with pytest.raises(baddispatch):
        compile('src/resources/semantic/input/baddispatch.cool')

def test_badequalitytest():
    with pytest.raises(badequalitytest):
        compile('src/resources/semantic/input/badequalitytest.cool')

def test_badequalitytest2():
    with pytest.raises(badequalitytest2):
        compile('src/resources/semantic/input/badequalitytest2.cool')

def test_badwhilebody():
    with pytest.raises(badwhilebody):
        compile('src/resources/semantic/input/badwhilebody.cool')

def test_badwhilecond():
    with pytest.raises(badwhilecond):
        compile('src/resources/semantic/input/badwhilecond.cool')

def test_caseidenticalbranch():
    with pytest.raises(caseidenticalbranch):
        compile('src/resources/semantic/input/caseidenticalbranch.cool')

def test_missingclass():
    with pytest.raises(missingclass):
        compile('src/resources/semantic/input/missingclass.cool')

def test_outofscope():
    with pytest.raises(outofscope):
        compile('src/resources/semantic/input/outofscope.cool')

def test_redefinedclass():
    with pytest.raises(redefinedclass):
        compile('src/resources/semantic/input/redefinedclass.cool')

def test_returntypenoexist():
    with pytest.raises(returntypenoexist):
        compile('src/resources/semantic/input/returntypenoexist.cool')

def test_selftypebadreturn():
    with pytest.raises(selftypebadreturn):
        compile('src/resources/semantic/input/selftypebadreturn.cool')