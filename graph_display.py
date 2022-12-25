import plotly.express as px
import plotly.io as pio
import pandas as pd
import runner

pio.renderers.default = 'browser'

def full_test():
    values, names = runner.final_values('Du Haberdasher')

    df = pd.DataFrame(dict(
        r=values,
        theta=names))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True, range_r=(0, 1))

    fig.write_html("C:/Coding/Non-Assignments/Playstyle Analyzer/Graph_images/fig1.html")



full_test()

def multi_test():
    values1 = runner.final_values("ItzBoiBen")
    values2 = runner.final_values("Clodon")

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[1, 5, 2, 2, 3],
        theta=categories,
        fill='toself',
        name='Product A'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[4, 3, 2.5, 1, 2],
        theta=categories,
        fill='toself',
        name='Product B'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5]
            )),
        showlegend=False
    )

full_test()