#!/usr/bin/env python3
"""
Generate Liquid Sun Creative local-SEO pages (Services, Areas We Serve hub,
and one landing page per city). Output is plain static HTML committed to the
repo root — there is no runtime build step. Re-run after editing CITY data:

    python3 tools/build_local_pages.py

Pages share /lsc.css for styling.
"""
import os
import html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://liquidsuncreative.com"
PHONE_DISPLAY = "(720) 965-5359"
PHONE_E164 = "+1-720-965-5359"
EMAIL = "matt@gissentanna.com"

# --- City data ------------------------------------------------------------
# Each entry carries genuinely unique localized copy so the pages are not
# thin / templated duplicates (which Google penalizes for local landing pages).
CITIES = [
    {
        "slug": "brighton-co", "name": "Brighton", "county": "Adams County",
        "lat": 39.9853, "lng": -104.8205, "hq": True,
        "intro": [
            "Brighton is home base for Liquid Sun Creative. As the Adams County seat and one of the fastest-growing communities on the northern Front Range, Brighton is adding residential subdivisions, commercial corridors along Bridge Street and Highway 7, and new municipal and agricultural projects every season — all of which benefit from consistent aerial documentation.",
            "Because we are based here, Brighton clients get the shortest lead times we offer: same-week scheduling for most flights, quick re-shoots, and an operator who already knows the local airspace around Barr Lake, the Prairie Center, and the Vasquez Boulevard corridor.",
        ],
        "focus": "construction progress monitoring, land and agricultural mapping, and commercial real estate video",
    },
    {
        "slug": "thornton-co", "name": "Thornton", "county": "Adams County",
        "lat": 39.8680, "lng": -104.9719,
        "intro": [
            "Thornton sits about seven miles southwest of our Brighton studio, which makes it one of the easiest service areas for us to cover on short notice. The city's rapid northward expansion — new rooftops around Trail Winds, retail along I-25 and 136th, and ongoing infrastructure work — keeps a steady demand for aerial site documentation.",
            "Whether you're a builder tracking a residential phase, a property manager marketing a retail pad, or a contractor documenting a road or utility project, we deliver clean, repeatable aerial captures that hold up in client decks and permitting packages.",
        ],
        "focus": "residential construction monitoring, retail and commercial marketing, and site documentation",
    },
    {
        "slug": "northglenn-co", "name": "Northglenn", "county": "Adams County",
        "lat": 39.8856, "lng": -104.9811,
        "intro": [
            "Northglenn is a compact, established community just south of Thornton, and its ongoing redevelopment — around Webster Lake, the civic center, and the Huron Street corridor — is exactly the kind of work aerial imaging documents well. Tight infill sites are easier to communicate to stakeholders with a clear overhead view than with ground photos alone.",
            "We handle the airspace planning and FAA compliance so flights over Northglenn's denser neighborhoods are buttoned up before we ever launch, then deliver edited stills, orthomosaics, or flyover video formatted for the channel you need.",
        ],
        "focus": "redevelopment documentation, infill site mapping, and municipal project visuals",
    },
    {
        "slug": "commerce-city-co", "name": "Commerce City", "county": "Adams County",
        "lat": 39.8083, "lng": -104.9342,
        "intro": [
            "Commerce City is one of the busiest industrial and logistics corridors in the metro, with warehouse, distribution, and energy development continuing across the northern end near the Rocky Mountain Arsenal and Dick's Sporting Goods Park. Large-footprint sites like these are where aerial mapping pays for itself — a single orthomosaic captures acreage that would take days to walk.",
            "We provide scheduled progress flights for ground-up industrial builds, rooftop and asset inspections that keep crews off ladders, and GIS-ready 2D mapping for site planning and stockpile tracking.",
        ],
        "focus": "industrial and warehouse construction monitoring, asset inspection, and orthomosaic mapping",
    },
    {
        "slug": "aurora-co", "name": "Aurora", "county": "Arapahoe & Adams Counties",
        "lat": 39.7294, "lng": -104.8319,
        "intro": [
            "Aurora is Colorado's third-largest city, and its scale — from the Anschutz Medical Campus to commercial growth around E-470 and the airport — means there is no shortage of large sites that benefit from an aerial perspective. We coordinate carefully around the controlled airspace near Buckley and Denver International when a project calls for it.",
            "From healthcare and commercial construction documentation to listing video for Aurora's active real estate market, we scope each project to the deliverable you actually need and handle the compliance that larger sites require.",
        ],
        "focus": "commercial construction monitoring, real estate video, and large-site mapping",
    },
    {
        "slug": "denver-co", "name": "Denver", "county": "Denver County",
        "lat": 39.7392, "lng": -104.9903,
        "intro": [
            "Denver is the heart of the market we serve, and also the most airspace-sensitive — much of the urban core sits under controlled airspace that requires LAANC authorization and careful flight planning. That's exactly the kind of operational discipline a Part 107 operator brings, so your downtown, RiNo, or LoDo project gets documented legally and safely.",
            "We produce cinematic real estate and development video, rooftop and facade documentation, and progress capture for commercial builds across the city — packaged for the presentations, listings, and social channels Denver clients actually use.",
        ],
        "focus": "commercial and real estate video, rooftop documentation, and progress monitoring",
    },
    {
        "slug": "lakewood-co", "name": "Lakewood", "county": "Jefferson County",
        "lat": 39.7047, "lng": -105.0814,
        "intro": [
            "Lakewood spans a wide mix of property types — the Belmar district, the Federal Center, established neighborhoods, and open space around Green Mountain and Bear Creek Lake Park. That variety makes it a strong fit for both marketing-driven aerial video and technical site mapping.",
            "We shoot listing and development flyovers that showcase Lakewood's foothills backdrop, and we run progress and inspection flights for commercial and residential projects across the west metro.",
        ],
        "focus": "real estate and development video, residential construction, and property documentation",
    },
    {
        "slug": "wheat-ridge-co", "name": "Wheat Ridge", "county": "Jefferson County",
        "lat": 39.7661, "lng": -105.0772,
        "intro": [
            "Wheat Ridge is in the middle of a visible transformation, with redevelopment along the Wadsworth and 38th Avenue corridors and continued investment around the Clear Creek greenbelt. Aerial imaging is a clean way to document before-and-after change and to market new mixed-use and residential projects.",
            "We deliver progress flights for active builds, marketing video for new developments, and orthomosaic mapping for smaller infill and corridor projects throughout the city.",
        ],
        "focus": "redevelopment documentation, mixed-use marketing video, and corridor mapping",
    },
    {
        "slug": "westminster-co", "name": "Westminster", "county": "Adams & Jefferson Counties",
        "lat": 39.8367, "lng": -105.0372,
        "intro": [
            "Westminster straddles two counties and is anchored by major projects like the Downtown Westminster redevelopment and recreation around Standley Lake. Large master-planned sites and public spaces are well suited to scheduled aerial documentation that tracks change over months.",
            "We provide milestone construction flights, development marketing video, and 2D mapping for planning and stakeholder reporting across Westminster's commercial and residential corridors.",
        ],
        "focus": "master-planned development monitoring, marketing video, and site mapping",
    },
    {
        "slug": "arvada-co", "name": "Arvada", "county": "Jefferson & Adams Counties",
        "lat": 39.8028, "lng": -105.0875,
        "intro": [
            "Arvada blends the historic Olde Town district with steady new growth toward the northwest, along Ralston Creek and the Leyden area. That mix gives us both character-rich marketing backdrops and active construction sites to document.",
            "We shoot real estate and neighborhood flyovers that play up Arvada's foothills setting, and we run progress and inspection flights for residential and commercial projects across the city.",
        ],
        "focus": "real estate video, residential construction monitoring, and site documentation",
    },
    {
        "slug": "broomfield-co", "name": "Broomfield", "county": "City & County of Broomfield",
        "lat": 39.9205, "lng": -105.0867,
        "intro": [
            "Broomfield is a corporate and tech hub, with the Interlocken business park, FlatIron Crossing, and a dense cluster of campus-style commercial development along the US-36 corridor. Large building footprints and parking-structure projects are ideal candidates for aerial progress monitoring and rooftop inspection.",
            "We deliver scheduled construction flights, corporate-campus marketing video, and orthomosaic mapping for site planning, all flown with the airspace coordination Broomfield's location between Denver and Boulder requires.",
        ],
        "focus": "commercial campus monitoring, corporate marketing video, and rooftop inspection",
    },
    {
        "slug": "henderson-co", "name": "Henderson", "county": "Adams County",
        "lat": 39.9219, "lng": -104.8569,
        "intro": [
            "Henderson sits just minutes from our Brighton studio, along the South Platte between Brighton and Commerce City. It's a corridor of agriculture, gravel and aggregate operations, and growing logistics development — large rural and industrial parcels where a single flight covers ground that would take a long time on foot.",
            "We provide aerial mapping and stockpile documentation for aggregate and agricultural sites, progress flights for new industrial builds, and land documentation for owners and developers near Barr Lake.",
        ],
        "focus": "agricultural and aggregate mapping, industrial construction, and land documentation",
    },
]

