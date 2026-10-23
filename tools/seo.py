"""Shared, source-driven metadata for every canonical EN/ES page.

Preview intentionally stays noindex. Does not submit URLs or enable indexing.
"""
import json
from html import escape
from pathlib import Path
import content as C

ROOT = Path(__file__).resolve().parents[1]
BASE = C.SITE_URL

SHORT_TITLES = {
 '0NjEr4251uM': ('Bitcoin Economics: merchants and savers, 2023', 'Bitcoin Economics: comercios y ahorradores, 2023'),
 '1ktrkr1tg6g': ('Eliazar on One Love Bitcoin: the Kaboom story', 'Eliazar en One Love Bitcoin: la historia de Kaboom'),
 '4SxWlCcMDiU': ('Eliazar on Ordermoon: fewer merchants, more spending', 'Eliazar en Ordermoon: menos comercios, más uso'),
 '63kbzc9GfaQ': ('Soy502: bitcoin businesses at Atitlán, 2022', 'Soy502: negocios bitcoin en Atitlán, 2022'),
 '79cIKf_T3N0': ('Adopting Bitcoin 2023: Rudy and Eliazar', 'Adopting Bitcoin 2023: Rudy y Eliazar'),
 'AkaHBhfKQhk': ('Spending bitcoin in Panajachel: a Sunday visit', 'Pagar con bitcoin en Panajachel: un domingo'),
 'DYYwE05ehMs': ('CGTN: bitcoin in Panajachel during the 2022 slump', 'CGTN: bitcoin en Panajachel durante la caída de 2022'),
 'iU7EruLMre0': ('Eliazar explains the circular bitcoin economy', 'Eliazar explica la economía circular bitcoin'),
 'MjDnc7ZzQwA': ('Patrick Melder: teaching children bitcoin, 2022', 'Patrick Melder: enseñar bitcoin a los niños, 2022'),
 'mJf9LcwfaTU': ('Ricky explains the thinking behind Bitcoin Lago', 'Ricky explica la idea detrás de Bitcoin Lago'),
 'pm4mZxMzvCU': ('Blink at Lago Summit 2023: Lightning payments', 'Blink en Lago Summit 2023: pagos Lightning'),
 'vYdp8yS1exU': ('A visit to Atitlán: bitcoin mining and weaving', 'Una visita a Atitlán: minería bitcoin y tejidos'),
 'how-bitcoin-lago-started': ('How Bitcoin Lago started at Lake Atitlán', 'Cómo empezó Bitcoin Lago en el Lago de Atitlán'),
 'kaboom-cooking-oil-generator': ('Kaboom: mining bitcoin with used cooking oil', 'Kaboom: minar bitcoin con aceite de cocina usado'),
 'merchants-over-time': ('Bitcoin merchants at Atitlán: the counts, 2022 to 2026', 'Comercios bitcoin en Atitlán: cifras de 2022 a 2026'),
 'a-day-paying-with-bitcoin': ('A day paying only with bitcoin at Atitlán', 'Un día pagando solo con bitcoin en Atitlán'),
 'wallets-at-the-lake': ('Bitcoin wallets used at Lake Atitlán', 'Billeteras bitcoin usadas en Atitlán'),
 'waste-to-energy-plan-2022': ('The 2022 waste-to-energy plan: what happened', 'El plan de energía de 2022: qué ocurrió'),
 'visiting-lake-atitlan-with-bitcoin': ('Visiting Lake Atitlán with bitcoin', 'Visitar el Lago de Atitlán con bitcoin'),
 'learning-and-supporting-bitcoin-lago': ('Learning bitcoin and supporting the lake', 'Aprender sobre bitcoin y apoyar al lago'),
}


def description(text):
    """Keep source copy, at a word boundary; never add unsupported claims."""
    text = ' '.join(text.split())
    if len(text) <= 160:
        return text
    cut = text[:157].rsplit(' ', 1)[0].rstrip(' ,:;.')
    return cut + '…'


