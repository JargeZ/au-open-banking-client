#
#  This file was a quick attempt to make a modification via ast,
#  until I quickly realized that it was simply easier to make
#  patches for the openapi contract
#
import ast
from pathlib import Path

API_PATH = 'spec/au_open_banking_spec/api'

def main():
    for file in Path(API_PATH).glob('*.py'):
        with open(file, 'r') as source:
            code = source.read()

        tree = ast.parse(code)
        new_tree = modify_tree(tree)
        modified_code = ast.unparse(new_tree)

        with open(file, 'w') as source:
            source.write(modified_code)


def modify_tree(tree: ast.AST) -> ast.AST:
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):  # Check if the node is a class
            for method in node.body:  # Iterate over the methods in the class
                if isinstance(method, ast.FunctionDef):  # Check if the node is a function
                    for arg in method.args.args:  # Iterate over the arguments of the function
                        if arg.arg == 'x_v':
                            if arg.annotation is not None:
                                if isinstance(arg.annotation, ast.Subscript) and isinstance(arg.annotation.value, ast.Name) and arg.annotation.value.id == 'Annotated':
                                    # Обработка аннотаций типов Annotated
                                    old_annotation = arg.annotation.slice.value.elts[0]
                                    new_annotation = ast.parse(f'Union[None, {ast.unparse(old_annotation)}]').body[0].value
                                    arg.annotation.slice.value.elts[0] = new_annotation
                                else:
                                    # Обработка обычных аннотаций типов
                                    arg.annotation = ast.parse(f'Union[None, {ast.unparse(arg.annotation)}]').body[0].value
                            else:
                                arg.annotation = ast.parse('Union[None]').body[0].value
                            arg.default = ast.NameConstant(None)
    return tree

if __name__ == '__main__':
    main()
