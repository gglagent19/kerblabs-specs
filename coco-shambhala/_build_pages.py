# Builds villas/experiences/stay pages sharing the Descent design system.
import os
HERE = os.path.dirname(os.path.abspath(__file__))

HEAD = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;1,9..144,300;1,9..144,400&family=Archivo:wght@300;400;500&family=Space+Mono&display=swap" rel="stylesheet">
<style>
:root{{--night:#12211D;--salt:#E9E2D2;--laterite:#B4552D;--palm:#7A8C6E;--gold:#D9A441;--ink:#1A2420}}
*{{margin:0;padding:0;box-sizing:border-box}}
html::-webkit-scrollbar,body::-webkit-scrollbar{{display:none}}html,body{{scrollbar-width:none}}
body{{background:var(--night);color:var(--salt);font-family:'Archivo',sans-serif;font-weight:300;overflow-x:hidden;cursor:none}}
::selection{{background:var(--laterite);color:var(--salt)}}
a{{color:inherit;text-decoration:none}}img,video{{display:block;width:100%;height:100%;object-fit:cover}}
.mono{{font-family:'Space Mono',monospace;font-size:11px;letter-spacing:.14em;text-transform:uppercase}}
.cur{{position:fixed;top:0;left:0;width:10px;height:10px;border-radius:50%;background:var(--salt);pointer-events:none;z-index:2000;mix-blend-mode:difference}}
.curo{{position:fixed;top:0;left:0;width:44px;height:44px;border-radius:50%;border:1px solid rgba(233,226,210,.5);pointer-events:none;z-index:2000;transition:width .3s,height .3s;mix-blend-mode:difference}}
.curo.big{{width:92px;height:92px}}
@media(hover:none){{.cur,.curo{{display:none}}body{{cursor:auto}}}}
nav{{position:fixed;top:0;left:0;right:0;z-index:1000;display:flex;justify-content:space-between;align-items:center;padding:26px 40px;mix-blend-mode:difference}}
nav .wordmark{{font-family:'Fraunces',serif;font-size:19px}}
nav .wordmark em{{font-style:italic}}
nav .links{{display:flex;gap:30px;align-items:center}}
nav .links a{{font-size:12px;letter-spacing:.18em;text-transform:uppercase;opacity:.85}}
nav .links a.on{{border-bottom:1px solid var(--gold);padding-bottom:4px}}
nav .book{{border:1px solid rgba(233,226,210,.6);border-radius:40px;padding:10px 22px;font-size:12px;letter-spacing:.18em;text-transform:uppercase}}
@media(max-width:860px){{nav .links a:not(.book){{display:none}}}}
.vhero{{position:relative;height:92vh;overflow:hidden;display:flex;align-items:flex-end}}
.vhero .media{{position:absolute;inset:0}}
.vhero .media::after{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(18,33,29,.5),rgba(18,33,29,.2) 45%,rgba(18,33,29,.88))}}
.vhero .inner{{position:relative;z-index:3;padding:0 8vw 9vh;max-width:1200px}}
.vhero .kicker{{color:var(--gold)}}
.vhero h1{{font-family:'Fraunces',serif;font-weight:300;font-size:clamp(46px,7.6vw,120px);line-height:1.02;margin-top:16px}}
.vhero h1 em{{font-style:italic;color:var(--gold)}}
.vhero h1 .ln{{display:block;overflow:hidden}}.vhero h1 .ln span{{display:inline-block;transform:translateY(110%)}}
.vhero .lede{{margin-top:22px;max-width:56ch;color:rgba(233,226,210,.85);line-height:1.7;opacity:0}}
section.body{{padding:14vh 8vw}}
.rule{{height:1px;background:rgba(233,226,210,.14);margin:0 8vw}}
h2.sec{{font-family:'Fraunces',serif;font-weight:300;font-size:clamp(34px,4.6vw,72px);line-height:1.08}}
h2.sec em{{font-style:italic;color:var(--gold)}}
.rev{{opacity:0;transform:translateY(46px)}}
footer{{padding:14vh 8vw 7vh;text-align:center}}
footer h2{{font-family:'Fraunces',serif;font-weight:300;font-size:clamp(40px,6.4vw,100px)}}
footer h2 em{{font-style:italic;color:var(--gold)}}
footer .btn{{display:inline-block;margin-top:44px;border:1px solid rgba(233,226,210,.4);border-radius:60px;padding:22px 54px;font-size:13px;letter-spacing:.24em;text-transform:uppercase;position:relative;overflow:hidden}}
footer .btn i{{position:absolute;inset:0;background:var(--laterite);transform:translateY(101%);transition:transform .45s cubic-bezier(.6,0,.2,1);z-index:-1}}
footer .btn:hover i{{transform:translateY(0)}}
footer .fine{{margin-top:11vh;color:rgba(233,226,210,.5)}}
{extra}
</style></head><body>
<div class="cur" id="cur"></div><div class="curo" id="curo"></div>
<nav>
  <a class="wordmark hov" href="index.html">Coco <em>Shambhala</em></a>
  <div class="links">
    <a class="hov {on_v}" href="villas.html">Villas</a>
    <a class="hov {on_e}" href="experiences.html">Experiences</a>
    <a class="hov {on_s}" href="stay.html">Your stay</a>
    <a class="book hov" href="stay.html">Reserve</a>
  </div>
