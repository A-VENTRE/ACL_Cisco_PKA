import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Définition des nœuds
nodes = [
    # Routeurs
    'R1',
    'R2',
    'R3',
    'R4',

    # Switches
    'Switch Admin\nVLAN 100',
    'Switch User\nVLAN 200',
    'Switch DMZ\nVLAN 300',

    # PCs Admin
    'PC1\nNIC:192.168.100.10/24\nVLAN 100 (Admin)',
    'PC2\nNIC:192.168.100.20/24\nVLAN 100 (Admin)',
    'PC3\nNIC:192.168.100.30/24\nVLAN 100 (Admin)',

    # PCs User
    'PC4\nNIC:192.168.200.10/24\nVLAN 200 (User)',
    'PC5\nNIC:192.168.200.20/24\nVLAN 200 (User)',
    'PC6\nNIC:192.168.200.30/24\nVLAN 200 (User)',

    # Serveurs DMZ
    'Serveur Web\nNIC:192.168.300.10/24\nVLAN 300 (DMZ)',
    'Serveur DNS\nNIC:192.168.300.20/24\nVLAN 300 (DMZ)',

    # Internet et Serveur DNS Externe
    'Internet',
    'Serveur DNS Externe\n8.8.8.8',
]

G.add_nodes_from(nodes)

# Définition des liaisons avec interfaces
edges = [
    # Connexions entre routeurs pour la redondance
    ('R1', 'R2', {'interface': 'Serial0/1/0 - Serial0/1/0'}),
    ('R1', 'R3', {'interface': 'Serial0/1/1 - Serial0/1/1'}),
    ('R1', 'R4', {'interface': 'Serial0/2/0 - Serial0/2/0'}),
    ('R2', 'R3', {'interface': 'Serial0/2/0 - Serial0/2/0'}),
    ('R2', 'R4', {'interface': 'Serial0/1/1 - Serial0/1/1'}),
    ('R3', 'R4', {'interface': 'Serial0/2/1 - Serial0/2/1'}),

    # Connexions routeurs vers Switch Admin
    ('R1', 'Switch Admin\nVLAN 100', {'interface': 'Gig0/0/0 - Fa0/24'}),
    ('R2', 'Switch Admin\nVLAN 100', {'interface': 'Gig0/0/0 - Fa0/23'}),
    ('R3', 'Switch Admin\nVLAN 100', {'interface': 'Gig0/0/0 - Fa0/22'}),
    ('R4', 'Switch Admin\nVLAN 100', {'interface': 'Gig0/0/0 - Fa0/21'}),

    # Connexions Switch Admin vers PCs Admin
    ('Switch Admin\nVLAN 100', 'PC1\nNIC:192.168.100.10/24\nVLAN 100 (Admin)', {'interface': 'Fa0/1 - NIC'}),
    ('Switch Admin\nVLAN 100', 'PC2\nNIC:192.168.100.20/24\nVLAN 100 (Admin)', {'interface': 'Fa0/2 - NIC'}),
    ('Switch Admin\nVLAN 100', 'PC3\nNIC:192.168.100.30/24\nVLAN 100 (Admin)', {'interface': 'Fa0/3 - NIC'}),

    # Connexions routeurs vers Switch User
    ('R1', 'Switch User\nVLAN 200', {'interface': 'Gig0/0/1 - Fa0/24'}),
    ('R2', 'Switch User\nVLAN 200', {'interface': 'Gig0/0/1 - Fa0/23'}),
    ('R3', 'Switch User\nVLAN 200', {'interface': 'Gig0/0/1 - Fa0/22'}),
    ('R4', 'Switch User\nVLAN 200', {'interface': 'Gig0/0/1 - Fa0/21'}),

    # Connexions Switch User vers PCs User
    ('Switch User\nVLAN 200', 'PC4\nNIC:192.168.200.10/24\nVLAN 200 (User)', {'interface': 'Fa0/1 - NIC'}),
    ('Switch User\nVLAN 200', 'PC5\nNIC:192.168.200.20/24\nVLAN 200 (User)', {'interface': 'Fa0/2 - NIC'}),
    ('Switch User\nVLAN 200', 'PC6\nNIC:192.168.200.30/24\nVLAN 200 (User)', {'interface': 'Fa0/3 - NIC'}),

    # Connexions routeurs vers Switch DMZ
    ('R1', 'Switch DMZ\nVLAN 300', {'interface': 'Gig0/0/2 - Fa0/24'}),
    ('R2', 'Switch DMZ\nVLAN 300', {'interface': 'Gig0/0/2 - Fa0/23'}),
    ('R3', 'Switch DMZ\nVLAN 300', {'interface': 'Gig0/0/2 - Fa0/22'}),
    ('R4', 'Switch DMZ\nVLAN 300', {'interface': 'Gig0/0/2 - Fa0/21'}),

    # Connexions Switch DMZ vers Serveurs DMZ
    ('Switch DMZ\nVLAN 300', 'Serveur Web\nNIC:192.168.300.10/24\nVLAN 300 (DMZ)', {'interface': 'Fa0/1 - NIC'}),
    ('Switch DMZ\nVLAN 300', 'Serveur DNS\nNIC:192.168.300.20/24\nVLAN 300 (DMZ)', {'interface': 'Fa0/2 - NIC'}),

    # Connexions routeurs vers Internet
    ('R1', 'Internet', {'interface': 'Serial0/2/1 - ISP1'}),
    ('R2', 'Internet', {'interface': 'Serial0/2/1 - ISP2'}),
    ('R3', 'Internet', {'interface': 'Serial0/1/0 - ISP3'}),
    ('R4', 'Internet', {'interface': 'Serial0/1/0 - ISP4'}),

    # Connexion Internet vers Serveur DNS Externe
    ('Internet', 'Serveur DNS Externe\n8.8.8.8', {'interface': 'Public Network'}),
]

