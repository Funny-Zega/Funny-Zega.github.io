import sys

with open(r"d:\Web\DongNguyenKhanhDuy_Portfolio\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. About
about_old = """<p>I'm a <em>Computer Engineering student</em> at <b>HCM City University of Technology (Bach Khoa)</b>, graduating 2027. My work lives at the intersection of <em>Streaming Data</em>, <em>Machine Learning</em>, and <em>IoT systems</em>.</p>
      <p>I build end-to-end data pipelines from raw sensor ingestion at the edge to Gold Layer analytics — using Kafka, Spark, MinIO, Delta Lake, and Kubernetes. Currently researching <em>micro-Doppler signal processing</em> for drone detection at the HCMUT Lab.</p>
      <p>Short-term: an <b>Intern Data Engineer</b> role on a real production system. Long-term: leading data infrastructure at scale.</p>"""

about_new = """<p>I'm a <em>Computer Engineering student</em> at <b>HCM City University of Technology (Bach Khoa)</b>, graduating 2027. I specialize in <em>hardware-software co-design</em>, <em>low-level firmware</em>, and <em>Digital Signal Processing (DSP)</em>.</p>
      <p>My work involves engineering reliable systems using STM32 microcontrollers, applying C/C++ for hardware interaction, and designing real-time communication protocols (UART, SPI, I2C, CAN). Currently researching <em>AI-driven drone RF detection</em> at the HCMUT Lab.</p>
      <p>Short-term: an <b>Embedded Systems Internship</b> to leverage my system architecture expertise. Long-term: building secure, intelligent embedded solutions.</p>"""
html = html.replace(about_old, about_new)

# stats in about
stats_old = """<div class="stats">
      <div class="sc"><div class="snum">20</div><div class="slbl">Public Repos</div></div>
      <div class="sc"><div class="snum">90%</div><div class="slbl">DeepFake Accuracy</div></div>
      <div class="sc"><div class="snum">40%</div><div class="slbl">Config Time Saved</div></div>
      <div class="sc"><div class="snum">3yr</div><div class="slbl">OISP Scholarship</div></div>
    </div>"""

stats_new = """<div class="stats">
      <div class="sc"><div class="snum">3.0/4.0</div><div class="slbl">Current GPA</div></div>
      <div class="sc"><div class="snum">99.8%</div><div class="slbl">Detection Accuracy</div></div>
      <div class="sc"><div class="snum">STM32</div><div class="slbl">Core Focus</div></div>
      <div class="sc"><div class="snum">IELTS 6.5</div><div class="slbl">English Proficient</div></div>
    </div>"""
html = html.replace(stats_old, stats_new)

# 2. EXP
exp_old = """<div class="ti"><div class="tdate">Dec 2025 — Mar 2026</div><div class="trole">Data Engineer Intern</div><div class="tco">Vietnam Technology-Communications JSC (VNTT) · Ho Chi Minh City</div>
      <ul class="tlist"><li>Built metadata-driven ingestion framework — cut config time by <b style="color:var(--c1)">40%</b>.</li><li>Optimised spatial data pipelines with PostGIS + MinIO.</li><li>Deployed Edge Computing using EdgeX Foundry with senior engineers.</li></ul></div>
    <div class="ti"><div class="tdate">Jul 2024 — Present</div><div class="trole">Lab Assistant Researcher</div><div class="tco">HCM City University of Technology (HCMUT) · Ho Chi Minh City</div>
      <ul class="tlist"><li>Researching micro-Doppler signal processing for drone detection.</li><li>Real-time analysis: Python, Kafka, Spark, Trino, MinIO on Raspberry Pi 4 / DHT22.</li><li>Analysing HTTP, CDN, DNS, MQTT, REST protocols to strengthen IoT security.</li></ul></div>"""

exp_new = """<div class="ti"><div class="tdate">Jan 2026 — Present</div><div class="trole">Lab Assistant Researcher — AI & RF Systems</div><div class="tco">HCM City University of Technology (HCMUT) · Ho Chi Minh City</div>
      <ul class="tlist"><li>Researching AI-driven drone RF detection and classification using STFT signal processing.</li><li>Built EfficientNet-B0 + CBAM architecture, achieving <b style="color:var(--c1)">99.89%</b> accuracy in clean data.</li><li>Focusing on model quantization for low-latency edge inference on embedded devices.</li></ul></div>
    <div class="ti"><div class="tdate">Nov 2025</div><div class="trole">Embedded Software Developer</div><div class="tco">Academic Project · HCMUT</div>
      <ul class="tlist"><li>Engineered UART communication protocol on STM32 (C HAL) with interrupt-driven receiver & ring buffer.</li><li>Developed multi-mode FSM-Based Smart Traffic Light managing real-time states and timers.</li></ul></div>"""
html = html.replace(exp_old, exp_new)

# 3. EDU
edu_old = """<div class="cgrid">
      <div class="cert"><i class="fa fa-award"></i><span>OISP Scholarship — 3 consecutive years (2023–2026)</span></div>
      <div class="cert"><i class="fa fa-language"></i><span>IELTS 6.0 Certificate (2023)</span></div>
      <div class="cert"><i class="fa fa-users"></i><span>Soft Skills Certificate — OISP CAMP 2023 Organiser</span></div>
      <div class="cert"><i class="fa fa-chalkboard-teacher"></i><span>Honors: Teaching Assistant — Soft Skills subject</span></div>
    </div>"""

edu_new = """<div class="cgrid">
      <div class="cert"><i class="fa fa-award"></i><span>OISP Scholarship Top 20 Best in Year 1 and 2</span></div>
      <div class="cert"><i class="fa fa-language"></i><span>IELTS 6.5 Certificate</span></div>
      <div class="cert"><i class="fa fa-file-excel"></i><span>MOS-EXCEL Certificate</span></div>
      <div class="cert"><i class="fa fa-camera"></i><span>THE FACE OISP — Media Communications</span></div>
    </div>"""
html = html.replace(edu_old, edu_new)

# 4. Fix some lingering data engineering text
html = html.replace("Data Engineering<br>Infrastructure", "Embedded Systems<br>Architecture")
html = html.replace("20 Open Source<br>Repositories", "Embedded & Firmware<br>Projects")
html = html.replace("Data Engineer<br>Growth Path", "Embedded Engineer<br>Growth Path")
html = html.replace("End-to-end stack: streaming ingestion, distributed processing, lakehouse storage, spatial analytics, IoT edge, and cloud-native orchestration.", "Developing intelligent hardware, writing bare-metal firmware, and creating robust real-time systems using modern MCUs and C/C++.")
html = html.replace("IoT streaming platforms, DeepFake detection, metadata ingestion frameworks, spatial data pipelines, and ML systems.", "Low-level firmware, communication protocols, finite state machines, and DSP/AI integration for bare-metal systems.")
html = html.replace("From IoT streaming platforms and DeepFake detection to metadata ingestion frameworks and hybrid recommender systems.", "From complex interrupt-driven UART protocols to AI-driven drone detection systems.")

# Update counts
html = html.replace('<div class="pcard-num"><span class="pcard-n">30+</span><span class="pcard-nl">Technologies</span></div>', '<div class="pcard-num"><span class="pcard-n">10+</span><span class="pcard-nl">Technologies</span></div>')
html = html.replace('<div class="pcard-num"><span class="pcard-n">20</span><span class="pcard-nl">Repos</span></div>', '<div class="pcard-num"><span class="pcard-n">3</span><span class="pcard-nl">Repos</span></div>')

with open(r"d:\Web\DongNguyenKhanhDuy_Portfolio\index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Sections replaced successfully.")
