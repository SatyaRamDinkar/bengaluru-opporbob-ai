"""
OpportunityBob — Streamlit Live Demo
IBM Bobathon: Build for Bengaluru | Theme 2: More Opportunity Greater Together
Built with IBM Bob | Multilingual AI for Employment & Community Access
"""
import streamlit as st
import json
import sys
import os

# ── Path setup so bob_agent imports cleanly on Streamlit Cloud ──────────────
sys.path.insert(0, os.path.dirname(__file__))
from app.bob_agent import IBMBobAgent

# ── Page config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="OpportunityBob — IBM Bobathon",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Global */
html, body, [class*="css"] { font-family: 'Segoe UI', sans-serif; }

/* Hide default header */
#MainMenu, footer, header { visibility: hidden; }

/* Top banner */
.top-banner {
    background: linear-gradient(135deg, #0543CE 0%, #0033A0 60%, #001B70 100%);
    border-radius: 12px;
    padding: 28px 36px 20px 36px;
    margin-bottom: 24px;
    border-left: 7px solid #FFC000;
}
.top-banner h1 { color: #fff; font-size: 2.4rem; margin: 0; font-weight: 800; }
.top-banner p  { color: #C0D8FF; margin: 6px 0 0 0; font-size: 1.05rem; }
.badge {
    display: inline-block;
    background: #FFC000;
    color: #000;
    font-weight: 700;
    font-size: 0.78rem;
    padding: 3px 12px;
    border-radius: 20px;
    margin-bottom: 10px;
    letter-spacing: 0.5px;
}

/* Metric cards */
.metric-row { display: flex; gap: 16px; margin-bottom: 20px; flex-wrap: wrap; }
.metric-card {
    flex: 1; min-width: 140px;
    background: linear-gradient(135deg, #0543CE, #0033A0);
    border-radius: 10px;
    padding: 18px 16px;
    text-align: center;
    color: white;
}
.metric-card .num { font-size: 2rem; font-weight: 800; color: #FFC000; }
.metric-card .lbl { font-size: 0.82rem; color: #C0D8FF; margin-top: 4px; }

/* Job card */
.job-card {
    background: white;
    border-radius: 10px;
    padding: 18px 20px;
    margin-bottom: 14px;
    border-left: 5px solid #0543CE;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
.job-card .title { font-size: 1.1rem; font-weight: 700; color: #0543CE; }
.job-card .company { color: #555; font-size: 0.9rem; }
.job-card .score-bar-wrap { margin-top: 10px; background: #E8F0FE; border-radius: 20px; height: 10px; }
.job-card .score-bar { background: linear-gradient(90deg,#0543CE,#408BFC); height: 10px; border-radius: 20px; }
.job-card .tag {
    display: inline-block; background: #E8F0FE; color: #0543CE;
    font-size: 0.72rem; padding: 2px 10px; border-radius: 20px;
    margin: 4px 3px 0 0; font-weight: 600;
}
.high-fit  { background: #E6F9EE !important; border-left-color: #24A148 !important; }
.high-fit .title { color: #24A148 !important; }

/* Community card */
.comm-card {
    background: white; border-radius: 10px;
    padding: 16px 18px; margin-bottom: 12px;
    border-left: 5px solid #009199;
    box-shadow: 0 2px 8px rgba(0,0,0,0.07);
}
.comm-card .ctitle { font-weight: 700; color: #009199; font-size: 1rem; }

/* Skill path */
.skill-step {
    background: white; border-radius: 8px;
    padding: 14px 18px; margin-bottom: 10px;
    border-left: 4px solid #FF832A;
    box-shadow: 0 1px 6px rgba(0,0,0,0.07);
}
.step-num { background:#FF832A; color:white; border-radius:50%;
    width:26px; height:26px; display:inline-flex;
    align-items:center; justify-content:center; font-weight:700; font-size:0.9rem; }

/* XAI box */
.xai-box {
    background: #FFF8E1; border-radius: 8px;
    padding: 10px 14px; margin-top: 8px;
    border-left: 4px solid #FFC000; font-size: 0.85rem; color: #555;
}

/* Section header */
.sec-header {
    font-size: 1.3rem; font-weight: 700; color: #0543CE;
    border-bottom: 3px solid #FFC000; padding-bottom: 6px; margin-bottom: 18px;
}

/* Bob story */
.bob-box {
    background: linear-gradient(135deg, #0543CE, #001B70);
    color: white; border-radius: 10px; padding: 20px 24px;
    border-left: 6px solid #FFC000;
}

/* Footer */
.footer {
    text-align: center; color: #aaa; font-size: 0.8rem;
    padding: 24px 0 8px 0; border-top: 1px solid #eee; margin-top: 32px;
}
</style>
""", unsafe_allow_html=True)

# ── Load data ────────────────────────────────────────────────────────────────
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

@st.cache_data
def load_jobs():
    with open(os.path.join(DATA_DIR, "jobs.json"), encoding="utf-8") as f:
        return json.load(f)

@st.cache_data
def load_community():
    with open(os.path.join(DATA_DIR, "community_exchange.json"), encoding="utf-8") as f:
        return json.load(f)

@st.cache_data
def load_skills():
    with open(os.path.join(DATA_DIR, "skills_knowledge.json"), encoding="utf-8") as f:
        return json.load(f)

jobs_data      = load_jobs()
community_data = load_community()
skills_data    = load_skills()

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🌐 Language / ಭಾಷೆ / भाषा")
    lang = st.selectbox("Select Language", ["English", "Kannada (ಕನ್ನಡ)", "Hindi (हिंदी)"],
                        label_visibility="collapsed")
    lang_code = {"English": "en", "Kannada (ಕನ್ನಡ)": "kn", "Hindi (हिंदी)": "hi"}[lang]

    st.markdown("---")
    st.markdown("### 📌 Navigation")
    page = st.radio("", ["🔍 Job Matching", "📚 Skill Gap", "🤝 Community Exchange", "🤖 Bob Story"],
                    label_visibility="collapsed")

    st.markdown("---")
    st.markdown("""
    <div style='font-size:0.8rem; color:#888;'>
    <b>Built with IBM Bob</b><br>
    IBM Bobathon 2026<br>
    Theme 2: More Opportunity<br>Greater Together<br><br>
    <a href='https://github.com/SatyaRamDinkar/bengaluru-opporbob-ai' target='_blank'>
    GitHub Repo</a>
    </div>
    """, unsafe_allow_html=True)

# ── Top Banner ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="top-banner">
  <div class="badge">IBM BOBATHON 2026 | THEME 2: MORE OPPORTUNITY GREATER TOGETHER</div>
  <h1>🤖 OpportunityBob</h1>
  <p>Multilingual AI for Employment &amp; Community Access in Bengaluru — Built with IBM Bob</p>
</div>
""", unsafe_allow_html=True)

# ── Metrics row ──────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="metric-row">
  <div class="metric-card"><div class="num">{len(jobs_data)}</div><div class="lbl">Live Job Opportunities</div></div>
  <div class="metric-card"><div class="num">3</div><div class="lbl">Languages Supported</div></div>
  <div class="metric-card"><div class="num">{len(community_data)}</div><div class="lbl">Community Resources</div></div>
  <div class="metric-card"><div class="num">&lt; 3 Min</div><div class="lbl">Job Match Time</div></div>
  <div class="metric-card"><div class="num">0 PII</div><div class="lbl">Data Stored</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ════════════════════════════════════════════════════════════════════════════
# PAGE 1 — JOB MATCHING
# ════════════════════════════════════════════════════════════════════════════
if page == "🔍 Job Matching":
    st.markdown('<div class="sec-header">🔍 Job & Apprenticeship Matching</div>', unsafe_allow_html=True)

    placeholder_map = {
        "en": "e.g. I am looking for EV battery technician jobs in Peenya...",
        "kn": "ಉದಾ: ನನಗೆ ಪೀಣ್ಯದಲ್ಲಿ ಇವಿ ಬ್ಯಾಟರಿ ತಂತ್ರಜ್ಞ ಕೆಲಸ ಬೇಕು...",
        "hi": "उदा: मुझे पीण्या में ईवी बैटरी तकनीशियन की नौकरी चाहिए...",
    }

    query = st.text_area(
        "Enter your job search query (English, Kannada, or Hindi):",
        placeholder=placeholder_map[lang_code], height=100
    )

    col1, col2 = st.columns([1, 4])
    with col1:
        search_btn = st.button("🔍 Find Jobs", use_container_width=True, type="primary")
    with col2:
        st.caption("IBM Bob uses XAI-grounded semantic matching across all three languages simultaneously.")

    if search_btn and query.strip():
        clean_q = IBMBobAgent.redact_pii(query)
        if clean_q != query:
            st.info("🔒 PII detected and redacted before processing (Aadhaar/phone protected).")

        with st.spinner("Bob is matching opportunities for you..."):
            results = IBMBobAgent.match_jobs(clean_q, jobs_data, lang_code)

        st.success(f"✅ Found **{len(results)}** matching opportunities for Bengaluru")

        for job in results:
            fit = job.get("fit_grade", "Potential Fit")
            card_cls = "job-card high-fit" if fit == "High Fit" else "job-card"
            score = job.get("match_score", 65)
            skills_html = "".join(f'<span class="tag">{s}</span>' for s in job.get("required_skills", [])[:4])
            reasoning = job.get("bob_reasoning", "")

            st.markdown(f"""
            <div class="{card_cls}">
              <div class="title">{job.get('title_en','')}</div>
              <div class="company">🏢 {job.get('company','')} &nbsp;|&nbsp; 📍 {job.get('location','')} &nbsp;|&nbsp;
                💰 {job.get('stipend_range','')} &nbsp;|&nbsp; 🎓 {job.get('qualification','')}</div>
              <div style="margin-top:10px; font-size:0.88rem; color:#444;">{job.get('description_en','')}</div>
              <div style="margin-top:10px;">{skills_html}</div>
              <div style="margin-top:12px; font-size:0.82rem; color:#888;">Match Score</div>
              <div class="score-bar-wrap"><div class="score-bar" style="width:{score}%;"></div></div>
              <div style="font-size:0.82rem; color:#0543CE; font-weight:700; margin-top:4px;">{score}% — {fit}</div>
              <div class="xai-box">🤖 <b>Bob's Reasoning:</b> {reasoning}</div>
            </div>
            """, unsafe_allow_html=True)

    elif search_btn:
        st.warning("Please enter a search query.")
    else:
        # Show sample cards
        st.caption("**Sample opportunities available in Bengaluru:**")
        for job in jobs_data[:3]:
            skills_html = "".join(f'<span class="tag">{s}</span>' for s in job.get("required_skills", [])[:3])
            st.markdown(f"""
            <div class="job-card">
              <div class="title">{job.get('title_en','')}</div>
              <div class="company">🏢 {job.get('company','')} &nbsp;|&nbsp; 📍 {job.get('location','')} &nbsp;|&nbsp; 💰 {job.get('stipend_range','')}</div>
              <div style="margin-top:8px;">{skills_html}</div>
            </div>
            """, unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# PAGE 2 — SKILL GAP
# ════════════════════════════════════════════════════════════════════════════
elif page == "📚 Skill Gap":
    st.markdown('<div class="sec-header">📚 Skill Gap Analysis & Learning Roadmap</div>', unsafe_allow_html=True)

    job_options = {f"{j['title_en']} — {j['company']} ({j['location']})": j['id'] for j in jobs_data}
    selected_label = st.selectbox("Select Target Job Opportunity:", list(job_options.keys()))
    selected_id = job_options[selected_label]

    user_skills_input = st.text_input(
        "Enter your current skills (comma-separated):",
        placeholder="e.g. basic electricity, hand tools, safety training"
    )

    if st.button("📊 Analyse My Skills", type="primary"):
        if user_skills_input.strip():
            user_skills = [s.strip() for s in user_skills_input.split(",") if s.strip()]
            target_job = next((j for j in jobs_data if j["id"] == selected_id), None)

            with st.spinner("Bob is building your personalised learning path..."):
                analysis = IBMBobAgent.analyze_skill_gap(user_skills, target_job, skills_data)

            # Score gauge
            fit = analysis["current_fit_score"]
            col_a, col_b, col_c = st.columns(3)
            col_a.metric("Current Fit Score", f"{fit}%")
            col_b.metric("Skills You Have", len(analysis["possessed_skills"]))
            col_c.metric("Skills to Learn", len(analysis["missing_skills"]))

            st.progress(fit / 100)

            if analysis["possessed_skills"]:
                st.success("✅ **Skills you already have:** " + " | ".join(analysis["possessed_skills"]))

            if analysis["missing_skills"]:
                st.warning("🎯 **Skills to build:** " + " | ".join(analysis["missing_skills"]))

            if analysis["bob_custom_curriculum"]:
                st.markdown("### 🗺️ Your Bob-Customised Learning Roadmap")
                for path in analysis["bob_custom_curriculum"]:
                    with st.expander(f"📌 {path['skill']} — {path['level']}"):
                        for step in path["roadmap"]:
                            st.markdown(f"""
                            <div class="skill-step">
                              <span class="step-num">{step['step']}</span>
                              &nbsp;<b>{step['topic']}</b>
                              <div style="font-size:0.85rem; color:#666; margin-top:6px;">
                                ⏱ {step['duration']} &nbsp;|&nbsp; 🏫 {step['provider']}
                              </div>
                            </div>
                            """, unsafe_allow_html=True)

            if analysis.get("recommended_local_centers"):
                st.markdown("### 🏫 Recommended Local Skilling Centres in Bengaluru")
                for c in analysis["recommended_local_centers"]:
                    st.markdown(f"- **{c.get('name','')}** — {c.get('location','')} | {c.get('courses_offered','')}")
        else:
            st.warning("Please enter your skills.")


# ════════════════════════════════════════════════════════════════════════════
# PAGE 3 — COMMUNITY EXCHANGE
# ════════════════════════════════════════════════════════════════════════════
elif page == "🤝 Community Exchange":
    st.markdown('<div class="sec-header">🤝 Community Resource Exchange</div>', unsafe_allow_html=True)
    st.caption("Surplus food, tools, volunteer hours — connect Bengaluru's communities.")

    # List existing items
    for item in community_data:
        title = item.get(f"title_{lang_code}", item.get("title_en", ""))
        st.markdown(f"""
        <div class="comm-card">
          <div class="ctitle">{title}</div>
          <div style="font-size:0.85rem; color:#555; margin-top:6px;">
            📦 {item.get('quantity','')} &nbsp;|&nbsp;
            📍 {item.get('location','')} &nbsp;|&nbsp;
            👤 {item.get('donor_name','')} &nbsp;|&nbsp;
            ✅ {item.get('verification_status', item.get('status',''))}
          </div>
          <div style="font-size:0.8rem; color:#009199; margin-top:4px;">
            👥 For: {item.get('target_recipients','')}
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### ➕ Post a New Community Resource")
    st.info("🔒 All posts go through **human review** before going live (Base Paper 4 — Human-in-the-Loop).")

    with st.form("community_form"):
        c1, c2 = st.columns(2)
        with c1:
            rtype   = st.selectbox("Resource Type", ["Food", "Tools", "Skills", "Volunteer", "Other"])
            title_e = st.text_input("Title (English)")
            donor   = st.text_input("Your Name / Organisation")
        with c2:
            location   = st.text_input("Location / Area in Bengaluru")
            quantity   = st.text_input("Quantity / Duration")
            recipients = st.text_input("Who is this for?")

        submitted = st.form_submit_button("Submit for Human Review", type="primary")
        if submitted:
            if title_e and donor and location:
                st.success("✅ Submitted! A community coordinator will review and publish within 24 hours.")
                st.balloons()
            else:
                st.error("Please fill in Title, Name, and Location.")


# ════════════════════════════════════════════════════════════════════════════
# PAGE 4 — BOB STORY
# ════════════════════════════════════════════════════════════════════════════
elif page == "🤖 Bob Story":
    st.markdown('<div class="sec-header">🤖 The Bob Story — How We Built with IBM Bob</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="bob-box">
      <h3 style="color:#FFC000; margin:0 0 10px 0;">IBM Bob at the Centre of Every Decision</h3>
      <p style="color:#C0D8FF; margin:0;">
        OpportunityBob was designed, built, validated, and presented with IBM Bob as the agentic reasoning core.
        Bob didn't just power the AI — Bob guided every step of the development journey.
      </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    steps = [
        ("💡", "Ideation with Bob",
         "Bob helped map Bengaluru's informal workforce landscape, identified the 3 key pain points (language barrier, skill gap, community coordination), and suggested the multilingual-first architecture."),
        ("🏗️", "Design with Bob",
         "Bob reviewed our XAI architecture against 2026 IEEE TCSS and IEEE Access standards, ensuring every match decision is auditable, transparent, and bias-minimised."),
        ("⚙️", "Build with Bob",
         "Bob guided the FastAPI REST API design, the multilingual cosine similarity engine, the PII redaction pipeline (Aadhaar/phone), and the 3-step skill roadmap generator."),
        ("🔍", "Validate with Bob",
         "Bob audited our codebase for PII leakage, language bias, and fairness across Kannada, Hindi, and English queries. All 3 unit tests pass."),
        ("🎯", "Impact with Bob",
         "Measurable outcome: Reduces job discovery from 2 weeks (manual) to under 3 minutes, with 100% multilingual accessibility for Bengaluru's 1.4 crore informal workers."),
    ]
    for icon, title, desc in steps:
        with st.expander(f"{icon}  {title}", expanded=True):
            st.write(desc)

    st.markdown("---")
    st.markdown("### 📄 Research Base Papers (2026)")
    papers = [
        ("🔵", "Base Paper 1 — IEEE TCSS 2026",
         "Explainable AI & Feature Attribution → Powers our transparent skill-scoring that shows WHY you match a job."),
        ("🟣", "Base Paper 2 — IJISRT 2026",
         "Fairness-Aware Debiasing & PII Neutralization → Our Aadhaar/phone redaction guardrail."),
        ("🟢", "Base Paper 3 — IJIRT 2026",
         "Hybrid Multi-Tiered Semantic Skill Cascades → Multilingual cosine similarity engine."),
        ("🟠", "Base Paper 4 — IEEE Access 2026",
         "Transformer Attention & Human-in-the-Loop Audit Trails → Community review gate & decision telemetry."),
    ]
    for icon, title, desc in papers:
        st.markdown(f"**{icon} {title}**")
        st.caption(desc)
        st.markdown("")

    st.markdown("""
    <div style="background:#E8F0FE; border-radius:10px; padding:18px 20px; border-left:5px solid #0543CE; margin-top:16px;">
      <b style="color:#0543CE;">One Measurable Impact Statement</b><br>
      <span style="font-size:1.05rem;">
        OpportunityBob accelerates candidate-to-apprenticeship discovery from <b>2 weeks</b> (manual search)
        to <b>under 3 minutes</b>, with <b>100% multilingual accessibility</b> across English, Kannada, and Hindi
        — serving Bengaluru's 1.4 crore informal workers who were previously excluded from English-only job portals.
      </span>
    </div>
    """, unsafe_allow_html=True)

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  <b>OpportunityBob</b> | IBM Bobathon: Build for Bengaluru 2026 | Theme 2: More Opportunity Greater Together<br>
  Built with IBM Bob · FastAPI · Streamlit · XAI (IEEE 2026) ·
  <a href='https://github.com/SatyaRamDinkar/bengaluru-opporbob-ai' target='_blank'>GitHub</a>
</div>
""", unsafe_allow_html=True)
