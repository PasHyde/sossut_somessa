
import re
import networkx as nx
import matplotlib.pyplot as plt

text = open("/path/to/the/file.txt", encoding='latin-1').read()
text = text.lower()
text = re.sub('[^qwertyuiopäölkjhgfdsazxcvbnm]+', ' ', text)
text = text.split()

def co_occurence(text):
    result = []
    result1 = []
    result2 = []
    position = 0
    sana_1 = 'sossu'
    sana_2 = 'sosiaality'
    for word in text:
        position += 1
        if word.startswith(sana_1):
           result1 += text[position-2:position]
           result2 += text[position-1:position+1]
        elif word.startswith(sana_2):
            result1 += text[position-2:position]
            result2 += text[position-1:position+1]
    result = list(zip(result1, result2))
    result = [x for x in result if "ja" not in x and "mutta" not in x and "niin" not in x and "joten" not in x and "myos" not in x and "vaikka" not in x
              and "vaan" not in x and "kaksi" not in x and "vaikka" not in x and "on" not in x and "kun" not in x and "oli" not in x
              and "viides" not in x and "etta" not in x and "nakemaanlisaksi" not in x and "muut" not in x and "jopa" not in x and "nyt" not in x and "yksi" not in x
              and "ei" not in x and "eraan" not in x and "ovat" not in x and "kavi" not in x]
    return result

def network(co_occurence):
    result1 = co_occurence(text)
    G = nx.Graph()
    new_values = []
    G.add_edges_from(result1)
    degrees = [G.degree[node] for node in G.nodes()]
    pos = nx.spring_layout(G, k=0.1, iterations=15, scale=2.0)
    for value in degrees:
        value = [value * 30]
        new_values += value
    degrees = new_values
    nx.draw_networkx_nodes(G, pos, node_size = degrees, node_color='pink')
    nx.draw_networkx_edges(G, pos, edge_color=['hotpink'], width=1.0, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=14, font_family="sans-serif", verticalalignment='center')
    ax = plt.gca()
    ax.margins(0.0)
    plt.axis("off")
    plt.show()
    return

tulos = network(co_occurence)
print(tulos)


