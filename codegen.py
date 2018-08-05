# -*- coding: utf-8 -*-

import json
import re

import click

REGEX = re.compile('((?:[A-Z]?[a-z\d]+)|(?:[A-Z\d]+))')


class Generator(object):

    def __init__(self, output, swagger):
        self.file = open(output, 'w', encoding='utf-8')
        self.indent_level = 0
        with open(swagger, mode='r', encoding='utf-8') as fp:
            self.swagger = json.load(fp)

    def write(self, s):
        self.file.write(s)

    def writeln(self, s):
        self.write(s)
        self.newline()

    def revert_indent(self, level=1):
        self.write('\n\n')
        self.indent_level -= level
        self.write('    ' * self.indent_level)

    def indent(self):
        self.write('    ')
        self.indent_level += 1

    def newline(self):
        self.write('\n')
        self.write('    ' * self.indent_level)

    def flush(self):
        self.file.flush()

    def close(self):
        self.file.close()

    def class_begin(self):
        self.write('class BitmexAdapter(metaclass=RequestMeta):\n')
        self.newline()
        self.indent()
        self.write_method('__init__', ['client'], [])
        self.indent()
        self.write('self.client = client')
        self.revert_indent()

    def write_doc(self, s):
        self.writeln('"""')
        self.writeln(s)
        self.writeln('"""')

    def gen(self):
        self.file_doc()
        self.newline()
        self.writeln('from psyduck.client.meta import RequestMeta')
        self.newline()
        self.newline()
        self.class_begin()
        for path, detail in self.swagger['paths'].items():
            for method, api in detail.items():
                self.write_api(api)
        self.revert_indent()
        self.flush()
        self.close()

    def file_doc(self):
        info = self.swagger['info']
        s = '{}\n\n{}'.format(info['title'], info['description'])
        self.write_doc(s)

    def write_api(self, api):
        method = self.get_method_name(api['operationId'])
        params = api['parameters']
        args = [p['name'] for p in params if p['required']]
        kwargs = [p['name'] for p in params if not p['required']]
        self.write_method(method, args, kwargs)
        self.indent()
        self.write_api_doc(api)
        self.write_call(api)
        self.revert_indent()

    def write_method(self, method, args, kwargs):
        self.write('def {method}(self'.format(method=method))
        if args:
            self.write(', ')
            self.write(', '.join(map(self.snake_format, args)))
        if kwargs:
            self.write(', ')
            self.write(', '.join(
                ['{}=None'.format(self.snake_format(k)) for k in kwargs]
            ))
        self.write('):')
        self.newline()

    def write_api_doc(self, api):
        self.writeln('"""')
        self.writeln(api['summary'])
        self.newline()
        for param in api['parameters']:
            desc = self.format_param_desc(param.get('description', ''))
            self.writeln(
                ':param {}: {}'.format(self.snake_format(param['name']), desc)
            )
        self.writeln('"""')

    def write_call(self, api):
        args = [p['name'] for p in api['parameters']]
        tag = api['tags'][0]
        method = api['operationId'].replace('.', '_')
        self.write(
            'return self.client.{tag}.{method}('.format(tag=tag, method=method)
        )
        self.write(', '.join(['{}={}'.format(
            arg, self.snake_format(arg)) for arg in args]
        ))
        self.write(').result()')

    def format_param_desc(self, desc):
        text = '\n' + '    ' * self.indent_level
        return desc.replace('\n\n', text)

    @classmethod
    def get_method_name(cls, operation_id):
        """Get method name from operation_id
        eg:
        Order.getOrders -> get_orders
        OrderBook.getL2 -> get_order_book_l2
        """

        tag, method = operation_id.split('.')
        words = re.findall(REGEX, method)
        if len(words) > 1 and (tag == words[1] or tag + 's' == words[1]):
            return cls.snake_format(''.join(words))
        return cls.snake_format(''.join([words[0], tag] + words[1:]))

    @classmethod
    def snake_format(cls, string):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


@click.command()
@click.option('--output', '-o')
@click.option('--swagger', '-s')
def generate(output, swagger):
    Generator(output, swagger).gen()


if __name__ == '__main__':
    generate()
