class Node:
    def __init__(self, name, amount=0.0, parent=None):
        self.name = name
        self.amount = amount
        self.parent = parent
        self.children = []

        if parent:
            self.parent.children.append(self)


root = Node('Total', amount=1000000.0)
node1 = Node('Bonos', amount=300000.0, parent=root)
node2 = Node('Acciones', amount=700000.0, parent=root)
node3 = Node('Bonos US', amount=100000.0, parent=node1)
node4 = Node('Bonos Chile', amount=200000.0, parent=node1)
node5 = Node('Acciones US', amount=500000.0, parent=node2)
node6 = Node('Acciones Chile', amount=200000.0, parent=node2)

"""
Implementa la función print_tree, que debe recibir como único argumento el nodo
raíz de un árbol e imprime los valores de name y amount de cada nodo
de forma ordenada y con la indentación del ejemplo.
Ejemplo:
>> print_tree(root)
Total: 1000000.0
  Bonos: 300000.0
    Bonos US: 100000.0
    Bonos Chile: 200000.0
  Acciones: 700000.0
    Acciones US: 500000.0
    Acciones Chile: 200000.0
>>
"""


def print_tree(root_node):
    #Nodo actual igual a la raiz
    nodoActual = root_node
    #Lista para almacenar los nodos visitados o impresos dentro del arbol para evitar la redundancia
    impresos = []
    # Variable para identar segun lo solicitado, de acuerdo al nivel en el que se encuentra el nodo
    ident = []

    #Variable auxiliar para detener el ciclo una vez impreso todos los nodos, al parecer DFS
    flag = True
    #Se imprime la informacion de la raiz
    print(nodoActual.name,":",nodoActual.amount)
    while flag:
        # Si el nodo actual es distinto de None, ya que al ir hacia arriba segun los impresos,
        # El parent de la Raiz es None, sirve para detener el ciclo una vez todos los nodos fueron impresos
        if nodoActual:
            #Si el  nodo actual tiene hijos
            if nodoActual.children:
                #Para cada uno de los hijos de todos los hijos del nodo actual
                for children in nodoActual.children:
                    #Si el hijo no se encuentra en los impresos se asignar el nuevo nodo actual
                    if children not in impresos:
                        #Se agrega identancion ya que se esta hablando de un nivel mas abajo
                        ident.append("  ")
                        
                        nodoActual = children
                        print(''.join(map(str,ident)),nodoActual.name,":",nodoActual.amount)
                        impresos.append(children)
                        break
                    # Si  el ultimo hijo del nodo actual se encuentra impreso
                    if nodoActual.children[len(nodoActual.children)-1] in impresos:
                        nodoActual = nodoActual.parent
                        ident = ident[:-1]
            #Si el nodo actual no tiene hijos
            else:
                nodoActual = nodoActual.parent
                ident = ident[:-1]
        #Si el nodo actual no existe
        else:
            flag = False


            


        
       

    pass


if __name__ == "__main__":
    print_tree(root)
