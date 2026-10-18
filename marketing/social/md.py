import importlib.util,sys,json,re
def load(n):
    s=importlib.util.spec_from_file_location(n,f"{n}.py"); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m.WEEK
def quote(t): return "\n>\n".join("> "+l.rstrip() for l in t.split("\n") if l.strip())
def check(W):
    probs=[]
    ban=r"\b(furthermore|moreover|additionally|kicker|supercharge|seamless\w*|revolutioni\w+|unlock\w*|game-changer|delve|dive deep|elevate|leverage|foster|crucial|it's important to note|the reality is|optimiz\w*|organiz\w*|color|labor|shop floor|Infor|Kunal)\b"
    for p in W["posts"]:
        for i,t in enumerate(p["x"]):
            if len(t)>280: probs.append((p["id"],"x",i,len(t)))
        txt=" ".join([p["li"],p.get("ig",""),*p["x"],*[a+" "+b for _,a,b in p.get("slides",[])]])
        for m in re.findall(ban,txt,re.I): probs.append((p["id"],"word",m))
        for k,a,b in p.get("slides",[]):
            if k=="list" and len(b.split("|"))==3: probs.append((p["id"],"list of three",a))
            if len(a)>(90 if k=="quote" else 70): probs.append((p["id"],"slide head long",a))
    return probs
def md(W):
    out=[f"## {W['title']}",f"Featured article: [{W['article']}]({W['url']})"]
    for p in W["posts"]:
        out.append(f"### {p['day']} · {p['type']}: {p['title']}")
        out.append("**LinkedIn**"); out.append(quote(p["li"]))
        if p.get("li_poll"): out.append("Poll options: "+" / ".join(p["li_poll"]))
        if p.get("li_comment"): out.append("**First comment:** "+p["li_comment"])
        out.append("**X**" + (" (thread)" if len(p["x"])>1 else ""))
        if len(p["x"])>1: out.append("\n".join(f"{i}. "+t.replace("\n\n"," ").replace("\n"," ") for i,t in enumerate(p["x"],1)))
        else: out.append(quote(p["x"][0]))
        if p.get("x_poll"): out.append("Poll options: "+" / ".join(p["x_poll"]))
        out.append(f"**Instagram** · {p['ig_format']}")
        if p.get("ig_story"): out.append("Story poll: "+p["ig_story"])
        sl=p.get("slides",[])
        if sl:
            tag="Carousel" if len(sl)>1 else "Graphic"
            out.append(f"{tag} `{p['id']}` slides:" if len(sl)>1 else f"{tag} `{p['id']}`:")
            out.append("\n".join(f"{i}. **{a}**"+(f" {b.replace('|','; ')}" if b else "") for i,(_,a,b) in enumerate(sl,1)))
        if p.get("reel"): out.append("Reel script:\n"+quote(p["reel"]))
        out.append("Caption:"); out.append(quote(p["ig"]))
    return "\n\n".join(out)
if __name__=="__main__":
    W=load(sys.argv[1]); print(json.dumps(check(W))); open(sys.argv[1]+".md","w").write(md(W))
