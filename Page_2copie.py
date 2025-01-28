import streamlit as st

# Informations de profil
profile = """
Data Addict, diplômé d’un master data management et certifié expert en stratégie digitale, j’ai acquis au cours de mon parcours une très bonne expérience dans l’analyse de larges variétés de données, dans la recherche et la détection d’insights pertinents ainsi que dans la construction d’outils d’aide à la décision.

Mon expérience, associée à ma curiosité et à mon dynamisme, m’a également permis de mener plusieurs projets significatifs tout en développant plusieurs compétences techniques tels qu’en Python, R, SQL, Excel avancé et power Bi.

Au-delà de mes compétences techniques, j'ai développé un sens aigu de la collaboration tout au long de mon parcours. Travaillant étroitement avec différentes équipes, j'ai appris à écouter et à comprendre leurs besoins spécifiques, ce qui m'a permis de proposer des solutions sur mesure favorisant l’amélioration des performances.
"""

# Formations
formations = """

- **<span style='color:blue;'>MSC Data management, Efrei Paris / Paris School of Business, 2022-2024</span>**

  **<u>Mention :</u>** Bien

  Le MSc Data Management forme les futurs décideurs aux problématiques transverses liées à la création de valeur à partir des Big Data. 
  
  **<u>Compétences :</u>** Gestion de projet · Tableau · Big data · SQL · Bases de données · Analyse de données · Résolution de problèmes · Visualisation de données · R · Développement de bases de données · Microsoft PowerPoint · Amélioration des processus · Python (langage de programmation) · Microsoft Excel · Stratégie marketing · Anglais

- **<span style='color:blue;'>MSC1 Data scientist & Business analysis, EDC Paris Business School, 2021-2022</span>**

  **<u>Mention :</u>** Bien

  Développer les compétences de base en big data. Faire des data scientists de véritables business partners.
  
  **<u>Compétences :</u>** Gestion de projet · Tableau · Big data · SQL · Bases de données · Analyse de données · Analyse financière · Résolution de problèmes · Visualisation de données · Microsoft Power BI · R · Présentation d’idées · Microsoft PowerPoint · Python (langage de programmation) · Microsoft Excel · Parler en public · Analyse des affaires · Anglais

- **<span style='color:blue;'>Licence Management des entreprises, IHEM - Bamako Mali, 2017-2020</span>**

  **<u>Mention :</u>** Bien

  Cette licence forme les cadres aux métiers du management et permet aux étudiants d’acquérir des méthodes de travail pouvant être transposées facilement dans le monde professionnel.
   
  **<u>Compétences :</u>** Gestion de projet · Management · Analyse financière · Marketing digital · Microsoft PowerPoint · Microsoft Excel · Stratégie marketing · Analyse des affaires · Anglais · Amélioration des processus d’affaires · Études de marché
"""

