from redbaron import RedBaron


def read_source(input_file):
    """Parses the input_file into a RedBaron FST."""
    with open(input_file, "r") as source_code:
        red = RedBaron(source_code.read())
    return red


def write_source(red, input_file):
    """Overwrites the input_file once the FST has been modified."""
    with open(input_file, "w") as source_code:
        source_code.write(red.dumps())


def fix_imports(red):
    """Wrapper which fixes "from" style imports and then "import" style."""
    red = fix_standard_imports(red)
    red = fix_from_imports(red)
    return red


def fix_from_imports(red):
    """
    Converts "from" style imports to not use "flask.ext".

    Handles (with or without parens or linebreaks):
    from flask.ext.foo import bam --> from flask_foo import bam
    from flask.ext.foo.bar import bam --> from flask_foo.bar import bam
    from flask.ext import foo --> import flask_foo as foo
    """
    from_imports = red.find_all("FromImport")
    for node in from_imports:
        modules = node.value

        if modules[0].value != 'flask' and modules[1].value != 'ext':
            continue

        if len(modules) >= 3:
            name_str = ''
            if len(node.targets) == 1:
                name = node.targets[0].target
                module = node.targets[0].value

                if (name and name != module):
                    name_str = '%s as %s' % (module, name)
                else:
                    name_str = module
            else:
                for target in node.targets:
                    name_str += target.value

                    if not target.next:
                        continue

                    if (target.type == 'name_as_name'
                            and target.next.type != 'right_parenthesis'):
                        name_str += ', '

            modules_str = '.'.join([i.value for i in modules[2:]])

            node.replace('from flask_%s import %s'
                         % (modules_str, name_str))

        elif len(modules) == 2:
            module = node.modules()[0]
            node.replace("import flask_%s as %s"
                         % (module, module))
    return red


def fix_standard_imports(red):
    """
    Handles import modification in the form:
    import flask.ext.foo" --> import flask_foo
    """
    imports = red.find_all("ImportNode")
    for x, node in enumerate(imports):
        try:
            if (node.value[0].value[0].value == 'flask' and
               node.value[0].value[1].value == 'ext'):
                package = node.value[0].value[2].value
                name = node.names()[0].split('.')[-1]
                if name == package:
                    node.replace("import flask_%s" % (package))
                else:
                    node.replace("import flask_%s as %s" % (package, name))
        except IndexError:
            pass

    return red


def fix_function_calls(red):
    """
    Modifies function calls in the source to reflect import changes.

    Searches the AST for AtomtrailerNodes and replaces them.
    """
    atoms = red.find_all("Atomtrailers")
    for x, node in enumerate(atoms):
        try:
            if (node.value[0].value == 'flask' and
               node.value[1].value == 'ext'):
                params = _form_function_call(node)
                node.replace("flask_%s%s" % (node.value[2], params))
        except IndexError:
            pass

    return red


def _form_function_call(node):
    """
    Reconstructs function call strings when making attribute access calls.
    """
    node_vals = node.value
    output = "."
    for x, param in enumerate(node_vals[3::]):
        if param.dumps()[0] == "(":
            output = output[0:-1] + param.dumps()
            return output
        else:
            output += param.dumps() + "."


def fix_tester(string):
    """Wrapper which allows for testing when not running from shell."""
    ast = RedBaron(string)
    ast = fix_imports(ast)
    ast = fix_function_calls(ast)
    return ast.dumps()


def fix(input_file=None):
    """Wrapper for user argument checking and import fixing."""
    ast = read_source(input_file)
    ast = fix_imports(ast)
    ast = fix_function_calls(ast)
    write_source(ast, input_file)