SERVICES = [
    {
        "title": "Construction Progress Monitoring",
        "tagline": "A smarter way to manage your build.",
        "body": "Consistent aerial documentation to spot problems early, keep crews safe, and give stakeholders a clear view of progress — across commercial, residential, and public infrastructure.",
        "points": ["Scheduled weekly or milestone flights", "Progress photos and timeline flyovers", "Decks, RFI support, and documentation"],
    },
    {
        "title": "Asset & Site Capture",
        "tagline": "See every detail without the risk.",
        "body": "High-resolution visuals and orthomosaics of hard-to-reach assets — rooftops, towers, solar arrays, agricultural fields — captured safely from the air.",
        "points": ["2D orthomosaic mapping (GIS-ready)", "Telecom and infrastructure inspection", "Property and rooftop documentation"],
    },
    {
        "title": "Video Marketing",
        "tagline": "Stories that sell.",
        "body": "Cinematic, strategy-driven video for real estate, outdoor brands, and industrial clients — written, filmed, edited, and packaged for the channels you actually use.",
        "points": ["Listing videos and aerial flyovers", "Lifestyle and adventure brand films", "Time-lapse builds and progress recaps"],
    },
]


def e(s):
    return html.escape(s, quote=True)


def header(active=""):
    def cls(name):
        return ' aria-current="page"' if name == active else ""
    return f"""  <header class="site-header">
    <div class="container">
      <a class="site-mark" href="/" aria-label="Liquid Sun Creative — home">
        <img src="/logo.png" alt="">
        <span>Liquid Sun Creative</span>
      </a>
      <nav class="site-nav" aria-label="Primary">
        <a href="/services/"{cls('services')}>Services</a>
        <a href="/areas-served/"{cls('areas')}>Areas Served</a>
        <a href="/#work">Work</a>
        <a href="/blog/">Newsletter</a>
        <a href="/#contact">Contact</a>
      </nav>
    </div>
  </header>"""


