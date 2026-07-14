import streamlit as st

# ── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Seydou Soumano · Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── CSS GLOBAL ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

/* RESET & BASE */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    background-color: #0A0F1E !important;
    color: #E8ECF4 !important;
    font-family: 'Inter', sans-serif !important;
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0A0F1E 0%, #0D1628 50%, #0A0F1E 100%) !important;
}

/* Hide Streamlit chrome */
#MainMenu, header, footer, [data-testid="stToolbar"],
[data-testid="stDecoration"], [data-testid="stStatusWidget"] { display: none !important; }

/* Remove sidebar */
[data-testid="stSidebar"] { display: none !important; }

/* Main container */
.main .block-container {
    max-width: 1100px !important;
    padding: 0 2rem 4rem !important;
    margin: 0 auto !important;
}

/* ── TYPOGRAPHY ── */
h1, h2, h3 { font-family: 'Space Grotesk', sans-serif !important; }

/* ── NAV ── */
.nav-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.5rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 4rem;
}
.nav-logo {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #E8ECF4;
    letter-spacing: -0.02em;
}
.nav-logo span { color: #4F8EF7; }
.nav-links { display: flex; gap: 2rem; }
.nav-links a {
    color: #8B9CB8;
    text-decoration: none;
    font-size: 0.875rem;
    font-weight: 500;
    transition: color 0.2s;
}
.nav-links a:hover { color: #E8ECF4; }
.nav-cta {
    background: #4F8EF7;
    color: white !important;
    padding: 0.5rem 1.25rem;
    border-radius: 6px;
    font-size: 0.875rem;
    font-weight: 600;
}

/* ── HERO ── */
.hero {
    padding: 2rem 0 5rem;
    position: relative;
}
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(79,142,247,0.12);
    border: 1px solid rgba(79,142,247,0.3);
    border-radius: 100px;
    padding: 0.35rem 1rem;
    font-size: 0.8rem;
    font-weight: 600;
    color: #4F8EF7;
    margin-bottom: 1.75rem;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}
.hero-badge::before {
    content: '';
    width: 6px; height: 6px;
    background: #4F8EF7;
    border-radius: 50%;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(1.3); }
}
.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(2.5rem, 5vw, 3.75rem);
    font-weight: 700;
    line-height: 1.1;
    letter-spacing: -0.03em;
    color: #E8ECF4;
    margin-bottom: 1.25rem;
}
.hero-title .accent { color: #4F8EF7; }
.hero-title .dim { color: #8B9CB8; }
.hero-sub {
    font-size: 1.1rem;
    color: #8B9CB8;
    line-height: 1.7;
    max-width: 560px;
    margin-bottom: 2.5rem;
    font-weight: 400;
}
.hero-sub strong { color: #C8D4E8; font-weight: 600; }
.hero-actions { display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 3.5rem; }
.btn-primary {
    background: #4F8EF7;
    color: white;
    padding: 0.8rem 1.75rem;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 600;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    transition: all 0.2s;
    box-shadow: 0 4px 20px rgba(79,142,247,0.3);
}
.btn-primary:hover { background: #3A7AE4; transform: translateY(-1px); }
.btn-secondary {
    background: transparent;
    color: #C8D4E8;
    padding: 0.8rem 1.75rem;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 600;
    text-decoration: none;
    border: 1px solid rgba(255,255,255,0.15);
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    transition: all 0.2s;
}
.btn-secondary:hover { border-color: rgba(255,255,255,0.3); color: white; }

/* ── STATS BAR (Anchoring bias) ── */
.stats-bar {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1px;
    background: rgba(255,255,255,0.06);
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.06);
}
.stat-item {
    background: rgba(255,255,255,0.02);
    padding: 1.25rem 1.5rem;
    text-align: center;
    transition: background 0.2s;
}
.stat-item:hover { background: rgba(79,142,247,0.05); }
.stat-number {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.8rem;
    font-weight: 700;
    color: #4F8EF7;
    line-height: 1;
    margin-bottom: 0.3rem;
    letter-spacing: -0.02em;
}
.stat-label {
    font-size: 0.75rem;
    color: #8B9CB8;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* ── SECTION TITLES ── */
.section {
    margin-top: 5rem;
}
.section-eyebrow {
    font-size: 0.75rem;
    font-weight: 700;
    color: #4F8EF7;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 0.75rem;
}
.section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.75rem;
    font-weight: 700;
    color: #E8ECF4;
    letter-spacing: -0.02em;
    margin-bottom: 0.5rem;
}
.section-sub {
    color: #8B9CB8;
    font-size: 0.95rem;
    line-height: 1.6;
    margin-bottom: 2.5rem;
}

/* ── SKILL TAGS ── */
.skills-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin-bottom: 1.5rem;
}
.skill-tag {
    background: rgba(79,142,247,0.08);
    border: 1px solid rgba(79,142,247,0.2);
    color: #C8D4E8;
    padding: 0.4rem 0.9rem;
    border-radius: 6px;
    font-size: 0.82rem;
    font-weight: 500;
    transition: all 0.2s;
}
.skill-tag:hover {
    background: rgba(79,142,247,0.15);
    border-color: rgba(79,142,247,0.4);
    color: white;
}
.skill-tag.highlight {
    background: rgba(79,142,247,0.2);
    border-color: #4F8EF7;
    color: #4F8EF7;
    font-weight: 600;
}

/* ── EXPERIENCE CARDS ── */
.exp-card {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 12px;
    padding: 1.75rem;
    margin-bottom: 1rem;
    transition: all 0.25s;
    position: relative;
    overflow: hidden;
}
.exp-card::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 3px;
    background: #4F8EF7;
    opacity: 0;
    transition: opacity 0.25s;
}
.exp-card:hover {
    border-color: rgba(79,142,247,0.3);
    background: rgba(79,142,247,0.04);
    transform: translateX(4px);
}
.exp-card:hover::before { opacity: 1; }
.exp-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 1rem;
    flex-wrap: wrap;
    gap: 0.5rem;
}
.exp-role {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: #E8ECF4;
    margin-bottom: 0.2rem;
}
.exp-company {
    font-size: 0.875rem;
    color: #4F8EF7;
    font-weight: 600;
}
.exp-period {
    font-size: 0.78rem;
    color: #8B9CB8;
    background: rgba(255,255,255,0.05);
    padding: 0.25rem 0.75rem;
    border-radius: 100px;
    font-weight: 500;
    white-space: nowrap;
}
.exp-bullets { list-style: none; }
.exp-bullets li {
    font-size: 0.875rem;
    color: #8B9CB8;
    line-height: 1.6;
    padding: 0.2rem 0;
    padding-left: 1.25rem;
    position: relative;
}
.exp-bullets li::before {
    content: '→';
    position: absolute;
    left: 0;
    color: #4F8EF7;
    font-size: 0.75rem;
}
.exp-bullets li strong { color: #C8D4E8; font-weight: 600; }
.exp-tags { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 1rem; }
.exp-tag {
    font-size: 0.72rem;
    background: rgba(255,255,255,0.04);
    color: #8B9CB8;
    padding: 0.2rem 0.6rem;
    border-radius: 4px;
    font-weight: 500;
}

/* ── PROJECT CARDS ── */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
}
.project-card {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 12px;
    padding: 1.5rem;
    transition: all 0.25s;
    text-decoration: none;
    display: block;
}
.project-card:hover {
    border-color: rgba(79,142,247,0.4);
    background: rgba(79,142,247,0.05);
    transform: translateY(-3px);
    box-shadow: 0 12px 40px rgba(0,0,0,0.3);
}
.project-icon {
    font-size: 1.75rem;
    margin-bottom: 1rem;
}
.project-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.95rem;
    font-weight: 700;
    color: #E8ECF4;
    margin-bottom: 0.4rem;
}
.project-desc {
    font-size: 0.83rem;
    color: #8B9CB8;
    line-height: 1.5;
    margin-bottom: 1rem;
}
.project-stack {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
}
.stack-tag {
    font-size: 0.7rem;
    background: rgba(79,142,247,0.1);
    color: #4F8EF7;
    padding: 0.2rem 0.55rem;
    border-radius: 4px;
    font-weight: 600;
}
.project-live {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    font-size: 0.75rem;
    color: #4F8EF7;
    font-weight: 600;
    margin-top: 0.75rem;
}
.project-live::before {
    content: '';
    width: 6px; height: 6px;
    background: #22C55E;
    border-radius: 50%;
}

