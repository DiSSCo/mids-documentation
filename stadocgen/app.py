from flask import Flask, render_template
from markupsafe import Markup
import markdown2
import pandas as pd
from flask_flatpages import FlatPages, pygmented_markdown, pygments_style_defs

app = Flask(__name__)
app.config.from_pyfile("config.py")

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}

# Homepage with content stored in markdown file
@app.route('/')
def home():
    home_mdfile = 'md/ltc/home-content.md'
    marked_text = ''
    with open(home_mdfile, encoding="utf8") as f:
        marked_text = markdown2.markdown(f.read())
    return render_template('home.html',
                           homemd=Markup(marked_text),
                           title='Home',
                           slug='home')

@app.route('/skos-mappings')
def skosMappings():
    skos_mdfile = 'md/ltc/skos-header.md'
    skos_text = ''
    with open(skos_mdfile, encoding="utf8") as f:
        skos_text = markdown2.markdown(f.read())

    sssom_mdfile = 'md/ltc/sssom-header.md'
    sssom_text = ''
    with open(sssom_mdfile, encoding="utf8") as f:
        sssom_text = markdown2.markdown(f.read())

    skoscsv = 'data/ltc/ltc-docs/ltc-skos.csv'
    skos = pd.read_csv(skoscsv, encoding='utf8')

    sssomcsv = 'data/ltc/ltc-docs/ltc-sssom.csv'
    sssom = pd.read_csv(sssomcsv, encoding='utf8')

    return render_template('skos.html',
                           sssom=sssom,
                           skosmd=Markup(skos_text),
                           sssommd=Markup(sssom_text),
                           title='SKOS Mappings',
                           slug='skos-mappings'
    )


@app.route('/terms')
def terms():
    header_mdfile = 'md/ltc/terms-list-header.md'
    marked_text = ''
    with open(header_mdfile, encoding="utf8") as f:
        marked_text = markdown2.markdown(f.read(), extras=["tables", "fenced-code-blocks"])

    # Terms
    terms_csv = 'data/ltc/ltc-docs/ltc-terms-list.csv'
    df = pd.read_csv(terms_csv, encoding='utf8')
    terms = df.sort_values(by=['class_name'])

    # Unique Class Names
    ltcCls = df["class_name"].dropna().unique()

    # Terms by Class
    grpdict2 = df.groupby('class_name')[['term_ns_name', 'term_local_name']].apply(
        lambda g: list(map(tuple, g.values.tolist()))).to_dict()
    termsByClass = []
    for i in grpdict2:
        termsByClass.append({
            'class': i,
            'terms': grpdict2[i]
        })

    return render_template('terms.html',
                           headerMarkdown=Markup(marked_text),
                           ltcCls=ltcCls,
                           terms=terms,
                           termsByClass=termsByClass,
                           title='Terms List',
                           slug='terms-list'
    )

@app.route('/quick-reference')
def quickReference():
    header_mdfile = 'md/ltc/quick-reference-header.md'
    marked_text = ''
    with open(header_mdfile, encoding="utf8") as f:
        marked_text = markdown2.markdown(f.read())

    # Quick Reference Main
    df = pd.read_csv('data/ltc/ltc-docs/ltc-terms-list.csv', encoding='utf8')

    # Group by Class
    grpdict = df.fillna(-1).groupby('class_name')[['namespace', 'term_local_name', 'label', 'definition',
                                                   'usage', 'notes','examples', 'rdf_type', 'class_name',
                                                   'is_required', 'is_repeatable', 'compound_name',
                                                   'datatype', 'term_ns_name']].apply(
        lambda g: list(map(tuple, g.values.tolist()))).to_dict()
    grplists = []
    for i in grpdict:
        grplists.append({
            'class': i,
            'terms': grpdict[i]
        })

    return render_template('quick-reference.html',
                           headerMarkdown=Markup(marked_text),
                           grplists=grplists,
                           title='Quick Reference',
                           slug='quick-reference'
    )


if (__name__ == "__main__"):
    app.run(port = 5000, debug=True)