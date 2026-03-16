import sys

def replace_between(text, start_marker, end_marker, new_content):
    start_idx = text.find(start_marker)
    end_idx = text.find(end_marker)
    if start_idx != -1 and end_idx != -1:
        return text[:start_idx] + new_content + text[end_idx:]
    return text

with open(r"d:\Web\DongNguyenKhanhDuy_Portfolio\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# ROADMAP REPLACEMENT
roadmap_start = '<section id="roadmap"'
roadmap_end = '<!-- PAGE STACK -->'

roadmap_new = """<section id="roadmap" style="padding:6rem 0;background:var(--bg2)"><div class="wrap">
  <div class="stag rv">07 — Career Roadmap</div>
  <h2 class="stitle rv">Embedded Engineer<br>Growth Path</h2>
  <p class="ssub rv" style="margin-bottom:3.5rem">From bare-metal programming fundamentals to advanced AI-integrated hardware.</p>
  <div class="rdm rv">

    <div class="rdm-phase">
      <div class="rdm-left"><div class="rdm-dot" style="background:var(--c1);box-shadow:0 0 0 4px rgba(51,153,255,.15)"></div><div class="rdm-line"></div></div>
      <div class="rdm-content">
        <div class="rdm-meta"><span class="rdm-period">2023 — 2024</span><span class="rdm-badge" style="color:var(--c1);border-color:rgba(51,153,255,.3);background:rgba(51,153,255,.08)">✓ Completed</span></div>
        <div class="rdm-title">Foundation Layer</div>
        <p class="rdm-desc">Gained comprehensive knowledge in digital logic design, microprocessors, and basic hardware architectures. Mastered C programming for system-level interaction and algorithmic thinking.</p>
        <div class="rdm-skills"><span class="rsk" style="color:var(--c1);border-color:rgba(51,153,255,.25);background:rgba(51,153,255,.06)">C/C++</span><span class="rsk" style="color:var(--c1);border-color:rgba(51,153,255,.25);background:rgba(51,153,255,.06)">Digital Logic</span></div>
      </div>
    </div>

    <div class="rdm-phase">
      <div class="rdm-left"><div class="rdm-dot" style="background:var(--c1);box-shadow:0 0 0 4px rgba(51,153,255,.15)"></div><div class="rdm-line"></div></div>
      <div class="rdm-content">
        <div class="rdm-meta"><span class="rdm-period">2024 — 2025</span><span class="rdm-badge" style="color:var(--c1);border-color:rgba(51,153,255,.3);background:rgba(51,153,255,.08)">✓ Completed</span></div>
        <div class="rdm-title">Microcontrollers &amp; Bare-Metal</div>
        <p class="rdm-desc">Started building applications and drivers for STM32 and ARM Cortex-M processors. Developed bare-metal firmware using MCU hardware abstraction layers (HAL) and optimized low-level registers.</p>
        <div class="rdm-skills"><span class="rsk" style="color:var(--c1);border-color:rgba(51,153,255,.25);background:rgba(51,153,255,.06)">STM32</span><span class="rsk" style="color:var(--c1);border-color:rgba(51,153,255,.25);background:rgba(51,153,255,.06)">ARM Cortex-M</span></div>
      </div>
    </div>

    <div class="rdm-phase" style="position:relative">
      <div class="rdm-left"><div class="rdm-dot" style="background:var(--bg2);border:2px solid var(--c1);position:relative"><span style="position:absolute;inset:-6px;border-radius:50%;border:2px solid var(--c1);opacity:.4;animation:ripple 1.6s ease-out infinite"></span><span style="position:absolute;inset:-12px;border-radius:50%;border:2px solid var(--c1);opacity:.2;animation:ripple 1.6s ease-out .4s infinite"></span></div><div class="rdm-line"></div></div>
      <div class="rdm-content" style="border-color:rgba(51,153,255,.25);background:rgba(51,153,255,.03)">
        <div class="rdm-meta"><span class="rdm-period">2025 — 2026</span><span class="rdm-badge" style="color:#ff8c42;border-color:rgba(255,140,66,.35);background:rgba(255,140,66,.1)">⚡ Current</span></div>
        <div class="rdm-title" style="color:var(--c1)">Advanced Systems &amp; DSP</div>
        <p class="rdm-desc">Designing robust interrupt-driven communication protocols (UART, SPI, I2C, CAN) and real-time state machines for multi-tasking systems. Researching Digital Signal Processing (DSP) and integrating AI models on edge hardware.</p>
        <div style="margin:.9rem 0;display:flex;flex-direction:column;gap:.45rem">
          <div style="display:flex;align-items:center;gap:.6rem;font-size:.78rem;color:var(--txt2)"><i class="fa fa-check-circle" style="color:var(--c1);font-size:.75rem"></i>Interrupt-Driven UART Protocol</div>
          <div style="display:flex;align-items:center;gap:.6rem;font-size:.78rem;color:var(--txt2)"><i class="fa fa-check-circle" style="color:var(--c1);font-size:.75rem"></i>FSM-Based Traffic Light Controller</div>
          <div style="display:flex;align-items:center;gap:.6rem;font-size:.78rem;color:var(--txt2)"><i class="fa fa-check-circle" style="color:var(--c1);font-size:.75rem"></i>AI-Driven DSP for Drone Detection</div>
        </div>
        <div class="rdm-skills"><span class="rsk" style="color:var(--c1);border-color:rgba(51,153,255,.3);background:rgba(51,153,255,.08)">UART/SPI/I2C</span><span class="rsk" style="color:var(--c1);border-color:rgba(51,153,255,.3);background:rgba(51,153,255,.08)">FSM</span><span class="rsk" style="color:var(--c1);border-color:rgba(51,153,255,.3);background:rgba(51,153,255,.08)">DSP</span></div>
      </div>
    </div>

    <div class="rdm-phase" style="padding-bottom:0">
      <div class="rdm-left"><div class="rdm-dot" style="background:var(--surf);border:2px solid var(--brd)"></div></div>
      <div class="rdm-content" style="opacity:.45">
        <div class="rdm-meta"><span class="rdm-period">2026+</span><span class="rdm-badge" style="color:var(--txt);border-color:var(--brd)">→ Next</span></div>
        <div class="rdm-title">Embedded Systems Lead</div>
        <p class="rdm-desc">Designing mission-critical embedded systems and leading firmware architecture. Implementing real-time operating systems (RTOS) and robust security in IoT applications.</p>
        <div class="rdm-skills"><span class="rsk" style="color:var(--txt);border-color:var(--brd)">RTOS</span><span class="rsk" style="color:var(--txt);border-color:var(--brd)">IoT Security</span></div>
      </div>
    </div>

  </div>
</div></section>
<footer><div class="ftc">Đồng Nguyễn Khánh Duy © 2026</div><div class="fts"><a href="https://github.com/Funny-Zega" target="_blank" class="fta"><i class="fab fa-github"></i></a><a href="https://www.linkedin.com/in/duy-%C4%91%E1%BB%93ng-nguy%E1%BB%85n-kh%C3%A1nh-6a2657366/" target="_blank" class="fta"><i class="fab fa-linkedin-in"></i></a><a href="mailto:dnkd04012005@gmail.com" class="fta"><i class="fa fa-envelope"></i></a><a href="https://www.facebook.com/ongnguyenkhanhduy/" target="_blank" class="fta"><i class="fab fa-facebook-f"></i></a></div></footer>
</div>
"""
html = replace_between(html, roadmap_start, roadmap_end, roadmap_new)

# PAGE STACK REPLACEMENT
stack_start = '<!-- PAGE STACK -->'
stack_end = '<!-- PAGE PROJECTS -->'

stack_new = """<!-- PAGE STACK -->
<div class="page" id="page-stack">
<div class="sub-hero"><div class="sub-inner"><div class="sub-tag">02 — Full Tech Stack</div><h1 class="sub-title">Embedded Systems<br><mark>Architecture</mark></h1><p class="sub-desc">Comprehensive expertise spanning microprocessor architecture, bare-metal C/C++, communication protocols, hardware debuggers, and digital signal processing.</p><div class="sub-stats"><div><div class="sst-n">10+</div><div class="sst-l">Technologies</div></div><div><div class="sst-n">3</div><div class="sst-l">Domains</div></div></div></div></div>

<div class="domain"><div class="domain-inner"><div class="domain-grid rv"><div><div class="domain-ico"><i class="fa fa-code"></i></div><div class="domain-num">Domain 01</div><div class="domain-name">Languages</div><p class="domain-blurb">Mastery in low-level programming to interact directly with hardware components, optimize memory, and ensure timing constraints are met.</p></div><div class="tech-grid">
<div class="tcard"><div class="tcard-name">C / C++</div><p class="tcard-desc">Primary languages for bare-metal firmware development and hardware abstractions.</p><div class="prof-wrap"><div class="prof-bar"><div class="prof-fill" data-w="95"></div></div><span class="prof-label">95%</span></div><span class="tcard-badge">Primary</span></div>
<div class="tcard"><div class="tcard-name">Python</div><p class="tcard-desc">Used for data analysis, signal processing, and testing automation.</p><div class="prof-wrap"><div class="prof-bar"><div class="prof-fill" data-w="85"></div></div><span class="prof-label">85%</span></div></div>
<div class="tcard"><div class="tcard-name">Assembly</div><p class="tcard-desc">Low-level ARM/MIPS instruction set understanding for deep system debugging.</p><div class="prof-wrap"><div class="prof-bar"><div class="prof-fill" data-w="70"></div></div><span class="prof-label">70%</span></div></div>
</div></div></div></div>

<div class="domain"><div class="domain-inner"><div class="domain-grid rv"><div><div class="domain-ico"><i class="fa fa-microchip"></i></div><div class="domain-num">Domain 02</div><div class="domain-name">Microcontrollers &amp; IDEs</div><p class="domain-blurb">Targeting ARM Cortex-M architecture with STM32 families. Proficient in configuring and managing complex peripheral workflows via integrated development environments.</p></div><div class="tech-grid">
<div class="tcard"><div class="tcard-name">STM32</div><p class="tcard-desc">Extensive experience coding STM32 devices using C HAL and standard peripheral libraries.</p><div class="prof-wrap"><div class="prof-bar"><div class="prof-fill" data-w="90"></div></div><span class="prof-label">90%</span></div><span class="tcard-badge">Core</span></div>
<div class="tcard"><div class="tcard-name">STM32CubeIDE</div><p class="tcard-desc">Advanced configuration, peripheral setup, and hardware debugging.</p><div class="prof-wrap"><div class="prof-bar"><div class="prof-fill" data-w="85"></div></div><span class="prof-label">85%</span></div></div>
<div class="tcard"><div class="tcard-name">PlatformIO</div><p class="tcard-desc">Flexible VS Code extension for building and deploying firmware rapidly.</p><div class="prof-wrap"><div class="prof-bar"><div class="prof-fill" data-w="80"></div></div><span class="prof-label">80%</span></div></div>
</div></div></div></div>

<div class="domain"><div class="domain-inner"><div class="domain-grid rv"><div><div class="domain-ico"><i class="fa fa-network-wired"></i></div><div class="domain-num">Domain 03</div><div class="domain-name">Protocols &amp; Concepts</div><p class="domain-blurb">Building resilient applications using state-driven logic and robust communication interfaces.</p></div><div class="tech-grid">
<div class="tcard"><div class="tcard-name">UART/SPI/I2C/CAN</div><p class="tcard-desc">Implementation of interrupt-driven communication over serial buses.</p><div class="prof-wrap"><div class="prof-bar"><div class="prof-fill" data-w="85"></div></div><span class="prof-label">85%</span></div></div>
<div class="tcard"><div class="tcard-name">FSM Architecture</div><p class="tcard-desc">Utilizing Finite State Machines for predictable real-time program flow.</p><div class="prof-wrap"><div class="prof-bar"><div class="prof-fill" data-w="90"></div></div><span class="prof-label">90%</span></div></div>
<div class="tcard"><div class="tcard-name">DSP &amp; AI Ext.</div><p class="tcard-desc">Digital Signal Processing integration (STFT) and model deployment to edge environments.</p><div class="prof-wrap"><div class="prof-bar"><div class="prof-fill" data-w="75"></div></div><span class="prof-label">75%</span></div></div>
</div></div></div></div>

<footer><div class="ftc">Đồng Nguyễn Khánh Duy © 2026</div><div class="fts"><a href="https://github.com/Funny-Zega" target="_blank" class="fta"><i class="fab fa-github"></i></a><a href="https://www.linkedin.com/in/duy-%C4%91%E1%BB%93ng-nguy%E1%BB%85n-kh%C3%A1nh-6a2657366/" target="_blank" class="fta"><i class="fab fa-linkedin-in"></i></a></div></footer>
</div>
"""
html = replace_between(html, stack_start, stack_end, stack_new)

# PAGE PROJECTS REPLACEMENT
projects_start = '<!-- PAGE PROJECTS -->'
projects_end = '<script data-cfasync'

projects_new = """<!-- PAGE PROJECTS -->
<div class="page" id="page-projects">
<div class="sub-hero proj"><div class="sub-inner"><div class="sub-tag proj">03 — GitHub Projects</div><h1 class="sub-title proj">Embedded &amp; Firmware<br><mark>Projects</mark></h1><p class="sub-desc">Showcasing deep technical integration with microcontrollers, from complex interrupt-driven UART protocols to AI-driven drone detection systems.</p><div class="sub-stats proj"><div><div class="sst-n">3</div><div class="sst-l">Public Repos</div></div><div><div class="sst-n">2</div><div class="sst-l">Featured</div></div></div><div class="filters"><button class="ftab active" onclick="filterCat('all',this)">All</button><button class="ftab" onclick="filterCat('embedded',this)"><i class="fa fa-microchip"></i> Embedded Systems</button><button class="ftab" onclick="filterCat('ai',this)"><i class="fa fa-brain"></i> Edge AI</button></div></div></div>

<div class="cat-section" data-cat="embedded"><div class="cat-inner"><div class="cat-head rv"><div class="cat-ico" style="background:rgba(51,153,255,.08);border:1px solid rgba(51,153,255,.2);color:var(--c1)"><i class="fa fa-microchip"></i></div><div><span class="cat-label">Category</span><span class="cat-title">Embedded Systems</span></div></div>
<div class="pgrid">

  <div class="pc feat rv"><span class="feat-badge">★ Featured</span><div class="pt"><div class="pico"><i class="fa fa-project-diagram"></i></div><a href="https://github.com/Funny-Zega/STM32-UART-FSM-PROTOCOL" target="_blank" class="plnk"><i class="fab fa-github"></i></a></div><div class="pname">Interrupt-Driven UART Protocol</div><div class="pmeta"><span class="pdate">Nov 2025</span><span class="prole">Lead Developer</span></div><p class="pdesc">Engineered a UART-based data acquisition system on STM32 (C HAL) with an interrupt-driven receiver, ring buffer, and FSM command parsing.</p><ul class="phigh"><li>Implemented a reliable ARQ transmission mechanism</li><li>Integrated timeout handling &amp; parameter modifications</li><li>Synchronized with real-time ADC hardware polling</li></ul><div class="ptags"><span class="ptag hi">C/C++</span><span class="ptag hi">STM32 HAL</span><span class="ptag hi">UART</span><span class="ptag hi">FSM</span></div></div>

  <div class="pc feat rv"><span class="feat-badge">★ Featured</span><div class="pt"><div class="pico"><i class="fa fa-traffic-light"></i></div><a href="https://github.com/Funny-Zega/Traffic_Light-" target="_blank" class="plnk"><i class="fab fa-github"></i></a></div><div class="pname">FSM-Based Smart Traffic Light</div><div class="pmeta"><span class="pdate">Nov 2026</span><span class="prole">Lead Developer</span></div><p class="pdesc">Developed a multi-mode traffic light system on STM32 utilizing Finite State Machines to manage state transitions and dynamic parameter modifications.</p><ul class="phigh"><li>Timer interrupts (TIM2) for precise timekeeping</li><li>Multiplexed 7-segment displays control</li><li>Robust software-based button debouncing algorithms</li></ul><div class="ptags"><span class="ptag hi">C/C++</span><span class="ptag hi">STM32</span><span class="ptag hi">FSM</span><span class="ptag hi">Timers</span></div></div>

</div></div></div>

<div class="cat-section" data-cat="ai"><div class="cat-inner"><div class="cat-head rv"><div class="cat-ico" style="background:rgba(162,89,255,.08);border:1px solid rgba(162,89,255,.2);color:var(--c4)"><i class="fa fa-brain"></i></div><div><span class="cat-label">Category</span><span class="cat-title">Edge AI</span></div></div>
<div class="pgrid">

  <div class="pc feat rv"><span class="feat-badge">★ Featured</span><div class="pt"><div class="pico"><i class="fa fa-fighter-jet"></i></div><a href="https://github.com/Funny-Zega" target="_blank" class="plnk"><i class="fab fa-github"></i></a></div><div class="pname">AI-Driven Drone RF Detection</div><div class="pmeta"><span class="pdate">Jan 2026</span><span class="prole">Researcher</span></div><p class="pdesc">Built a counter-UAV detection system using RF signal processing (STFT) and an EfficientNet-B0 + CBAM architecture.</p><ul class="phigh"><li>Achieved 99.89% accuracy in clean data</li><li>Focusing on model quantization for edge inference</li></ul><div class="ptags"><span class="ptag hi">Python</span><span class="ptag hi">DSP</span><span class="ptag hi">EfficientNet</span><span class="ptag hi">Model Quantization</span></div></div>

</div></div></div>

<div style="text-align:center;padding:3rem 2rem;background:var(--bg)"><a href="https://github.com/Funny-Zega?tab=repositories" target="_blank" class="btn btno"><i class="fab fa-github"></i> View All Repos on GitHub</a></div>
<footer><div class="ftc">Đồng Nguyễn Khánh Duy © 2026 · <a href="javascript:void(0)" onclick="goPage('home')">Back to Portfolio</a></div><div class="fts"><a href="https://github.com/Funny-Zega" target="_blank" class="fta"><i class="fab fa-github"></i></a><a href="https://www.linkedin.com/in/duy-%C4%91%E1%BB%93ng-nguy%E1%BB%85n-kh%C3%A1nh-6a2657366/" target="_blank" class="fta"><i class="fab fa-linkedin-in"></i></a></div></footer>
</div>
"""

html = replace_between(html, projects_start, projects_end, projects_new)

with open(r"d:\Web\DongNguyenKhanhDuy_Portfolio\index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Projects replaced successfully")
