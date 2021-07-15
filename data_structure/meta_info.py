# -*- coding:utf-8 -*-


class NodeMetaInfo(object):
    def __init__(self, node_id, key, key_path, data_type, data_source, children, is_list, unique_key, order_key,
                 special_rule):
        self.node_id = node_id
        self.key = key
        self.key_path = key_path
        self.data_type = data_type
        self.data_source = data_source
        self.children = children
        self._is_list = is_list
        self.unique_key = unique_key
        self.order_key = order_key
        self.special_rule = special_rule

    def add_child(self, child_id):
        self.children.append(child_id)

    def get_node_id(self):
        return self.node_id

    def get_key(self):
        return self.key

    def get_key_path(self):
        return self.key_path

    def get_data_type(self):
        return self.data_type

    def get_data_source(self):
        return self.data_source

    def is_list(self):
        return self._is_list

    def is_parent(self):
        return bool(self.children)

    def get_unique_child_key(self):
        return self.unique_key

    def get_order_key(self):
        return self.order_key

    def get_special_rule(self, source):
        if self.special_rule:
            return self.special_rule[self.data_source.index(source)]


class TreeMetaInfo(object):
    def __init__(self):
        self.roots = []
        self.node_metas = {}
        self.key_path_2_node = {}
        self.source_2_node = {}

    def init(self, config):
        temp_child_2_parent = {}
        for node_id, node_info in config.items():
            if not node_id.startswith('zhyl'):
                continue
            key = node_info['id']
            key_path = [key]
            parent = temp_child_2_parent.get(node_id)
            while parent:
                key_path.insert(0, self.node_metas[parent].get_key())
                parent = temp_child_2_parent.get(parent)
            key_path = '.'.join(key_path)
            data_type = node_info.get('data_type', None)
            source = node_info.get('source', [])
            children = node_info.get('child_list', [])
            is_list = node_info.get('is_list', False)
            unique_key = node_info.get('unique_key')
            order_key = node_info.get('order_key')
            special_rule = node_info.get('special_rules')
            node = NodeMetaInfo(node_id, key, key_path, data_type, source, children, is_list, unique_key, order_key,
                                special_rule)
            self.node_metas[node_id] = node

            for child in children:
                temp_child_2_parent[child] = node_id

            if node_id not in temp_child_2_parent:
                self.roots.append(node_id)
            assert not key_path in self.key_path_2_node
            self.key_path_2_node[key_path] = node_id
            for source_id in source:
                if source_id not in self.source_2_node:
                    self.source_2_node[source_id] = []
                self.source_2_node[source_id].append(node_id)

    def get_node_by_source(self, source):
        return self.source_2_node.get(source)

    def get_node_meta(self, node_id):
        return self.node_metas.get(node_id)

    def get_node_by_path(self, key_path):
        return self.get_node_meta(self.key_path_2_node.get(key_path))
