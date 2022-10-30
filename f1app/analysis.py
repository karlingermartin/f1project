import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io, base64
import numpy as np
import pandas as pd
import seaborn as sb

class Charts():

        def first_ten(self, **kwargs):
                fig, ax = plt.subplots()
                ax.plot([1, 3, 4], [3, 2, 5])
                #return fig

                flike = io.BytesIO()
                fig.savefig(flike)
                b64 = base64.b64encode(flike.getvalue()).decode()
                print(b64)
                context = {}
                context['chart'] = b64
                return context