# Expériences
experiences = """

- **<span style='color:blue;'>Consultant chef de projets SIt**, CLAP PARTNERS - Paris, 08/2024 - Aujourd’hui</span>**

  -Analyse des données projets avec suivi des performances et mise en œuvre des actions correctives.
  -Conception d’indicateurs clés (KPI) et création de tableaux de bord pour un pilotage efficace des budgets projets, de la qualité des données et une prise de décision éclairée.
  -Gestion des dépassements de projets avec identification des écarts, analyse des causes et recommandations d’amélioration.
  -Gestion des ressources avec analyse des staffings et planification des besoins prévisionnels.
  -Organisation des comités projets avec animation des réunions clients et préparation des supports stratégiques.
  -Suivi, planification et gestion des projets SI avec pilotage des activités, coordination des équipes et respect des délais.


- **<span style='color:blue;'>Business analyst**, VWR AVANTOR - Paris, 10/2022 - Aujourd’hui</span>**

  - Collecte, traitement et analyse des données business sur 4 pays.
  - Détection d’insights exploitables pour le processus de digitalisation de l’entreprise.
  - Mise en place et analyse d’impacts de stratégies marketing et marketing digital.
  - Automatisation de la classification des clients en fonction de leurs performances.
  - Développement, suivi et actualisation régulière de tableaux de bord dynamiques et autres solutions data pour les équipes métiers.
  
- **<span style='color:blue;'>Data analyst - Stage**, MOBY-DECK - Paris, 04/2022 - 06/2022</span>**
  
  - Analyse et traitement des données.
  - Automatisation de la classification des véhicules selon des critères spécifiques.
  - Collecte des données et établissement d’une base de plus de 32000 datas de 8000 modèles de véhicules.
  
- **<span style='color:blue;'>Auto-entrepreneur**, SOUM MARO - Mali, 10/2020 - 08/2021</span>**

  - Définition des différentes stratégies commerciales et marketing. 
  - Communication avec les clients pour recueillir leurs besoins et garantir leur satisfaction.
  - Gestion des commandes spécifiques des clients.
  - Gestion des stocks de matériaux et de produits finis.
  - Négociation avec les différents partenaires.

- **<span style='color:blue;'>Data Analyst**, ORANGE - Mali, 07/2019 - 09/2019</span>**

  - Analyses ponctuelles sur la satisfaction client et les motifs d’insatisfaction. 
  - Collecte des données de satisfaction client.
  - Reporting des résultats sur l’évolution de la relation client.
"""

# Certifications
certifications = """
- Expert en stratégie digitale (Digital campus)
- Concevoir une solution de déploiement de modèle (Microsoft)
- Concevoir une solution de formation de modèle Machine Learning (Microsoft)
- Understand Machine learning (DataCamp)
- Analyst de Données (Microsoft)
- Data analysis industry training (Brainnest)
- R Programming (DataCamp)
- Python Fundamentals (DataCamp)
- Intermediate SQL (DataCamp)
- Data Visualization in Power BI (DataCamp)
- Introduction to DAX in Power BI (DataCamp)
- Excel: Les formules avancées (Linkedin Learning)
- Apprenez à coder en C (OpenClassroom)
"""

# Langues
langues = """
- English : Despite not growing up in an English-speaking country, I have developed a professional level of the English language through self-study and formal education. Today, I am fully capable of engaging in conversations, comprehending entire documents, and writing proficiently.
- Français : Ayant vécu dans un pays où la langue officielle est le français, je le maîtrise parfaitement à l'écrit, à l'oral et en compréhension écrite.
"""

