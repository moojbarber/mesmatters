#!/usr/bin/env python3
"""Build the social calendar page from social/queue and social/state.

  python scripts/social/calendar.py <out_dir>

Writes <out_dir>/index.html plus <out_dir>/thumbs/*.jpg (small previews).
Publish the folder as an artifact (root = out_dir).
"""
import datetime as dt
import glob
import html
import json
import os
import sys

import yaml
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
QUEUE = os.path.join(ROOT, "social", "queue")
STATE = os.path.join(ROOT, "social", "state", "posted.json")


def status(item, p, state):
    spec = item.get(p)
    if not spec:
        return None
    rec = state.get(item["id"], {}).get(p, {})
    if rec.get("id"):
        return "posted"
    if rec.get("error"):
        return "failed"
    if spec.get("needs_text") or spec.get("kind") == "manual_reel":
        return "needs"
    return "approved" if item.get("approved") else "waiting"


def thumb(item, out):
    src = None
    for m in item.get("instagram", {}).get("media", []):
        if m.endswith(".jpg"):
            src = m
            break
    if not src:
        cands = sorted(glob.glob(os.path.join(ROOT, "marketing", "social", "weeks-*", item["id"], f"{item['id']}-01.png")))
        src = cands and os.path.relpath(cands[0], ROOT)
    if not src:
        return None
    os.makedirs(os.path.join(out, "thumbs"), exist_ok=True)
    name = f"thumbs/{item['id']}.jpg"
    im = Image.open(os.path.join(ROOT, src)).convert("RGB")
    im.thumbnail((360, 450))
    im.save(os.path.join(out, name), quality=82)
    return name


def main(out):
    state = json.load(open(STATE)) if os.path.exists(STATE) else {}
    rows = []
    for f in sorted(glob.glob(os.path.join(QUEUE, "*.yaml"))):
        it = yaml.safe_load(open(f))
        r = {"id": it["id"], "week": it["week"], "date": str(it["date"]), "type": it["type"], "title": it["title"],
             "approved": bool(it.get("approved")), "article": it.get("article"), "thumb": thumb(it, out), "p": {}}
        for p in ("linkedin", "x", "instagram"):
            s = it.get(p)
            if not s:
                continue
            d = {"at": str(s.get("at", "")), "status": status(it, p, state)}
            if p == "linkedin":
                d.update(text=s["text"], comment=s.get("comment"), poll=s.get("poll"), doc=bool(s.get("document")))
            elif p == "x":
                d.update(posts=s["posts"], poll=s.get("poll"))
            else:
                d.update(kind=s["kind"], caption=s.get("caption", ""), slides=len(s.get("media", [])))
            r["p"][p] = d
        rows.append(r)
    built = dt.datetime.now().strftime("%d %b %Y, %H:%M")
    page = TEMPLATE.replace("__DATA__", json.dumps(rows, ensure_ascii=False).replace("</", "<\\/")).replace("__BUILT__", html.escape(built))
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w").write(page)
    print(f"Calendar: {len(rows)} posts → {out}/index.html")


