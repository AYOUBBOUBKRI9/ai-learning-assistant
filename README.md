# 🤖 Assistant IA pour la formation et l'aide aux utilisateurs

**Application conversationnelle basée sur l'intelligence artificielle générative, développée avec Python, Streamlit et l'API Gemini.**

---

## 👨‍💻 Auteur

**MOHAMED AYOUB BOUBKRI**

---

## 📌 1. Présentation du projet

L'Assistant IA pour la formation et l'aide aux utilisateurs est une application web interactive conçue pour accompagner les utilisateurs dans leur apprentissage, répondre à leurs questions et faciliter la compréhension de notions professionnelles ou techniques.

L'application s'appuie sur un modèle de langage (LLM) accessible via l'API Gemini de Google. Elle permet à l'utilisateur de poser des questions en langage naturel et de recevoir des réponses générées par l'intelligence artificielle.

Le comportement de l'assistant est défini par un prompt système qui l'oriente vers la formation professionnelle, la pédagogie et l'assistance aux utilisateurs.

L'objectif est de concevoir une première version fonctionnelle d'un assistant conversationnel pouvant évoluer vers une solution plus complète d'accompagnement et de formation.

## 🎯 2. Objectifs du projet

- Développer un assistant conversationnel reposant sur un modèle de langage.
- Intégrer une API d'intelligence artificielle dans une application Python.
- Concevoir des prompts pour orienter les réponses du modèle.
- Maintenir le contexte des échanges grâce à un historique conversationnel.
- Développer une interface web interactive avec Streamlit.
- Gérer les erreurs liées aux appels API.
- Préparer une architecture évolutive permettant d'ajouter de nouvelles fonctionnalités.

## ⚙️ 3. Technologies utilisées

| Technologie | Utilisation |
|---|---|
| Python | Développement de la logique applicative |
| API Gemini | Génération des réponses par l'intelligence artificielle |
| Google GenAI SDK | Communication avec l'API Gemini |
| Streamlit | Développement de l'interface web |
| Google Colab | Environnement de développement et de test |
| ngrok | Exposition temporaire de l'application locale à travers un tunnel HTTP |
| Git et GitHub | Gestion de versions et hébergement du code source |

## 🏗️ 4. Architecture de l'application

L'application suit un fonctionnement simple :

1. L'utilisateur saisit une question dans l'interface Streamlit.
2. L'application récupère la question et l'historique de la conversation.
3. Le prompt système définit le comportement attendu de l'assistant.
4. Le SDK Google GenAI transmet la requête à l'API Gemini.
5. Le modèle génère une réponse.
6. L'application affiche la réponse et conserve l'échange dans l'historique de la session.

```text
                 UTILISATEUR
                      |
                      v
             INTERFACE STREAMLIT
                      |
                      v
              APPLICATION PYTHON
                /             \
               v               v
       PROMPT SYSTÈME    HISTORIQUE
                \             /
                 v           v
                 API GEMINI
                      |
                      v
             RÉPONSE GÉNÉRÉE
                      |
                      v
             AFFICHAGE DU TEXTE
```

## 🛠️ 5. Étapes de réalisation

### Étape 1 — Préparation de l'environnement

Le développement a commencé dans Google Colab, un environnement permettant d'exécuter du code Python dans des notebooks.

La bibliothèque Google GenAI a été installée afin de faciliter la communication avec les modèles Gemini.

```python
%pip install -q -U google-genai
```

### Étape 2 — Configuration de la clé API

Une clé API Gemini a été créée pour authentifier les requêtes envoyées au service.

La clé est conservée dans les secrets de Google Colab et récupérée au moment de l'exécution.

```python
from google.colab import userdata

api_key = userdata.get("GEMINI_API_KEY")
```

Cette méthode évite d'inscrire directement la clé dans le code source du notebook.

### Étape 3 — Initialisation du client Gemini

Le client permet à l'application d'envoyer des requêtes au modèle de langage.

```python
from google import genai

client = genai.Client(api_key=api_key)
```

Cette initialisation prépare les appels à l'API, sans générer de réponse à elle seule.

### Étape 4 — Premier appel au modèle

Une première requête a été réalisée pour vérifier que le programme pouvait envoyer une question et récupérer une réponse textuelle.

```python
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explique ce qu'est l'intelligence artificielle en trois phrases."
)

print(response.text)
```

Cette étape a permis de valider le principe de génération de texte à partir d'une requête Python.

### Étape 5 — Conception du prompt système

Un prompt système a été conçu pour orienter l'assistant vers la formation professionnelle et l'aide aux utilisateurs.

Il définit notamment :

- Le rôle et les objectifs de l'assistant.
- Le ton professionnel, pédagogique et bienveillant.
- La langue de réponse par défaut.
- La nécessité d'adapter les explications au niveau de l'utilisateur.
- Les règles de fiabilité et les limites de l'assistant.

