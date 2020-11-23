import ast
import sys
import tokenize

def read_file(filename):
    with tokenize.open(filename) as fd:
        return fd.read()

class BaseChecker(ast.NodeVisitor):
    def __init__(self):
        self.violations = []

    def check(self, paths):
        for filepath in paths:
            self.filename = filepath
            tree = ast.parse(read_file(filepath))
            self.visit(tree)

    def report(self):
        for violation in self.violations:
            filename, lineno, msg = violation
            print(filename + ":" + str(lineno) + ": " + msg)
            
class WrapDecoratorChecker(BaseChecker):
    msg = "@functools.wraps decorator used"

    def visit_FunctionDef(self, node):
        for decorator in node.decorator_list:
            if isinstance(decorator, ast.Call):
                if isinstance(decorator.func, ast.Attribute) and decorator.func.attr == "wraps":
                    self.violations.append((self.filename, node.lineno, self.msg))
                if isinstance(decorator.func, ast.Name) and decorator.func.id == "wraps":
                    self.violations.append((self.filename, node.lineno, self.msg))
      
        for child in node.body:
            self.visit(child)
            
if __name__ == '__main__':
    files = sys.argv[1:]
    checker = WrapDecoratorChecker()
    checker.check(files)
    checker.report()
