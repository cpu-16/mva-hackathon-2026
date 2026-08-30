import asyncio, json, sys, websockets
S="/tmp/claude-1000/-home-gar16-datos-HACKATHON-MVA-2026/73c78b9c-1ca2-475e-b268-ff227ecf3d33/scratchpad"
WS="ws://localhost:9222/devtools/page/C2A7ECE3A140797C82C803B66047DBA0"
async def main():
    async with websockets.connect(WS, max_size=None) as ws:
        n=0
        async def cmd(m,p=None):
            nonlocal n; n+=1
            await ws.send(json.dumps({"id":n,"method":m,"params":p or {}}))
            while True:
                r=json.loads(await ws.recv())
                if r.get("id")==n:
                    if "error" in r: raise RuntimeError(r["error"])
                    return r["result"]
        async def ev(expr):
            r=await cmd("Runtime.evaluate",{"expression":expr,"returnByValue":True,"awaitPromise":True}); return r["result"].get("value")
        # text fields: focus + real typing
        for i,val in enumerate(["ciberpty","https://github.com/cpu-16/mva-hackathon-2026"]):
            await ev(f'(()=>{{const e=[...document.querySelectorAll("input[type=text], textarea")].filter(e=>e.offsetParent)[{i}];e.focus();e.select();return e.getBoundingClientRect().y}})()')
            await cmd("Input.insertText",{"text":val})
        await cmd("DOM.enable"); doc=(await cmd("DOM.getDocument",{"depth":0}))["root"]["nodeId"]
        ids=(await cmd("DOM.querySelectorAll",{"nodeId":doc,"selector":"input[type=file]"}))["nodeIds"]
        print("file inputs:",ids)
        await cmd("DOM.setFileInputFiles",{"nodeId":ids[0],"files":[f"{S}/envio/ciberpty_convergent-hpo-genomewide-and-panel.csv"]})
        await cmd("DOM.setFileInputFiles",{"nodeId":ids[1],"files":[f"{S}/envio/ciberpty_track1_report.pdf"]})
        await asyncio.sleep(6)
        print(json.dumps(await ev('({texts:[...document.querySelectorAll("input[type=text], textarea")].filter(e=>e.offsetParent).map(e=>e.value), files:document.body.innerText.match(/ciberpty_[^\\n]*/g)})'),indent=1))
asyncio.run(main())