def records():
    core = {
      'home': {
        'title': ('Bitcoin at Lake Atitlán, Guatemala | Bitcoin Lago', 'Bitcoin en el Lago de Atitlán, Guatemala | Bitcoin Lago'),
        'description': ('Explore bitcoin at Lake Atitlán, Guatemala: find local businesses, read the community story and get practical visitor answers in English and Spanish.', 'Explora bitcoin en el Lago de Atitlán, Guatemala: encuentra comercios, conoce la historia de la comunidad y consulta respuestas prácticas para tu visita.'),
        'heading': ('Bitcoin lives here.', 'Aquí se vive bitcoin.'),
        'label': ('LAKE ATITLÁN · GUATEMALA', 'LAGO DE ATITLÁN · GUATEMALA'),
        'path': '', 'type': 'WebPage'},
      'story': {
        'title': ('Bitcoin Lago history at Lake Atitlán | Bitcoin Lago', 'Historia de Bitcoin Lago en Atitlán | Bitcoin Lago'),
        'description': ('Follow Bitcoin Lago’s history at Lake Atitlán through sourced community posts, photos, education projects, merchant stories, interviews and local meetups.', 'Conoce la historia de Bitcoin Lago en Atitlán con publicaciones, fotos y fuentes sobre educación, comercios, entrevistas y encuentros de la comunidad.'),
        'heading': ('Our story, year by year.', 'Nuestra historia, año por año.'),
        'label': ('THE COMMUNITY STORY', 'LA HISTORIA DE LA COMUNIDAD'),
        'path': 'story/', 'type': 'CollectionPage'},
      'blog': {
        'title': ('Bitcoin Lago videos and stories from Lake Atitlán', 'Videos e historias de Bitcoin Lago en el Lago de Atitlán'),
        'description': ('Read sourced stories and video summaries about Bitcoin Lago at Lake Atitlán: community origins, bitcoin education, local merchants and cooking-oil mining.', 'Lee historias y resúmenes de videos sobre Bitcoin Lago en Atitlán: los orígenes de la comunidad, educación, comercios y minería con aceite de cocina usado.'),
        'heading': ('Stories from the lake.', 'Historias desde el lago.'),
        'label': ('VIDEOS · INTERVIEWS · STORIES', 'VIDEOS · ENTREVISTAS · HISTORIAS'),
        'path': 'blog/', 'type': 'CollectionPage'},
      'faq': {
        'title': ('Using bitcoin at Lake Atitlán: visitor FAQ | Bitcoin Lago', 'Usar bitcoin en Atitlán: preguntas frecuentes | Bitcoin Lago'),
        'description': ('Plan your visit to Lake Atitlán with bitcoin: practical, sourced answers about payments, wallets, cash, transport and contacting the Bitcoin Lago community.', 'Prepara tu visita al Lago de Atitlán con bitcoin: respuestas con fuentes sobre pagos, billeteras, efectivo, transporte y contacto con la comunidad local.'),
        'heading': ('Visit with bitcoin.', 'Visita con bitcoin.'),
        'label': ('THE VISITOR GUIDE', 'LA GUÍA PARA VISITANTES'),
        'path': 'faq/', 'type': 'WebPage'},
    }
    result = {}
    for key, a in core.items():
        for i, lang in enumerate(('en', 'es')):
            path = ('' if lang == 'en' else 'es/') + a['path']
            result[path] = dict(key=key, path=path, lang=lang, title=a['title'][i], description=description(a['description'][i]), heading=a['heading'][i], label=a['label'][i], type=a['type'], image=f'images/og/{key}-{lang}.jpg')
    for folder in ('blog', 'topics'):
        for f in sorted((ROOT / 'tools' / folder).glob('*.json')):
            a = json.loads(f.read_text(encoding='utf-8'))
            if 'slug' not in a:
                continue
            key = a.get('video_id', a['slug'])
            for i, lang in enumerate(('en', 'es')):
                path = ('' if lang == 'en' else 'es/') + 'blog/' + a['slug'] + '/'
                title = SHORT_TITLES[key][i]
                if 'Bitcoin Lago' not in title:
                    title += ' | Bitcoin Lago'
                result[path] = dict(key=a['slug'], path=path, lang=lang, title=title, description=description(('Eliazar explains why more than 100 merchants fell to around 40 or 50, what the change says about bitcoin use, and how the team is adapting its work at Lake Atitlán.' if lang=='en' else 'Eliazar explica por qué más de 100 comercios bajaron a unos 40 o 50, qué revela el cambio sobre el uso de bitcoin y cómo adapta su trabajo el equipo en Atitlán.') if key=='4SxWlCcMDiU' else a['dek_' + lang]), heading=SHORT_TITLES[key][i], label=('FROM THE LAKE · STORIES' if lang=='en' else 'DESDE EL LAGO · HISTORIAS'), type='WebPage', article=True, image=f'images/og/{a["slug"]}-{lang}.jpg')
                if folder == 'topics': result[path]['date'] = a['date']
                else: result[path]['citation'] = f'https://www.youtube.com/watch?v={a["video_id"]}'
    return result