/* ── RECOMMANDATIONS (Social Proof) ── */
.reco-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
}
.reco-card {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 12px;
    padding: 1.5rem;
}
.reco-quote {
    font-size: 0.875rem;
    color: #C8D4E8;
    line-height: 1.7;
    font-style: italic;
    margin-bottom: 1rem;
    position: relative;
}
.reco-quote::before {
    content: '"';
    font-size: 3rem;
    color: rgba(79,142,247,0.2);
    font-family: Georgia, serif;
    line-height: 1;
    float: left;
    margin-right: 0.25rem;
    margin-top: -0.5rem;
}
.reco-author {
    font-size: 0.8rem;
    font-weight: 700;
    color: #4F8EF7;
}
.reco-role {
    font-size: 0.75rem;
    color: #8B9CB8;
    margin-top: 0.1rem;
}

/* ── CERTIF BADGES ── */
.certif-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
}
.certif-badge {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 8px;
    padding: 0.6rem 1rem;
    font-size: 0.82rem;
    color: #C8D4E8;
    font-weight: 500;
}
.certif-badge .certif-icon { font-size: 1.1rem; }
.certif-badge.featured {
    border-color: rgba(79,142,247,0.4);
    background: rgba(79,142,247,0.08);
    color: #4F8EF7;
    font-weight: 700;
}