def contact_band():
    return f"""  <section class="band contact" id="contact" aria-labelledby="contact-heading">
    <div class="container">
      <div class="section-head">
        <p class="mono eyebrow">Contact</p>
        <h2 id="contact-heading">Tell us what you need.</h2>
        <p>Send a note or call — we typically reply within one business day.</p>
      </div>
      <div class="contact-grid">
        <div class="contact-card">
          <span class="mono">Email</span>
          <a href="mailto:{EMAIL}">{EMAIL}</a>
        </div>
        <div class="contact-card">
          <span class="mono">Phone</span>
          <a href="tel:{PHONE_E164.replace('-', '').replace('+', '+')}">{PHONE_DISPLAY}</a>
        </div>
      </div>
    </div>
  </section>"""


def footer():
    return f"""  <footer class="site-footer">
    <div class="container">
      <div class="footer-mark">
        <img src="/logo.png" alt="">
        <span>Liquid Sun Creative · Brighton, CO</span>
      </div>
      <nav aria-label="Footer" class="footer-nav">
        <a href="/services/">Services</a>
        <a href="/areas-served/">Areas Served</a>
        <a href="/blog/">Newsletter</a>
        <a href="https://gissentanna.com/matthew/">Portfolio</a>
      </nav>
      <p class="legal">© 2026 Liquid Sun Creative</p>
    </div>
  </footer>"""


def head(title, description, canonical, extra_jsonld=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(description)}">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" href="/logo.png" type="image/png">
  <meta name="theme-color" content="#1B1714">

  <meta property="og:type" content="website">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(description)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="Liquid Sun Creative">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{e(title)}">
  <meta name="twitter:description" content="{e(description)}">
{extra_jsonld}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alata&family=IBM+Plex+Mono:wght@400;500&display=swap">
  <link rel="stylesheet" href="/lsc.css">