def prepare(T):
    path = T['canonical'].removeprefix(BASE)
    a = records()[path]
    T = dict(T)
    T.update(title=a['title'], description=a['description'], og_image=BASE+a['image'], og_alt=a['heading'] + ' Bitcoin Lago, ' + ('Lake Atitlán, Guatemala.' if a['lang']=='en' else 'Lago de Atitlán, Guatemala.'), og_type='article' if a.get('article') else 'website', og_locale_other='es_GT' if a['lang']=='en' else 'en_US')
    return T


def structured(T):
    path = T['canonical'].removeprefix(BASE)
    a = records()[path]
    lang = a['lang']; url = T['canonical']; orgid = BASE+'#organization'
    image = {'@type': 'ImageObject', 'url': T['og_image'], 'width': 1200, 'height': 630, 'caption': T['og_alt']}
    graph = [
      {'@type': 'Organization', '@id': orgid, 'name': 'Bitcoin Lago', 'url': BASE, 'logo': {'@type': 'ImageObject', 'url': BASE+'images/logo/lago-bitcoin-logo.png'}},
      {'@type': 'WebSite', '@id': BASE+'#website', 'name': 'Bitcoin Lago', 'url': BASE, 'inLanguage': ['en', 'es'], 'publisher': {'@id': orgid}},
      {'@type': a['type'], '@id': url+'#webpage', 'url': url, 'name': T['title'], 'description': T['description'], 'inLanguage': lang, 'isPartOf': {'@id': BASE+'#website'}, 'primaryImageOfPage': image},
    ]
    if a.get('article'):
        post = {'@type': 'BlogPosting', '@id': url+'#article', 'mainEntityOfPage': {'@id': url+'#webpage'}, 'headline': a['heading'], 'description': T['description'], 'image': image, 'inLanguage': lang, 'author': {'@type': 'Organization', 'name': 'Bitcoin Lago site team', 'url': BASE}, 'publisher': {'@id': orgid}}
        if a.get('date'): post['datePublished'] = a['date']
        if a.get('citation'): post['citation'] = a['citation']
        graph.append(post)
    home = BASE + ('' if lang=='en' else 'es/')
    if a['key'] != 'home':
        crumbs = [{'@type':'ListItem', 'position':1, 'name':'Bitcoin Lago', 'item':home}]
        if a.get('article'): crumbs.append({'@type':'ListItem', 'position':2, 'name':'Videos and stories' if lang=='en' else 'Videos e historias', 'item':home+'blog/'})
        crumbs.append({'@type':'ListItem', 'position':len(crumbs)+1, 'name':a['heading'].rstrip('.'), 'item':url})
        graph.append({'@type':'BreadcrumbList', '@id':url+'#breadcrumbs', 'itemListElement':crumbs})
    data = json.dumps({'@context':'https://schema.org', '@graph':graph}, ensure_ascii=False).replace('<', '\\u003c')
    return '<script type="application/ld+json">'+data+'</script>\n'


def extra_meta(T):
    values = [('property','og:image:secure_url',T['og_image']), ('property','og:image:type','image/jpeg'), ('property','og:image:width','1200'), ('property','og:image:height','630'), ('property','og:image:alt',T['og_alt']), ('property','og:locale:alternate',T['og_locale_other']), ('name','twitter:title',T['title']), ('name','twitter:description',T['description']), ('name','twitter:image',T['og_image']), ('name','twitter:image:alt',T['og_alt'])]
    return ''.join(f'<meta {kind}="{key}" content="{escape(value, quote=True)}">\n' for kind,key,value in values) + structured(T)


def write_manifest():
    photo = json.loads((ROOT/'data/photos.json').read_text(encoding='utf-8'))['hero']
    manifest = {'base_url': BASE, 'width':1200, 'height':630, 'preview_noindex':True, 'license': 'CC BY-SA 4.0 for the adapted lake photograph; existing brand marks excluded. Photo cropped and combined with typography.', 'photo':photo, 'pages':records()}
    out = ROOT/'images/og'; out.mkdir(parents=True, exist_ok=True)
    (out/'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    return manifest