/* ── FORMATION ── */
.edu-item {
    display: flex;
    gap: 1.25rem;
    padding: 1.25rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
.edu-item:last-child { border-bottom: none; }
.edu-year {
    font-size: 0.78rem;
    color: #8B9CB8;
    font-weight: 600;
    min-width: 70px;
    padding-top: 0.1rem;
}
.edu-title {
    font-weight: 700;
    color: #E8ECF4;
    font-size: 0.9rem;
    margin-bottom: 0.1rem;
}
.edu-school {
    font-size: 0.82rem;
    color: #4F8EF7;
    font-weight: 500;
}
.edu-mention {
    font-size: 0.75rem;
    color: #8B9CB8;
    margin-top: 0.25rem;
}

/* ── CONTACT SECTION ── */
.contact-section {
    background: linear-gradient(135deg, rgba(79,142,247,0.08) 0%, rgba(79,142,247,0.03) 100%);
    border: 1px solid rgba(79,142,247,0.2);
    border-radius: 16px;
    padding: 3rem;
    text-align: center;
    margin-top: 5rem;
}
.contact-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.75rem;
    font-weight: 700;
    color: #E8ECF4;
    margin-bottom: 0.75rem;
}
.contact-sub {
    color: #8B9CB8;
    font-size: 0.95rem;
    margin-bottom: 2rem;
}
.contact-links {
    display: flex;
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
}
.contact-link {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.7rem 1.5rem;
    border-radius: 8px;
    font-size: 0.875rem;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.2s;
}
.contact-link.primary {
    background: #4F8EF7;
    color: white;
    box-shadow: 0 4px 15px rgba(79,142,247,0.3);
}
.contact-link.secondary {
    background: rgba(255,255,255,0.05);
    color: #C8D4E8;
    border: 1px solid rgba(255,255,255,0.1);
}
.contact-link:hover { opacity: 0.85; transform: translateY(-1px); }

/* ── DIVIDER ── */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(79,142,247,0.3), transparent);
    margin: 1rem 0;
}

/* Streamlit element cleanup */
[data-testid="stMarkdownContainer"] p { margin: 0; }
.stMarkdown { width: 100%; }
</style>
""", unsafe_allow_html=True)


# ── NAV ──────────────────────────────────────────────────────────────────────
st.markdown("""
<nav class="nav-bar">
    <div class="nav-logo">Seydou<span>.</span></div>
    <div class="nav-links">
        <a href="#experience">Expériences</a>
        <a href="#projets">Projets</a>
        <a href="#recommandations">Recommandations</a>
        <a href="mailto:soumanoseydou@icloud.com" class="nav-cta">Me contacter</a>
    </div>
