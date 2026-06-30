# -*- coding: utf-8 -*-
import os

BASE = os.path.dirname(os.path.abspath(__file__))
LOGO = 'images/logo.png'
LOGO_HEADER = 'images/logo-trans.png'
WHATSAPP_UK = '447304150461'
PHONE_UK = '+44 7304 150 461'
PHONE_UK_TEL = '+447304150461'
PHONE_ISB = '+92 51 260 4334'
PHONE_ISB_TEL = '+92512604334'
PHONE_HYD = '+92 222 657 214'
PHONE_HYD_TEL = '+92222657214'

def write(name, content):
    path = os.path.join(BASE, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('wrote', name)

def head(title, desc, keywords='', transparent=False, prefix='', home=False):
    canon = prefix + ('index.html' if not prefix else '')
    home_css = f'<link rel="stylesheet" href="{prefix}css/home.css">\n' if home else ''
    body_home = ' page-home' if home else ''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<meta name="robots" content="index, follow">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="{prefix}{LOGO}">
<link rel="icon" type="image/png" href="{prefix}{LOGO}">
<link rel="apple-touch-icon" href="{prefix}{LOGO}">
<meta name="theme-color" content="#1a1f26">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Encode+Sans+Expanded:wght@500;600;700&family=Encode+Sans+Semi+Expanded:wght@500;600;700&display=swap">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/assets/owl.carousel.min.css">
<link rel="stylesheet" href="{prefix}css/style.css">
{home_css}</head>
<body class="site_layout_lisbon header_style_5{body_home} {'header_transparent header_inverse' if transparent else 'header_solid header_inverse'} sticky_menu">'''

def header(active, prefix=''):
    home = prefix + 'index.html'
    items = [
        ('home','Home',home),('about','About Us',prefix+'about.html'),
        ('services','Services',prefix+'services.html'),('sectors','Sectors',prefix+'sectors.html'),
        ('where','Where We Work',prefix+'where-we-work.html'),('clients','Clients',prefix+'clients.html'),
        ('careers','Careers',prefix+'careers.html'),('publications','Publications &amp; Insights',prefix+'publications.html'),
        ('contact','Contact',prefix+'contact.html'),
    ]
    nav = ''.join(f'<li class="menu-item{" current-menu-item" if active==k else ""}"><a href="{h}">{l}</a></li>' for k,l,h in items)
    return f'''<header id="header">
<div class="header-box"><div class="container">
<div class="header-top-row">
<div class="logo-box"><div class="logo logo-desktop"><a href="{home}"><img src="{prefix}{LOGO_HEADER}" alt="PRD Consultants (Pvt.) Ltd" class="site-logo"></a></div></div>
<div class="header-phones hide_on_mobile">
<a href="tel:{PHONE_UK_TEL}" class="header-phone"><span class="header-phone__label">UK</span><span class="header-phone__num">{PHONE_UK}</span></a>
<a href="tel:{PHONE_ISB_TEL}" class="header-phone"><span class="header-phone__label">Islamabad</span><span class="header-phone__num">{PHONE_ISB}</span></a>
<a href="tel:{PHONE_HYD_TEL}" class="header-phone"><span class="header-phone__label">Sindh</span><span class="header-phone__num">{PHONE_HYD}</span></a>
</div>
<button type="button" class="menu-toggle" aria-label="Menu"><span></span></button>
</div>
</div></div>
<div class="nav-box"><div class="container"><ul class="main_menu_nav">{nav}</ul></div></div>
</header>
<div id="header-spacer" aria-hidden="true"></div>'''

def page_hero(title, sub='', bc='', bg='images/hero-page.jpg'):
    return f'''<section class="page-hero" style="background-image:url('{bg}')"><div class="container">
<nav class="breadcrumb-nav"><a href="index.html">Home</a><span>/</span><span>{bc or title}</span></nav>
<h1>{title}</h1>{f"<p>{sub}</p>" if sub else ""}</div></section>'''

def footer(prefix=''):
    return f'''<footer id="contact"><div class="container">
<div class="footer-top row">
<div class="col-md-4 footer-brand"><img src="{prefix}{LOGO}" alt="PRD Consultants" class="footer-logo" width="180" height="48">
<p>Delivering evidence-based solutions for sustainable development, institutional strengthening, and lasting impact.</p></div>
<div class="col-md-8"><div class="footer-offices">
<div class="office-col"><div class="title">United Kingdom</div><ul>
<li><span class="icon"><span class="stm-location-2"></span></span><span>86 Wind Road, Ystradgynlais, Swansea, Wales, United Kingdom</span></li>
<li><span class="icon"><span class="stm-iphone"></span></span><span>+44 7304 150 461</span></li>
<li><span class="icon"><span class="stm-email"></span></span><span><a href="mailto:info.UK@prdconsultantsltd.com">info.UK@prdconsultantsltd.com</a></span></li></ul></div>
<div class="office-col"><div class="title">Pakistan – Islamabad</div><ul>
<li><span class="icon"><span class="stm-location-2"></span></span><span>Office No. 1, Mezzanine Floor, 25-Huma Plaza, Fazal-e-Haq Road, Blue Area, Islamabad, Pakistan</span></li>
<li><span class="icon"><span class="stm-iphone"></span></span><span>+92 51 260 4334</span></li>
<li><span class="icon"><span class="stm-email"></span></span><span><a href="mailto:info.ISB@prdconsultantsltd.com">info.ISB@prdconsultantsltd.com</a></span></li></ul></div>
<div class="office-col"><div class="title">Pakistan – Sindh</div><ul>
<li><span class="icon"><span class="stm-location-2"></span></span><span>House No. A28 &amp; 29, Bakhtawar Colony, Opposite Abdullah Sports City, Qasimabad, Hyderabad, Pakistan</span></li>
<li><span class="icon"><span class="stm-iphone"></span></span><span>+92 222 657 214</span></li>
<li><span class="icon"><span class="stm-email"></span></span><span><a href="mailto:info.HYD@prdconsultantsltd.com">info.HYD@prdconsultantsltd.com</a></span></li></ul></div>
</div></div></div>
<div class="copyright-row">
<p class="copyright-text">© 2026 PRD Consultants (Private) Limited. All rights reserved.</p>
<p class="footer-powered">Powered by <a href="https://xcltechnologies.com/" target="_blank" rel="noopener noreferrer">XCl Technologies</a></p>
</div>
</div></footer>'''

def map_section():
    return '''<section id="locations-map" class="map-section">
<div class="container">
<div class="section-header text-center reveal">
<span class="section-eyebrow">Global Presence</span>
<h2 class="section-title">Our Office Locations<span class="subtitle">United Kingdom Head Office and Pakistan Country &amp; Regional Operations</span></h2>
</div>
<div class="map-tabs reveal">
<button type="button" class="map-tab active" data-map="uk"><i class="fa fa-map-marker"></i> United Kingdom</button>
<button type="button" class="map-tab" data-map="isb"><i class="fa fa-map-marker"></i> Islamabad</button>
<button type="button" class="map-tab" data-map="hyd"><i class="fa fa-map-marker"></i> Hyderabad, Sindh</button>
</div>
<div class="map-frame reveal">
<iframe id="office-map" title="PRD Consultants Office Location" src="https://www.google.com/maps?q=86+Wind+Road,Ystradgynlais,Swansea,Wales,UK&amp;hl=en&amp;z=14&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
</div>
<div class="map-cards row reveal">
<div class="col-md-4"><div class="map-card">
<h4>Head Office – United Kingdom</h4>
<p class="role">International Operations &amp; Partnerships</p>
<p>86 Wind Road, Ystradgynlais, Swansea, Wales, United Kingdom</p>
<p><strong>Phone:</strong> +44 7304 150 461</p>
<p><strong>Email:</strong> <a href="mailto:info.UK@prdconsultantsltd.com">info.UK@prdconsultantsltd.com</a></p>
</div></div>
<div class="col-md-4"><div class="map-card">
<h4>Country Office – Pakistan</h4>
<p class="role">Programme Delivery &amp; Technical Support</p>
<p>Office No. 1, Mezzanine Floor, 25-Huma Plaza, Fazal-e-Haq Road, Blue Area, Islamabad, Pakistan</p>
<p><strong>Phone:</strong> +92 51 260 4334</p>
<p><strong>Email:</strong> <a href="mailto:info.ISB@prdconsultantsltd.com">info.ISB@prdconsultantsltd.com</a></p>
</div></div>
<div class="col-md-4"><div class="map-card">
<h4>Regional Office – Sindh</h4>
<p class="role">Field Operations &amp; Provincial Engagement</p>
<p>House No. A28 &amp; 29, Bakhtawar Colony, Opposite Abdullah Sports City, Qasimabad, Hyderabad, Pakistan</p>
<p><strong>Phone:</strong> +92 222 657 214</p>
<p><strong>Email:</strong> <a href="mailto:info.HYD@prdconsultantsltd.com">info.HYD@prdconsultantsltd.com</a></p>
</div></div>
</div>
</div></section>'''

def whatsapp_float():
    return f'''<a href="https://wa.me/{WHATSAPP_UK}?text=Hello%20PRD%20Consultants%2C%20I%20would%20like%20to%20inquire%20about%20your%20services." class="whatsapp-float" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp" title="WhatsApp {PHONE_UK}">
<span class="whatsapp-float__icon"><i class="fa fa-whatsapp"></i></span>
<span class="whatsapp-float__pulse"></span>
</a>'''

def page_end(prefix=''):
    return map_section() + footer(prefix) + whatsapp_float() + '</div>' + scripts(prefix)

def scripts(prefix=''):
    return f'''<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/owl.carousel.min.js"></script>
<script src="{prefix}js/main.js"></script></body></html>'''

CLIENTS = [
    ('image4.png','United Nations'),('image11.png','USAID'),('image16.png','UK Aid'),
    ('image6.png','IOM UN Migration'),('image12.jpeg','European Union'),('image13.png','Save the Children'),
    ('image8.png','Government of Sindh'),('image9.jpeg','Agriculture Department Sindh'),
    ('image10.png','Sindh Agricultural Growth Project'),('image7.png','ICT Agricultural Extension Services'),
    ('image5.jpg','Development Partner'),
]

def clients_grid():
    return '<div class="clients-logo-grid">' + ''.join(
        f'<div class="client-logo-item"><img src="images/{i}" alt="{a}" title="{a}"></div>' for i,a in CLIENTS) + '</div>'

def cta(text, href):
    return f'<div class="section-cta text-center"><a href="{href}" class="btn-outline">{text} <i class="fa fa-arrow-right"></i></a></div>'

SECTOR_CARDS = [
    ('agriculture.jpg', 'agriculture', 'Agriculture', 'Agriculture & Rural Development',
     'Rural livelihoods, agricultural development, food systems, and community resilience.'),
    ('food-security.jpg', 'agriculture', 'Livelihoods', 'Food Security & Livelihoods',
     'Household resilience, economic opportunities, and sustainable livelihoods.'),
    ('water.jpg', 'agriculture', 'Water', 'Water Resources Management',
     'Water access, resource management, and community-based solutions.'),
    ('health.jpg', 'health', 'Health', 'Health & Nutrition',
     'Public health initiatives, awareness programmes, and nutrition interventions.'),
    ('education.jpg', 'governance', 'Education', 'Education',
     'Education programmes, institutional strengthening, and learning improvement.'),
    ('governance.jpg', 'governance', 'Governance', 'Governance & Public Sector Development',
     'Institutional strengthening, governance improvement, and public sector initiatives.'),
    ('climate.jpg', 'climate', 'Climate', 'Climate Resilience & Disaster Risk Reduction',
     'Climate adaptation, resilience building, emergency preparedness, and recovery.'),
    ('social-protection.jpg', 'governance', 'Social', 'Social Protection & Community Development',
     'Inclusive development that strengthens vulnerable communities and social outcomes.'),
]

def sectors_grid(with_filter=False):
    items = []
    for img, group, cat, title, desc in SECTOR_CARDS:
        data_attr = f' data-cat="{group}"' if with_filter else ''
        alt = title.replace('&', '&amp;')
        cat_html = cat.replace('&', '&amp;')
        title_html = title.replace('&', '&amp;')
        desc_html = desc.replace('&', '&amp;')
        items.append(
            f'<div class="case-item"{data_attr}><div class="case-card">'
            f'<img src="images/sectors/{img}" alt="{alt}">'
            f'<div class="case-overlay"><span class="cat">{cat_html}</span><h5>{title_html}</h5>'
            f'<p>{desc_html}</p></div>'
            f'</div></div>'
        )
    return '<div class="cases-grid">' + ''.join(items) + '</div>'

def sectors_carousel():
    items = []
    for img, group, cat, title, desc in SECTOR_CARDS:
        alt = title.replace('&', '&amp;')
        cat_html = cat.replace('&', '&amp;')
        title_html = title.replace('&', '&amp;')
        desc_html = desc.replace('&', '&amp;')
        items.append(
            f'<div class="case-card">'
            f'<img src="images/sectors/{img}" alt="{alt}">'
            f'<div class="case-overlay"><span class="cat">{cat_html}</span><h5>{title_html}</h5>'
            f'<p>{desc_html}</p></div>'
            f'</div>'
        )
    return '<div class="owl-carousel cards-carousel" data-items="4">' + ''.join(items) + '</div>'

VALUES = [
    ('Integrity', 'We uphold the highest standards of ethics, professionalism, transparency, and accountability in all our engagements.'),
    ('Excellence', 'We are committed to delivering high-quality services, technical excellence, and results that create meaningful value for our clients and partners.'),
    ('Innovation', 'We embrace creativity, learning, technology, and evidence-based approaches to address complex development challenges.'),
    ('Collaboration', 'We believe in meaningful partnerships, stakeholder engagement, and collective action to achieve sustainable impact.'),
    ('Inclusiveness', 'We promote equitable participation, diversity, and people-centered approaches that ensure development benefits reach all communities.'),
    ('Accountability', 'We take responsibility for our commitments, performance, and the quality, integrity, and effectiveness of our work.'),
    ('Sustainability', 'We support solutions that generate lasting social, economic, environmental, and institutional benefits.'),
]

def values_grid():
    cards = ''.join(
        f'<div class="value-card"><h4>{t}</h4><p>{d}</p></div>' for t, d in VALUES)
    return f'''<div class="values-light-grid values-grid-7">{cards}</div>'''

VALUE_ICONS = {
    'Integrity': 'fa-shield', 'Excellence': 'fa-trophy', 'Innovation': 'fa-lightbulb-o',
    'Collaboration': 'fa-handshake-o', 'Inclusiveness': 'fa-users',
    'Accountability': 'fa-check-square-o', 'Sustainability': 'fa-leaf',
}

def values_carousel():
    cards = ''.join(
        f'<div class="value-card value-card-slide"><div class="vc-icon"><i class="fa {VALUE_ICONS.get(t, "fa-star")}"></i></div><h4>{t}</h4><p>{d}</p></div>'
        for t, d in VALUES)
    return f'<div class="owl-carousel cards-carousel values-carousel-slider" data-items="3">{cards}</div>'

# ─── INDEX ───
index = head(
    'PRD Consultants | Development Consulting, Research & Technical Assistance',
    'PRD Consultants is an international development consulting firm in the UK and Pakistan. Consulting, research, MEAL, technical assistance and project management.',
    'PRD Consultants, development consulting, Pakistan, UK, MEAL, research',
    transparent=True,
    home=True
) + '<div id="wrapper">' + header('home') + '''
<section id="hero">
<div class="hero-slide active" style="background-image:url('https://consulting.stylemixthemes.com/lisbon/wp-content/uploads/sites/38/revslider/highlight-carousel7/lisbon.jpg')">
<div class="container"><div class="hero-caption">
<div class="eyebrow">Welcome to</div>
<h1>PRD Consultants (Private) Limited</h1>
<p>Development Consulting | Research | Technical Assistance | Project Management | Monitoring, Evaluation, Accountability &amp; Learning (MEAL)</p>
<div class="hero-btns"><a class="btn-green" href="services.html">Our Services</a><a class="btn-dark" href="contact.html">Contact Us</a></div>
</div></div></div>
<div class="hero-slide" style="background-image:url('https://consulting.stylemixthemes.com/lisbon/wp-content/uploads/sites/38/revslider/highlight-carousel7/slide_2.jpg')">
<div class="container"><div class="hero-caption center">
<div class="eyebrow">The Organization</div>
<h1>Delivering Evidence-Based Solutions for Sustainable Development</h1>
<p>Institutional Strengthening, and Lasting Impact.</p>
<div class="hero-btns center"><a class="btn-green" href="about.html">About Us</a><a class="btn-dark" href="contact.html">Contact Us</a></div>
</div></div></div>
<div class="hero-slide" style="background-image:url('https://consulting.stylemixthemes.com/lisbon/wp-content/uploads/sites/38/revslider/highlight-carousel7/slide_3.jpg')">
<div class="container"><div class="hero-caption right">
<div class="eyebrow">About Us</div>
<h1>From Development Practice to Development Consulting</h1>
<p>PRD Consultants was established on a simple belief: effective development solutions are built on experience, evidence, innovation, and strong partnerships.</p>
<div class="hero-btns right"><a class="btn-green" href="sectors.html">Our Sectors</a><a class="btn-dark" href="clients.html">Our Clients</a></div>
</div></div></div>
<div class="hero-bullets"><span class="selected" data-index="0"></span><span data-index="1"></span><span data-index="2"></span></div>
</section>

<main id="main-content">

<section id="ceo-message" class="ceo-section reveal"><div class="container">
<div class="section-header text-center"><span class="section-eyebrow">Who We Are</span><h2 class="section-title">Welcome to PRD Consultants</h2></div>
<div class="ceo-pro-wrap">
<aside class="ceo-pro-aside">
<div class="ceo-pro-photo"><img src="images/image2.jpeg" alt="Aftab A. Solangi, Chief Executive Officer"></div>
<div class="ceo-pro-id"><h4>Aftab A. Solangi</h4><p>Chief Executive Officer</p></div>
</aside>
<div class="ceo-pro-body">
<i class="fa fa-quote-left ceo-quote-mark"></i>
<p>Welcome to PRD Consultants (Private) Limited. As development challenges continue to evolve, organizations need trusted partners who can combine technical expertise with practical implementation experience. We bring together global perspectives, local knowledge, and evidence-based approaches to help governments, development partners, international organizations, NGOs, and private sector institutions achieve sustainable and measurable results.</p>
<p>Our strength lies in understanding both the strategic and operational dimensions of development, enabling us to deliver solutions that are practical, innovative, and responsive to real-world challenges.</p>
<p>We are committed to professionalism, integrity, partnership, and continuous learning, and we look forward to working with our clients and partners to strengthen institutions, improve programme performance, and contribute to sustainable development outcomes.</p>
</div>
</div></div></section>

<section id="org-intro" class="org-intro section-sm reveal"><div class="container">
<div class="row"><div class="col-md-10 col-md-offset-1 text-center">
<span class="section-eyebrow">The Organization</span>
<h2 class="section-title">PRD Consultants (Private) Limited</h2>
<p class="org-lead">PRD Consultants is an international development consulting and advisory firm operating through registered entities in the United Kingdom and Pakistan. PRD Consultants Ltd is registered with Companies House under the laws of England and Wales, while PRD Consultants (Private) Limited is incorporated under the corporate laws of Pakistan and registered with the Securities and Exchange Commission of Pakistan (SECP), currently governed by the Companies Act, 2017.</p>
<p class="org-lead">Building on more than a decade of development and humanitarian experience through Partners for Research and Development (PRD), PRD Consultants combines practical field knowledge with professional consulting expertise to support governments, development partners, donor-funded programmes, international organizations, NGOs, research institutions, and private sector organizations.</p>
<p class="org-lead">Supported by a multidisciplinary network of national and international experts, the firm delivers evidence-based, innovative, and context-sensitive solutions that help organizations strengthen institutions, improve programme performance, enhance accountability, and achieve sustainable development outcomes.</p>
<p class="org-tagline"><strong>Delivering Evidence-Based Solutions for Sustainable Development, Institutional Strengthening, and Lasting Impact.</strong></p>
</div></div></div></section>

<section id="what-we-do" class="section section-alt reveal"><div class="container">
<div class="section-header text-center"><span class="section-eyebrow">Our Expertise</span><h2 class="section-title">What we do</h2></div>
<div class="icon-box-grid">
<div class="icon-box-col"><div class="icon-box"><div class="ib-icon"><i class="fa fa-line-chart"></i></div><h4>Development Consulting</h4><p>Strategic advisory services that strengthen institutions and improve programme performance.</p></div></div>
<div class="icon-box-col"><div class="icon-box"><div class="ib-icon"><i class="fa fa-search"></i></div><h4>Research &amp; Assessments</h4><p>Surveys, baseline studies, needs assessments, and evidence-based reporting.</p></div></div>
<div class="icon-box-col"><div class="icon-box"><div class="ib-icon"><i class="fa fa-cogs"></i></div><h4>Technical Assistance</h4><p>Institutional strengthening, capacity building, and operational support.</p></div></div>
<div class="icon-box-col"><div class="icon-box"><div class="ib-icon"><i class="fa fa-tasks"></i></div><h4>Project Management &amp; MEAL</h4><p>End-to-end delivery with monitoring, evaluation, accountability and learning.</p></div></div>
</div>''' + cta('Explore All Services', 'services.html') + '</div></section>\n'

index += '''<section id="values" class="values-section reveal"><div class="container">
<div class="section-header text-center"><span class="section-eyebrow">What We Stand For</span><h2 class="section-title">Our Values</h2></div>
''' + values_carousel() + '''</div></section>

<section id="services" class="section services-section reveal"><div class="container">
<div class="section-header text-center"><span class="section-eyebrow">What We Offer</span><h2 class="section-title">Our Services</h2></div>
<div class="owl-carousel services-carousel">
<div class="service-item"><div class="s-icon"><i class="fa fa-briefcase"></i></div><h5>Consulting</h5></div>
<div class="service-item"><div class="s-icon"><i class="fa fa-bar-chart"></i></div><h5>Research</h5></div>
<div class="service-item"><div class="s-icon"><i class="fa fa-wrench"></i></div><h5>Technical Assistance</h5></div>
<div class="service-item"><div class="s-icon"><i class="fa fa-calendar-check-o"></i></div><h5>Project Management</h5></div>
<div class="service-item"><div class="s-icon"><i class="fa fa-pie-chart"></i></div><h5>MEAL</h5></div>
</div>''' + cta('View All Services', 'services.html') + '</div></section>\n'

index += '''<section id="sectors" class="section reveal"><div class="container">
<div class="section-header text-center"><span class="section-eyebrow">Industries</span><h2 class="section-title">Sector Expertise<span class="subtitle">Experience across development sectors</span></h2></div>
''' + sectors_carousel() + cta('Explore All Sectors', 'sectors.html') + '''</div></section>

<section id="experience" class="experience-section reveal"><div class="container">
<h2>Experience Built Through Practice, Partnership, and Impact</h2>
<div class="exp-stats">
<div class="exp-stat"><h3>2010</h3><p>Established<br>through PRD</p></div>
<div class="exp-stat"><h3 class="counter" data-target="8">0<span>+</span></h3><p>Development<br>sectors</p></div>
<div class="exp-stat"><h3 class="counter" data-target="2">0</h3><p>Countries<br>UK &amp; Pakistan</p></div>
<div class="exp-stat"><h3 class="counter" data-target="5">0<span>+</span></h3><p>Provinces<br>covered</p></div>
</div></div></section>

<section id="clients" class="section section-alt reveal"><div class="container">
<div class="section-header text-center"><span class="section-eyebrow">Partnerships</span><h2 class="section-title">Our Clients &amp; Partners</h2></div>
''' + clients_grid() + cta('View All Partners', 'clients.html') + '''</div></section>

<section id="why-choose" class="section section-alt"><div class="container">
<div class="section-header text-center"><span class="section-eyebrow">Why PRD</span><h2 class="section-title">The PRD Difference</h2></div>
<div class="owl-carousel cards-carousel" data-items="3">
<div class="why-card"><div class="w-icon"><i class="fa fa-globe"></i></div><h4>Field Experience</h4><p>Practical understanding gained through direct engagement with communities and development programmes.</p></div>
<div class="why-card"><div class="w-icon"><i class="fa fa-certificate"></i></div><h4>Technical Expertise</h4><p>Professional capabilities in research, evaluation, advisory services, and institutional development.</p></div>
<div class="why-card"><div class="w-icon"><i class="fa fa-handshake-o"></i></div><h4>Partnership Approach</h4><p>A commitment to working collaboratively with clients, stakeholders, and communities.</p></div>
<div class="why-card"><div class="w-icon"><i class="fa fa-bar-chart"></i></div><h4>Evidence-Based Practice</h4><p>A focus on data, learning, accountability, and measurable results.</p></div>
<div class="why-card"><div class="w-icon"><i class="fa fa-map"></i></div><h4>Local Understanding with International Standards</h4><p>Solutions that are context-sensitive while aligned with global development practices.</p></div>
</div></div></section>

<section id="careers" class="section"><div class="container">
<div class="section-header text-center"><h2 class="section-title">Careers</h2></div>
<div class="career-grid">
<div class="career-item"><a href="careers.html#jobs" class="career-card career-card-link"><i class="fa fa-briefcase"></i><h4>Jobs</h4></a></div>
<div class="career-item"><a href="careers.html#consultancies" class="career-card career-card-link"><i class="fa fa-user-md"></i><h4>Consultancies</h4></a></div>
<div class="career-item"><a href="careers.html#internships" class="career-card career-card-link"><i class="fa fa-graduation-cap"></i><h4>Internships</h4></a></div>
</div>''' + cta('View Careers', 'careers.html') + '''</div></section>

<section id="where-we-work" class="section reveal"><div class="container">
<div class="section-header text-center"><span class="section-eyebrow">Global Presence</span><h2 class="section-title">Where We Work<span class="subtitle">Experience across all provinces of Pakistan and international operations from the United Kingdom</span></h2></div>
<div class="location-cards">
<div class="location-card"><div class="loc-inner"><h4>United Kingdom</h4><div class="role">Head Office | International Operations &amp; Partnerships</div><p>86 Wind Road, Ystradgynlais, Swansea, Wales, United Kingdom</p><p>+44 7304 150 461 | info.UK@prdconsultantsltd.com</p></div></div>
<div class="location-card"><div class="loc-inner"><h4>Pakistan – Islamabad</h4><div class="role">Country Operations | Programme Delivery</div><p>25-Huma Plaza, Fazal-e-Haq Road, Blue Area, Islamabad</p><p>+92 51 260 4334 | info.ISB@prdconsultantsltd.com</p></div></div>
</div>
<div class="location-cards" style="margin-top:20px"><div class="location-card" style="flex:0 0 100%;max-width:100%"><div class="loc-inner">
<h4>Pakistan – Country Coverage</h4><div class="role">Provincial &amp; Regional Experience</div>
<div class="provinces"><span>Sindh</span><span>Punjab</span><span>Khyber Pakhtunkhwa</span><span>Balochistan</span><span>Islamabad Capital Territory</span></div>
<p style="margin-top:14px"><strong>Regional Office – Sindh:</strong> Bakhtawar Colony, Qasimabad, Hyderabad | +92 222 657 214</p>
</div></div></div>''' + cta('Learn More', 'where-we-work.html') + '''</div></section>

<section id="publications" class="section section-alt"><div class="container">
<div class="section-header text-center"><span class="section-eyebrow">Knowledge &amp; Insights</span><h2 class="section-title">Publications &amp; Insights<span class="subtitle">Stay updated with the latest developments, achievements, and activities of PRD Consultants — including project milestones, publications, partnerships, events, and knowledge-sharing initiatives across the development sector.</span></h2></div>
<ul class="pub-list">
<li><span class="pub-icon"><i class="fa fa-file-text-o"></i></span><div><h5>Onion Research Study Sindh</h5><p>Research &amp; Reports</p></div></li>
<li><span class="pub-icon"><i class="fa fa-file-text-o"></i></span><div><h5>Development of PC-1 for the Sindh Water and Agriculture Transformation Project</h5><p>Agriculture Department, Government of Sindh</p></div></li>
<li><span class="pub-icon"><i class="fa fa-file-text-o"></i></span><div><h5>Revision of PC-1 Sindh Agricultural Growth Project</h5><p>Agriculture Department, Government of Sindh</p></div></li>
<li><span class="pub-icon"><i class="fa fa-file-text-o"></i></span><div><h5>Articles &amp; Thought Leadership</h5><p>Articles &amp; Thought Leadership</p></div></li>
<li><span class="pub-icon"><i class="fa fa-file-text-o"></i></span><div><h5>News &amp; Events</h5><p>News &amp; Events</p></div></li>
</ul>''' + cta('View All Publications', 'publications.html') + '''</div></section>
</main>
'''

index += page_end()
write('index.html', index)

# ─── ABOUT ───
about = head('About Us | PRD Consultants – Our Story, Vision & Leadership',
    'Learn about PRD Consultants – our journey from humanitarian practice to professional development consulting across the UK and Pakistan since 2010.',
    'PRD Consultants about, CEO message, vision mission values, development consulting Pakistan') 
about += '<div id="wrapper">' + header('about') + page_hero('About Us', 'From Development Practice to Development Consulting', bg='images/hero-page.jpg') + '''
<section class="section"><div class="container"><div class="row">
<div class="col-md-7 content-block">
<h2 class="section-title">The Organization</h2>
<p>PRD Consultants is an international development consulting and advisory firm operating through registered entities in the United Kingdom and Pakistan. PRD Consultants Ltd is registered with Companies House under the laws of England and Wales, while PRD Consultants (Private) Limited is incorporated under the corporate laws of Pakistan and registered with the Securities and Exchange Commission of Pakistan (SECP).</p>
<p>Building on more than a decade of development and humanitarian experience through Partners for Research and Development (PRD), PRD Consultants combines practical field knowledge with professional consulting expertise to support governments, development partners, donor-funded programmes, international organizations, NGOs, research institutions, and private sector organizations.</p>
<h3>Our Unique Strength</h3>
<p>What sets PRD Consultants apart is its foundation in real-world development practice combined with an international outlook. Our firm builds upon the experience and legacy of Partners for Research and Development (PRD), which has been engaged in humanitarian assistance, community development, public health, research, training, and social development initiatives since 2010.</p>
<p>During the floods of 2010 and 2011 in Pakistan, PRD worked alongside communities and stakeholders to support relief, recovery, and resilience-building efforts. These experiences strengthened our understanding of programme delivery, community engagement, institutional systems, and evidence-based development practice.</p>
<h3>Who We Serve</h3>
<ul>
<li>Government institutions and public sector organizations</li>
<li>United Nations agencies and international development partners</li>
<li>Bilateral and multilateral donor-funded programmes</li>
<li>National and international non-governmental organizations</li>
<li>Humanitarian and relief agencies</li>
<li>Research institutions and academic organizations</li>
<li>Private sector organizations, social enterprises, and development-focused initiatives</li>
</ul>
<div class="ceo-card">
<img src="images/image2.jpeg" alt="Aftab A. Solangi, CEO">
<div><blockquote>Welcome to PRD Consultants (Private) Limited. As development challenges continue to evolve, organizations need trusted partners who can combine technical expertise with practical implementation experience. At PRD Consultants, we bring together global perspectives, local knowledge, and evidence-based approaches to help governments, development partners, international organizations, NGOs, and private sector institutions achieve sustainable and measurable results.</blockquote>
<div class="author">Aftab A. Solangi</div><div class="role">Chief Executive Officer, PRD Consultants</div></div>
</div>
</div>
<div class="col-md-5">
<img src="images/image15.jpg" alt="Partners for Research and Development" style="margin-bottom:25px;border-radius:4px">
<div class="accordion-panel open"><div class="accordion-head"><h4>Vision</h4><i class="fa fa-chevron-down"></i></div>
<div class="accordion-body"><p>To be a trusted global partner in development, delivering innovative, evidence-based solutions that strengthen institutions, improve lives, and create sustainable impact for communities and organizations.</p></div></div>
<div class="accordion-panel"><div class="accordion-head"><h4>Mission</h4><i class="fa fa-chevron-down"></i></div>
<div class="accordion-body"><p>To provide high-quality consulting, research, technical assistance, project management, monitoring and evaluation, and capacity-building services that enable governments, development partners, and organizations to achieve inclusive, measurable, and sustainable development outcomes.</p></div></div>
<div class="accordion-panel"><div class="accordion-head"><h4>Our Approach</h4><i class="fa fa-chevron-down"></i></div>
<div class="accordion-body"><p>We believe sustainable development is achieved through collaboration, evidence-based decision-making, innovation, and accountability. Our approach combines local knowledge and contextual understanding with international standards and best practices.</p></div></div>
</div></div></div></section>
<section class="section section-alt"><div class="container">
<div class="section-header text-center"><span class="section-eyebrow">Experience &amp; Credentials</span><h2 class="section-title">Experience Built Through Practice, Partnership, and Impact</h2></div>
<div class="content-block">
<p>PRD Consultants brings together years of development practice, humanitarian engagement, and professional consulting expertise to support organizations in designing, implementing, monitoring, and improving development interventions. Our experience is rooted in the legacy of Partners for Research and Development (PRD), engaged in humanitarian assistance, community development, public health, research, training, and social development initiatives since 2010.</p>
<h3>Humanitarian and Community Development Experience</h3>
<p>During the devastating floods of 2010 and 2011 in Sindh, PRD implemented humanitarian response and early recovery initiatives to support affected and vulnerable communities, gaining valuable experience in emergency coordination, community engagement, service delivery, and recovery planning. Key areas of engagement included:</p>
<ul>
<li>Emergency relief assistance for flood-affected communities</li>
<li>Distribution of food and non-food assistance to displaced and vulnerable populations</li>
<li>Support for safe drinking water, basic humanitarian needs, and community services</li>
<li>Community-based health promotion and awareness initiatives</li>
<li>Maternal and child health and nutrition awareness activities</li>
<li>Community mobilization and volunteer-led support mechanisms</li>
<li>Coordination with local institutions, government stakeholders, and humanitarian partners</li>
</ul>
<h3>Research and Evidence Generation</h3>
<p>PRD Consultants supports organizations in generating reliable evidence to inform policies, strategies, programmes, and investment decisions. Our research capabilities include:</p>
<ul>
<li>Socioeconomic and household surveys</li>
<li>Baseline, midline, and endline assessments</li>
<li>Needs assessments and vulnerability analysis</li>
<li>Market and institutional assessments</li>
<li>Feasibility studies and sector research</li>
<li>Quantitative and qualitative data collection and analysis</li>
<li>Evidence-based reporting, knowledge products, and learning documentation</li>
</ul>
<h3>Technical Assistance and Institutional Strengthening</h3>
<p>We support organizations in strengthening their systems, improving programme effectiveness, and enhancing institutional capacity through tailored technical assistance and advisory services, including:</p>
<ul>
<li>Programme design, review, and improvement strategies</li>
<li>Institutional capacity assessments and strengthening initiatives</li>
<li>Strategic planning and operational support</li>
<li>Policy analysis, development, and advisory services</li>
<li>Development of manuals, guidelines, frameworks, and standard operating procedures</li>
<li>Training, knowledge transfer, and organizational development</li>
<li>Capacity building for institutions, teams, and stakeholders</li>
</ul>
</div>
</div></section>
<section id="leadership" class="section"><div class="container">
<div class="section-header text-center"><span class="section-eyebrow">Our Team</span><h2 class="section-title">Leadership &amp; Expert Network</h2></div>
<div class="content-block" style="max-width:900px;margin:0 auto;text-align:center">
<p>PRD Consultants is supported by a multidisciplinary network of national and international experts with extensive experience across diverse development sectors. Our experts bring specialized knowledge and practical experience in areas including agriculture and rural development, livelihoods, governance, health, education, climate resilience, social protection, humanitarian response, monitoring and evaluation, and institutional development.</p>
<p>This diverse expertise enables PRD Consultants to assemble context-specific teams and provide high-quality technical solutions tailored to the needs of each assignment and client.</p>
</div>
<div class="ceo-pro-wrap" style="margin-top:40px">
<aside class="ceo-pro-aside">
<div class="ceo-pro-photo"><img src="images/image2.jpeg" alt="Aftab A. Solangi, Chief Executive Officer"></div>
<div class="ceo-pro-id"><h4>Aftab A. Solangi</h4><p>Chief Executive Officer</p></div>
</aside>
<div class="ceo-pro-body">
<i class="fa fa-quote-left ceo-quote-mark"></i>
<p>Our strength lies in understanding both the strategic and operational dimensions of development, enabling us to deliver solutions that are practical, innovative, and responsive to real-world challenges. We are committed to professionalism, integrity, partnership, and continuous learning.</p>
<p>As PRD Consultants continues to grow, our commitment remains focused on helping organizations transform ideas into action, evidence into informed decisions, and investments into meaningful development outcomes.</p>
</div>
</div>
</div></section>
<section class="values-section section-sm"><div class="container">
<div class="section-header text-center"><h2 class="section-title" style="color:#fff">Our Values</h2></div>
''' + values_grid() + '''
</div></section>''' + page_end()
write('about.html', about)

# ─── SERVICES ───
services = head('Our Services | PRD Consultants – Consulting, Research & MEAL',
    'PRD Consultants offers development consulting, research and assessments, technical assistance, project management, MEAL, and institutional strengthening services.',
    'consulting services, research assessments, technical assistance, MEAL, project management')
services += '<div id="wrapper">' + header('services') + page_hero('Our Services', 'Consulting | Research &amp; Assessments | Technical Assistance | Project Management | MEAL', bg='images/hero-page-2.jpg') + '''
<section class="section"><div class="container">
<div class="service-detail-card"><h3><i class="fa fa-briefcase" style="color:#7bc74d;margin-right:10px"></i> Consulting Services</h3>
<p>Strategic advisory services that help organizations strengthen institutions, improve programme performance, enhance accountability, and achieve sustainable development outcomes.</p></div>
<div class="service-detail-card"><h3><i class="fa fa-bar-chart" style="color:#7bc74d;margin-right:10px"></i> Research &amp; Assessments</h3>
<p>Socioeconomic and household surveys, baseline, midline and endline assessments, needs assessments, vulnerability analysis, market and institutional assessments, feasibility studies, and evidence-based reporting.</p></div>
<div class="service-detail-card"><h3><i class="fa fa-wrench" style="color:#7bc74d;margin-right:10px"></i> Technical Assistance</h3>
<p>Programme design, institutional capacity assessments, strategic planning, policy analysis, development of manuals and SOPs, training, knowledge transfer, and organizational development.</p></div>
<div class="service-detail-card"><h3><i class="fa fa-calendar-check-o" style="color:#7bc74d;margin-right:10px"></i> Project Management</h3>
<p>End-to-end project management support from design through implementation.</p></div>
<div class="service-detail-card"><h3><i class="fa fa-pie-chart" style="color:#7bc74d;margin-right:10px"></i> Monitoring, Evaluation, Accountability &amp; Learning (MEAL)</h3>
<p>Monitoring, evaluation, accountability and learning across the full programme cycle.</p></div>
</div></section>''' + page_end()
write('services.html', services)

# ─── SECTORS ───
sectors = head('Sector Expertise | PRD Consultants – Agriculture, Health, Governance & More',
    'PRD Consultants provides development consulting across agriculture, food security, water, health, education, governance, climate resilience, and social protection.',
    'agriculture development, health nutrition, climate resilience, governance Pakistan')
sectors += '<div id="wrapper">' + header('sectors') + page_hero('Sector Expertise', 'Experience across development sectors', bg='images/hero-page-3.jpg') + '''
<section class="section"><div class="container">
<ul class="filter-tabs">
<li><a href="#" class="active" data-filter="all">All</a></li>
<li><a href="#" data-filter="agriculture">Agriculture</a></li>
<li><a href="#" data-filter="health">Health</a></li>
<li><a href="#" data-filter="governance">Governance</a></li>
<li><a href="#" data-filter="climate">Climate</a></li>
</ul>
''' + sectors_grid(with_filter=True) + '''
<div class="row" style="margin-top:50px">
<div class="col-md-6"><div class="sector-detail"><h3>Agriculture &amp; Rural Development</h3><p>Supporting initiatives focused on rural livelihoods, agricultural development, food systems, and community resilience.</p></div></div>
<div class="col-md-6"><div class="sector-detail"><h3>Food Security &amp; Livelihoods</h3><p>Supporting programmes designed to improve household resilience, economic opportunities, and sustainable livelihoods.</p></div></div>
<div class="col-md-6"><div class="sector-detail"><h3>Water Resources Management</h3><p>Providing support related to water access, resource management, and community-based solutions.</p></div></div>
<div class="col-md-6"><div class="sector-detail"><h3>Health &amp; Nutrition</h3><p>Supporting public health initiatives, awareness programmes, health assessments, and nutrition interventions.</p></div></div>
<div class="col-md-6"><div class="sector-detail"><h3>Education</h3><p>Supporting education programmes, institutional strengthening, and learning improvement initiatives.</p></div></div>
<div class="col-md-6"><div class="sector-detail"><h3>Governance &amp; Public Sector Development</h3><p>Supporting institutional strengthening, governance improvement, and public sector initiatives.</p></div></div>
<div class="col-md-6"><div class="sector-detail"><h3>Climate Resilience &amp; Disaster Risk Reduction</h3><p>Supporting programmes focused on climate adaptation, resilience building, emergency preparedness, and recovery.</p></div></div>
<div class="col-md-6"><div class="sector-detail"><h3>Social Protection &amp; Community Development</h3><p>Supporting inclusive development approaches that strengthen vulnerable communities and improve social outcomes.</p></div></div>
</div></div></section>''' + page_end()
write('sectors.html', sectors)

# ─── WHERE WE WORK ───
where = head('Where We Work | PRD Consultants – UK & Pakistan Operations',
    'PRD Consultants operates from the United Kingdom head office and Pakistan country offices with experience across all provinces.',
    'PRD Consultants UK, Pakistan offices, Sindh Punjab KP Balochistan')
where += '<div id="wrapper">' + header('where') + page_hero('Where We Work', 'Experience across all provinces of Pakistan', bg='images/hero-page-2.jpg') + '''
<section class="section"><div class="container">
<div class="location-cards">
<div class="location-card"><div class="loc-inner"><h4>United Kingdom</h4><div class="role">Head Office | International Operations &amp; Partnerships</div>
<p>86 Wind Road, Ystradgynlais, Swansea, Wales, United Kingdom</p><p>Phone: +44 7304 150 461</p><p>Email: info.UK@prdconsultantsltd.com</p></div></div>
<div class="location-card"><div class="loc-inner"><h4>Pakistan</h4><div class="role">Country Operations | Programme Delivery &amp; Technical Support</div>
<p>Office No. 1, Mezzanine Floor, 25-Huma Plaza, Fazal-e-Haq Road, Blue Area, Islamabad</p><p>Phone: +92 51 260 4334</p><p>Email: info.ISB@prdconsultantsltd.com</p>
<div class="provinces"><span>Sindh</span><span>Punjab</span><span>Khyber Pakhtunkhwa</span><span>Balochistan</span><span>Islamabad</span></div></div></div>
</div>
<div class="content-block" style="margin-top:40px"><p>With extensive experience across Pakistan, our team and expert network have supported development initiatives in all provinces, working with communities, government institutions, development partners, humanitarian actors, and implementing organizations.</p>
<p><strong>Regional Office – Sindh:</strong> House No. A28 &amp; 29, Bakhtawar Colony, Opposite Abdullah Sports City, Qasimabad, Hyderabad. Phone: +92 222 657 214 | Email: info.HYD@prdconsultantsltd.com</p></div>
</div></section>''' + page_end()
write('where-we-work.html', where)

# ─── CLIENTS ───
clients = head('Clients & Partners | PRD Consultants – Trusted Development Partner',
    'PRD Consultants partners with UN agencies, USAID, UK Aid, Government of Sindh, IOM, Save the Children, and leading development organizations.',
    'PRD clients, development partners, UN USAID, Government Sindh')
clients += '<div id="wrapper">' + header('clients') + page_hero('Clients &amp; Partners', 'A trusted partner for development solutions', bg='images/hero-page.jpg') + '''
<section class="section"><div class="container">
<div class="clients-text"><p>At PRD Consultants, we believe effective consulting goes beyond providing recommendations. It requires a deep understanding of challenges, meaningful collaboration with stakeholders, and the ability to develop solutions that are practical, implementable, and sustainable.</p>
<p>Our experience enables us to work as a trusted partner for organizations seeking evidence-based, context-sensitive, and results-oriented solutions to complex development challenges.</p></div>
<div class="clients-showcase"><img src="images/image3.png" alt="PRD Consultants Clients and Partners"></div>
<h3 class="section-title text-center" style="margin:50px 0 30px">Our Partners</h3>
''' + clients_grid() + '''
<div class="content-block" style="max-width:900px;margin:60px auto 0;text-align:center">
<h3>Institutional &amp; Development Partnerships</h3>
<p>Over the years, PRD and its leadership have engaged with a diverse range of development stakeholders, contributing technical expertise, research, implementation support, monitoring and evaluation, and advisory services to donor-supported programmes, United Nations initiatives, and World Bank-funded projects:</p>
</div>
<div class="why-grid" style="margin-top:30px">
<div class="why-item"><div class="why-card"><div class="w-icon"><i class="fa fa-globe"></i></div><h4>UN &amp; International Partners</h4><p>United Nations agencies and international development partners.</p></div></div>
<div class="why-item"><div class="why-card"><div class="w-icon"><i class="fa fa-university"></i></div><h4>Development Institutions</h4><p>Multilateral and bilateral development institutions.</p></div></div>
<div class="why-item"><div class="why-card"><div class="w-icon"><i class="fa fa-building-o"></i></div><h4>Government</h4><p>Government ministries, departments, and public sector organizations.</p></div></div>
<div class="why-item"><div class="why-card"><div class="w-icon"><i class="fa fa-users"></i></div><h4>NGOs &amp; Civil Society</h4><p>International and national NGOs, humanitarian agencies, and civil society organizations.</p></div></div>
<div class="why-item"><div class="why-card"><div class="w-icon"><i class="fa fa-flask"></i></div><h4>Research &amp; Academia</h4><p>Research institutions and academic organizations.</p></div></div>
</div>
<div class="why-grid" style="margin-top:60px">
<div class="why-item"><div class="why-card"><div class="w-icon"><i class="fa fa-globe"></i></div><h4>Field Experience</h4><p>Practical understanding gained through direct engagement with communities and development programmes.</p></div></div>
<div class="why-item"><div class="why-card"><div class="w-icon"><i class="fa fa-certificate"></i></div><h4>Technical Expertise</h4><p>Professional capabilities in research, evaluation, advisory services, and institutional development.</p></div></div>
<div class="why-item"><div class="why-card"><div class="w-icon"><i class="fa fa-handshake-o"></i></div><h4>Partnership Approach</h4><p>A commitment to working collaboratively with clients, stakeholders, and communities.</p></div></div>
<div class="why-item"><div class="why-card"><div class="w-icon"><i class="fa fa-bar-chart"></i></div><h4>Evidence-Based Practice</h4><p>A focus on data, learning, accountability, and measurable results.</p></div></div>
<div class="why-item"><div class="why-card"><div class="w-icon"><i class="fa fa-map"></i></div><h4>Local Understanding with International Standards</h4><p>Solutions that are context-sensitive while aligned with global development practices.</p></div></div>
</div></div></section>''' + page_end()
write('clients.html', clients)

def careers_section():
    sectors_opts = ''.join(
        f'<option value="{s}">{s}</option>' for s in [
            'Agriculture & Rural Development', 'Food Security & Livelihoods',
            'Water Resources Management', 'Health & Nutrition', 'Education',
            'Governance & Public Sector Development', 'Climate Resilience & DRR',
            'Social Protection & Community Development', 'Research & Assessments',
            'MEAL', 'Project Management', 'Technical Assistance', 'Other'
        ])
    return f'''<section class="section careers-page"><div class="container">
<div class="career-grid">
<div class="career-item"><button type="button" class="career-card" data-career-type="jobs" aria-expanded="false">
<i class="fa fa-briefcase"></i><h4>Jobs</h4><span class="career-card-hint">Apply for full-time positions</span></button></div>
<div class="career-item"><button type="button" class="career-card" data-career-type="consultancies" aria-expanded="false">
<i class="fa fa-user-md"></i><h4>Consultancies</h4><span class="career-card-hint">Register as an expert consultant</span></button></div>
<div class="career-item"><button type="button" class="career-card" data-career-type="internships" aria-expanded="false">
<i class="fa fa-graduation-cap"></i><h4>Internships</h4><span class="career-card-hint">Apply for internship opportunities</span></button></div>
</div>
<div class="career-form-backdrop" id="career-form-backdrop" hidden></div>
<div class="career-form-modal" id="career-form-modal" role="dialog" aria-modal="true" aria-labelledby="career-form-title" hidden>
<div class="career-form-wrap contact-form-wrap">
<button type="button" class="career-form-close" aria-label="Close form"><i class="fa fa-times"></i></button>
<h3 id="career-form-title">Application Form</h3>
<p class="career-form-intro" id="career-form-intro"></p>
<form id="career-application-form" enctype="multipart/form-data" novalidate>
<input type="hidden" name="application_type" id="application-type" value="">
<div class="row">
<div class="col-sm-6"><input type="text" class="form-control" name="full_name" placeholder="Full Name *" required></div>
<div class="col-sm-6"><input type="email" class="form-control" name="email" placeholder="Email Address *" required></div>
</div>
<div class="row">
<div class="col-sm-6"><input type="tel" class="form-control" name="phone" placeholder="Phone / WhatsApp *" required></div>
<div class="col-sm-6 career-field career-field-jobs career-field-consultancies career-field-internships">
<input type="text" class="form-control" name="location" placeholder="Current Location (City, Country) *" required></div>
</div>
<div class="career-field career-field-jobs">
<input type="text" class="form-control" name="position" placeholder="Position of Interest *" required>
</div>
<div class="row career-field career-field-jobs">
<div class="col-sm-6"><input type="text" class="form-control" name="qualification" placeholder="Highest Qualification *" required></div>
<div class="col-sm-6"><input type="number" class="form-control" name="experience_years" min="0" placeholder="Years of Experience *" required></div>
</div>
<div class="career-field career-field-jobs">
<select class="form-control" name="job_sector" required>
<option value="">Primary Sector Experience *</option>
{sectors_opts}
</select>
</div>
<div class="row career-field career-field-consultancies">
<div class="col-sm-6"><select class="form-control" name="expertise_area" required>
<option value="">Area of Expertise *</option>
{sectors_opts}
</select></div>
<div class="col-sm-6"><select class="form-control" name="engagement_type" required>
<option value="">Type of Engagement *</option>
<option value="Short-term assignment">Short-term assignment</option>
<option value="Long-term assignment">Long-term assignment</option>
<option value="Both">Both</option>
</select></div>
</div>
<div class="row career-field career-field-consultancies">
<div class="col-sm-6"><input type="number" class="form-control" name="consulting_years" min="0" placeholder="Years of Consulting Experience *" required></div>
<div class="col-sm-6"><input type="text" class="form-control" name="availability" placeholder="Availability (e.g. March 2026 onwards) *" required></div>
</div>
<div class="career-field career-field-consultancies">
<textarea class="form-control" name="past_assignments" placeholder="Previous development agencies, donors, or projects worked with *" required></textarea>
</div>
<div class="row career-field career-field-internships">
<div class="col-sm-6"><input type="text" class="form-control" name="university" placeholder="University / Institution *" required></div>
<div class="col-sm-6"><input type="text" class="form-control" name="degree" placeholder="Degree Programme *" required></div>
</div>
<div class="row career-field career-field-internships">
<div class="col-sm-6"><input type="text" class="form-control" name="graduation" placeholder="Year of Study / Expected Graduation *" required></div>
<div class="col-sm-6"><select class="form-control" name="interest_area" required>
<option value="">Area of Interest *</option>
{sectors_opts}
</select></div>
</div>
<div class="row career-field career-field-internships">
<div class="col-sm-6"><select class="form-control" name="preferred_office" required>
<option value="">Preferred Location *</option>
<option value="United Kingdom">United Kingdom</option>
<option value="Islamabad, Pakistan">Islamabad, Pakistan</option>
<option value="Hyderabad, Pakistan">Hyderabad, Pakistan</option>
<option value="Remote">Remote</option>
</select></div>
<div class="col-sm-6"><input type="text" class="form-control" name="duration" placeholder="Available Duration (e.g. 3 months) *" required></div>
</div>
<div class="career-field career-field-jobs career-field-consultancies career-field-internships">
<textarea class="form-control" name="message" id="career-message" placeholder="Cover letter / profile summary / statement of interest *" required></textarea>
</div>
<div class="career-cv-upload">
<label class="cv-upload-label" for="career-cv"><i class="fa fa-paperclip"></i> Upload CV / Resume * <span>(PDF, DOC, DOCX — max 5MB)</span></label>
<input type="file" id="career-cv" name="cv" class="career-cv-input" accept=".pdf,.doc,.docx" required>
<p class="cv-file-name" id="cv-file-name"></p>
</div>
<button type="submit" class="btn-green">Submit Application</button>
</form></div></div>
</div></section>'''

# ─── CAREERS ───
careers = head('Careers | PRD Consultants – Jobs, Consultancies & Internships',
    'Join PRD Consultants. Explore career opportunities in development consulting, research, technical assistance, and project management.',
    'PRD careers, development jobs Pakistan, consulting internships')
careers += '<div id="wrapper">' + header('careers') + page_hero('Careers', '', bg='images/hero-page-3.jpg') + careers_section() + page_end()
write('careers.html', careers)

# ─── PUBLICATIONS ───
pubs = head('Publications & Insights | PRD Consultants – Research & Reports',
    'PRD Consultants publications including research studies, PC-1 development, agricultural reports, and thought leadership from Sindh and Pakistan.',
    'PRD publications, research reports Sindh, agricultural studies Pakistan')
pubs += '<div id="wrapper">' + header('publications') + page_hero('Publications &amp; Insights', 'Knowledge &amp; Insights', bg='images/hero-page-2.jpg') + '''
<section class="section"><div class="container">
<div class="content-block" style="max-width:860px;margin:0 auto 40px;text-align:center">
<p>Stay updated with the latest developments, achievements, and activities of PRD Consultants. This section highlights our organizational updates, project milestones, publications, partnerships, events, and knowledge-sharing initiatives across the development sector.</p>
<p>Through our news and updates, we share insights from our work, celebrate collaborations with partners, and highlight contributions toward evidence-based solutions, institutional strengthening, and sustainable development.</p>
</div>
<ul class="pub-list">
<li><span class="pub-icon"><i class="fa fa-file-text-o"></i></span><div><h5>Onion Research Study Sindh</h5><p>Research &amp; Reports</p></div></li>
<li><span class="pub-icon"><i class="fa fa-file-text-o"></i></span><div><h5>Development of PC-1 for the Sindh Water and Agriculture Transformation Project</h5><p>Agriculture Department, Government of Sindh</p></div></li>
<li><span class="pub-icon"><i class="fa fa-file-text-o"></i></span><div><h5>Revision of PC-1 Sindh Agricultural Growth Project</h5><p>Agriculture Department, Government of Sindh</p></div></li>
<li><span class="pub-icon"><i class="fa fa-file-text-o"></i></span><div><h5>Articles &amp; Thought Leadership</h5><p>Articles &amp; Thought Leadership</p></div></li>
<li><span class="pub-icon"><i class="fa fa-file-text-o"></i></span><div><h5>News &amp; Events</h5><p>News &amp; Events</p></div></li>
</ul></div></section>''' + page_end()
write('publications.html', pubs)

# ─── CONTACT ───
contact = head('Contact Us | PRD Consultants – UK, Islamabad & Hyderabad Offices',
    'Contact PRD Consultants. Head Office UK, Islamabad and Hyderabad offices. Phone, email and office addresses.',
    'contact PRD Consultants, Islamabad office, UK head office Hyderabad')
contact += '<div id="wrapper">' + header('contact') + page_hero('Contact Us', '', bg='images/hero-page.jpg') + '''
<section class="section"><div class="container"><div class="row">
<div class="col-md-7">
<div class="contact-form-wrap">
<h3 style="margin-top:0;font-weight:600;color:#222831">Contact Us</h3>
<form id="contact-form">
<div class="row"><div class="col-sm-6"><input type="text" class="form-control" placeholder="Your Name" required></div>
<div class="col-sm-6"><input type="email" class="form-control" placeholder="Your Email" required></div></div>
<input type="text" class="form-control" placeholder="Subject">
<textarea class="form-control" placeholder="Your Message" required></textarea>
<button type="submit" class="btn-green">Send Message</button>
</form></div></div>
<div class="col-md-5">
<div class="contact-info-block"><h4>Head Office – United Kingdom</h4>
<p>86 Wind Road, Ystradgynlais, Swansea, Wales, United Kingdom<br>Phone: +44 7304 150 461<br><a href="mailto:info.UK@prdconsultantsltd.com">info.UK@prdconsultantsltd.com</a></p></div>
<div class="contact-info-block"><h4>Country Office – Pakistan</h4>
<p>Office No. 1, Mezzanine Floor, 25-Huma Plaza, Fazal-e-Haq Road, Blue Area, Islamabad, Pakistan<br>Phone: +92 51 260 4334<br><a href="mailto:info.ISB@prdconsultantsltd.com">info.ISB@prdconsultantsltd.com</a></p></div>
<div class="contact-info-block"><h4>Regional Office – Sindh</h4>
<p>House No. A28 &amp; 29, Bakhtawar Colony, Opposite Abdullah Sports City, Qasimabad, Hyderabad, Pakistan<br>Phone: +92 222 657 214<br><a href="mailto:info.HYD@prdconsultantsltd.com">info.HYD@prdconsultantsltd.com</a></p></div>
</div></div></div></section>''' + page_end()
write('contact.html', contact)

print('All pages generated successfully.')