</head>
<body>
"""


def jsonld(block):
    import json
    return '  <script type="application/ld+json">\n  ' + json.dumps(block, indent=2).replace("\n", "\n  ") + "\n  </script>\n"


# --- City page -------------------------------------------------------------
def city_faq(c):
    name = c["name"]
    qa = [
        (f"Do you fly drone missions in {name}, Colorado?",
         f"Yes. Liquid Sun Creative is an FAA Part 107 certified operator based in Brighton, and {name} is within our regular {c['county']} service area. We handle the airspace authorizations (including LAANC where required) before any flight."),
        (f"What does drone work in {name} cost?",
         "Most projects are scoped to a flat package based on site size, the deliverable, and whether you need a one-time capture or recurring flights. Send us the details and we'll return a clear quote — typically within one business day."),
        (f"How fast can you get on site in {name}?",
         (f"{name} is our home base, so we can usually schedule flights the same week — weather and airspace permitting."
          if c.get("hq") else
          f"Because we operate out of nearby Brighton, we can usually schedule {name} flights the same week, weather and airspace permitting.")),
    ]
    items = "\n".join(
        f"""        <details>
          <summary>{e(q)}</summary>
          <p>{e(a)}</p>
        </details>""" for q, a in qa)
    return qa, items


def build_city(c):
    name = c["name"]
    full = f"{name}, CO"
    canonical = f"{SITE}/areas-served/{c['slug']}/"
    title = f"Drone Services in {full} | Aerial Mapping & Video — Liquid Sun Creative"
    based = "Based in Brighton" if c.get("hq") else "Based in nearby Brighton"
    desc = (f"FAA Part 107 drone services in {name}, Colorado — aerial mapping, "
            f"construction progress monitoring, asset inspection, and cinematic video marketing. "
            f"{based}, CO. Call {PHONE_DISPLAY}.")

    qa, faq_items = city_faq(c)

    # Schema: LocalBusiness/ProfessionalService scoped to this city + Breadcrumb + FAQ
    ld_service = {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "@id": f"{canonical}#service",
        "name": f"Liquid Sun Creative — Drone Services in {name}",
        "url": canonical,
        "image": f"{SITE}/logo.png",
        "description": desc,
        "telephone": PHONE_E164,
        "email": f"mailto:{EMAIL}",
        "priceRange": "$$",
        "address": {"@type": "PostalAddress", "addressLocality": "Brighton", "addressRegion": "CO", "addressCountry": "US"},
        "areaServed": {"@type": "City", "name": name,
                       "containedInPlace": {"@type": "State", "name": "Colorado"}},
        "geo": {"@type": "GeoCoordinates", "latitude": c["lat"], "longitude": c["lng"]},
        "knowsAbout": ["Drone services", "Aerial photogrammetry", "Orthomosaic mapping",
                       "Construction progress monitoring", "Asset inspection", "Video marketing"],
        "founder": {"@type": "Person", "name": "Matthew Gissentanna",
                    "url": "https://gissentanna.com/matthew/",
                    "jobTitle": "Geospatial Analyst & UAS Pilot",
                    "hasCredential": "FAA Part 107 Remote Pilot"},
    }
    ld_crumb = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Areas Served", "item": f"{SITE}/areas-served/"},
            {"@type": "ListItem", "position": 3, "name": full, "item": canonical},
        ],
    }
    ld_faq = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa],
    }
    extra = jsonld(ld_service) + jsonld(ld_crumb) + jsonld(ld_faq)

    intro_html = "\n".join(f"        <p>{e(p)}</p>" for p in c["intro"])

    services_html = "\n".join(f"""        <article class="service">
          <h3>{e(s['title'])}</h3>
          <p class="tagline">{e(s['tagline'])}</p>
          <p>{e(s['body'])}</p>
          <ul>
{chr(10).join(f"            <li>{e(p)}</li>" for p in s['points'])}
          </ul>
        </article>""" for s in SERVICES)

    # nearby chips: every other city
    chips = "\n".join(
        f'        <a class="chip" href="/areas-served/{o["slug"]}/">{e(o["name"])}</a>'
        for o in CITIES if o["slug"] != c["slug"])

    hq_note = ""
    if c.get("hq"):
        hq_note = ' This is our home base.'

    body = f"""{header('areas')}

  <section class="page-hero" aria-label="Intro">
    <div class="container">
      <p class="crumbs mono"><a href="/">Home</a> / <a href="/areas-served/">Areas Served</a> / {e(full)}</p>
      <p class="mono eyebrow">Drone services · {e(c['county'])}</p>
      <h1>Drone Services in <em>{e(full)}</em></h1>
      <p class="lede">FAA Part 107 aerial mapping, construction monitoring, asset inspection, and cinematic video — for clients in {e(name)} and across the north Denver metro.{hq_note}</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="#contact">Start a Project</a>
        <a class="btn btn-ghost" href="tel:{PHONE_E164.replace('-', '')}">Call {PHONE_DISPLAY}</a>
      </div>
    </div>
  </section>

  <section class="band" aria-labelledby="intro-heading">
    <div class="container">
      <div class="section-head">
        <p class="mono eyebrow">Local drone services</p>
        <h2 id="intro-heading">Aerial imaging for {e(name)}, Colorado</h2>
      </div>
      <div class="prose">
{intro_html}
        <p>In {e(name)}, the work we're asked for most often is {e(c['focus'])}. Whatever the brief, every project is flown by a Part 107 certified pilot, fully insured for commercial operations.</p>
      </div>
    </div>
  </section>

  <section class="band" aria-labelledby="svc-heading">
    <div class="container">
      <div class="section-head">
        <p class="mono eyebrow">What we do here</p>
        <h2 id="svc-heading">Services available in {e(name)}</h2>
        <p>Three lines of work, one operator — see the <a href="/services/">full services page</a> for details.</p>
      </div>
      <div class="service-grid">
{services_html}
      </div>
    </div>
  </section>

  <section class="band" aria-labelledby="faq-heading">
    <div class="container">
      <div class="section-head">
        <p class="mono eyebrow">FAQ</p>
        <h2 id="faq-heading">{e(name)} drone services — common questions</h2>
      </div>
      <div class="faq">
{faq_items}
      </div>
    </div>
  </section>

  <section class="band" aria-labelledby="nearby-heading">
    <div class="container">
      <div class="section-head">
        <p class="mono eyebrow">Nearby</p>
        <h2 id="nearby-heading">Other areas we serve</h2>
        <p>We cover the full north and central Denver metro from our Brighton studio.</p>
      </div>
      <div class="chip-row">
{chips}
      </div>
    </div>
  </section>