</nav>
""", unsafe_allow_html=True)


# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<section class="hero">
    <div class="hero-badge">🟢 Disponible immédiatement · Île-de-France</div>
    <h1 class="hero-title">
        Data Analyst.<br>
        <span class="dim">Je transforme la donnée</span><br>
        <span class="accent">en décisions.</span>
    </h1>
    <p class="hero-sub">
        3 ans d'expérience en <strong>BI, SQL, Python et IA générative</strong>.
        Certifié <strong>Google Cloud ACE</strong>. Je construis des pipelines,
        des dashboards et des solutions IA déployées en production —
        pas juste des slides.
    </p>
    <div class="hero-actions">
        <a href="mailto:soumanoseydou@icloud.com" class="btn-primary">📧 Me contacter</a>
        <a href="https://linkedin.com/in/seydou-soumano" class="btn-secondary">🔗 LinkedIn</a>
        <a href="https://github.com/Ssoumano" class="btn-secondary">⚙️ GitHub</a>
    </div>
</section>
""", unsafe_allow_html=True)

st.markdown("""
<div class="stats-bar">
    <div class="stat-item">
        <div class="stat-number">3 ans</div>
        <div class="stat-label">Expérience data</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">98%</div>
        <div class="stat-label">Anomalies corrigées</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">+18%</div>
        <div class="stat-label">Clients réactivés</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">GCP</div>
        <div class="stat-label">Certifié ACE · 2026</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ── COMPÉTENCES ──────────────────────────────────────────────────────────────
st.markdown("""
<section class="section">
    <div class="section-eyebrow">Stack technique</div>
    <h2 class="section-title">Compétences</h2>
    <p class="section-sub">Outils que j'utilise en production, pas juste sur un CV.</p>

    <div style="margin-bottom:1.25rem">
        <div style="font-size:0.78rem;font-weight:700;color:#8B9CB8;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.6rem">Data & Analyse</div>
        <div class="skills-grid">
            <span class="skill-tag highlight">SQL avancé</span>
            <span class="skill-tag highlight">Python</span>
            <span class="skill-tag">Pandas · NumPy</span>
            <span class="skill-tag">Segmentation</span>
            <span class="skill-tag">A/B Testing</span>
            <span class="skill-tag">Scoring</span>
            <span class="skill-tag">Data profiling</span>
            <span class="skill-tag">OpenMetadata</span>
        </div>
    </div>

    <div style="margin-bottom:1.25rem">
        <div style="font-size:0.78rem;font-weight:700;color:#8B9CB8;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.6rem">BI & Dataviz</div>
        <div class="skills-grid">
            <span class="skill-tag highlight">Power BI (DAX)</span>
            <span class="skill-tag highlight">QlikView</span>
            <span class="skill-tag">Looker Studio</span>
            <span class="skill-tag">Tableau</span>
            <span class="skill-tag">Excel VBA</span>
            <span class="skill-tag">Dashboards interactifs</span>
        </div>
    </div>

    <div>
        <div style="font-size:0.78rem;font-weight:700;color:#8B9CB8;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.6rem">Cloud & IA</div>
        <div class="skills-grid">
            <span class="skill-tag highlight">GCP (Certifié ACE)</span>
            <span class="skill-tag highlight">BigQuery</span>
            <span class="skill-tag">Cloud Storage</span>
            <span class="skill-tag">Streamlit</span>
            <span class="skill-tag">OpenAI API</span>
            <span class="skill-tag">IA générative</span>
            <span class="skill-tag">Agile / Scrum</span>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)


