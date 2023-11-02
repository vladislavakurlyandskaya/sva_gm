"""
Module for tab template
"""

import ipywidgets 
from IPython.display import display
from ipywidgets import Layout

def get_tab_template(graph, output):
    title = ipywidgets.HTML(value='Добавление алгоритма (ов):')
    algorithms = {
        'Breadth first search': ['name', 'ID node'],
        'Depth first search': ['name', 'ID node'],
        'Simple loops': ['name'],
        'Maximal matching': ['name'],
        'Attribute assortativity coefficient': ['name', 'Attribute'],
        'Attribute assortativity matrix': ['name', 'Attribute'],
        'Pagerank': ['name'],
        'Floyd Warshall': ['name', 'Attribute'],
        'Ford Fulkerson': ['name', 'Source node', 'Target node', 'weight'],
        'Shortest path': ['name', 'Source node', 'Target node'],
        'Shortest distance': ['name', 'Source node', 'Target node'],
        'Edges features': ['name'],
        'Nodes features': ['name']
    }

    add_algorithm_btn = ipywidgets.Button(
        description = '\u2795',
        button_style='success',
        layout=Layout(width='300px')
    )

    algorithm_items_vbox = ipywidgets.VBox([])
    filter_vbox = ipywidgets.VBox([algorithm_items_vbox, add_algorithm_btn])

    create_template_btn = ipywidgets.Button(
        description = 'Создать шаблон',
        button_style='success',
        layout=Layout(width='300px')
    )

    def btn_on_click_remove_alg(btn):
        for i, ch in enumerate(algorithm_items_vbox.children):
            if btn == ch.children[-1]:
                break
        algorithm_items_vbox.children = algorithm_items_vbox.children[:i] + algorithm_items_vbox.children[i+1:]

    def btn_on_click_add_filter(btn=None):
        remove_algorithm_btn = ipywidgets.Button(
            description='\u2796',
            layout=Layout(width='150px')
        )
        remove_algorithm_btn.on_click(btn_on_click_remove_alg)

        algorithm_dropdown= ipywidgets.Dropdown(
            options = list(algorithms.keys()),
            description = 'Алгоритм:',
            style = {'description_width': 'initial'},
            value = None
        )
        def on_algorithm_change(change):
            text_fields.children = ()
            params = algorithms[algorithm_dropdown.value]
            if params:
                for param in params:
                    text_field = ipywidgets.Text(description = param)
                    text_fields.children += (text_field,)

        text_fields = ipywidgets.VBox()
        algorithm_dropdown.observe(on_algorithm_change, names='value')
        filter_item = ipywidgets.HBox([
            ipywidgets.VBox([algorithm_dropdown, text_fields]),
            remove_algorithm_btn,
        ])
        algorithm_items_vbox.children += (filter_item,)

    btn_on_click_add_filter()
    add_algorithm_btn.on_click(btn_on_click_add_filter)

    result_graph_filter = ipywidgets.VBox([
        title,
        filter_vbox,
        create_template_btn
    ])

    return result_graph_filter