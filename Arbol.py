import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


G = nx.Graph()


nodo_central = "Jspp"


familia = ["Claudia", "Alicia", "Liliana", "Oscar"]
barrio = ["Karlos", "Juanda", "Mateo", "Camila"]
universidad = ["Juan Felipe", "Alejandro", "Deiber", "María Alejandra", "Eddy"]


G.add_node(nodo_central, grupo="Centro")


for integrante in familia:
    G.add_node(integrante, grupo="Familia")
    G.add_edge(nodo_central, integrante)

for integrante in barrio:
    G.add_node(integrante, grupo="Barrio")
    G.add_edge(nodo_central, integrante)

for integrante in universidad:
    G.add_node(integrante, grupo="Universidad")
    G.add_edge(nodo_central, integrante)


G.add_edge("Claudia", "Alicia")
G.add_edge("Claudia", "Liliana")
G.add_edge("Alicia", "Liliana")
G.add_edge("Oscar", "Claudia")


G.add_edge("Karlos", "Juanda")
G.add_edge("Mateo", "Camila")
G.add_edge("Juanda", "Mateo")


G.add_edge("Juan Felipe", "Alejandro")
G.add_edge("Deiber", "María Alejandra")
G.add_edge("Alejandro", "Eddy")
G.add_edge("Juan Felipe", "María Alejandra")


G.add_edge("Karlos", "Juan Felipe")


colores_grupo = {
    "Centro": "#257FA9",      # agua
    "Familia": "#D0BB1D",     # Dorado
    "Barrio": "#D311CC",      # Rosa
    "Universidad": "#BD4040"  # Rojo
}


color_map = []
node_sizes = []

for node in G.nodes():
    grupo = G.nodes[node]["grupo"]
    color_map.append(colores_grupo[grupo])
    if node == nodo_central:
        node_sizes.append(2800)  
    else:
        node_sizes.append(1200)


plt.figure(figsize=(11, 9))
pos = nx.spring_layout(G, seed=42, k=0.55)


nx.draw_networkx_nodes(G, pos, node_color=color_map, node_size=node_sizes, alpha=0.9, edgecolors="black")
nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.6, edge_color="gray")
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold", font_family="sans-serif")


leyenda = [
    mpatches.Patch(color=colores_grupo["Centro"], label="Centro (Jspp)"),
    mpatches.Patch(color=colores_grupo["Familia"], label="Familia"),
    mpatches.Patch(color=colores_grupo["Barrio"], label="Amigos del Barrio"),
    mpatches.Patch(color=colores_grupo["Universidad"], label="Compañeros de Universidad")
]
plt.legend(handles=leyenda, loc="upper right", fontsize=10)

plt.title("Red Social Personal - Grafo de Comunidades", fontsize=14, fontweight="bold")
plt.axis("off")
plt.tight_layout()


plt.show()