# ── EXPÉRIENCES ──────────────────────────────────────────────────────────────
st.markdown("""
<section class="section" id="experience">
    <div class="section-eyebrow">Parcours</div>
    <h2 class="section-title">Expériences professionnelles</h2>
    <p class="section-sub">Des missions avec des résultats mesurables, pas juste des missions.</p>

    <div class="exp-card">
        <div class="exp-header">
            <div>
                <div class="exp-role">Consultant Chef de Projets SI & Data Analyst</div>
                <div class="exp-company">Clap Partner · Paris · Industrie, Retail, Luxe</div>
            </div>
            <div class="exp-period">08/2024 – 10/2025 · Alternance</div>
        </div>
        <ul class="exp-bullets">
            <li>Analyse multi-sources en SQL et Python : détection d'anomalies, identification de tendances et d'opportunités business pour les directions métiers</li>
            <li><strong>98% des anomalies data corrigées</strong> grâce à des contrôles qualité rigoureux sur 10+ projets SI end-to-end</li>
            <li>Conception et maintien de dashboards Power BI pour le pilotage des KPIs de performance</li>
            <li>Animation d'ateliers clients, rédaction de roadmaps et restitution d'insights actionnables en COPROJ/COPIL</li>
            <li>Pilotage de projets en méthode Agile : sprints, reviews, backlog, démos</li>
        </ul>
        <div class="exp-tags">
            <span class="exp-tag">SQL</span><span class="exp-tag">Python</span>
            <span class="exp-tag">Power BI</span><span class="exp-tag">SAP SuccessFactors</span>
            <span class="exp-tag">Agile</span><span class="exp-tag">Data Quality</span>
        </div>
    </div>

    <div class="exp-card">
        <div class="exp-header">
            <div>
                <div class="exp-role">Business Data Analyst — Performance Commerciale BtoB</div>
                <div class="exp-company">VWR Avantor · Paris · 4 pays (FR, BE, ES, PT)</div>
            </div>
            <div class="exp-period">10/2022 – 05/2024</div>
        </div>
        <ul class="exp-bullets">
            <li>Analyse de performances commerciales sur 6 000+ clients dans 4 pays via SQL et Python</li>
            <li>Modèle de segmentation clients → <strong>+18% de clients réactivés en 3 mois</strong></li>
            <li>Dashboards automatisés (QlikView, Power BI, Excel VBA) utilisés comme référence par 3 équipes sur 4 pays</li>
            <li><strong>91% de taux de digitalisation atteint</strong> grâce aux analyses et recommandations data</li>
            <li>Restitution d'insights actionnables aux directions commerciales et marketing</li>
        </ul>
        <div class="exp-tags">
            <span class="exp-tag">SQL</span><span class="exp-tag">Python</span>
            <span class="exp-tag">QlikView</span><span class="exp-tag">Power BI</span>
            <span class="exp-tag">Excel VBA</span><span class="exp-tag">Segmentation</span>
        </div>
    </div>

    <div class="exp-card">
        <div class="exp-header">
            <div>
                <div class="exp-role">Data Analyst · Stage</div>
                <div class="exp-company">Moby Deck · Paris</div>
            </div>
            <div class="exp-period">04/2022 – 06/2022</div>
        </div>
        <ul class="exp-bullets">
            <li>Fiabilisation d'une base de <strong>32 000+ entrées</strong> (8 000 modèles de véhicules)</li>
            <li>Automatisation de la classification selon des critères métier spécifiques</li>
        </ul>
        <div class="exp-tags">
            <span class="exp-tag">Python</span><span class="exp-tag">Data Quality</span><span class="exp-tag">Automatisation</span>
        </div>
    </div>

    <div class="exp-card">
        <div class="exp-header">
            <div>
                <div class="exp-role">Data Analyst · Stage</div>
                <div class="exp-company">Orange · Mali</div>
            </div>
            <div class="exp-period">07/2019 – 09/2019</div>
        </div>
        <ul class="exp-bullets">
            <li>Reporting satisfaction clients pour les comités de direction</li>
            <li>Collecte et analyse des données de satisfaction et motifs d'insatisfaction</li>
        </ul>
        <div class="exp-tags">
            <span class="exp-tag">Reporting</span><span class="exp-tag">Excel</span>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)


# ── PROJETS ──────────────────────────────────────────────────────────────────
st.markdown("""
<section class="section" id="projets">
    <div class="section-eyebrow">Portfolio technique</div>
    <h2 class="section-title">Projets déployés</h2>
    <p class="section-sub">Du code en production. Pas juste des notebooks.</p>

    <div class="projects-grid">
        <a class="project-card" href="https://plateforme-data-quality-fgtzf5rzl9tgr39wvk22tz.streamlit.app/" target="_blank">
            <div class="project-icon">🤖</div>
            <div class="project-title">Plateforme Data Quality IA</div>
            <div class="project-desc">Automatisation de la détection d'anomalies et fiabilisation des données via IA générative. Déployé en production.</div>
            <div class="project-stack">
                <span class="stack-tag">Python</span>
                <span class="stack-tag">Streamlit</span>
                <span class="stack-tag">OpenAI API</span>
                <span class="stack-tag">IA Générative</span>
            </div>
            <div class="project-live">Live en production</div>
        </a>

        <a class="project-card" href="https://soumano-seydou.streamlit.app/" target="_blank">
            <div class="project-icon">☁️</div>
            <div class="project-title">Pipeline Analytique GCP</div>
            <div class="project-desc">Ingestion de 212 000+ lignes de données publiques. Modélisation SQL, vues analytiques et dashboard Looker Studio.</div>
            <div class="project-stack">
                <span class="stack-tag">BigQuery</span>
                <span class="stack-tag">GCS</span>
                <span class="stack-tag">Looker Studio</span>
                <span class="stack-tag">SQL</span>
                <span class="stack-tag">Python</span>
            </div>
            <div class="project-live">Portfolio en ligne</div>
        </a>

        <div class="project-card">
            <div class="project-icon">📊</div>
            <div class="project-title">Dashboard Performance 4 Pays</div>
            <div class="project-desc">Dashboard automatisé pour le pilotage des performances commerciales (France, Belgique, Espagne, Portugal). Macros VBA + navigation dynamique.</div>
            <div class="project-stack">
                <span class="stack-tag">Excel VBA</span>
                <span class="stack-tag">QlikView</span>
                <span class="stack-tag">Power BI</span>
            </div>
        </div>

        <div class="project-card">
            <div class="project-icon">🔄</div>
            <div class="project-title">Analyse Churn & Rétention Client</div>
            <div class="project-desc">Modèle prédictif d'identification des segments clients à risque pour une entreprise téléphonique.</div>
            <div class="project-stack">
                <span class="stack-tag">Python</span>
                <span class="stack-tag">SQL</span>
                <span class="stack-tag">Power BI</span>
                <span class="stack-tag">ML</span>
            </div>
        </div>

        <div class="project-card">
            <div class="project-icon">🗺️</div>
            <div class="project-title">Dashboard Criminalité par Région</div>
            <div class="project-desc">Analyse de l'évolution des crimes dans chaque région française. Interface interactive déployée en ligne.</div>
            <div class="project-stack">
                <span class="stack-tag">Python</span>
                <span class="stack-tag">Streamlit</span>
                <span class="stack-tag">Pandas</span>
                <span class="stack-tag">Data.gouv</span>
            </div>
        </div>

        <div class="project-card">
            <div class="project-icon">📈</div>
            <div class="project-title">Analyse Prédictive Égalité F/H</div>
            <div class="project-desc">Analyse prédictive de l'évolution de l'indice d'égalité Femmes/Hommes à partir de données publiques.</div>
            <div class="project-stack">
                <span class="stack-tag">SQL</span>
                <span class="stack-tag">Python</span>
                <span class="stack-tag">Excel</span>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)


