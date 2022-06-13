from main import compile
from util.exceptions import *

def test_assignment():
     compile('src/resources/semantic/input/assignment.cool')

def test_basic():
     compile('src/resources/semantic/input/basic.cool')

def test_basicclassestree():
    compile('src/resources/semantic/input/basicclassestree.cool')

def test_cells():
    compile('src/resources/semantic/input/cells.cool')

def test_classes():
    compile('src/resources/semantic/input/classes.cool')

def test_compare():
    compile('src/resources/semantic/input/compare.cool')

def test_comparisons():
    compile('src/resources/semantic/input/comparisons.cool')

def test_cycleinmethods():
    compile('src/resources/semantic/input/cycleinmethods.cool')

def test_dispatch():
    compile('src/resources/semantic/input/dispatch.cool')

def test_expressionblock():
    compile('src/resources/semantic/input/expressionblock.cool')

def test_forwardinherits():
    compile('src/resources/semantic/input/forwardinherits.cool')


def test_hairyscary():
    compile('src/resources/semantic/input/hairyscary.cool')

def test_if():
    compile('src/resources/semantic/input/if.cool')

def test_inheritsObject():
    compile('src/resources/semantic/input/inheritsObject.cool')

def test_initwithself():
    compile('src/resources/semantic/input/initwithself.cool')


def test_io():
    compile('src/resources/semantic/input/io.cool')


def test_isvoid():
    compile('src/resources/semantic/input/isvoid.cool')

def test_letinit():
    compile('src/resources/semantic/input/letinit.cool')

def test_letnoinit():
    compile('src/resources/semantic/input/letnoinit.cool')

def test_letselftype():
    compile('src/resources/semantic/input/letselftype.cool')

def test_letshadows():
    compile('src/resources/semantic/input/letshadows.cool')

def test_list():
    compile('src/resources/semantic/input/list.cool')

def test_methodcallsitself():
    compile('src/resources/semantic/input/methodcallsitself.cool')

def test_methodnameclash():
    compile('src/resources/semantic/input/methodnameclash.cool')


def test_neg():
    compile('src/resources/semantic/input/neg.cool')


def test_newselftype():
    compile('src/resources/semantic/input/newselftype.cool')


def test_objectdispatchabort():
    compile('src/resources/semantic/input/objectdispatchabort.cool')


def test_overriderenamearg():
    compile('src/resources/semantic/input/overriderenamearg.cool')

def test_overridingmethod():
    compile('src/resources/semantic/input/overridingmethod.cool')


def test_overridingmethod2():
    compile('src/resources/semantic/input/overridingmethod2.cool')


def test_overridingmethod3():
    compile('src/resources/semantic/input/overridingmethod3.cool')


def test_scopes():
    compile('src/resources/semantic/input/scopes.cool')

def test_simplearith():
    compile('src/resources/semantic/input/simplearith.cool')

def test_simplecase():
    compile('src/resources/semantic/input/simplecase.cool')


def test_staticdispatch():
    compile('src/resources/semantic/input/staticdispatch.cool')

def test_stringtest():
    compile('src/resources/semantic/input/stringtest.cool')

def test_subtypemethodreturn():
    compile('src/resources/semantic/input/subtypemethodreturn.cool')

def test_trickyatdispatch():
    compile('src/resources/semantic/input/trickyatdispatch.cool')