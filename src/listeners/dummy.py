from util.exceptions import *
from antlr.coolListener import coolListener
from antlr.coolParser import coolParser

class dummyListener(coolListener):

    def __init__(self):
        self.selfTypeInformalParameter = False
        self.selfInformalParameter = False
        self.klassInheritsString = False
        self.klassInheritsBool = False
        self.klassInheritsSelf = False
        self.letHasNamedSelf = False
        self.selfAssignment = False
        self.klassSelfType = False
        self.hasNamedSelf = False
        self.klassObject = False
        self.klassInt = False
        self.main = False

    def enterKlass(self, ctx:coolParser.KlassContext):
        ctx_type = ctx.TYPE(0).getText()
        self.main = ctx_type == 'Main'
        self.klassInt = ctx_type == 'Int'
        self.klassObject = ctx_type == 'Object'
        self.klassSelfType = ctx_type == 'SELF_TYPE'
        if ctx.TYPE(1):
            ctx_type = ctx.TYPE(1).getText()
            self.klassInheritsBool = ctx_type == 'Bool'
            self.klassInheritsSelf = ctx_type == 'SELF_TYPE'
            self.klassInheritsString = ctx_type == 'String'
            

    def exitKlass(self, ctx:coolParser.KlassContext):
        if (not self.main):
            raise nomain()
        if self.klassInt:
            raise badredefineint()
        if self.klassObject:
            raise redefinedobject()
        if self.klassInheritsBool:
            raise inheritsbool()
        if self.klassInheritsSelf:
            raise inheritsselftype()
        if self.klassInheritsString:
            raise inheritsstring
        if self.klassSelfType:
            raise selftyperedeclared()

    def enterFeature(self, ctx: coolParser.FeatureContext):
        if ctx.ID().getText() == 'self':
            self.hasNamedSelf = True

    def exitFeature(self, ctx: coolParser.FeatureContext):
        if self.hasNamedSelf:
            raise anattributenamedself()
        if self.selfassignment:
            raise selfassignment()

    def enterExpr(self, ctx: coolParser.ExprContext):
        if ctx.ID() and ctx.ID().getText() == 'self':
            self.selfAssignment = True

    def exitExpr(self, ctx: coolParser.ExprContext):
        if self.selfAssignment:
            raise selfassignment()

    def enterFormal(self, ctx: coolParser.FormalContext):
        self.selfInformalParameter = ctx.ID().getText() == 'self'
        self.selfTypeInformalParameter = ctx.TYPE().getText() == 'SELF_TYPE'

    def exitFormal(self, ctx: coolParser.FormalContext):
        if self.selfInformalParameter:
            raise selfinformalparameter()
        if self.selfTypeInformalParameter:
            raise selftypeparameterposition()

    def enterLet_decl(self, ctx: coolParser.Let_declContext):
        self.letHasNamedSelf = ctx.ID().getText() == 'self'

    def exitLet_decl(self, ctx: coolParser.Let_declContext):
        if self.letHasNamedSelf:
            raise letself()