# ── RECOMMANDATIONS (Social Proof bias) ──────────────────────────────────────
st.markdown("""
<section class="section" id="recommandations">
    <div class="section-eyebrow">Social proof</div>
    <h2 class="section-title">Ce que disent ceux qui ont travaillé avec moi</h2>
    <p class="section-sub">Des recommandations réelles, pas des phrases génériques.</p>

    <div class="reco-grid">
        <div class="reco-card">
            <div class="reco-quote">Sa capacité à appliquer ses connaissances de manière innovante dans des projets concrets a grandement contribué à la réussite de ceux-ci.</div>
            <div class="reco-author">O. Mamavi</div>
            <div class="reco-role">Docteur en Sciences de gestion · Directeur Data, Management & Datascience · Professeur PSB</div>
        </div>
        <div class="reco-card">
            <div class="reco-quote">Sa facilité à coordonner et à motiver ses camarades reflète ses fortes aptitudes en management et leadership, des qualités qui le rendent particulièrement bien adapté pour exceller.</div>
            <div class="reco-author">O. Mamavi</div>
            <div class="reco-role">Docteur en Sciences de gestion · Directeur Data, Management & Datascience</div>
        </div>
        <div class="reco-card">
            <div class="reco-quote">Je voudrais en toute honnêteté exprimer ma très grande satisfaction et confiance en ses qualités personnelles, sur un plan disciplinaire et intellectuel, ainsi que son dynamisme constant dans le travail individuel et collectif.</div>
            <div class="reco-author">I. Traore</div>
            <div class="reco-role">Psychologue et Manager des organisations</div>
        </div>
        <div class="reco-card">
            <div class="reco-quote">Bienveillant, motivant et empathique. Son sens du collectif et son attachement à l'humain sont évidents et font de lui un professionnel compétent et unique.</div>
            <div class="reco-author">M. Iche</div>
            <div class="reco-role">Développeur Web · Bpartner</div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)


# ── FORMATIONS ───────────────────────────────────────────────────────────────
st.markdown("""
<section class="section">
    <div class="section-eyebrow">Éducation</div>
    <h2 class="section-title">Formation & Certifications</h2>

    <div style="margin-bottom:2rem">
        <div class="certif-grid">
            <div class="certif-badge featured">
                <span class="certif-icon">☁️</span>
                Google Cloud Certified — Associate Cloud Engineer · Mars 2026
            </div>
            <div class="certif-badge">
                <span class="certif-icon">🤖</span>
                ML Model Training Solution (Microsoft)
            </div>
            <div class="certif-badge">
                <span class="certif-icon">📊</span>
                Analyst de Données (Microsoft)
            </div>
            <div class="certif-badge">
                <span class="certif-icon">🎯</span>
                Expert Stratégies Digitales (Digital Campus)
            </div>
            <div class="certif-badge">
                <span class="certif-icon">🐍</span>
                Python Fundamentals (DataCamp)
            </div>
            <div class="certif-badge">
                <span class="certif-icon">💾</span>
                Intermediate SQL (DataCamp)
            </div>
            <div class="certif-badge">
                <span class="certif-icon">📉</span>
                Data Visualization in Power BI (DataCamp)
            </div>
            <div class="certif-badge">
                <span class="certif-icon">R</span>
                R Programming (DataCamp)
            </div>
        </div>
    </div>

    <div class="divider"></div>

    <div class="edu-item">
        <div class="edu-year">2024–2025</div>
        <div>
            <div class="edu-title">MBA Big Data & Intelligence Artificielle</div>
            <div class="edu-school">MBA ESG · Paris</div>
            <div class="edu-mention">MLOps · Data Engineering · Data Quality · BI · Gestion de projets</div>
        </div>
    </div>
    <div class="edu-item">
        <div class="edu-year">2022–2024</div>
        <div>
            <div class="edu-title">MSc Data Management</div>
            <div class="edu-school">Paris School of Business & EFREI</div>
            <div class="edu-mention">Mention Bien · Data gouvernance · ML · Modélisation · Statistiques</div>
        </div>
    </div>
    <div class="edu-item">
        <div class="edu-year">2021–2022</div>
        <div>
            <div class="edu-title">MSc1 Data Scientist & Business Analysis</div>
            <div class="edu-school">EDC Paris Business School</div>
            <div class="edu-mention">Mention Bien · Algorithmie · Finance · Bases de données</div>
        </div>
    </div>
    <div class="edu-item">
        <div class="edu-year">2017–2020</div>
        <div>
            <div class="edu-title">Licence Management des Entreprises</div>
            <div class="edu-school">IHEM · Bamako, Mali</div>
            <div class="edu-mention">Mention Bien · Management · Marketing · Finances</div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)


# ── CONTACT ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="contact-section">
    <div class="contact-title">On travaille ensemble ?</div>
    <div class="contact-sub">Disponible immédiatement en Île-de-France · Anglais C1 · Ouvert au remote</div>
    <div class="contact-links">
        <a href="mailto:soumanoseydou@icloud.com" class="contact-link primary">📧 soumanoseydou@icloud.com</a>
        <a href="https://linkedin.com/in/seydou-soumano" class="contact-link secondary">🔗 LinkedIn</a>
        <a href="tel:+33664678887" class="contact-link secondary">📱 +33 6 64 67 88 87</a>
        <a href="https://github.com/Ssoumano" class="contact-link secondary">⚙️ GitHub</a>
    </div>
</div>
""", unsafe_allow_html=True)
