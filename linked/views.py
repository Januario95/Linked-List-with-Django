from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .linked_list import Node, LinkedList
import json


def index(request):
    return render(request, 'index.html', {})


def get_nodes(tree):
    arr = []
    for node in tree:
        arr.append(node.data)
    return arr


@api_view(['POST'])
def remove_node(request):
    data = json.loads(request.body)
    nodes = data['nodes']
    target_node = data['target_node']

    if target_node != '':
        lk_list = LinkedList(nodes)
        lk_list.remove_node(target_node)

    nodes = get_nodes(lk_list)
    data['nodes'] = nodes

    return Response({
        'target_node': target_node,
        'nodes': nodes
    })


@api_view(['POST'])
def linked_list_api(request):
    data = json.loads(request.body)
    operation = data['operation']
    target_node = data['target_node']
    new_node = data['new_node']
    nodes = data['nodes']

    data = {}

    if nodes == []:
        lk_list = LinkedList([new_node])
    else:
        lk_list = LinkedList(nodes)
        if operation == 'before':
            lk_list.add_before(target_node, Node(new_node))
        elif operation == 'after':
            lk_list.add_after(target_node, Node(new_node))

    nodes = get_nodes(lk_list)
    data['nodes'] = nodes

    return Response(data)