</nav>"""

TAIL = """
<footer>
  <div class="mono" style="color:var(--palm)">{foot_kicker}</div>
  <h2 style="margin-top:18px">{foot_title}</h2>
  <a class="btn hov" href="{foot_href}">{foot_cta}<i></i></a>
  <div class="fine mono">Bhogave · Sindhudurg · 15°58′ N — 73°32′ E · Concept redesign by Kerblabs</div>
</footer>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.14/dist/lenis.min.js"></script>
<script>
gsap.registerPlugin(ScrollTrigger);
const lenis=new Lenis({lerp:.09});lenis.on('scroll',ScrollTrigger.update);
gsap.ticker.add(t=>lenis.raf(t*1000));gsap.ticker.lagSmoothing(0);
const cur=document.getElementById('cur'),curo=document.getElementById('curo');
let cx=0,cy=0,ox=0,oy=0;
addEventListener('mousemove',e=>{cx=e.clientX;cy=e.clientY;cur.style.transform=`translate(${cx-5}px,${cy-5}px)`});
gsap.ticker.add(()=>{ox+=(cx-ox)*.12;oy+=(cy-oy)*.12;curo.style.transform=`translate(${ox-22}px,${oy-22}px)`});
document.querySelectorAll('.hov,a').forEach(el=>{el.addEventListener('mouseenter',()=>curo.classList.add('big'));el.addEventListener('mouseleave',()=>curo.classList.remove('big'))});
gsap.to('.vhero h1 .ln span',{y:0,duration:1.1,ease:'power4.out',stagger:.12,delay:.2});
gsap.to('.vhero .lede',{opacity:1,duration:.9,delay:.9});
const hm=document.querySelector('.vhero .media');
if(hm) gsap.to(hm,{yPercent:14,scale:1.08,ease:'none',scrollTrigger:{trigger:'.vhero',start:'top top',end:'bottom top',scrub:true}});
document.querySelectorAll('.rev').forEach(el=>{gsap.to(el,{opacity:1,y:0,duration:1,ease:'power3.out',scrollTrigger:{trigger:el,start:'top 84%'}})});
PAGEJS
if(matchMedia('(prefers-reduced-motion: reduce)').matches){lenis.destroy();gsap.globalTimeline.timeScale(100)}
</script></body></html>"""

def page(fn, title, desc, on, extra_css, body, pagejs, foot):
    on_v = "on" if on=="v" else ""; on_e = "on" if on=="e" else ""; on_s = "on" if on=="s" else ""
    html = HEAD.format(title=title, desc=desc, extra=extra_css, on_v=on_v, on_e=on_e, on_s=on_s)
    html += body
    html += TAIL.replace("PAGEJS", pagejs).replace("{foot_kicker}",foot[0]).replace("{foot_title}",foot[1]).replace("{foot_href}",foot[2]).replace("{foot_cta}",foot[3])
    open(os.path.join(HERE, fn), "w", encoding="utf-8").write(html)
    print("built", fn)

# ---------------- VILLAS ----------------
villas_css = """
.vlist{display:flex;flex-direction:column;gap:16vh}
.vrow{display:grid;grid-template-columns:1.15fr .85fr;gap:5vw;align-items:center}
.vrow:nth-child(even){grid-template-columns:.85fr 1.15fr}
.vrow:nth-child(even) .vmedia{order:2}
.vmedia{height:74vh;overflow:hidden;border-radius:3px;position:relative}
.vmedia img{transform:scale(1.15)}
.vmedia .tag{position:absolute;top:22px;left:22px;background:rgba(18,33,29,.72);backdrop-filter:blur(6px);padding:10px 16px;border-radius:30px;color:var(--gold)}
.vinfo .idx{font-family:'Fraunces',serif;font-style:italic;font-size:78px;color:transparent;-webkit-text-stroke:1px rgba(233,226,210,.35);line-height:1}
.vinfo h3{font-family:'Fraunces',serif;font-weight:400;font-size:clamp(38px,4.4vw,64px);margin-top:10px}
.vinfo .mean{color:var(--gold);font-style:italic;font-family:'Fraunces',serif;font-size:21px;margin-top:6px}
.vinfo p{margin-top:20px;color:rgba(233,226,210,.8);line-height:1.75;max-width:52ch}
.vinfo .specs{display:flex;flex-wrap:wrap;gap:14px;margin-top:26px}
.vinfo .specs span{border:1px solid rgba(233,226,210,.25);border-radius:30px;padding:9px 18px;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:rgba(233,226,210,.75)}
.amen{margin-top:18vh;border-top:1px solid rgba(233,226,210,.14);padding-top:9vh}
.amen .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:1px;background:rgba(233,226,210,.12);margin-top:7vh}
.amen .cell{background:var(--night);padding:38px 30px}
.amen .cell .mono{color:var(--laterite)}
.amen .cell h4{font-family:'Fraunces',serif;font-weight:400;font-size:24px;margin-top:12px}
.vidband{position:relative;height:78vh;overflow:hidden;margin-top:18vh;border-radius:3px}
.vidband video{position:absolute;inset:0}
.vidband::after{content:"";position:absolute;inset:0;background:rgba(12,20,17,.35)}
.vidband .cap{position:absolute;bottom:34px;left:38px;z-index:2}
@media(max-width:900px){.vrow,.vrow:nth-child(even){grid-template-columns:1fr}.vrow:nth-child(even) .vmedia{order:0}.vmedia{height:52vh}}
"""
villas_body = """
<section class="vhero">
  <div class="media"><img src="https://cocoshambhala.com/wp-content/uploads/2023/11/Main-image-1-1-e1720067150796-1500x663.jpg" alt="Coco Shambhala villas"></div>
  <div class="inner">
    <div class="mono kicker">The villas · Four residences, twenty guests</div>
    <h1><span class="ln"><span>Four names for</span></span><span class="ln"><span>the same <em>horizon</em></span></span></h1>
    <p class="lede">Each villa holds two bedrooms, an open-air living pavilion, and a private infinity pool aimed at the Arabian Sea. Built into the hillside without cutting the terrain, furnished in coconut wood, cooled by the same breeze that moves the palms.</p>
  </div>
