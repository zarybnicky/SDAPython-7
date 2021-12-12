import jp_proxy_widget
import uuid
from IPython.display import Image, SVG


class FlowchartWidget(jp_proxy_widget.JSProxyWidget):
    """jp_proxy_widget to render flowchart.js diagrams."""

    def __init__(self, *pargs, **kwargs):
        super(FlowchartWidget, self).__init__(*pargs, **kwargs)
        e = self.element
        e.empty()
        self.load_js_files(["https://cdnjs.cloudflare.com/ajax/libs/raphael/2.3.0/raphael.min.js",
                            'https://cdnjs.cloudflare.com/ajax/libs/flowchart/1.14.1/flowchart.js'])
        self.uid = None
        self.svg = None

    def charter(self, chart, embed=False):
        """Render chart from chart description."""
        self.uid = uid = uuid.uuid4()
        self.element.html(f'<div id="{uid}"></div>')
        self.set_element("chartdef", chart)
        self.js_init(
            f"chart = flowchart.parse(element.chartdef); chart.drawSVG('{uid}');svg_data = document.getElementById('{uid}').innerHTML;")
        self.get_value_async(self.svg_callback, "svg_data")
        if embed:
            return self

    def svg_callback(self, svg):
        """Persist SVG state on Python side."""
        self.svg = svg

    def get_svg(self):
        """Return raw SVG data for flowchart."""
        return self.svg

    def embed_svg(self):
        """Return SVG data of flowchart."""
        return SVG(self.svg)


from IPython.core.magic import Magics, magics_class, cell_magic
from pyflowchart import Flowchart


@magics_class
class FlowchartMagics(Magics):
    """Magics for flowchart.js """

    def __init__(self, shell):
        super(FlowchartMagics, self).__init__(shell)

    @cell_magic
    def flowchart_magic(self, line, cell):
        "Send code to flow charter."
        return FlowchartWidget().charter(cell, embed=True)

    @cell_magic
    def pyflowchart_magic(self, line, cell):
        "Generate flowchart code and send to flow charter."
        fc = Flowchart.from_code(cell)
        return FlowchartWidget().charter(str(fc.flowchart()), embed=True)


def load_ipython_extension(ip):
    """Load the extension in IPython."""
    ipython.register_magics(FlowchartMagics)


ip = get_ipython()
ip.register_magics(FlowchartMagics)