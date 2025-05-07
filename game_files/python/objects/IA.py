import torch
import torch.nn.functional as F
import torch.optim as optim

# === Paramètres d'initialisation ===
taille_etat = 6          # Taille de l'état (vecteur des informations du jeu)
taille_action = 3        # Nombre d'actions possibles : 0 = rester, 1 = frapper, 2 = se déplacer
gamma = 0.99             # Facteur de réduction pour la récompense future
learning_rate = 0.001    # Taux d'apprentissage

# === Création des couches du modèle ===
fc1 = torch.nn.Linear(taille_etat, 64)  # Première couche (6 entrées)
fc2 = torch.nn.Linear(64, taille_action)  # Deuxième couche (3 sorties)

# === Fonction de prédiction ===
def model_forward(x):
    x = F.relu(fc1(x))  # Activation ReLU pour non-linéarité
    x = fc2(x)          # Sortie finale (valeurs pour chaque action)
    return x

# === Fonction de perte ===
loss_fn = torch.nn.MSELoss()

# === Optimiseur ===
params = list(fc1.parameters()) + list(fc2.parameters())
optimizer = optim.Adam(params, lr=learning_rate)

# === Initialisation de l'état du jeu ===
def reset_state():
    # Exemple d'état initial (à adapter à ton jeu)
    # Exemple : [position_monstre, position_joueur, obstacles_proches, etc.]
    state = [0.5, 0.2, 0.8, 0.1, 0.0, 0.3]
    return torch.tensor(state, dtype=torch.float32)

# === Fonction principale qui choisit une action ===
def choose_action(state):
    # Choisir une action (exploitation : la meilleure action, exploration : choix aléatoire)
    with torch.no_grad():
        q_values = model_forward(state)
        action = torch.argmax(q_values).item()  # Action avec la plus grande valeur
    return action

# === Apprentissage après une action ===
def learn(state, action, reward, next_state):
    # Calculer la cible (récompense actuelle + futur possible)
    with torch.no_grad():
        target = reward + gamma * torch.max(model_forward(next_state))

    # Prédiction actuelle pour l'action faite
    prediction = model_forward(state)[action]

    # Calculer la perte (différence entre prédiction et cible)
    loss = loss_fn(prediction, target)

    # Rétropropagation et mise à jour des poids
    optimizer.zero_grad()  # Réinitialise les gradients
    loss.backward()        # Rétropropagation
    optimizer.step()       # Mise à jour des poids

# === Initialisation ===
state = reset_state()  # Réinitialiser l'état du jeu à chaque nouvelle partie ou boucle

# Exemple de boucle (remplace avec la logique de ton jeu)
def run_game_step(action, reward):
    # Simule l'évolution de l'état du jeu (cela doit être remplacé par ta logique de jeu)
    next_state = state  # Par exemple, dans un vrai jeu, l'état serait mis à jour
    if action == 0:  # Rester
        print("L'IA reste sur place")
    elif action == 1:  # Frapper
        print("L'IA frappe")
    elif action == 2:  # Se déplacer
        print("L'IA se déplace")

    # Apprentissage basé sur la récompense
    learn(state, action, reward, next_state)
    return next_state
