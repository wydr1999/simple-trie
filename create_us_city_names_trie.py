from simple_trie import Trie


# create a trie from city name only
us_city_names_trie = Trie()

total_us_city_names = 0

with open("./city_names") as f:
    for line in f:
        total_us_city_names += 1
        us_city_names_trie.insert(line)

print "total city: %d; total leaf nodes: %d" % (total_us_city_names, us_city_names_trie.leaf_nodes_num)

# create a trie from city name, but with state name as a prefix
us_state_city_names_trie = Trie()

total_us_state_city_names = 0

with open("./state_city_names") as f:
    for line in f:
        total_us_state_city_names += 1
        us_state_city_names_trie.insert(line.strip())

print "total state city: %d; total leaf nodes: %d" % (total_us_state_city_names, us_state_city_names_trie.leaf_nodes_num)


# create a trie from city name, but with state name as a postfix
us_city_state_names_trie = Trie()

total_us_city_state_names = 0

with open("./city_state_names") as f:
    for line in f:
        total_us_city_state_names += 1
        us_city_state_names_trie.insert(line.strip())

print "total city state: %d; total leaf nodes: %d" % (total_us_city_state_names, us_city_state_names_trie.leaf_nodes_num)
