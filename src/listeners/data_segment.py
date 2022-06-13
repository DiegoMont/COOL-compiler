from antlr.coolListener import coolListener
from antlr.coolParser import coolParser
import util.asm as asm
from util.structure import _allClasses

class DataGenerator(coolListener):
    def __init__(self):
        self.result = ''
        self.constant = 0

    def enterProgram(self, ctx: coolParser.ProgramContext):
        self.result += asm.tpl_start_data

    def enterAttribute(self, ctx: coolParser.AttributeContext):
        ctx_type = ctx.type
        ctx_value = 0
        ctx_varname = ctx.ID().getText()
        if(ctx.expr()):
            ctx_value = ctx.expr().getText()
        if ctx_type == 'Int':
            self.result += asm.tpl_attribute.substitute(
                varname=ctx_varname,
                value=ctx_value
            )
        if ctx_type == 'String':
            self.result += asm.tpl_attribute_string.substitute(
                varname=ctx_varname,
                value= '""' if ctx_value == 0 else ctx_value
            )
        if ctx_type == 'Bool':
            self.result += asm.tpl_attribute.substitute(
                varname=ctx_varname,
                value = 0 if (ctx_value == 'false' or ctx_value == 0) else 1
            )
        ctx.code = ''

    def createDispatchTable (self):
        for name in _allClasses.keys():
            self.result += asm.tpl_dispatch_table.substitute(
                name = name, 
                methods = self.getMethods(_allClasses[name].methods)
            )

    def createClassNameTable(self):
        for name in _allClasses.keys():
            self.result += asm.tpl_classname_table.substitute(
                name = name
            )

    def exitProgram(self):
        self.createClassNameTable()
        self.createDispatchTable()
        self.genGlobalData()
        self.heapStart()

    def getMethods(self, methodTable):
        methods = []
        for method in methodTable.keys():
            methods.append(method)
            return methods