import plotly.graph_objects as go
import numpy as np

# Creating the data
xx = np.linspace(-2, 2, 50)
yy = np.linspace(-2, 2, 50)
x, y = np.meshgrid(yy, xx)
R = np.sqrt(x ** 2 + y ** 2)
z = x*x - y*y + 4

# Creating the plot
lines = []
# Saddle
for i, j, k in zip(x, y, z):
    lines.append(go.Scatter3d(
        x=i, 
        y=j, 
        z=k, 
        mode='lines', 
        line=dict(
            colorscale='jet',
            color=k, 
            width=2,
            ),
        )
    )

t = np.linspace(0, 2*np.pi, 50)
x, y = np.cos(t), np.sin(t),
z = x*x - y*y + 4
z0 = x*0

lines.append(go.Scatter3d(
    x=x,
    y=y,
    z=z0,
    mode='lines',
    line=dict(
        color='black',
        width=2,
        ),
    )
)

lines.append(go.Scatter3d(
    x=x,
    y=y,
    z=x*x-y*y+4,
    mode='lines',
    line=dict(
        color='black',
        width=2,
        ),
    )
)

# Axis settings
axis_settings = dict(
    gridcolor='#7d7d7d',
    #zerolinecolor='#5d5d5d',
    #zerolinewidth=3,
    showbackground=True,
    backgroundcolor='rgba(0, 0, 0, 0)',
    showspikes=False,
)

layout = go.Layout(
    scene=dict(
        xaxis=axis_settings,
        yaxis=axis_settings,
        zaxis=axis_settings,
        aspectratio=dict(x=1, y=1, z=0.6),
        hovermode=False
    ),
    showlegend=False,
    width=700,
    height=600,
    margin=dict(
        l=0,
        r=0,
        t=0,
        b=0
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
)


config = {
    'displayModeBar': False,
    'scrollZoom': False,
    #'staticPlot': True
}

fig = go.Figure(data=lines, layout=layout)
fig.write_html(file='xx-yy+4.html', config=config)