</section>
<section class="body">
  <div class="vlist">
    <div class="vrow rev"><div class="vmedia hov"><img class="pz" src="https://images.unsplash.com/photo-1571896349842-33c89424de2d?q=80&w=1600&auto=format&fit=crop" alt="Villa Arka"><div class="tag mono">Sea &amp; beach views</div></div>
      <div class="vinfo"><div class="idx">No.1</div><h3>Arka</h3><div class="mean">named for the tropical sun</div>
      <p>The first villa you reach, and the one the light finds first. Arka faces the water squarely, so the pool, the pavilion, and both bedrooms share the same wide view of sand and sea.</p>
      <div class="specs"><span>2 bedrooms</span><span>Sleeps 5</span><span>Private infinity pool</span><span>Open-air pavilion</span></div></div></div>
    <div class="vrow rev"><div class="vmedia hov"><img class="pz" src="https://images.unsplash.com/photo-1540541338287-41700207dee6?q=80&w=1600&auto=format&fit=crop" alt="Villa Amaresha"><div class="tag mono">Framed by kokum trees</div></div>
      <div class="vinfo"><div class="idx">No.2</div><h3>Amaresha</h3><div class="mean">named for the sky and its hues</div>
      <p>Amaresha watches the weather. Kokum trees frame its terraces, and the villa is set so that dawn, monsoon cloud, and the long violet dusk all play out over the beach below.</p>
      <div class="specs"><span>2 bedrooms</span><span>Sleeps 5</span><span>Private infinity pool</span><span>Kokum-framed terraces</span></div></div></div>
    <div class="vrow rev"><div class="vmedia hov"><img class="pz" src="https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?q=80&w=1600&auto=format&fit=crop" alt="Villa Inaya"><div class="tag mono">Palms to the water</div></div>
      <div class="vinfo"><div class="idx">No.3</div><h3>Inaya</h3><div class="mean">named for grace and kindness</div>
      <p>The gentlest of the four. From Inaya the sea appears through a screen of coconut palms, and the villa's pavilion is where long afternoons tend to dissolve.</p>
      <div class="specs"><span>2 bedrooms</span><span>Sleeps 5</span><span>Private infinity pool</span><span>Palm-dotted sea view</span></div></div></div>
    <div class="vrow rev"><div class="vmedia hov"><img class="pz" src="https://images.unsplash.com/photo-1582719508461-905c673771fd?q=80&w=1600&auto=format&fit=crop" alt="Villa Varenya"><div class="tag mono">Horizon views</div></div>
      <div class="vinfo"><div class="idx">No.4</div><h3>Varenya</h3><div class="mean">named for excellence and perseverance</div>
      <p>The villa of the long view. Red clay-tiled roofs step down the hill beneath it, and past them there is nothing but horizon. This is the one photographers ask for.</p>
      <div class="specs"><span>2 bedrooms</span><span>Sleeps 5</span><span>Private infinity pool</span><span>Clay-tile rooflines</span></div></div></div>
  </div>
  <div class="amen rev">
    <h2 class="sec">In every <em>villa</em></h2>
    <div class="grid">
      <div class="cell"><div class="mono">01</div><h4>Daily housekeeping</h4></div>
      <div class="cell"><div class="mono">02</div><h4>24-hour concierge &amp; security</h4></div>
      <div class="cell"><div class="mono">03</div><h4>In-villa spa therapies</h4></div>
      <div class="cell"><div class="mono">04</div><h4>Kitchenette &amp; house phone</h4></div>
      <div class="cell"><div class="mono">05</div><h4>Complimentary Wi-Fi</h4></div>
      <div class="cell"><div class="mono">06</div><h4>Coconut-wood interiors</h4></div>
    </div>
  </div>
  <div class="vidband rev hov">
    <video src="https://videos.pexels.com/video-files/7108800/7108800-hd_1080_1920_25fps.mp4" autoplay muted loop playsinline></video>
    <div class="cap mono">The coast below the villas · film</div>
  </div>
