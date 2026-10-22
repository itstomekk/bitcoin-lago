import sys, urllib.parse
from playwright.sync_api import sync_playwright

base = sys.argv[1]
with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(locale="en-US")
    ctx.route("**/config.js", lambda r: r.fulfill(content_type="application/javascript",
              body='window.LBC_CONFIG={whatsapp:"",facebook:"",email:"",tourBooking:"",expatContact:"",whatsappNumber:"+502 1234 5678"};'))
    pg = ctx.new_page()
    pg.goto(base, wait_until="load")
    pg.evaluate("window.__opened=null; window.open=function(u){window.__opened=u; return null;}")
    pg.select_option("#ask-need", index=1)
    pg.fill("#ask-dates", "3 to 10 March")
    pg.fill("#ask-people", "6")
    pg.fill("#ask-name", "Test")
    pg.fill("#ask-msg", "Team retreat, villa in San Pedro")
    pg.click("#ask button[type=submit]")
    u = pg.evaluate("window.__opened")
    print("opened:", u[:40] if u else u)
    print(urllib.parse.unquote(u.split("text=", 1)[1]) if u else "")
    print("badge gone:", pg.evaluate("!document.querySelector('.send-ph').hasAttribute('data-placeholder')"))
    b.close()
