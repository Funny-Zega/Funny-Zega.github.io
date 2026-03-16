import sys

with open(r"d:\Web\DongNguyenKhanhDuy_Portfolio\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Title & Meta
html = html.replace("<title>Lê Thanh Bình — Data Engineer</title>", "<title>Đồng Nguyễn Khánh Duy — Embedded Systems Engineer</title>")

# 2. Fonts
html = html.replace(
    "family=DM+Mono:ital,wght@0,300;0,400;0,500&family=Cabinet+Grotesk:wght@400;700;800;900",
    "family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,700&family=Montserrat:ital,wght@0,400;0,700;0,800;0,900"
)
html = html.replace("--mono:'DM Mono'", "--mono:'JetBrains Mono'")
html = html.replace("--sans:'Cabinet Grotesk'", "--sans:'Montserrat'")

# 3. Colors to Blue vibe
html = html.replace("--c1:#00f0d0", "--c1:#3399ff")
html = html.replace("--c2:#2979ff", "--c2:#0055ff")
html = html.replace("rgba(0,240,208", "rgba(51,153,255")

# 4. Hero & Basic text
html = html.replace("LÊ THANH <mark>BÌNH</mark>", "ĐỒNG NGUYỄN KHÁNH <mark>DUY</mark>")
html = html.replace("ltb<em>.dev</em>", "dnkd<em>.dev</em>")
html = html.replace("Data Engineer &amp; ML Researcher", "Embedded Systems Engineer")
html = html.replace("'Building Data Pipelines at Scale','IoT Streaming · Edge → Cloud','ML Research @ HCMUT Lab','Kafka · Spark · MinIO · K8s','20 Public Repos on GitHub','Open to Intern DE Roles'", 
                    "'Hardware-Software Co-design','Low-level Firmware & DSP','Bare-metal C/C++ Programming','STM32 & ARM Cortex-M','Open to Embedded Intern Roles'")

# 5. Social Links
html = html.replace("github.com/Mouse2204", "github.com/Funny-Zega")
html = html.replace("https://github.com/Mouse2204", "https://github.com/Funny-Zega")
html = html.replace("in/thanhbinhdata", "in/duy-đồng-nguyễn-khánh-6a2657366")
html = html.replace("https://www.linkedin.com/in/thanhbinhdata", "https://www.linkedin.com/in/duy-%C4%91%E1%BB%93ng-nguy%E1%BB%85n-kh%C3%A1nh-6a2657366/")
html = html.replace("letb2204@gmail.com", "dnkd04012005@gmail.com")
html = html.replace("0768 778 942", "0973 749 278")
html = html.replace("https://www.facebook.com/lethanh.binh.3576224", "https://www.facebook.com/ongnguyenkhanhduy/")

# Replace name
html = html.replace("Lê Thanh Bình", "Đồng Nguyễn Khánh Duy")

with open(r"d:\Web\DongNguyenKhanhDuy_Portfolio\index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Basic replacements done")
