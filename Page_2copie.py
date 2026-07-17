import streamlit as st
import base64
import glob
from pathlib import Path

# ── PHOTO DE PROFIL ─────────────────────────────────────────────────────────
def get_base64_image(path: str) -> str:
    data = Path(path).read_bytes()
    return base64.b64encode(data).decode()

def find_photo() -> str | None:
    search_dirs = [".", "assets"]
    for d in search_dirs:
        if not Path(d).is_dir():
            continue
        for ext in ("jpg", "jpeg", "png", "JPG", "JPEG", "PNG"):
            matches = glob.glob(f"{d}/seydou.{ext}") + glob.glob(f"{d}/Seydou.{ext}")
            if matches:
                return matches[0]
    return None

photo_path = find_photo()
photo_b64 = get_base64_image(photo_path) if photo_path else ""

# ── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Seydou Soumano · Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── LANGUAGE STATE ───────────────────────────────────────────────────────────
if "lang" not in st.session_state:
    st.session_state.lang = "fr"

# ── CONTENT DICTIONARY ───────────────────────────────────────────────────────
content = {
    "fr": {
        "nav_exp": "Expériences",
        "nav_proj": "Projets",
        "nav_reco": "Recommandations",
        "nav_contact": "Me contacter",
        "badge": "🟢 Disponible immédiatement · Île-de-France",
        "hero_title": "Data Analyst.<br><span class='dim'>Je transforme la donnée</span><br><span class='accent'>en décisions.</span>",
        "hero_sub": "3 ans d'expérience en <strong>BI, SQL, Python et IA générative</strong>. Certifié <strong>Google Cloud ACE</strong>. Je construis des pipelines, des dashboards et des solutions IA déployées en production — pas juste des slides.",
        "btn_contact": "📧 Me contacter",
        "stat_1_num": "3 ans", "stat_1_lab": "Expérience data",
        "stat_2_num": "98%", "stat_2_lab": "Anomalies corrigées · dernière mission",
        "stat_3_num": "+18%", "stat_3_lab": "Clients réactivés · en 3 mois",
        "stat_4_num": "GCP", "stat_4_lab": "Certifié ACE · 2026",
        "skills_eyebrow": "Stack technique",
        "skills_title": "Compétences",
        "skills_sub": "Outils que j'utilise en production, pas juste sur un CV.",
        "skills_cat_1": "Data & Analyse",
        "skills_cat_2": "BI & Dataviz",
        "skills_cat_3": "Cloud & IA",
        "exp_eyebrow": "Parcours",
        "exp_title": "Expériences professionnelles",
        "exp_sub": "Des missions avec des résultats mesurables, pas juste des missions.",
        "exp1_role": "Consultant Chef de Projets SI & Data Analyst",
        "exp1_company": "Clap Partner · Paris · Industrie, Retail, Luxe",
        "exp1_period": "08/2024 – 10/2025",
        "exp1_b1": "Analyse multi-sources en SQL et Python : détection d'anomalies, identification de tendances et d'opportunités business pour les directions métiers",
        "exp1_b2": "<strong>98% des anomalies data corrigées</strong> grâce à des contrôles qualité rigoureux sur <strong>10+</strong> projets SI end-to-end",
        "exp1_b3": "Conception et maintien de dashboards Power BI pour le pilotage des KPIs de performance",
        "exp1_b4": "Animation d'ateliers clients, rédaction de roadmaps et restitution d'insights actionnables en COPROJ/COPIL",
        "exp1_b5": "Pilotage de projets en méthode Agile : sprints, reviews, backlog, démos",
        "exp2_role": "Business Data Analyst — Performance Commerciale BtoB",
        "exp2_company": "VWR Avantor · Paris · 4 pays (FR, BE, ES, PT)",
        "exp2_period": "10/2022 – 05/2024",
        "exp2_b1": "Analyse de performances commerciales sur <strong>6 000+</strong> clients dans <strong>4 pays</strong> via SQL et Python",
        "exp2_b2": "Modèle de segmentation clients → <strong>+18% de clients réactivés en 3 mois</strong>",
        "exp2_b3": "Dashboards automatisés (QlikView, Power BI, Excel VBA) utilisés comme référence par <strong>3 équipes</strong> sur <strong>4 pays</strong>",
        "exp2_b4": "<strong>91% de taux de digitalisation atteint</strong> grâce aux analyses et recommandations data",
        "exp2_b5": "Restitution d'insights actionnables aux directions commerciales et marketing",
        "exp3_role": "Data Analyst · Stage",
        "exp3_company": "Moby Deck · Paris",
        "exp3_period": "04/2022 – 06/2022",
        "exp3_b1": "Fiabilisation d'une base de <strong>32 000+ entrées</strong> (8 000 modèles de véhicules)",
        "exp3_b2": "Automatisation de la classification selon des critères métier spécifiques",
        "exp4_role": "Data Analyst · Stage",
        "exp4_company": "Orange · Mali",
        "exp4_period": "07/2019 – 09/2019",
        "exp4_b1": "Reporting satisfaction clients pour les comités de direction",
        "exp4_b2": "Collecte et analyse des données de satisfaction et motifs d'insatisfaction",
        "proj_eyebrow": "Portfolio technique",
        "proj_title": "Projets déployés",
        "proj_sub": "Du code en production. Pas juste des notebooks.",
        "proj1_title": "Plateforme Data Quality IA",
        "proj1_desc": "Automatisation de la détection d'anomalies et fiabilisation des données via IA générative. Déployé en production.",
        "proj1_live": "Live en production",
        "proj2_title": "Pipeline Analytique GCP",
        "proj2_desc": "Ingestion de 212 000+ lignes de données publiques. Modélisation SQL, vues analytiques et dashboard Looker Studio.",
        "proj2_live": "Live en production",
        "proj3_title": "Dashboard Performance 4 Pays",
        "proj3_desc": "Dashboard automatisé pour le pilotage des performances commerciales (France, Belgique, Espagne, Portugal). Macros VBA + navigation dynamique.",
        "proj4_title": "Analyse Churn & Rétention Client",
        "proj4_desc": "Modèle prédictif d'identification des segments clients à risque pour une entreprise téléphonique.",
        "proj5_title": "Dashboard Criminalité par Région",
        "proj5_desc": "Analyse de l'évolution des crimes dans chaque région française. Interface interactive déployée en ligne.",
        "proj6_title": "Analyse Prédictive Égalité F/H",
        "proj6_desc": "Analyse prédictive de l'évolution de l'indice d'égalité Femmes/Hommes à partir de données publiques.",
        "reco_eyebrow": "Social proof",
        "reco_title": "Ce que disent ceux qui ont travaillé avec moi",
        "reco_sub": "Des recommandations réelles, pas des phrases génériques.",
        "reco1_q": "Sa capacité à appliquer ses connaissances de manière innovante dans des projets concrets a grandement contribué à la réussite de ceux-ci.",
        "reco1_a": "O. Mamavi", "reco1_r": "Docteur en Sciences de gestion · Directeur Data, Management & Datascience · Professeur PSB",
        "reco2_q": "Sa facilité à coordonner et à motiver ses camarades reflète ses fortes aptitudes en management et leadership, des qualités qui le rendent particulièrement bien adapté pour exceller.",
        "reco2_a": "O. Mamavi", "reco2_r": "Docteur en Sciences de gestion · Directeur Data, Management & Datascience",
        "reco3_q": "Je voudrais en toute honnêteté exprimer ma très grande satisfaction et confiance en ses qualités personnelles, sur un plan disciplinaire et intellectuel, ainsi que son dynamisme constant dans le travail individuel et collectif.",
        "reco3_a": "I. Traore", "reco3_r": "Psychologue et Manager des organisations",
        "reco4_q": "Bienveillant, motivant et empathique. Son sens du collectif et son attachement à l'humain sont évidents et font de lui un professionnel compétent et unique.",
        "reco4_a": "M. Iche", "reco4_r": "Développeur Web · Bpartner",
        "edu_eyebrow": "Éducation",
        "edu_title": "Formation & Certifications",
        "edu1_title": "MBA Big Data & Intelligence Artificielle",
        "edu1_school": "MBA ESG · Paris",
        "edu1_mention": "MLOps · Data Engineering · Data Quality · BI · Gestion de projets",
        "edu2_title": "MSc Data Management",
        "edu2_school": "Paris School of Business & EFREI",
        "edu2_mention": "Mention Bien · Data gouvernance · ML · Modélisation · Statistiques",
        "contact_title": "On travaille ensemble ?",
        "contact_sub": "Disponible immédiatement en Île-de-France · Anglais C1 · Ouvert au remote",
    },
    "en": {
        "nav_exp": "Experience",
        "nav_proj": "Projects",
        "nav_reco": "Recommendations",
        "nav_contact": "Contact me",
        "badge": "🟢 Available immediately · Île-de-France",
        "hero_title": "Data Analyst.<br><span class='dim'>I turn data</span><br><span class='accent'>into decisions.</span>",
        "hero_sub": "3 years of experience in <strong>BI, SQL, Python and Generative AI</strong>. <strong>Google Cloud ACE Certified</strong>. I build pipelines, dashboards and AI solutions deployed in production — not just slides.",
        "btn_contact": "📧 Contact me",
        "stat_1_num": "3 yrs", "stat_1_lab": "Data experience",
        "stat_2_num": "98%", "stat_2_lab": "Anomalies corrected · last project",
        "stat_3_num": "+18%", "stat_3_lab": "Clients reactivated · in 3 months",
        "stat_4_num": "GCP", "stat_4_lab": "Certified ACE · 2026",
        "skills_eyebrow": "Tech stack",
        "skills_title": "Skills",
        "skills_sub": "Tools I use in production, not just on a CV.",
        "skills_cat_1": "Data & Analytics",
        "skills_cat_2": "BI & Dataviz",
        "skills_cat_3": "Cloud & AI",
        "exp_eyebrow": "Career",
        "exp_title": "Professional Experience",
        "exp_sub": "Missions with measurable results, not just job descriptions.",
        "exp1_role": "SI Project Consultant & Data Analyst",
        "exp1_company": "Clap Partner · Paris · Industry, Retail, Luxury",
        "exp1_period": "08/2024 – 10/2025",
        "exp1_b1": "Multi-source analysis in SQL and Python: anomaly detection, trend identification and business opportunities for management teams",
        "exp1_b2": "<strong>98% of data anomalies corrected</strong> through rigorous quality controls across <strong>10+</strong> end-to-end SI projects",
        "exp1_b3": "Designed and maintained Power BI dashboards for performance KPI monitoring",
        "exp1_b4": "Client workshops, roadmaps and actionable insight delivery in steering committees",
        "exp1_b5": "Agile project management: sprints, reviews, backlog, demos",
        "exp2_role": "Business Data Analyst — BtoB Commercial Performance",
        "exp2_company": "VWR Avantor · Paris · 4 countries (FR, BE, ES, PT)",
        "exp2_period": "10/2022 – 05/2024",
        "exp2_b1": "Commercial performance analysis on <strong>6,000+</strong> clients across <strong>4 countries</strong> using SQL and Python",
        "exp2_b2": "Client segmentation model → <strong>+18% reactivated clients in 3 months</strong>",
        "exp2_b3": "Automated dashboards (QlikView, Power BI, Excel VBA) used as reference by <strong>3 teams</strong> across <strong>4 countries</strong>",
        "exp2_b4": "<strong>91% digitalisation rate achieved</strong> through data analysis and recommendations",
        "exp2_b5": "Actionable insight delivery to commercial and marketing leadership",
        "exp3_role": "Data Analyst · Internship",
        "exp3_company": "Moby Deck · Paris",
        "exp3_period": "04/2022 – 06/2022",
        "exp3_b1": "Data quality control on a <strong>32,000+ entry</strong> database (8,000 vehicle models)",
        "exp3_b2": "Automated classification based on business-specific criteria",
        "exp4_role": "Data Analyst · Internship",
        "exp4_company": "Orange · Mali",
        "exp4_period": "07/2019 – 09/2019",
        "exp4_b1": "Customer satisfaction reporting for board-level committees",
        "exp4_b2": "Data collection and analysis of satisfaction scores and dissatisfaction drivers",
        "proj_eyebrow": "Technical portfolio",
        "proj_title": "Deployed Projects",
        "proj_sub": "Code in production. Not just notebooks.",
        "proj1_title": "AI Data Quality Platform",
        "proj1_desc": "Automated anomaly detection and data reliability using generative AI. Deployed in production.",
        "proj1_live": "Live in production",
        "proj2_title": "GCP Analytics Pipeline",
        "proj2_desc": "Ingestion of 212,000+ rows of public data. SQL modelling, analytical views and Looker Studio dashboard.",
        "proj2_live": "Live in production",
        "proj3_title": "4-Country Performance Dashboard",
        "proj3_desc": "Automated dashboard for commercial performance tracking (France, Belgium, Spain, Portugal). VBA macros + dynamic navigation.",
        "proj4_title": "Churn & Client Retention Analysis",
        "proj4_desc": "Predictive model identifying at-risk client segments for a telecom company.",
        "proj5_title": "Crime by Region Dashboard",
        "proj5_desc": "Analysis of crime trends across French regions. Interactive interface deployed online.",
        "proj6_title": "Predictive Analysis — Gender Equality",
        "proj6_desc": "Predictive analysis of the gender equality index evolution using public data.",
        "reco_eyebrow": "Social proof",
        "reco_title": "What people who worked with me say",
        "reco_sub": "Real recommendations, not generic phrases.",
        "reco1_q": "His ability to apply his knowledge innovatively in concrete projects greatly contributed to their success.",
        "reco1_a": "O. Mamavi", "reco1_r": "PhD in Management · Data Director, Management & Datascience · PSB Professor",
        "reco2_q": "His ability to coordinate and motivate his peers reflects strong management and leadership skills — qualities that make him particularly well-suited to excel.",
        "reco2_a": "O. Mamavi", "reco2_r": "PhD in Management · Data Director, Management & Datascience",
        "reco3_q": "I would like to honestly express my great satisfaction and confidence in his personal qualities — his discipline, intellectual rigor, and constant dynamism in both individual and collective work.",
        "reco3_a": "I. Traore", "reco3_r": "Psychologist and Organizational Manager",
        "reco4_q": "Caring, motivating and empathetic. His team spirit and human connection are obvious — they make him a uniquely competent professional.",
        "reco4_a": "M. Iche", "reco4_r": "Web Developer · Bpartner",
        "edu_eyebrow": "Education",
        "edu_title": "Education & Certifications",
        "edu1_title": "MBA Big Data & Artificial Intelligence",
        "edu1_school": "MBA ESG · Paris",
        "edu1_mention": "MLOps · Data Engineering · Data Quality · BI · Project Management",
        "edu2_title": "MSc Data Management",
        "edu2_school": "Paris School of Business & EFREI",
        "edu2_mention": "With Merit · Data governance · ML · Modelling · Statistics",
        "contact_title": "Let's work together?",
        "contact_sub": "Available immediately in Île-de-France · English C1 · Open to remote",
    }
}

