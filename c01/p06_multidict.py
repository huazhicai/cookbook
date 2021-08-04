# topic: 多值映射

from collections import defaultdict, ChainMap, Counter
import os, argparse


def multi_dict():
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)

    d = defaultdict(set)
    d['a'].add(1)
    d['b'].add(2)
    d['a'].add(4)

    d = {}  # a regular dictionary
    d.setdefault('a', []).append(1)
    d.setdefault('a', []).append(2)
    d.setdefault('b', []).append(4)


# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
print(vars(namespace))
command_line_args = {k: v for k, v in vars(namespace).items() if v}

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

c = Counter()
for i in 'programing':
    c[i] = c[i] + 1

print(c)