TEMPLATE = r"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Social Calendar</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#0a0820;--bg2:#120f33;--card:rgba(255,255,255,.055);--card2:rgba(255,255,255,.09);--line:rgba(255,255,255,.12);--tx:#e9e6ff;--mut:#a9a4d6;--dim:#7d78ad;--a:#8b6cff;--b:#33d4e0;
--posted:#3ddc97;--approved:#33d4e0;--waiting:#8b86b8;--needs:#ffb86b;--failed:#ff6b81;--disp:'Space Grotesk',system-ui,sans-serif;--body:Inter,system-ui,-apple-system,'Segoe UI',sans-serif}
@media (prefers-color-scheme: light){:root:not([data-theme="dark"]){--bg:#f7f6fd;--bg2:#ffffff;--card:rgba(20,10,80,.04);--card2:rgba(20,10,80,.08);--line:rgba(20,10,80,.12);--tx:#17133a;--mut:#4f4a7a;--dim:#7a76a0;--waiting:#8d89ad;--approved:#119aa6;--posted:#18a86b;--needs:#d9822b}}
:root[data-theme="light"]{--bg:#f7f6fd;--bg2:#ffffff;--card:rgba(20,10,80,.04);--card2:rgba(20,10,80,.08);--line:rgba(20,10,80,.12);--tx:#17133a;--mut:#4f4a7a;--dim:#7a76a0;--waiting:#8d89ad;--approved:#119aa6;--posted:#18a86b;--needs:#d9822b}
:root[data-theme="dark"]{--bg:#0a0820}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--tx);font:15px/1.55 var(--body);-webkit-font-smoothing:antialiased}
.wrap{max-width:1180px;margin:0 auto;padding:28px 16px 60px}
header{display:flex;flex-wrap:wrap;gap:14px 24px;align-items:end;justify-content:space-between;margin-bottom:20px}
h1{font:700 30px/1.1 var(--disp);margin:0;letter-spacing:-.01em}
h1 span{background:linear-gradient(120deg,#8b6cff,#33d4e0);-webkit-background-clip:text;background-clip:text;color:transparent}
.sub{color:var(--mut);margin:6px 0 0;font-size:14px}
.legend{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:13px;color:var(--mut)}
.legend i,.dot{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:6px;vertical-align:1px}
.s-posted{background:var(--posted)}.s-approved{background:var(--approved)}.s-waiting{background:var(--waiting)}.s-needs{background:var(--needs)}.s-failed{background:var(--failed)}
.bar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;justify-content:space-between;margin:18px 0 12px}
.nav{display:flex;align-items:center;gap:8px}
.nav h2{font:700 20px var(--disp);margin:0 8px;min-width:170px}
button{font:inherit;color:inherit;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:7px 12px;cursor:pointer}
button:hover{background:var(--card2)}button[aria-pressed="true"]{border-color:var(--a);background:color-mix(in srgb,var(--a) 22%,transparent)}
.filters{display:flex;gap:6px;flex-wrap:wrap}
.todo{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--needs);border-radius:14px;padding:14px 16px;margin-bottom:8px}
.todo h3{font:600 15px var(--disp);margin:0 0 6px}.todo ul{margin:0;padding-left:18px;color:var(--mut);font-size:14px}.todo li{margin:3px 0}
.todo a{color:var(--b);cursor:pointer;text-decoration:underline}
.grid{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:6px}
.dow{font-size:12px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;padding:0 6px 2px}
.day{min-height:118px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:7px;display:flex;flex-direction:column;gap:5px}
.day.out{opacity:.35}.day.today{border-color:var(--b)}
.dn{font:600 13px var(--disp);color:var(--mut)}
.post{text-align:left;width:100%;padding:6px 7px;border-radius:9px;background:var(--bg2);border:1px solid var(--line);font-size:12.5px;line-height:1.3}
.post .t{display:block;font-weight:600;overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
.post .k{display:block;color:var(--dim);font-size:11px;margin-bottom:2px}
.pl{display:flex;flex-wrap:wrap;gap:2px 7px;margin-top:4px;font-size:11px;color:var(--mut)}
.pl span{white-space:nowrap}
.list{display:none}
.lday{margin:14px 0 6px;font:600 14px var(--disp);color:var(--mut)}
.list .post{margin-bottom:6px;padding:10px 12px;font-size:14px}
@media (max-width:760px){.grid,.dows{display:none}.list{display:block}h1{font-size:24px}.nav h2{min-width:0;font-size:18px}}
dialog{width:min(760px,100vw);max-height:92vh;padding:0;border:1px solid var(--line);border-radius:18px;background:var(--bg2);color:var(--tx)}
dialog::backdrop{background:rgba(5,3,20,.6);backdrop-filter:blur(3px)}
.dh{display:flex;gap:16px;padding:20px 20px 12px;border-bottom:1px solid var(--line);position:sticky;top:0;background:var(--bg2)}
.dh img{width:92px;border-radius:8px;flex:none;align-self:start}
.dh h3{font:700 20px/1.2 var(--disp);margin:2px 0 6px}.dh p{margin:0;color:var(--mut);font-size:13px}
.dh .x{margin-left:auto;align-self:start}
.db{padding:6px 20px 22px}
.sec{margin-top:16px}.sec h4{display:flex;align-items:center;gap:8px;font:600 14px var(--disp);margin:0 0 8px}
.sec h4 small{font:400 12px var(--body);color:var(--dim)}
.copy{white-space:pre-wrap;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:11px 13px;font-size:14px;margin:0 0 6px}
.meta{font-size:13px;color:var(--mut);margin:4px 0}
.note{font-size:13px;color:var(--needs)}
a.ext{color:var(--b)}
</style>
</head>
<body>
<div class="wrap">
<header>
 <div><h1>Social <span>calendar</span></h1><p class="sub">LinkedIn, X and Instagram, from the posting queue · updated __BUILT__ (UK)</p></div>
 <div class="legend"><span><i class="s-posted"></i>Posted</span><span><i class="s-approved"></i>Approved, will post</span><span><i class="s-waiting"></i>Waiting for your approval</span><span><i class="s-needs"></i>Needs your words</span><span><i class="s-failed"></i>Failed</span></div>
</header>
<div id="todo"></div>
<div class="bar">
 <div class="nav"><button id="prev" aria-label="Previous month">‹</button><h2 id="mlabel"></h2><button id="next" aria-label="Next month">›</button></div>
 <div class="filters" id="filters"></div>
</div>
<div class="grid dows"><div class="dow">Mon</div><div class="dow">Tue</div><div class="dow">Wed</div><div class="dow">Thu</div><div class="dow">Fri</div><div class="dow">Sat</div><div class="dow">Sun</div></div>
<div class="grid" id="grid"></div>
<div class="list" id="list"></div>
</div>
<dialog id="dlg"></dialog>
<script>
const DATA=__DATA__;
const P={linkedin:"LinkedIn",x:"X",instagram:"Instagram"};
const ST={posted:"Posted",approved:"Approved, will post",waiting:"Waiting for approval",needs:"Needs your words",failed:"Failed, see GitHub issue"};
const esc=s=>String(s??"").replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const fmt=d=>new Date(d+"T12:00").toLocaleDateString("en-GB",{weekday:"short",day:"numeric",month:"short"});
let show=new Set(Object.keys(P));
try{const s=JSON.parse(localStorage.getItem("calFilter"));if(Array.isArray(s)&&s.length)show=new Set(s)}catch(e){}
const today=new Date().toISOString().slice(0,10);
const first=DATA.find(d=>d.date>=today)||DATA[0];
let cur=first?new Date(first.date.slice(0,7)+"-01T12:00"):new Date();
const byDate={};DATA.forEach(d=>(byDate[d.date]=byDate[d.date]||[]).push(d));
function chip(d){const pl=Object.entries(d.p).filter(([k])=>show.has(k));if(!pl.length)return"";
 return `<button class="post" data-id="${d.id}"><span class="k">${esc(d.type)}</span><span class="t">${esc(d.title)}</span><span class="pl">${pl.map(([k,v])=>`<span><i class="dot s-${v.status}"></i>${k=="linkedin"?"in":k=="x"?"X":"IG"} ${esc(v.at)}</span>`).join("")}</span></button>`}
function render(){
 const y=cur.getFullYear(),m=cur.getMonth();
 document.getElementById("mlabel").textContent=cur.toLocaleDateString("en-GB",{month:"long",year:"numeric"});
 const start=new Date(y,m,1,12);start.setDate(1-((start.getDay()+6)%7));
 let g="";for(let i=0;i<42;i++){const d=new Date(start);d.setDate(start.getDate()+i);const iso=d.toISOString().slice(0,10);
  if(i>=35&&d.getMonth()!=m)break;
  g+=`<div class="day${d.getMonth()!=m?" out":""}${iso==today?" today":""}"><div class="dn">${d.getDate()}</div>${(byDate[iso]||[]).map(chip).join("")}</div>`}
 document.getElementById("grid").innerHTML=g;
 const mk=`${y}-${String(m+1).padStart(2,"0")}`;let l="";
 Object.keys(byDate).sort().filter(k=>k.startsWith(mk)).forEach(k=>{const c=byDate[k].map(chip).join("");if(c)l+=`<div class="lday">${fmt(k)}</div>${c}`});
 document.getElementById("list").innerHTML=l||`<p class="sub">Nothing scheduled this month yet.</p>`;
 document.querySelectorAll(".post").forEach(b=>b.onclick=()=>open(b.dataset.id));
 document.getElementById("filters").innerHTML=Object.entries(P).map(([k,v])=>`<button data-f="${k}" aria-pressed="${show.has(k)}">${v}</button>`).join("");
 document.querySelectorAll("[data-f]").forEach(b=>b.onclick=()=>{const k=b.dataset.f;show.has(k)?show.delete(k):show.add(k);if(!show.size)show.add(k);try{localStorage.setItem("calFilter",JSON.stringify([...show]))}catch(e){}render()});
}
function todo(){
 const up=DATA.filter(d=>d.date>=today);
 const needs=up.filter(d=>Object.values(d.p).some(v=>v.status=="needs"));
 const weeks={};up.filter(d=>!d.approved).forEach(d=>{(weeks[d.week]=weeks[d.week]||[]).push(d)});
 const failed=DATA.filter(d=>Object.values(d.p).some(v=>v.status=="failed"));
 let li=[];
 failed.forEach(d=>li.push(`<li><a data-id="${d.id}">${esc(d.title)}</a> failed to post. Check the GitHub issue.</li>`));
 Object.entries(weeks).forEach(([w,ds])=>{const f=ds[0].date;li.push(`<li>Approve week ${w} (first post ${fmt(f)}): ${ds.length} posts waiting. Tell Claude “approve week ${w}”.</li>`)});
 needs.forEach(d=>li.push(`<li><a data-id="${d.id}">${esc(d.title)}</a> (${fmt(d.date)}) needs your own story before it can go out.</li>`));
 document.getElementById("todo").innerHTML=li.length?`<div class="todo"><h3>Needs you</h3><ul>${li.join("")}</ul></div>`:"";
 document.querySelectorAll("#todo a").forEach(a=>a.onclick=()=>open(a.dataset.id));
}
function open(id){const d=DATA.find(x=>x.id==id);let h=`<div class="dh">${d.thumb?`<img src="${d.thumb}" alt="">`:""}<div><p>${fmt(d.date)} · Week ${d.week} · ${esc(d.type)}</p><h3>${esc(d.title)}</h3>${d.article?`<p><a class="ext" href="${esc(d.article)}" target="_blank" rel="noopener">Featured article ↗</a></p>`:""}</div><button class="x" aria-label="Close">✕</button></div><div class="db">`;
 for(const [k,v] of Object.entries(d.p)){h+=`<div class="sec"><h4><i class="dot s-${v.status}"></i>${P[k]} <small>${esc(v.at)} · ${ST[v.status]}</small></h4>`;
  if(v.status=="needs")h+=`<p class="note">${k=="instagram"&&v.kind=="manual_reel"?"Talking-head reel: film this one yourself.":"Add your real experience where the placeholder is, then it can be approved."}</p>`;
  if(k=="linkedin"){h+=`<div class="copy">${esc(v.text)}</div>`;if(v.poll)h+=`<p class="meta">Poll: ${v.poll.options.map(esc).join(" / ")}</p>`;if(v.doc)h+=`<p class="meta">With the carousel as a swipeable PDF.</p>`;if(v.comment)h+=`<p class="meta">First comment: ${esc(v.comment)}</p>`}
  if(k=="x"){v.posts.forEach((p,i)=>h+=`<div class="copy">${v.posts.length>1?`<b>${i+1}/${v.posts.length}</b> `:""}${esc(p)}</div>`);if(v.poll)h+=`<p class="meta">Poll: ${v.poll.map(esc).join(" / ")}</p>`}
  if(k=="instagram"){h+=`<p class="meta">${{reel:"Reel made from the slides",carousel:`Carousel, ${v.slides} slides`,image:"Single image",manual_reel:"Talking-head reel"}[v.kind]||v.kind}</p><div class="copy">${esc(v.caption)}</div>`}
  h+=`</div>`}
 const dlg=document.getElementById("dlg");dlg.innerHTML=h+"</div>";dlg.querySelector(".x").onclick=()=>dlg.close();dlg.showModal()}
document.getElementById("dlg").addEventListener("click",e=>{if(e.target.id=="dlg")e.target.close()});
document.getElementById("prev").onclick=()=>{cur.setMonth(cur.getMonth()-1);render()};
document.getElementById("next").onclick=()=>{cur.setMonth(cur.getMonth()+1);render()};
todo();render();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "social", "calendar"))