Le prompt système permet de guider le comportement du modèle sans modifier son entraînement.

### Étape 6 — Gestion de l'historique conversationnel

Une liste Python a été utilisée pour conserver les messages de l'utilisateur et les réponses du modèle.

```python
conversation_history = []
```

À chaque échange réussi, la question et la réponse sont ajoutées à l'historique.

Les messages précédents peuvent ainsi être transmis au modèle pour maintenir le contexte de la conversation.

Cette première implémentation conserve l'historique en mémoire pendant l'exécution et ne constitue pas un stockage permanent.

### Étape 7 — Création de la fonction conversationnelle

Une fonction Python `chat()` a été développée pour centraliser le traitement des questions.

Elle permet de :

- Vérifier que la question n'est pas vide.
- Préparer le contexte conversationnel.
- Appeler l'API Gemini.
- Récupérer la réponse textuelle.
- Enregistrer les échanges réussis.
- Intercepter les exceptions et afficher un message d'erreur compréhensible.

Une limite sur le nombre de messages transmis a également été introduite dans le prototype afin de réduire la taille du contexte envoyé au modèle.

### Étape 8 — Développement de l'interface Streamlit

Une interface web a été développée pour permettre une utilisation interactive de l'assistant.

Elle comprend :

- Un titre et une présentation de l'application.
- Une zone de saisie pour les questions.
- L'affichage des messages de l'utilisateur et de l'assistant.
- Un indicateur de chargement pendant la génération.
- Un bouton permettant de démarrer une nouvelle conversation.
- Des messages d'erreur en cas d'échec de génération.

Streamlit permet de construire cette interface directement en Python.

### Étape 9 — Exécution et accès à l'application

L'application a été exécutée dans l'environnement Google Colab avec Streamlit.

Un tunnel ngrok a été utilisé pour accéder temporairement à l'interface depuis le navigateur.

Cette solution sert à la démonstration et aux tests. Elle ne remplace pas un déploiement permanent sur une plateforme d'hébergement.

### Étape 10 — Tests et gestion des erreurs

Plusieurs difficultés techniques ont été rencontrées durant l'intégration :

- Indisponibilité de certains modèles.
- Erreurs temporaires de serveur HTTP 503.
- Problèmes de récupération des secrets dans Google Colab.
- Nécessité de distinguer les erreurs du service de celles du code.

Ces difficultés ont conduit à tester les modèles accessibles, à vérifier la configuration des secrets et à améliorer le diagnostic des erreurs.

## 💻 6. Organisation des fichiers

```text
ai-learning-assistant/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

| Fichier | Description |
|---|---|
| `app.py` | Code principal de l'application Streamlit et intégration Gemini |
| `requirements.txt` | Liste des bibliothèques Python nécessaires |
| `README.md` | Présentation et documentation du projet |
| `.gitignore` | Liste des fichiers et secrets à exclure du dépôt Git |

## 🚀 7. Installation et exécution

### Prérequis

- Python 3.10 ou version compatible avec les dépendances installées.
- Une clé API Gemini valide.
- Git pour récupérer le dépôt.

### Étape 1 — Cloner le dépôt

```bash
git clone https://github.com/TON-PSEUDO-GITHUB/ai-learning-assistant.git
cd ai-learning-assistant
```

Remplacer `TON-PSEUDO-GITHUB` par le nom d'utilisateur GitHub associé au dépôt.

### Étape 2 — Installer les dépendances

```bash
pip install -r requirements.txt
```

### Étape 3 — Configurer la clé API

Sous Linux ou macOS :

```bash
export GEMINI_API_KEY="votre_cle_api"
```

Sous Windows PowerShell :

```powershell
$env:GEMINI_API_KEY="votre_cle_api"
```

La clé doit être configurée dans l'environnement d'exécution et ne doit jamais être publiée dans le dépôt.

### Étape 4 — Lancer l'application

```bash
streamlit run app.py
```

L'application peut ensuite être ouverte dans le navigateur à l'adresse locale indiquée par Streamlit.

**Remarque :** le code de démonstration initial a été conçu dans Google Colab. Avant une exécution autonome sur un ordinateur, il faut vérifier que `app.py` récupère bien la clé via `os.environ` et qu'il ne dépend plus de `google.colab.userdata`.

## 🔐 8. Sécurité

La sécurité des identifiants est essentielle dans une application connectée à une API externe.

Les bonnes pratiques appliquées ou prévues comprennent :

- Ne pas inscrire les clés API directement dans le code source.
- Utiliser des variables d'environnement ou un gestionnaire de secrets.
- Exclure les fichiers sensibles avec `.gitignore`.
- Ne pas publier de jeton ngrok.
- Ne pas exposer publiquement une application de démonstration sans é
