from bokeh.plotting import figure, show, output_notebook, output_file, save
from bokeh.tile_providers import get_provider, Vendors  # CARTODBPOSITRON
# from bokeh.til
# from sklearn.datasets import fetch_california_housing
from bokeh.models import ColumnDataSource, HoverTool, ColorBar
import numpy as np


class Plots():
    ''' plots the cordinates on the map; the size of the circles determine the 
    median house value'''

    def __init__(self, df, x, y):
        self.df = df
        self.x = x
        self.y = y

    def holoViewPlot(self):
        self.df['sizeX'] = self.df['median_house_value'] / \
            np.min(self.df['median_house_value'])
        source = ColumnDataSource(
            data=dict(x=list(self.x), y=list(self.y),
                      ocean_proximity=list(self.df['ocean_proximity']),
                      house_median_age=list(self.df['housing_median_age']),
                      median_income=list(self.df['median_income']*10000),
                      median_house_value=list(self.df['median_house_value']),
                      sizes=list(self.df['sizeX'])))

        hover = HoverTool(tooltips=[('Median income', '@median_income'),
                                    ('Median house value', '@median_house_value')])
# get_provider('CARTODBPOSITRON')

        p = figure(x_axis_type="mercator", y_axis_type="mercator",
                   tools=[hover, 'wheel_zoom', 'save', 'pan', 'box_zoom'],
                   sizing_mode='scale_width')
        p.add_tile(get_provider(Vendors.STAMEN_TERRAIN))
        p.circle(x='x', y='y', source=source, size='sizes', line_color="#3f007d",
                 fill_color="#fdae6b",
                 fill_alpha=0.5)

        show(p)
        output_file('CaliPlot.html')
        save(p)