# Projets
projets = """
1. **<span style='color:blue;'>Élaboration d’un dashboard en ligne analysant l’évolution des crimes dans chaque région française</span>**
   - J’ai élaboré un dashboard interactif en ligne pour analyser l'évolution des crimes dans chaque région française. Les données nécessaires ont été obtenues à partir de la plateforme data.gouv, sous forme de fichiers CSV.
   - Python a été utilisé pour le traitement des données et la création du dashboard, tandis que Streamlit a servi pour le déploiement et l'interaction avec l'interface utilisateur.
   - Les données ont été importées, nettoyées et traitées à l'aide de bibliothèques Python telles que Pandas et NumPy. Ensuite, un dashboard interactif a été créé à l'aide de Streamlit, où les utilisateurs pouvaient visualiser différentes métriques de crime (par exemple, crimes par régions, évolution temporelle à travers une régression, comparaison du niveau de dangerosité des régions, etc.).
   
2. **<span style='color:blue;'>Analyse de la rétention client (customer churn) pour une entreprise téléphonique</span>**
   - Ce projet était un projet pour une certification LinkedIn Learning. J’ai effectué Une analyse de la rétention client pour une entreprise téléphonique pour comprendre et prévenir le churn, c'est-à-dire la perte de clients. Les données nécessaires pour cette analyse ont été fournies par l'entreprise ou étaient disponibles dans des ensembles de données publics.
   - Power BI, une plateforme d'analyse commerciale de Microsoft, a été utilisée pour cette analyse.
   - Les données sur les clients, telles que les habitudes d'utilisation, la durée de l'abonnement, les services utilisés, etc., ont été importées dans Power BI. Ensuite, des visualisations et des analyses ont été créées pour identifier les tendances de churn et les facteurs qui y sont associés.
   
3. **<span style='color:blue;'>Analyse prédictive de l’indice d'égalité homme/femme</span>**
   - Une analyse prédictive de l'indice d'égalité homme/femme a été réalisée en utilisant des données obtenues sur data.gouv. L'objectif était de comprendre les tendances passées et de prédire l'évolution.
   
4. **<span style='color:blue;'>Élaboration d’un dashboard automatisé pour l’analyse des performances commerciales sur 4 pays</span>**
   - **Description du projet** : J’ai élaboré Un dashboard automatisé pour analyser les performances commerciales dans quatre pays différents (France, Belgique, Espagne et Portugal). Les données nécessaires ont été extraites de QlickView.
   - **Outils utilisés** : qickView a été utilisé pour l’extraction des données et une macro Excel a été utilisé pour la création du dashboard automatisé.
   - **Méthodologie** : Les données de performance commerciale pour les quatre pays ont été importées dans Excel. Des tableaux de bord interactifs ont été créés en utilisant la macro excel, les graphiques et les formules automatisées pour calculer les indicateurs clés de performance (KPI) pertinents.
   - **Livraison** : Le dashboard final a été mis à la disposition de l'équipe E-Business de l'entreprise, facilitant ainsi le suivi des performances et la prise de décision basée sur des données pour chaque pays.
"""

# Vie Associative
vie_associative = """
- **<span style='color:blue;'>Représentant des étudiants ALJT Vitry (2024)</span>**  
  - En tant que représentant des étudiants ALJT à Vitry en 2024, j'ai servi en tant que voix des résidents, facilitant la communication entre les étudiants et l'administration de la résidence. J'ai organisé des ateliers et des événements sociaux pour promouvoir l'intégration et le bien-être des résidents, tout en travaillant à résoudre les préoccupations quotidiennes des étudiants.
  
- **<span style='color:blue;'>Délégué du MSC Data management (2022 - 2023)</span>**  
  - En tant que délégué des Masters à la PSB, j'ai représenté mes pairs, aidé à organiser des événements académiques, et agi comme un lien entre les étudiants et le corps professoral pour résoudre les problèmes académiques et administratifs.
  
- **<span style='color:blue;'>Délégué MSc Data Science & Business Analytics (2021 - 2022)</span>**  
  - En tant que délégué du MSc en Data Science & Business Analytics, j'ai contribué à créer un environnement d'apprentissage collaboratif et inclusif pour mes camarades de classe. J'ai facilité la communication entre les étudiants et les enseignants, et encouragé la coopération entre les différentes cohortes du programme.
  
- **<span style='color:blue;'>Président du club sport IHEM (2018 - 2020)</span>**  
  - En tant que président du club sport à l'IHEM, j'ai dirigé une équipe dévouée dans l'organisation d'activités sportives variées pour les étudiants. J'ai recherché des financements, planifié des événements et des tournois interclasses, et promu une culture du sport et du bien-être au sein de la communauté étudiante.
  
- **<span style='color:blue;'>Membre du BDE IHEM (2018 - 2020)</span>**  
  - En tant que membre du Bureau des Étudiants à l'IHEM, j'ai participé à la planification et à l'organisation d'événements sociaux, culturels et académiques pour enrichir l'expérience étudiante. J'ai travaillé en équipe pour créer un environnement dynamique et inclusif, favorisant l'engagement et la camaraderie entre les étudiants.
"""

