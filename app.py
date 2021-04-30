import os

import json, plotly
from jinja2 import Environment
from jinja2 import FileSystemLoader
from chalice import Chalice, Response, NotFoundError, ChaliceViewError, BadRequestError
from wrangling_scripts.wrangle_data import return_figures, return_figures_first, return_figures_second

from logging import basicConfig
log = basicConfig(level='DEBUG')

app = Chalice(app_name='sentiment')
app.debug = True



def _render_template(**kwargs):
    "render jinja template"
    env = Environment(loader=FileSystemLoader(os.path.abspath(os.path.dirname(__file__))))
    template = env.get_template('chalicelib/main.html')
    rendered_template = template.render(kwargs)
    return rendered_template

@app.route('/')
@app.route('/index')
def index():

    figures = return_figures()

    # plot ids for the html id tag
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

    # Convert the plotly figures to JSON for javascript in html template
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)


    return Response(_render_template(ids=ids,
                                     figuresJSON=figuresJSON),
                    status_code=200,
                    headers={'Content-Type': 'text/html'})


@app.route('/first', methods=['GET'])
def inference():

    figures = return_figures_first()

    # plot ids for the html id tag
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

    # Convert the plotly figures to JSON for javascript in html template
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)


    return Response(_render_template(ids=ids,
                                     figuresJSON=figuresJSON),
                    status_code=200,
                    headers={'Content-Type': 'text/html'})

@app.route('/second', methods=['GET'])
def inference():

    figures = return_figures_second()

    # plot ids for the html id tag
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

    # Convert the plotly figures to JSON for javascript in html template
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)


    return Response(_render_template(ids=ids,
                                     figuresJSON=figuresJSON),
                    status_code=200,
                    headers={'Content-Type': 'text/html'})