G.add_edges_from(edges)

# Positions des nœuds pour une meilleure visualisation
pos = {
    # Routeurs
    'R1': (-3, 2),
    'R2': (-1, 2),
    'R3': (1, 2),
    'R4': (3, 2),

    # Switches
    'Switch Admin\nVLAN 100': (-3, 0),
    'Switch User\nVLAN 200': (0, 0),
    'Switch DMZ\nVLAN 300': (3, 0),

    # PCs Admin
    'PC1\nNIC:192.168.100.10/24\nVLAN 100 (Admin)': (-4, -1),
    'PC2\nNIC:192.168.100.20/24\nVLAN 100 (Admin)': (-3, -1),
    'PC3\nNIC:192.168.100.30/24\nVLAN 100 (Admin)': (-2, -1),

    # PCs User
    'PC4\nNIC:192.168.200.10/24\nVLAN 200 (User)': (-1, -1),
    'PC5\nNIC:192.168.200.20/24\nVLAN 200 (User)': (0, -1),
    'PC6\nNIC:192.168.200.30/24\nVLAN 200 (User)': (1, -1),

    # Serveurs DMZ
    'Serveur Web\nNIC:192.168.300.10/24\nVLAN 300 (DMZ)': (2, -1),
    'Serveur DNS\nNIC:192.168.300.20/24\nVLAN 300 (DMZ)': (3, -1),

    # Internet et Serveur DNS Externe
    'Internet': (0, 4),
    'Serveur DNS Externe\n8.8.8.8': (0, 5),
}

# Définition des couleurs de nœuds selon le type de nœud
node_colors = []
for node in G.nodes():
    if 'VLAN 100' in node:
        node_colors.append('lightblue')
    elif 'VLAN 200' in node:
        node_colors.append('lightgreen')
    elif 'VLAN 300' in node:
        node_colors.append('lightpink')
    elif 'Internet' in node or 'Serveur DNS Externe' in node:
        node_colors.append('yellow')
    elif node.startswith('R'):
        node_colors.append('orange')  # Couleur pour les routeurs
    else:
        node_colors.append('grey')

# Dessiner le graphe
plt.figure(figsize=(15, 10))
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color=node_colors)
nx.draw_networkx_edges(G, pos)
edge_labels = nx.get_edge_attributes(G, 'interface')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
nx.draw_networkx_labels(G, pos, font_size=8)
plt.axis('off')
plt.title('Schéma Réseau avec VLANs, DMZ, Interfaces et Redondance')
plt.show()
