#!/usr/bin/python

from simple_trie import Trie
import unittest

class TrieTestEmpty(unittest.TestCase):
    def testEmptyTrie(self):
        self.simple_trie = Trie()
        self.assertFalse(self.simple_trie.search(""))

class TrieTestDuplicates(unittest.TestCase):
    def testDuplicateTrie(self):
        self.simple_trie = Trie()
        self.simple_trie.insert("aaaaaa")
        self.simple_trie.insert("aaaaaa")
        self.simple_trie.insert("aaaaaa")
        self.simple_trie.insert("aaaaaa")
        self.assertTrue(self.simple_trie.search("aaaaaa"))
        self.assertTrue(self.simple_trie.has_prefix("aaa"))
        self.assertFalse(self.simple_trie.has_prefix("c"))
        self.assertTrue(self.simple_trie.has_prefix(""))

class TrieTest1(unittest.TestCase):
    def setUp(self):
        self.simple_trie = Trie()
        self.simple_trie.insert("abcccc")
        self.simple_trie.insert("efffddd")
        self.simple_trie.insert("eff")
        self.simple_trie.insert("efff")
        self.simple_trie.insert("efffz")

    def testSearch(self):
        self.assertFalse(self.simple_trie.search("abcc"))
        self.assertTrue(self.simple_trie.search("abcccc"))
        self.assertTrue(self.simple_trie.search("efffddd"))
        self.assertFalse(self.simple_trie.search("efffdd"))

    def testStartsWithPrefix(self):
        self.assertEqual(
            self.simple_trie.starts_with_prefix("eff"),
            ['efff', 'efffz','efffddd'])
        self.assertEqual(self.simple_trie.starts_with_prefix("xf"), [])

class TrieTestLeafNodeNum(unittest.TestCase):
    def testLeafNodeNum1(self):
        self.simple_trie = Trie()
        self.simple_trie.insert("AK#Koyuk")
        self.simple_trie.insert("AK#Koyukuk")
        self.assertEqual(self.simple_trie.leaf_nodes_num, 1)

    def testLeafNodeNum2(self):
        self.simple_trie = Trie()
        self.simple_trie.insert("")
        self.simple_trie.insert("ssssssss")
        self.simple_trie.insert("sss")
        self.assertEqual(self.simple_trie.leaf_nodes_num, 1)
        self.simple_trie.insert("ssssssssssssssss")
        self.assertEqual(self.simple_trie.leaf_nodes_num, 1)
        self.simple_trie.insert("aaaassssssssssssssss")
        self.assertEqual(self.simple_trie.leaf_nodes_num, 2)

    def testLeafNodeNum3(self):
        self.simple_trie = Trie()
        self.simple_trie.insert("aaaaaa")
        self.simple_trie.insert("aaaaaa")
        self.assertEqual(self.simple_trie.leaf_nodes_num, 1)

if __name__ == "__main__":
    unittest.main()