</section>
"""
villas_js = """
document.querySelectorAll('.pz').forEach(img=>{gsap.to(img,{scale:1,ease:'none',scrollTrigger:{trigger:img,start:'top bottom',end:'bottom top',scrub:true}})});
"""
page("villas.html","Villas — Coco Shambhala · Arka, Amaresha, Inaya, Varenya",
 "Four two-bedroom villas with private infinity pools above Bhogave Beach, Sindhudurg.",
 "v",villas_css,villas_body,villas_js,
 ("Two bedrooms, one horizon","Which villa is <em>yours?</em>","stay.html","Plan your stay"))

# ---------------- EXPERIENCES ----------------
exp_css = """
.groups{display:flex;flex-direction:column;gap:16vh}
.group .gh{display:flex;align-items:baseline;gap:26px;margin-bottom:6vh}
.group .gh .mono{color:var(--laterite)}
.egrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:1px;background:rgba(233,226,210,.12)}
.ecell{background:var(--night);padding:40px 32px;position:relative;overflow:hidden}
.ecell h4{font-family:'Fraunces',serif;font-weight:400;font-size:26px}
.ecell p{margin-top:12px;color:rgba(233,226,210,.72);font-size:14px;line-height:1.65}
.ecell .mono{color:var(--palm);margin-bottom:14px;display:block}
.ecell::after{content:"";position:absolute;left:0;right:0;bottom:0;height:2px;background:var(--laterite);transform:scaleX(0);transform-origin:left;transition:transform .5s cubic-bezier(.6,0,.2,1)}
.ecell:hover::after{transform:scaleX(1)}
.featband{position:relative;height:86vh;overflow:hidden;margin:16vh 0 0;border-radius:3px}
.featband video,.featband img{position:absolute;inset:0}
.featband::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 40%,rgba(10,18,15,.8))}
.featband .cap{position:absolute;bottom:40px;left:44px;z-index:2;max-width:600px}
.featband .cap h3{font-family:'Fraunces',serif;font-weight:400;font-size:clamp(28px,3.6vw,52px)}
.featband .cap p{margin-top:10px;color:rgba(233,226,210,.8);line-height:1.65}
"""
exp_body = """
<section class="vhero">
  <div class="media"><video src="https://videos.pexels.com/video-files/17454112/17454112-hd_1920_1080_25fps.mp4" autoplay muted loop playsinline poster="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=1600&auto=format&fit=crop"></video></div>
  <div class="inner">
    <div class="mono kicker">Experiences · Nineteen ways into the Konkan</div>
    <h1><span class="ln"><span>The sea sets</span></span><span class="ln"><span>the <em>schedule</em></span></span></h1>
    <p class="lede">Every day here is arranged around water, jungle, stone, and the people who know them. Tell the concierge what kind of day you want; the coast does the rest.</p>
  </div>
