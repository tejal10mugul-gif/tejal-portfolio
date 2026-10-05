from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

if '/* ── NEW REFERENCE HERO THEME ── */' in s:
    raise SystemExit(0)

start = s.index('<section class="hero" id="home">')
end = s.index('</section>', start) + len('</section>')
new = '''<section class="hero" id="home">
  <div class="hero-shapes" aria-hidden="true">
    <div class="shape s1"></div><div class="shape s2"></div><div class="shape s3"></div>
  </div>
  <div class="hero-inner">
    <div class="hero-content">
      <h1>Tejal Mugul</h1>
      <h2>Competitive Intelligence &amp; Strategy<br>Consulting</h2>
      <p class="hero-proof">400+ company profiles <span>·</span> 20+ RFPs <span>·</span> Fortune 500 clients</p>
      <p class="hero-location">Pune · Open to roles across India and remote</p>
      <div class="hero-btns">
        <a href="https://tejal10mugul-gif.github.io/tejal-portfolio/proof-of-work.html" target="_blank" rel="noopener" class="btn-primary">View My Work</a>
        <a href="https://tejal10mugul-gif.github.io/tejal-portfolio/Tejal_Mugul_Master_Market_Research_Competitive_Intelligence_Strategy_02_Oct_2026.pdf" target="_blank" rel="noopener" class="btn-ghost">View Resume</a>
      </div>
    </div>
    <div class="hero-photo-wrap">
      <div class="hero-photo-ring"><img data-photo alt="Tejal Mugul" class="hero-photo-image"></div>
    </div>
  </div>
</section>'''
s = s[:start] + new + s[end:]

css = '''\n/* ── NEW REFERENCE HERO THEME ── */\n.hero{min-height:100vh;display:flex;align-items:center;position:relative;overflow:hidden;padding:8rem 6.5% 5rem;background:#0d4f5c}.hero-shapes{position:absolute;inset:0;pointer-events:none;overflow:hidden}.hero-shapes .shape{position:absolute;border-radius:50%;animation:none}.hero-shapes .s1{width:560px;height:560px;background:#1b6878;opacity:.55;top:-275px;right:-25px}.hero-shapes .s2{width:360px;height:360px;background:#14596a;opacity:.5;bottom:-245px;left:-135px}.hero-shapes .s3{width:230px;height:230px;background:#217789;opacity:.3;top:40%;right:25%}.hero-inner{width:100%;max-width:1200px;margin:0 auto;display:grid;grid-template-columns:minmax(0,1.35fr) minmax(280px,.65fr);align-items:center;gap:4rem;position:relative;z-index:2}.hero .hero-content{max-width:none}.hero h1{font-family:'Cormorant Garamond',serif;font-size:clamp(4.5rem,8vw,7rem);line-height:.92;font-weight:600;color:#fff;margin:0 0 1.8rem}.hero h2{font-family:'DM Sans',sans-serif;font-size:clamp(1.8rem,3vw,3rem);line-height:1.28;font-weight:400;color:#e8b99a;margin:0 0 2.8rem}.hero-proof{font-size:clamp(1rem,1.5vw,1.28rem);color:#fff;margin-bottom:.65rem;letter-spacing:.01em}.hero-proof span{color:#e8b99a;margin:0 .3rem}.hero-location{font-size:1.05rem;color:#8fc6d1;margin-bottom:2.5rem}.hero .hero-btns{display:flex;gap:1rem;flex-wrap:wrap}.hero .btn-primary{background:#e8b99a;color:#0d4f5c;border:1px solid #e8b99a;padding:.85rem 1.8rem;border-radius:5px}.hero .btn-primary:hover{background:#f2c8ad;border-color:#f2c8ad;transform:translateY(-2px)}.hero .btn-ghost{background:transparent;color:#fff;border:1px solid rgba(255,255,255,.48);padding:.85rem 1.8rem;border-radius:5px}.hero .btn-ghost:hover{background:rgba(255,255,255,.1);border-color:#fff;color:#fff}.hero-photo-wrap{display:flex;justify-content:center;align-items:center}.hero-photo-ring{width:min(310px,28vw);aspect-ratio:1;border-radius:50%;padding:7px;background:#fff;border:2px solid #d7e7eb;box-shadow:0 0 0 5px rgba(255,255,255,.16)}.hero-photo-image{width:100%;height:100%;border-radius:50%;object-fit:cover;display:block;background:#dce8ec}#main-nav{background:rgba(13,79,92,.96);border-bottom-color:rgba(255,255,255,.12)}#main-nav .nav-logo{color:#fff}#main-nav .nav-resume{background:#e8b99a;color:#0d4f5c}#main-nav .nav-resume:hover{background:#f2c8ad}#main-nav .dark-toggle,#main-nav .nav-menu-btn{color:rgba(255,255,255,.8);border-color:rgba(255,255,255,.25)}#main-nav .dark-toggle:hover,#main-nav .nav-menu-btn:hover{color:#fff;border-color:rgba(255,255,255,.6)}@media(max-width:900px){.hero-inner{grid-template-columns:1fr;gap:2.5rem;text-align:center}.hero{padding:9rem 1.5rem 4rem}.hero-photo-wrap{order:-1}.hero-photo-ring{width:190px}.hero-btns{justify-content:center}}@media(max-width:520px){.hero h1{font-size:4rem}.hero h2{font-size:1.65rem}.hero-proof{font-size:.95rem}.hero-btns a{flex:0 1 auto}}\n'''
s = s.replace('</style></head>', css + '</style></head>', 1)
p.write_text(s, encoding='utf-8')