T = content[st.session_state.lang]

# ── CSS GLOBAL ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body, [data-testid="stAppViewContainer"] {
    background-color: #0A0F1E !important;
    color: #E8ECF4 !important;
    font-family: 'Inter', sans-serif !important;
}
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0A0F1E 0%, #0D1628 50%, #0A0F1E 100%) !important;
}
#MainMenu, header, footer, [data-testid="stToolbar"],
[data-testid="stDecoration"], [data-testid="stStatusWidget"] { display: none !important; }
[data-testid="stSidebar"] { display: none !important; }
.main .block-container { max-width: 1100px !important; padding: 0 2rem 4rem !important; margin: 0 auto !important; }
h1, h2, h3 { font-family: 'Space Grotesk', sans-serif !important; }
.nav-bar { display: flex; justify-content: space-between; align-items: center; padding: 1.5rem 0; border-bottom: 1px solid rgba(255,255,255,0.06); margin-bottom: 4rem; }
.nav-logo { font-family: 'Space Grotesk', sans-serif; font-size: 1.1rem; font-weight: 700; color: #E8ECF4; letter-spacing: -0.02em; }
.nav-logo span { color: #4F8EF7; }
.nav-links { display: flex; gap: 2rem; align-items: center; }
.nav-links a { color: #8B9CB8; text-decoration: none; font-size: 0.875rem; font-weight: 500; transition: color 0.2s; }
.nav-links a:hover { color: #E8ECF4; }
.nav-cta { background: #4F8EF7; color: white !important; padding: 0.5rem 1.25rem; border-radius: 6px; font-size: 0.875rem; font-weight: 600; }
.lang-toggle { display: flex; gap: 0.4rem; align-items: center; }
.lang-btn { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); color: #8B9CB8; padding: 0.3rem 0.75rem; border-radius: 6px; font-size: 0.8rem; font-weight: 600; cursor: pointer; text-decoration: none; transition: all 0.2s; }
.lang-btn.active { background: rgba(79,142,247,0.2); border-color: #4F8EF7; color: #4F8EF7; }
.hero { padding: 2rem 0 5rem; }
.hero-content { display: flex; align-items: center; justify-content: space-between; gap: 3rem; }
.hero-text { flex: 1; min-width: 0; }
.hero-photo-wrap { flex-shrink: 0; position: relative; width: 200px; height: 200px; }
.hero-photo { width: 200px; height: 200px; border-radius: 50%; object-fit: cover; border: 3px solid rgba(79,142,247,0.4); box-shadow: 0 8px 40px rgba(79,142,247,0.25); }
.hero-photo-ring { position: absolute; inset: -10px; border-radius: 50%; border: 1px solid rgba(79,142,247,0.2); }
@media (max-width: 768px) { .hero-content { flex-direction: column-reverse; text-align: center; } .hero-photo, .hero-photo-wrap { width: 140px; height: 140px; } .hero-actions { justify-content: center; } }
.hero-badge { display: inline-flex; align-items: center; gap: 0.5rem; background: rgba(79,142,247,0.12); border: 1px solid rgba(79,142,247,0.3); border-radius: 100px; padding: 0.35rem 1rem; font-size: 0.8rem; font-weight: 600; color: #4F8EF7; margin-bottom: 1.75rem; letter-spacing: 0.04em; text-transform: uppercase; }
.hero-badge::before { content: ''; width: 6px; height: 6px; background: #4F8EF7; border-radius: 50%; animation: pulse 2s infinite; }
@keyframes pulse { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.5; transform: scale(1.3); } }
.hero-title { font-family: 'Space Grotesk', sans-serif; font-size: clamp(2.5rem, 5vw, 3.75rem); font-weight: 700; line-height: 1.1; letter-spacing: -0.03em; color: #E8ECF4; margin-bottom: 1.25rem; }
.hero-title .accent { color: #4F8EF7; }
.hero-title .dim { color: #8B9CB8; }
.hero-sub { font-size: 1.1rem; color: #8B9CB8; line-height: 1.7; max-width: 560px; margin-bottom: 2.5rem; font-weight: 400; }
.hero-sub strong { color: #C8D4E8; font-weight: 600; }
.hero-actions { display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 3.5rem; }
.btn-primary { background: #4F8EF7; color: white; padding: 0.8rem 1.75rem; border-radius: 8px; font-size: 0.9rem; font-weight: 600; text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem; transition: all 0.2s; box-shadow: 0 4px 20px rgba(79,142,247,0.3); }
.btn-primary:hover { background: #3A7AE4; transform: translateY(-1px); }
.btn-secondary { background: transparent; color: #C8D4E8; padding: 0.8rem 1.75rem; border-radius: 8px; font-size: 0.9rem; font-weight: 600; text-decoration: none; border: 1px solid rgba(255,255,255,0.15); display: inline-flex; align-items: center; gap: 0.5rem; transition: all 0.2s; }
.btn-secondary:hover { border-color: rgba(255,255,255,0.3); color: white; }
.stats-bar { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1px; background: rgba(255,255,255,0.06); border-radius: 12px; overflow: hidden; border: 1px solid rgba(255,255,255,0.06); }
.stat-item { background: rgba(255,255,255,0.02); padding: 1.25rem 1.5rem; text-align: center; transition: background 0.2s; }
.stat-item:hover { background: rgba(79,142,247,0.05); }
.stat-number { font-family: 'Space Grotesk', sans-serif; font-size: 1.8rem; font-weight: 700; color: #4F8EF7; line-height: 1; margin-bottom: 0.3rem; letter-spacing: -0.02em; }
.stat-label { font-size: 0.7rem; color: #8B9CB8; font-weight: 500; text-transform: uppercase; letter-spacing: 0.04em; line-height: 1.4; }
.section { margin-top: 5rem; }
.section-eyebrow { font-size: 0.75rem; font-weight: 700; color: #4F8EF7; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.75rem; }
.section-title { font-family: 'Space Grotesk', sans-serif; font-size: 1.75rem; font-weight: 700; color: #E8ECF4; letter-spacing: -0.02em; margin-bottom: 0.5rem; }
.section-sub { color: #8B9CB8; font-size: 0.95rem; line-height: 1.6; margin-bottom: 2.5rem; }
.skills-grid { display: flex; flex-wrap: wrap; gap: 0.6rem; margin-bottom: 1.5rem; }
.skill-tag { background: rgba(79,142,247,0.08); border: 1px solid rgba(79,142,247,0.2); color: #C8D4E8; padding: 0.4rem 0.9rem; border-radius: 6px; font-size: 0.82rem; font-weight: 500; transition: all 0.2s; }
.skill-tag.highlight { background: rgba(79,142,247,0.2); border-color: #4F8EF7; color: #4F8EF7; font-weight: 600; }
.exp-card { background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1.75rem; margin-bottom: 1rem; transition: all 0.25s; position: relative; overflow: hidden; }
.exp-card::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 3px; background: #4F8EF7; opacity: 0; transition: opacity 0.25s; }
.exp-card:hover { border-color: rgba(79,142,247,0.3); background: rgba(79,142,247,0.04); transform: translateX(4px); }
.exp-card:hover::before { opacity: 1; }
.exp-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem; flex-wrap: wrap; gap: 0.5rem; }
.exp-role { font-family: 'Space Grotesk', sans-serif; font-size: 1rem; font-weight: 700; color: #E8ECF4; margin-bottom: 0.2rem; }
.exp-company { font-size: 0.875rem; color: #4F8EF7; font-weight: 600; }
.exp-period { font-size: 0.78rem; color: #8B9CB8; background: rgba(255,255,255,0.05); padding: 0.25rem 0.75rem; border-radius: 100px; font-weight: 500; white-space: nowrap; }
.exp-bullets { list-style: none; }
.exp-bullets li { font-size: 0.875rem; color: #8B9CB8; line-height: 1.6; padding: 0.2rem 0; padding-left: 1.25rem; position: relative; }
.exp-bullets li::before { content: '→'; position: absolute; left: 0; color: #4F8EF7; font-size: 0.75rem; }
.exp-bullets li strong { color: #C8D4E8; font-weight: 600; }
.exp-tags { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 1rem; }
.exp-tag { font-size: 0.72rem; background: rgba(255,255,255,0.04); color: #8B9CB8; padding: 0.2rem 0.6rem; border-radius: 4px; font-weight: 500; }
.projects-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; }
.project-card { background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1.5rem; transition: all 0.25s; text-decoration: none; display: block; }
.project-card:hover { border-color: rgba(79,142,247,0.4); background: rgba(79,142,247,0.05); transform: translateY(-3px); box-shadow: 0 12px 40px rgba(0,0,0,0.3); }
.project-icon { font-size: 1.75rem; margin-bottom: 1rem; }
.project-title { font-family: 'Space Grotesk', sans-serif; font-size: 0.95rem; font-weight: 700; color: #E8ECF4; margin-bottom: 0.4rem; }
.project-desc { font-size: 0.83rem; color: #8B9CB8; line-height: 1.5; margin-bottom: 1rem; }
.project-stack { display: flex; flex-wrap: wrap; gap: 0.35rem; }
.stack-tag { font-size: 0.7rem; background: rgba(79,142,247,0.1); color: #4F8EF7; padding: 0.2rem 0.55rem; border-radius: 4px; font-weight: 600; }
.project-live { display: inline-flex; align-items: center; gap: 0.3rem; font-size: 0.75rem; color: #4F8EF7; font-weight: 600; margin-top: 0.75rem; }
.project-live::before { content: ''; width: 6px; height: 6px; background: #22C55E; border-radius: 50%; }
.reco-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; }
.reco-card { background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1.5rem; }
.reco-quote { font-size: 0.875rem; color: #C8D4E8; line-height: 1.7; font-style: italic; margin-bottom: 1rem; position: relative; }
.reco-quote::before { content: '"'; font-size: 3rem; color: rgba(79,142,247,0.2); font-family: Georgia, serif; line-height: 1; float: left; margin-right: 0.25rem; margin-top: -0.5rem; }
.reco-author { font-size: 0.8rem; font-weight: 700; color: #4F8EF7; }
.reco-role { font-size: 0.75rem; color: #8B9CB8; margin-top: 0.1rem; }
.certif-grid { display: flex; flex-wrap: wrap; gap: 0.75rem; }
.certif-badge { display: flex; align-items: center; gap: 0.6rem; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 0.6rem 1rem; font-size: 0.82rem; color: #C8D4E8; font-weight: 500; }
.certif-badge .certif-icon { font-size: 1.1rem; }
.certif-badge.featured { border-color: rgba(79,142,247,0.4); background: rgba(79,142,247,0.08); color: #4F8EF7; font-weight: 700; }
.edu-item { display: flex; gap: 1.25rem; padding: 1.25rem 0; border-bottom: 1px solid rgba(255,255,255,0.05); }
.edu-item:last-child { border-bottom: none; }
.edu-year { font-size: 0.78rem; color: #8B9CB8; font-weight: 600; min-width: 70px; padding-top: 0.1rem; }
.edu-title { font-weight: 700; color: #E8ECF4; font-size: 0.9rem; margin-bottom: 0.1rem; }
.edu-school { font-size: 0.82rem; color: #4F8EF7; font-weight: 500; }
.edu-mention { font-size: 0.75rem; color: #8B9CB8; margin-top: 0.25rem; }
.contact-section { background: linear-gradient(135deg, rgba(79,142,247,0.08) 0%, rgba(79,142,247,0.03) 100%); border: 1px solid rgba(79,142,247,0.2); border-radius: 16px; padding: 3rem; text-align: center; margin-top: 5rem; }
.contact-title { font-family: 'Space Grotesk', sans-serif; font-size: 1.75rem; font-weight: 700; color: #E8ECF4; margin-bottom: 0.75rem; }
.contact-sub { color: #8B9CB8; font-size: 0.95rem; margin-bottom: 2rem; }
.contact-links { display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; }
.contact-link { display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.7rem 1.5rem; border-radius: 8px; font-size: 0.875rem; font-weight: 600; text-decoration: none; transition: all 0.2s; }
.contact-link.primary { background: #4F8EF7; color: white; box-shadow: 0 4px 15px rgba(79,142,247,0.3); }
.contact-link.secondary { background: rgba(255,255,255,0.05); color: #C8D4E8; border: 1px solid rgba(255,255,255,0.1); }
.contact-link:hover { opacity: 0.85; transform: translateY(-1px); }
.divider { height: 1px; background: linear-gradient(90deg, transparent, rgba(79,142,247,0.3), transparent); margin: 1rem 0; }
[data-testid="stMarkdownContainer"] p { margin: 0; }
.stMarkdown { width: 100%; }
</style>
""", unsafe_allow_html=True)

# ── LANGUAGE TOGGLE (Streamlit buttons) ──────────────────────────────────────
col_nav, col_lang = st.columns([5, 1])
with col_nav:
    st.markdown(f"""
    <nav class="nav-bar">
        <div class="nav-logo">Seydou<span>.</span></div>
        <div class="nav-links">
            <a href="#experience">{T['nav_exp']}</a>
            <a href="#projets">{T['nav_proj']}</a>
            <a href="#recommandations">{T['nav_reco']}</a>
            <a href="mailto:soumanoseydou@icloud.com" class="nav-cta">{T['nav_contact']}</a>
        </div>
    </nav>
    """, unsafe_allow_html=True)
with col_lang:
    st.markdown("<div style='padding-top:1.5rem; display:flex; gap:0.4rem;'>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("FR", help="Français", use_container_width=True):
            st.session_state.lang = "fr"
            st.rerun()
    with c2:
        if st.button("EN", help="English", use_container_width=True):
            st.session_state.lang = "en"
            st.rerun()

# ── HERO ─────────────────────────────────────────────────────────────────────
photo_html = f'<img src="data:image/jpeg;base64,{photo_b64}" class="hero-photo" alt="Seydou Soumano">' if photo_b64 else ''

st.markdown(f"""
<section class="hero">
    <div class="hero-content">
        <div class="hero-text">
            <div class="hero-badge">{T['badge']}</div>
            <h1 class="hero-title">{T['hero_title']}</h1>
            <p class="hero-sub">{T['hero_sub']}</p>
            <div class="hero-actions">
                <a href="mailto:soumanoseydou@icloud.com" class="btn-primary">{T['btn_contact']}</a>
                <a href="https://linkedin.com/in/seydou-soumano" class="btn-secondary">🔗 LinkedIn</a>
                <a href="https://github.com/Ssoumano" class="btn-secondary">⚙️ GitHub</a>
            </div>
        </div>
        <div class="hero-photo-wrap">
            <div class="hero-photo-ring"></div>
            {photo_html}
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="stats-bar">
    <div class="stat-item"><div class="stat-number">{T['stat_1_num']}</div><div class="stat-label">{T['stat_1_lab']}</div></div>
    <div class="stat-item"><div class="stat-number">{T['stat_2_num']}</div><div class="stat-label">{T['stat_2_lab']}</div></div>
    <div class="stat-item"><div class="stat-number">{T['stat_3_num']}</div><div class="stat-label">{T['stat_3_lab']}</div></div>
    <div class="stat-item"><div class="stat-number">{T['stat_4_num']}</div><div class="stat-label">{T['stat_4_lab']}</div></div>
</div>
""", unsafe_allow_html=True)

# ── COMPÉTENCES ──────────────────────────────────────────────────────────────
st.markdown(f"""
<section class="section">
    <div class="section-eyebrow">{T['skills_eyebrow']}</div>
    <h2 class="section-title">{T['skills_title']}</h2>
    <p class="section-sub">{T['skills_sub']}</p>
    <div style="margin-bottom:1.25rem">
        <div style="font-size:0.78rem;font-weight:700;color:#8B9CB8;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.6rem">{T['skills_cat_1']}</div>
        <div class="skills-grid">
            <span class="skill-tag highlight">SQL</span><span class="skill-tag highlight">Python</span>
            <span class="skill-tag">Pandas · NumPy</span><span class="skill-tag">Segmentation</span>
            <span class="skill-tag">A/B Testing</span><span class="skill-tag">Scoring</span>
            <span class="skill-tag">Data profiling</span><span class="skill-tag">OpenMetadata</span>
        </div>
    </div>
    <div style="margin-bottom:1.25rem">
        <div style="font-size:0.78rem;font-weight:700;color:#8B9CB8;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.6rem">{T['skills_cat_2']}</div>
        <div class="skills-grid">
            <span class="skill-tag highlight">Power BI (DAX)</span><span class="skill-tag highlight">QlikView</span>
            <span class="skill-tag">Looker Studio</span><span class="skill-tag">Tableau</span>
            <span class="skill-tag">Excel VBA</span><span class="skill-tag">Dashboards</span>
        </div>
    </div>
    <div>
        <div style="font-size:0.78rem;font-weight:700;color:#8B9CB8;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.6rem">{T['skills_cat_3']}</div>
        <div class="skills-grid">
            <span class="skill-tag highlight">GCP (Certifié ACE)</span><span class="skill-tag highlight">BigQuery</span>
            <span class="skill-tag">Cloud Storage</span><span class="skill-tag">Streamlit</span>
            <span class="skill-tag">OpenAI API</span><span class="skill-tag">Generative AI</span><span class="skill-tag">Agile / Scrum</span>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ── EXPÉRIENCES ──────────────────────────────────────────────────────────────
st.markdown(f"""
<section class="section" id="experience">
    <div class="section-eyebrow">{T['exp_eyebrow']}</div>
    <h2 class="section-title">{T['exp_title']}</h2>
    <p class="section-sub">{T['exp_sub']}</p>

    <div class="exp-card">
        <div class="exp-header">
            <div><div class="exp-role">{T['exp1_role']}</div><div class="exp-company">{T['exp1_company']}</div></div>
            <div class="exp-period">{T['exp1_period']}</div>
        </div>
        <ul class="exp-bullets">
            <li>{T['exp1_b1']}</li><li>{T['exp1_b2']}</li><li>{T['exp1_b3']}</li><li>{T['exp1_b4']}</li><li>{T['exp1_b5']}</li>
        </ul>
        <div class="exp-tags"><span class="exp-tag">SQL</span><span class="exp-tag">Python</span><span class="exp-tag">Power BI</span><span class="exp-tag">SAP SuccessFactors</span><span class="exp-tag">Agile</span><span class="exp-tag">Data Quality</span></div>
    </div>

    <div class="exp-card">
        <div class="exp-header">
            <div><div class="exp-role">{T['exp2_role']}</div><div class="exp-company">{T['exp2_company']}</div></div>
            <div class="exp-period">{T['exp2_period']}</div>
        </div>
        <ul class="exp-bullets">
            <li>{T['exp2_b1']}</li><li>{T['exp2_b2']}</li><li>{T['exp2_b3']}</li><li>{T['exp2_b4']}</li><li>{T['exp2_b5']}</li>
        </ul>
        <div class="exp-tags"><span class="exp-tag">SQL</span><span class="exp-tag">Python</span><span class="exp-tag">QlikView</span><span class="exp-tag">Power BI</span><span class="exp-tag">Excel VBA</span><span class="exp-tag">Segmentation</span></div>
    </div>

    <div class="exp-card">
        <div class="exp-header">
            <div><div class="exp-role">{T['exp3_role']}</div><div class="exp-company">{T['exp3_company']}</div></div>
            <div class="exp-period">{T['exp3_period']}</div>
        </div>
        <ul class="exp-bullets"><li>{T['exp3_b1']}</li><li>{T['exp3_b2']}</li></ul>
        <div class="exp-tags"><span class="exp-tag">Python</span><span class="exp-tag">Data Quality</span></div>
    </div>

    <div class="exp-card">
        <div class="exp-header">
            <div><div class="exp-role">{T['exp4_role']}</div><div class="exp-company">{T['exp4_company']}</div></div>
            <div class="exp-period">{T['exp4_period']}</div>
        </div>
        <ul class="exp-bullets"><li>{T['exp4_b1']}</li><li>{T['exp4_b2']}</li></ul>
        <div class="exp-tags"><span class="exp-tag">Reporting</span><span class="exp-tag">Excel</span></div>
    </div>
</section>
""", unsafe_allow_html=True)

# ── PROJETS ──────────────────────────────────────────────────────────────────
st.markdown(f"""
<section class="section" id="projets">
    <div class="section-eyebrow">{T['proj_eyebrow']}</div>
    <h2 class="section-title">{T['proj_title']}</h2>
    <p class="section-sub">{T['proj_sub']}</p>
    <div class="projects-grid">
        <a class="project-card" href="https://plateforme-data-quality-fgtzf5rzl9tgr39wvk22tz.streamlit.app/" target="_blank">
            <div class="project-icon">🤖</div><div class="project-title">{T['proj1_title']}</div>
            <div class="project-desc">{T['proj1_desc']}</div>
            <div class="project-stack"><span class="stack-tag">Python</span><span class="stack-tag">Streamlit</span><span class="stack-tag">OpenAI API</span></div>
            <div class="project-live">{T['proj1_live']}</div>
        </a>
        <a class="project-card" href="https://soumano-seydou.streamlit.app/" target="_blank">
            <div class="project-icon">☁️</div><div class="project-title">{T['proj2_title']}</div>
            <div class="project-desc">{T['proj2_desc']}</div>
            <div class="project-stack"><span class="stack-tag">BigQuery</span><span class="stack-tag">GCS</span><span class="stack-tag">Looker Studio</span><span class="stack-tag">SQL</span></div>
            <div class="project-live">{T['proj2_live']}</div>
        </a>
        <div class="project-card">
            <div class="project-icon">📊</div><div class="project-title">{T['proj3_title']}</div>
            <div class="project-desc">{T['proj3_desc']}</div>
            <div class="project-stack"><span class="stack-tag">Excel VBA</span><span class="stack-tag">QlikView</span><span class="stack-tag">Power BI</span></div>
        </div>
        <div class="project-card">
            <div class="project-icon">🔄</div><div class="project-title">{T['proj4_title']}</div>
            <div class="project-desc">{T['proj4_desc']}</div>
            <div class="project-stack"><span class="stack-tag">Python</span><span class="stack-tag">SQL</span><span class="stack-tag">Power BI</span><span class="stack-tag">ML</span></div>
        </div>
        <div class="project-card">
            <div class="project-icon">🗺️</div><div class="project-title">{T['proj5_title']}</div>
            <div class="project-desc">{T['proj5_desc']}</div>
            <div class="project-stack"><span class="stack-tag">Python</span><span class="stack-tag">Streamlit</span><span class="stack-tag">Pandas</span></div>
        </div>
        <div class="project-card">
            <div class="project-icon">📈</div><div class="project-title">{T['proj6_title']}</div>
            <div class="project-desc">{T['proj6_desc']}</div>
            <div class="project-stack"><span class="stack-tag">SQL</span><span class="stack-tag">Python</span><span class="stack-tag">Excel</span></div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ── RECOMMANDATIONS ──────────────────────────────────────────────────────────
st.markdown(f"""
<section class="section" id="recommandations">
    <div class="section-eyebrow">{T['reco_eyebrow']}</div>
    <h2 class="section-title">{T['reco_title']}</h2>
    <p class="section-sub">{T['reco_sub']}</p>
    <div class="reco-grid">
        <div class="reco-card"><div class="reco-quote">{T['reco1_q']}</div><div class="reco-author">{T['reco1_a']}</div><div class="reco-role">{T['reco1_r']}</div></div>
        <div class="reco-card"><div class="reco-quote">{T['reco2_q']}</div><div class="reco-author">{T['reco2_a']}</div><div class="reco-role">{T['reco2_r']}</div></div>
        <div class="reco-card"><div class="reco-quote">{T['reco3_q']}</div><div class="reco-author">{T['reco3_a']}</div><div class="reco-role">{T['reco3_r']}</div></div>
        <div class="reco-card"><div class="reco-quote">{T['reco4_q']}</div><div class="reco-author">{T['reco4_a']}</div><div class="reco-role">{T['reco4_r']}</div></div>
    </div>
</section>
""", unsafe_allow_html=True)

# ── FORMATIONS ───────────────────────────────────────────────────────────────
st.markdown(f"""
<section class="section">
    <div class="section-eyebrow">{T['edu_eyebrow']}</div>
    <h2 class="section-title">{T['edu_title']}</h2>
    <div style="margin-bottom:2rem">
        <div class="certif-grid">
            <div class="certif-badge featured"><span class="certif-icon">☁️</span>Google Cloud Certified — Associate Cloud Engineer · 2026</div>
            <div class="certif-badge"><span class="certif-icon">🤖</span>ML Model Training Solution (Microsoft)</div>
            <div class="certif-badge"><span class="certif-icon">📊</span>Analyst de Données (Microsoft)</div>
            <div class="certif-badge"><span class="certif-icon">🎯</span>Expert Stratégies Digitales (Digital Campus)</div>
            <div class="certif-badge"><span class="certif-icon">🐍</span>Python Fundamentals (DataCamp)</div>
            <div class="certif-badge"><span class="certif-icon">💾</span>Intermediate SQL (DataCamp)</div>
            <div class="certif-badge"><span class="certif-icon">📉</span>Data Visualization in Power BI (DataCamp)</div>
            <div class="certif-badge"><span class="certif-icon">R</span>R Programming (DataCamp)</div>
        </div>
    </div>
    <div class="divider"></div>
    <div class="edu-item">
        <div class="edu-year">2024–2025</div>
        <div><div class="edu-title">{T['edu1_title']}</div><div class="edu-school">{T['edu1_school']}</div><div class="edu-mention">{T['edu1_mention']}</div></div>
    </div>
    <div class="edu-item">
        <div class="edu-year">2022–2024</div>
        <div><div class="edu-title">{T['edu2_title']}</div><div class="edu-school">{T['edu2_school']}</div><div class="edu-mention">{T['edu2_mention']}</div></div>
    </div>
</section>
""", unsafe_allow_html=True)

# ── CONTACT ──────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="contact-section">
    <div class="contact-title">{T['contact_title']}</div>
    <div class="contact-sub">{T['contact_sub']}</div>
    <div class="contact-links">
        <a href="mailto:soumanoseydou@icloud.com" class="contact-link primary">📧 soumanoseydou@icloud.com</a>
        <a href="https://linkedin.com/in/seydou-soumano" class="contact-link secondary">🔗 LinkedIn</a>
        <a href="tel:+33664678887" class="contact-link secondary">📱 +33 6 64 67 88 87</a>
        <a href="https://github.com/Ssoumano" class="contact-link secondary">⚙️ GitHub</a>
    </div>
</div>
""", unsafe_allow_html=True)