{contact_band()}

{footer()}
</body>
</html>
"""
    return head(title, desc, canonical, extra) + body


# --- Areas hub -------------------------------------------------------------
def build_hub():
    canonical = f"{SITE}/areas-served/"
    title = "Areas We Serve | Denver Metro Drone Services — Liquid Sun Creative"
    desc = ("Liquid Sun Creative provides FAA Part 107 drone mapping, inspection, and video "
            "marketing across the Denver metro — Brighton, Thornton, Northglenn, Commerce City, "
            "Aurora, Denver, Lakewood, Wheat Ridge, Westminster, Arvada, Broomfield, and Henderson, CO.")

    ld_crumb = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Areas Served", "item": canonical},
        ],
    }
    ld_service = {
        "@context": "https://schema.org", "@type": "ProfessionalService",
        "@id": f"{SITE}/#service", "name": "Liquid Sun Creative", "url": SITE + "/",
        "telephone": PHONE_E164, "email": f"mailto:{EMAIL}",
        "address": {"@type": "PostalAddress", "addressLocality": "Brighton", "addressRegion": "CO", "addressCountry": "US"},
        "areaServed": [{"@type": "City", "name": c["name"],
                        "containedInPlace": {"@type": "State", "name": "Colorado"}} for c in CITIES],
    }
    extra = jsonld(ld_service) + jsonld(ld_crumb)

    cards = "\n".join(f"""        <a class="area-card" href="/areas-served/{c['slug']}/">
          <span class="city">{e(c['name'])}, CO</span>
          <span class="county">{e(c['county'])}</span>
          <span class="go">Drone services →</span>
        </a>""" for c in CITIES)

    body = f"""{header('areas')}

  <section class="page-hero" aria-label="Intro">
    <div class="container">
      <p class="crumbs mono"><a href="/">Home</a> / Areas Served</p>
      <p class="mono eyebrow">Service area</p>
      <h1>Drone Services Across the <em>Denver Metro</em></h1>
      <p class="lede">Based in Brighton, Liquid Sun Creative flies FAA Part 107 aerial mapping, inspection, and video projects throughout the north and central Front Range. Pick your city for local details.</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="#contact">Start a Project</a>
        <a class="btn btn-ghost" href="/services/">See Services</a>
      </div>
    </div>
  </section>

  <section class="band" aria-labelledby="areas-heading">
    <div class="container">
      <div class="section-head">
        <p class="mono eyebrow">Cities we serve</p>
        <h2 id="areas-heading">Local drone services, city by city</h2>
        <p>Don't see your town? We travel — and we work nationwide for the right project. <a href="/#contact">Just ask.</a></p>
      </div>
      <div class="area-grid">
{cards}
      </div>
    </div>
  </section>

{contact_band()}

