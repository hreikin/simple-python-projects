from anytree import Node, RenderTree

source_txt = "output/url-list.txt"
output_txt = "output/tree-view.txt"
domain = "https://princetonscientific.com/"


with open(source_txt, "r") as stream:
    for line in stream:
        extracted_line = stream.read()

url_list = extracted_line.split("\n")
url_list.pop(-1)

stripped_list = []
for item in url_list:
    new_item = str(item).replace(domain, "")
    stripped_list.append(new_item)

stripped_list.pop(-1)

separated_list = []
for item in stripped_list:
    wip_item = str(item).split("/")
    wip_item.insert(0, "home")
    wip_item.pop(-1)
    separated_list.append(wip_item)

# if you have multiple nodes with the same name you can not use the dict version 
# below; you need to iterate from the root node over the children:
#
# def list_to_anytree(list_of_lists):
#     root_name = list_of_lists[0][0]
#     root_node = Node(root_name)
#     nodes = {root_name: root_node}  # keeping a dict of the nodes
#     for branch in list_of_lists:
#         assert branch[0] == root_name
#         for parent_name, node_name in zip(branch, branch[1:]):
#             node = nodes.setdefault(node_name, Node(node_name))
#             parent_node = nodes[parent_name]
#             if node.parent is not None:
#                 assert node.parent.name == parent_name
#             else:
#                 node.parent = parent_node
#     return root_node

def list_to_anytree(list_of_lists):
    root_name = list_of_lists[0][0]
    root_node = Node(root_name)
    for branch in list_of_lists:
        parent_node = root_node
        assert branch[0] == parent_node.name
        for cur_node_name in branch[1:]:
            cur_node = next(
                (node for node in parent_node.children if node.name == cur_node_name),
                None,
            )
            if cur_node is None:
                cur_node = Node(cur_node_name, parent=parent_node)
            parent_node = cur_node
    return root_node


anytree = list_to_anytree(separated_list)
with open(output_txt, "w") as stream:
    for pre, fill, node in RenderTree(anytree):
        stream.write(f"{pre}{node.name}" + "\n")