# Recommandations
recommandations = """
- « Sa capacité à appliquer ses connaissances de manière innovante dans des projets concrets a grandement contribué à la réussite de ceux-ci. »  
  **O. MAMAVI**, Docteur en Sciences de gestion, directeur des données chez Management & Datascience, professeur associé à Paris School of Business

- « Sa facilité à coordonner et à motiver ses camarades reflète ses fortes aptitudes en management et leadership, des qualités qui le rendent particulièrement bien adapté pour exceller. »  
  **O. MAMAVI**, Docteur en Sciences de gestion, directeur des données chez Management & Datascience, professeur associé à Paris School of Business
  
- « Je voudrais en toute honnêteté exprimer ma très grande satisfaction et confiance en ses qualités personnelles, sur un plan disciplinaire et intellectuel mais aussi son assiduité et son engagement caractérisé par un dynamisme tangible et constant dans le travail individuel et collectif. »  
  **I. TRAORE**, Psychologue et manager des organisations
  
- « Monsieur SOUMANO s’est toujours distingué par sa discipline, son sérieux au travail, son sens élevé du devoir et du travail bien fait. »  
  **Dr O. MAIGA**, Enseignant / Chercheur, Maître Assistant en Sciences économiques

- « Par la présente lettre, je confirme ainsi ma pleine confiance en sa personne, en ses capacités d’adaptation et en toute la rigueur dont j’ai pu être témoin de sa part. »  
  **Marie TRAORE**, Responsable qualité et process Orange MALI

- « Bienveillant, motivant et empathique. Je n'aurais pas pu compter sur un meilleur collaborateur: son sens du collectif et son attachement à l'humain sont évidents, et font de lui un professionnel compétent et unique. »  
  **M ICHE**, Développeur web chez Bpartner
"""

# Informations de contact
contact_info = {
    "Nom et Prénom": "SOUMANO Seydou",
    "E-mail": "soumanoseydou@icloud.com",
    "Téléphone": "+33 6 64 67 88 87",
    "LinkedIn": "https://linkedin.com/in/seydou-soumano",
    "Github": "https://github.com/Ssoumano",
}

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à", ["Accueil", "Formations", "Expériences", "Stack techniques et Soft Skills", "Certifications", "Langues", "Projets", "Vie Associative", "Recommandations", "Contact"])

# Main content
if page == "Accueil":
    st.markdown(
        """
        <div style='text-align: center; color: blue;'>
            <u><h1 style='color: blue;'>Hello world, bienvenue sur mon profil en ligne</h1></u>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write(profile)

elif page == "Formations":
    st.title("Formations")
    st.markdown(formations, unsafe_allow_html=True)

elif page == "Expériences":
    st.title("Expériences")
    st.markdown(experiences, unsafe_allow_html=True)

elif page == "Stack techniques et Soft Skills":
    st.title("Stack techniques et Soft Skills")
    st.write("""
    **Stack techniques :**
    - Data gouvernance (OpenMetadata)
    - Gestion de bases de données (SQL, POSTGRES, MYSQL)
    - Langages de programmation (Python, C, R)
    - Data visualisation (Power BI, Tableau, Qlik)
    - Pack Office (Excel, Word, PowerPoint)
    - Gestion de projet (Scrum Agile)
    
    **Soft Skills :**
    - Curieux
    - Rigoureux
    - Esprit d'équipe
    - Autonome et autodidacte 
    - Esprit d'analyse et de synthèse
    - Gestion de projet (Scrum Agile)
    """)

elif page == "Certifications":
    st.title("Certifications")
    st.markdown(certifications)

elif page == "Langues":
    st.title("Langues")
    st.markdown(langues)

elif page == "Projets":
    st.title("Projets")
    st.markdown(projets, unsafe_allow_html=True)

elif page == "Vie Associative":
    st.title("Vie Associative")
    st.markdown(vie_associative, unsafe_allow_html=True)

elif page == "Recommandations":
    st.title("Recommandations")
    st.markdown(recommandations)

elif page == "Contact":
    st.title("Contact")
    for key, value in contact_info.items():
        st.write(f"**{key}:** {value}")
    