</section>
<section class="body">
  <div class="groups">
    <div class="group rev"><div class="gh"><span class="mono">By sea</span><h2 class="sec">Into the <em>blue</em></h2></div>
      <div class="egrid">
        <div class="ecell hov"><span class="mono">01</span><h4>Dolphins at dawn</h4><p>A fisherman's boat out on a flat morning sea, and the pods that patrol this coast most days of the season.</p></div>
        <div class="ecell hov"><span class="mono">02</span><h4>Scuba diving</h4><p>PADI courses and first-time discovery dives over the reef waters off Sindhudurg.</p></div>
        <div class="ecell hov"><span class="mono">03</span><h4>Snorkelling</h4><p>Coral, reef fish, and warm shallow water. No experience needed, just a mask.</p></div>
        <div class="ecell hov"><span class="mono">04</span><h4>Sea foraging</h4><p>Line-fish, gather edible seaweed and urchins, then hand the basket to the chef.</p></div>
        <div class="ecell hov"><span class="mono">05</span><h4>Fishing trip</h4><p>Open-water angling the way the village has always done it.</p></div>
        <div class="ecell hov"><span class="mono">06</span><h4>Watersports at Tarkarli</h4><p>Parasailing, jet ski, banana boat and wake surfing on the famous white-sand stretch.</p></div>
      </div></div>
    <div class="group rev"><div class="gh"><span class="mono">By land</span><h2 class="sec">Jungle &amp; <em>stone</em></h2></div>
      <div class="egrid">
        <div class="ecell hov"><span class="mono">07</span><h4>Waterfall trail</h4><p>A guided trek through forest to cascades and natural pools. Swim where the jungle drinks.</p></div>
        <div class="ecell hov"><span class="mono">08</span><h4>Nivati fort expedition</h4><p>A rugged climb to laterite ruins with the sea on three sides of the summit.</p></div>
        <div class="ecell hov"><span class="mono">09</span><h4>Sindhudurg fort &amp; Malvan</h4><p>The great sea fortress and the fishing town beside it, a short boat ride away.</p></div>
        <div class="ecell hov"><span class="mono">10</span><h4>Hiking the groves</h4><p>Forest paths through villages and sacred groves that don't appear on maps.</p></div>
        <div class="ecell hov"><span class="mono">11</span><h4>Birdwatching at Pat Lake</h4><p>Local and migratory species over a quiet water sanctuary inland.</p></div>
        <div class="ecell hov"><span class="mono">12</span><h4>Walawal river</h4><p>A slow boat through mangrove channels, past temples and river villages.</p></div>
      </div></div>
    <div class="group rev"><div class="gh"><span class="mono">By hand</span><h2 class="sec">Craft &amp; <em>fire</em></h2></div>
      <div class="egrid">
        <div class="ecell hov"><span class="mono">13</span><h4>Chitrakathi art class</h4><p>Learn a rare Konkan storytelling art form from the artisans keeping it alive.</p></div>
        <div class="ecell hov"><span class="mono">14</span><h4>Puppetry showcase</h4><p>Traditional puppet theatre, performed the way it has been for generations.</p></div>
        <div class="ecell hov"><span class="mono">15</span><h4>Malvani cooking</h4><p>An interactive class in the region's own cuisine: sol kadhi, reef fish, coconut and kokum.</p></div>
        <div class="ecell hov"><span class="mono">16</span><h4>Barbeque on the beach</h4><p>A private bonfire dinner on the sand as the sun goes down.</p></div>
      </div></div>
    <div class="group rev"><div class="gh"><span class="mono">By shore</span><h2 class="sec">Slow <em>water</em></h2></div>
      <div class="egrid">
        <div class="ecell hov"><span class="mono">17</span><h4>Canoe the Karli</h4><p>Paddle the mangrove ecosystems of the Karli river at your own pace.</p></div>
        <div class="ecell hov"><span class="mono">18</span><h4>Nivati cove picnic</h4><p>A boat to a hidden cove, a hamper, and nowhere to be until the light changes.</p></div>
        <div class="ecell hov"><span class="mono">19</span><h4>Two beaches</h4><p>Bhogave, where the fishing village wakes; Nivati, dramatic and usually empty.</p></div>
      </div></div>
  </div>
  <div class="featband rev">
    <video src="https://videos.pexels.com/video-files/18420612/18420612-hd_1920_1080_25fps.mp4" autoplay muted loop playsinline></video>
    <div class="cap"><h3>The waterfall trail</h3><p>Monsoon feeds the falls; the falls feed the pools; the pools are why you brought a swimsuit on a hike.</p></div>
  </div>