{footer()}
</body>
</html>
"""
    return head(title, desc, canonical, extra) + body


# --- Services page ---------------------------------------------------------
def build_services():
    canonical = f"{SITE}/services/"
    title = "Drone Services | Aerial Mapping, Inspection & Video Marketing — Liquid Sun Creative"
    desc = ("FAA Part 107 drone services in the Denver metro: construction progress monitoring, "
            "aerial mapping and orthomosaics, asset and rooftop inspection, and cinematic video "
            "marketing. Based in Brighton, CO.")

    ld_crumb = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Services", "item": canonical},
        ],
    }
    ld_services = {
        "@context": "https://schema.org", "@type": "ProfessionalService",
        "@id": f"{SITE}/#service", "name": "Liquid Sun Creative", "url": SITE + "/",
        "telephone": PHONE_E164, "email": f"mailto:{EMAIL}",
        "address": {"@type": "PostalAddress", "addressLocality": "Brighton", "addressRegion": "CO", "addressCountry": "US"},
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "Drone & video services",
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["title"], "description": s["body"]}} for s in SERVICES],
        },
    }
    extra = jsonld(ld_services) + jsonld(ld_crumb)

    services_html = "\n".join(f"""        <article class="service">
          <h3>{e(s['title'])}</h3>
          <p class="tagline">{e(s['tagline'])}</p>
          <p>{e(s['body'])}</p>
          <ul>
{chr(10).join(f"            <li>{e(p)}</li>" for p in s['points'])}
          </ul>
        </article>""" for s in SERVICES)

    body = f"""{header('services')}

  <section class="page-hero" aria-label="Intro">
    <div class="container">
      <p class="crumbs mono"><a href="/">Home</a> / Services</p>
      <p class="mono eyebrow">Services</p>
      <h1>Drone Mapping, Inspection &amp; <em>Video Marketing</em></h1>
      <p class="lede">Three lines of work, one operator — built for clients who need precision in the data and craft in the story. FAA Part 107 certified and fully insured, based in Brighton, Colorado.</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="#contact">Start a Project</a>
        <a class="btn btn-ghost" href="/areas-served/">Areas We Serve</a>
      </div>
    </div>
  </section>

  <section class="band" aria-labelledby="svc-heading">
    <div class="container">
      <div class="section-head">
        <p class="mono eyebrow">What we do</p>
        <h2 id="svc-heading">Services</h2>
        <p>Each engagement is scoped to a clear deliverable, with airspace compliance, weather planning, and production logistics handled for you.</p>
      </div>
      <div class="service-grid">
{services_html}
      </div>
    </div>
  </section>

  <section class="band" aria-labelledby="proc-heading">
    <div class="container">
      <div class="section-head">
        <p class="mono eyebrow">How we work</p>
        <h2 id="proc-heading">Three steps from idea to deliverable.</h2>
      </div>
      <div class="service-grid">
        <div class="service"><h3>01 · You share the mission</h3><p>Tell us what you need, when you need it, and what success looks like. We translate goals into a scoped project with clear outcomes.</p></div>
        <div class="service"><h3>02 · We execute the plan</h3><p>Airspace checks, shot planning, compliance, weather reviews, production logistics — handled. Flights and filming run with operational discipline.</p></div>
        <div class="service"><h3>03 · You get the goods</h3><p>Curated media, edited and formatted, organized for immediate use — for client presentations, marketing, or site documentation.</p></div>
      </div>
    </div>
  </section>

  <section class="band" aria-labelledby="where-heading">
    <div class="container">
      <div class="section-head">
        <p class="mono eyebrow">Where we work</p>
        <h2 id="where-heading">Serving the Denver metro</h2>
        <p>From our Brighton studio we cover Brighton, Thornton, Northglenn, Commerce City, Aurora, Denver, Lakewood, Wheat Ridge, Westminster, Arvada, Broomfield, and Henderson — and travel nationwide for the right project.</p>
      </div>
      <div class="chip-row">
{chr(10).join(f'        <a class="chip" href="/areas-served/{c["slug"]}/">{e(c["name"])}</a>' for c in CITIES)}
      </div>
    </div>
  </section>

{contact_band()}

{footer()}
</body>
</html>
"""
    return head(title, desc, canonical, extra) + body


# --- Write -----------------------------------------------------------------
def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)
    print("wrote", path)


def main():
    write("services/index.html", build_services())
    write("areas-served/index.html", build_hub())
    for c in CITIES:
        write(f"areas-served/{c['slug']}/index.html", build_city(c))


if __name__ == "__main__":
    main()
