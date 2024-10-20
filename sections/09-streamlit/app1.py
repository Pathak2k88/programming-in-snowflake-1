import streamlit as st
import pandas as pd
import modules.graphs as graphs
import charts,animated
st.set_page_config(layout="wide")
st.title("Hierarchical Data Viewer")
st.caption("Display your hierarchical data with charts and graphs")

tabSource,tabFormat,tabGraph,tabChart,tabAnim = st.tabs(["Source","Format","Graph","Chart","Animated"])


with tabSource:
    filename = "data/employee-manager.csv"
    df = pd.read_csv(filename).convert_dtypes()
    st.dataframe(df)

with tabGraph:
    graph = graphs.getEdges(df)
    url = graphs.getUrl(graph)
    st.link_button("Visualise Online",url)
    st.graphviz_chart(graph)
with tabChart:
    labels = df[df.columns[0]]
    parents = df[df.columns[1]]

    sel = st.selectbox(
        "Select a chart type:",
        options=["Treemap", "Icicle", "Sunburst", "Sankey"])
    if sel == "Treemap":
        fig = charts.makeTreemap(labels, parents)
    elif sel == "Icicle":
        fig = charts.makeIcicle(labels, parents)
    elif sel == "Sunburst":
        fig = charts.makeSunburst(labels, parents)
    else:
        fig = charts.makeSankey(labels, parents)
    st.plotly_chart(fig, use_container_width=True)