</section>
"""
page("experiences.html","Experiences — Coco Shambhala · Sea, jungle, craft",
 "Nineteen curated Konkan experiences: dolphins at dawn, scuba, sea forts, waterfall treks, Malvani cooking, Chitrakathi art.",
 "e",exp_css,exp_body,"",
 ("The concierge is listening","Build your <em>days</em>","stay.html","Plan your stay"))

# ---------------- STAY ----------------
stay_css = """
.splitrow{display:grid;grid-template-columns:1fr 1fr;gap:5vw;align-items:stretch}
.splitrow .vid{height:80vh;overflow:hidden;border-radius:3px;position:relative}
.splitrow .vid video{position:absolute;inset:0}
.faq{margin-top:12vh}
.qa{border-top:1px solid rgba(233,226,210,.14);padding:44px 0}
.qa h4{font-family:'Fraunces',serif;font-weight:400;font-size:clamp(22px,2.6vw,34px)}
.qa p{margin-top:14px;color:rgba(233,226,210,.75);line-height:1.75;max-width:70ch}
.pack{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:26px;margin-top:7vh}
.pcard{border:1px solid rgba(233,226,210,.18);border-radius:3px;padding:40px 34px}
.pcard .mono{color:var(--gold)}
.pcard h4{font-family:'Fraunces',serif;font-weight:400;font-size:30px;margin-top:12px}
.pcard p{margin-top:12px;color:rgba(233,226,210,.72);font-size:14px;line-height:1.65}
"""
stay_body = """
<section class="vhero" style="height:78vh">
  <div class="media"><video src="https://videos.pexels.com/video-files/10761087/10761087-hd_1920_1080_30fps.mp4" autoplay muted loop playsinline poster="https://images.unsplash.com/photo-1439066615861-d1af74d74000?q=80&w=1600&auto=format&fit=crop"></video></div>
  <div class="inner">
    <div class="mono kicker">Your stay · Enquiries &amp; planning</div>
    <h1><span class="ln"><span>Begin the</span></span><span class="ln"><span><em>descent</em></span></span></h1>
    <p class="lede">Four villas, twenty guests at most, and a calendar that fills quietly. Tell us your dates and who's coming; the concierge builds everything else around you.</p>
  </div>
