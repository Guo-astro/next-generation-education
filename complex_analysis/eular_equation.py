import numpy as np
import plotly.graph_objects as go

# Define the range of theta
theta_max = 10 * np.pi  # Total angle (radians)
num_frames = 500  # Number of frames in the animation
theta = np.linspace(0, theta_max, num_frames)

# Compute the real and imaginary parts
x = np.cos(theta)
y = np.sin(theta)
z = theta

# Create the helix path data with opacity
helix_path = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='lines',
    line=dict(color='blue', width=4),  # Added opacity
    name=r'Path of $y = e^{i\theta}$'
)

# Create the moving point data with opacity
point = go.Scatter3d(
    x=[x[0]],
    y=[y[0]],
    z=[z[0]],
    mode='markers',
    marker=dict(color='red', size=8, opacity=0.9),  # Added opacity
    name='Current Point'
)

# Initialize the figure
fig = go.Figure(data=[helix_path, point])

# Create frames for the animation
frames = [
    go.Frame(
        data=[
            go.Scatter3d(
                x=x[:k],
                y=y[:k],
                z=z[:k],
                mode='lines',
                line=dict(color='blue', width=4)  # Consistent opacity
            ),
            go.Scatter3d(
                x=[x[k - 1]],
                y=[y[k - 1]],
                z=[z[k - 1]],
                mode='markers',
                marker=dict(color='red', size=8)  # Consistent opacity
            )
        ],
        name=str(k)
    )
    for k in range(1, num_frames)
]

fig.frames = frames

# Define the layout with animation settings, gridlines, and opacity
fig.update_layout(
    title=r'3D Visualization of $y = e^{i\theta}$',
    scene=dict(
        xaxis_title=r'$\cos(\theta)$',
        yaxis_title=r'$\sin(\theta)$',
        zaxis_title=r'$\theta$',
        xaxis=dict(
            range=[-1.5, 1.5],
            showgrid=True,  # Ensure grid is shown
            gridcolor='LightGray',  # Gridline color
            gridwidth=1,  # Gridline width
            zeroline=True,  # Show zero line
            zerolinecolor='Gray',  # Zero line color
            zerolinewidth=2  # Zero line width
        ),
        yaxis=dict(
            range=[-1.5, 1.5],
            showgrid=True,
            gridcolor='LightGray',
            gridwidth=1,
            zeroline=True,
            zerolinecolor='Gray',
            zerolinewidth=2
        ),
        zaxis=dict(
            range=[0, theta_max],
            showgrid=True,
            gridcolor='LightGray',
            gridwidth=1,
            zeroline=True,
            zerolinecolor='Gray',
            zerolinewidth=2
        ),
        aspectratio=dict(x=1, y=1, z=2)  # Adjust aspect ratio for better visualization
    ),
    updatemenus=[
        dict(
            type='buttons',
            showactive=False,
            buttons=[
                dict(
                    label='Play',
                    method='animate',
                    args=[
                        None,
                        dict(frame=dict(duration=20, redraw=True),
                             transition=dict(duration=0),
                             fromcurrent=True,
                             mode='immediate')
                    ]
                ),
                dict(
                    label='Pause',
                    method='animate',
                    args=[
                        [None],
                        dict(frame=dict(duration=0, redraw=False),
                             transition=dict(duration=0),
                             mode='immediate')
                    ]
                )
            ],
            x=0.1,
            y=0
        )
    ],
    sliders=[
        dict(
            steps=[
                dict(
                    method='animate',
                    args=[
                        [str(k)],
                        dict(mode='immediate',
                             frame=dict(duration=20, redraw=True),
                             transition=dict(duration=0))
                    ],
                    label=str(k)
                ) for k in range(1, num_frames, 50)  # Adjust step size for performance
            ],
            transition=dict(duration=0),
            x=0.1,
            y=0,
            currentvalue=dict(font=dict(size=12), prefix='Frame: ', visible=True, xanchor='center'),
            len=0.9
        )
    ],
    legend=dict(
        x=0,
        y=1
    )
)

# Show the figure
fig.show()
