from antlr4 import *
from antlr.coolLexer import coolLexer
from antlr.coolParser import coolParser

from listeners.semantic_one import semanticOneListener
from listeners.semantic_two import semanticTwoListener
from listeners.semantic_three import semanticThreeListener
from listeners.tree import TreePrinter
from listeners.data_segment import DataGenerator

def compile(file):
    parser = coolParser(CommonTokenStream(coolLexer(FileStream(file))))
    tree = parser.program()
    dataGen = DataGenerator() 
    walker = ParseTreeWalker()
    
    walker.walk(semanticOneListener(), tree)
    walker.walk(semanticTwoListener(), tree)
    walker.walk(semanticThreeListener(), tree)
    walker.walk(TreePrinter(), tree)

    #walker.walk(dataGen, tree)
    #with open('test.asm', 'w') as writer:
    #    writer.write(dataGen.result)

if __name__ == '__main__':
    compile('resources/semantic/input/hairyscary.cool')