</section>
<section class="body">
  <div class="splitrow">
    <div class="rev">
      <h2 class="sec">Made for <em>occasions</em></h2>
      <div class="pack">
        <div class="pcard hov"><div class="mono">For two</div><h4>Honeymoons</h4><p>A villa to yourselves, dinners on the sand, and a coastline that keeps no schedule.</p></div>
        <div class="pcard hov"><div class="mono">For the years</div><h4>Anniversaries</h4><p>Private pool, private chef, and the same sunset that never repeats itself.</p></div>
        <div class="pcard hov"><div class="mono">For everyone</div><h4>Celebrations &amp; buyouts</h4><p>Take all four villas: twenty guests, one hillside, your own private resort.</p></div>
      </div>
      <div class="faq">
        <div class="qa rev"><h4>Where exactly are you?</h4><p>Above Bhogave Beach near Parole village, Sindhudurg district, Maharashtra, on the quiet coast just north of Goa. 15°58′ N — 73°32′ E.</p></div>
        <div class="qa rev"><h4>How do rates work?</h4><p>Villas are let whole, with staff, breakfast and housekeeping included. Send your dates through the enquiry link below and the team responds with availability and a quote.</p></div>
        <div class="qa rev"><h4>What about getting there?</h4><p>The concierge arranges transfers from the nearest airports and rail heads; ask when you enquire and it will be planned for you.</p></div>
        <div class="qa rev"><h4>Recognition</h4><p>Condé Nast Traveller's world's top 25 beach villas, Outlook Traveller's best boutique hotel, and TripAdvisor's top hotels in India.</p></div>
      </div>
    </div>
    <div class="vid rev hov"><video src="https://videos.pexels.com/video-files/6981400/6981400-hd_1920_1080_25fps.mp4" autoplay muted loop playsinline></video></div>
  </div>
</section>
"""
page("stay.html","Your stay — Coco Shambhala · Enquiries",
 "Plan your stay at Coco Shambhala: four private villas above Bhogave Beach, Sindhudurg. Honeymoons, anniversaries, full buyouts.",
 "s",stay_css,stay_body,"",
 ("The calendar is short","Ask for your <em>dates</em>","https://cocoshambhala.com/enquiries-information/","Send an enquiry"))
print("ALL PAGES BUILT")
