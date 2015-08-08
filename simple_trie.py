#!/usr/bin/python

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_key = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.leaf_nodes_num = 0

    def insert(self, str):
        """
        Insert a string into the trie
        @param: str - the string to be inserted
        @return: void
        """
        if len(str) == 0:
            return

        self.__insert(str, self.root)

    def __insert(self, str, root):
        """
        The worker recursive function to add the string, creating new TrieNode
        in the process.
        @param: str - the string to be inserted
        @return: void
        """
        if len(root.children) == 0 and root.is_key:
            # this is an existing leaf node. It will no longer be leaf node
            # after this insertion.
            self.leaf_nodes_num -= 1

        is_new_node = False
        if not str[0] in root.children:
            root.children[str[0]] = TrieNode()
            is_new_node = True

        node = root.children[str[0]]

        if len(str) > 1:
            self.__insert(str[1:], node)
        else:
            node.is_key = True

            # increment the leaf node counter only when it is a new node and
            # has no children
            if is_new_node and len(node.children) == 0:
                self.leaf_nodes_num += 1

    def search(self, str):
        """
        Check if the string exits in the trie, non_recursive implementation
        @param: str - a string query
        @return: boolean - True if str is in the trie, False otherwise.
        """
        node = self.root

        for ch in str:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False

        return node.is_key

    def has_prefix(self, prefix):
        """
        Check whether there exists any string in the trie that has a given
        prefix.
        @param: prefix - a string prefix
        @return: boolean - True if there is any string with the prefix is
                           in the trie. False otherwise.
        """
        node = self.root

        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False

        return True

    def starts_with_prefix(self, prefix):
        """
        Returns all valid strings in the trie with the given prefix, recursive
        implementation
        @param: str - a string prefix
        @return: auto_complete_list - the list of all valid strings in the trie
                 with the given prefix string.
        """
        node = self.root
        auto_complete_list = []

        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
            else:
                return auto_complete_list

        self.__populate_list(node, prefix, auto_complete_list)

        return auto_complete_list


    def __populate_list(self, root, str, auto_complete_list):
        """
        A worker recursive function that iterates through all valid strings in
        a given (sub) trie.

        @param: root - the (sub)trie
        @param: str - the str containing all characters from the path leading
                       to this (sub)trie
        @param: auto_complete_list - the answer list containing all valid
                                     strings, added when found.
        @return: void
        """
        # a leaf node
        if len(root.children.keys()) == 0:
            return

        # iterate through this level
        for ch, node in root.children.iteritems():
            cur_str = str + ch
            if node.is_key:
                # this captures the intermediate nodes that are keys
                # as well as the nodes that are parent to leaf nodes.
                auto_complete_list.append(cur_str)
            self.__populate_list(node, cur_str, auto_complete_list)
