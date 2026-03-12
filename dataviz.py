import streamlit as st
import matplotlib.pyplot as plt

st.title("Simple Shape Visualizer")

choice = st.selectbox("Pick a shape:", ["Triangle", "Circle", "Trapezoid"])

if choice == "Triangle":
    st.header("Triangle")
    
    h = st.number_input("Height (h)", value=10.0)
    l = st.number_input("Base Length (l)", value=15.0)
    a = st.number_input("Side A (a)", value=10.0)
    b = st.number_input("Side B (b)", value=10.0)
    c = st.number_input("Side C (c)", value=15.0)

    S = h * l / 2
    P = a + b + c
    
    st.write(f"Area (S) = {S}")
    st.write(f"Perimeter (P) = {P}")

    x_points = [-l/2,  l/2, 0]
    y_points = [   0,    0, h]
    
    fig, ax = plt.subplots()
    ax.fill(x_points, y_points, color='green', alpha=0.5)
    ax.set_aspect('equal')
    st.pyplot(fig)

elif choice == "Circle":
    st.header("Circle")

    r = st.number_input("Radius (r)", value=5.0)

    S = 3.14 * r ** 2
    P = 2 * 3.14 * r
    
    st.write(f"Area (S) = {S}")
    st.write(f"Perimeter (P) = {P}")

    fig, ax = plt.subplots()
    my_circle = plt.Circle((0, 0), r, color='orange', alpha=0.5)
    ax.add_patch(my_circle)
    
    ax.set_xlim(-r-1, r+1)
    ax.set_ylim(-r-1, r+1)
    ax.set_aspect('equal')
    st.pyplot(fig)

elif choice == "Trapezoid":
    st.header("Trapezoid")

    b1 = st.number_input("Bottom Base (b1)", value=12.0)
    b2 = st.number_input("Top Base (b2)", value=8.0)
    h  = st.number_input("Height (h)", value=6.0)
    c  = st.number_input("Side C (c)", value=5.0)
    d  = st.number_input("Side D (d)", value=5.0)

    S = (b1 + b2) / 2 * h
    P = c + d + b1 + b2
    
    st.write(f"Area (S) = {S}")
    st.write(f"Perimeter (P) = {P}")

    x_points = [-b1/2, b1/2, b2/2, -b2/2]
    y_points = [    0,    0,    h,     h]

    fig, ax = plt.subplots()
    ax.fill(x_points, y_points, color='purple', alpha=0.5)
    ax.set_aspect('equal')
    st.pyplot(fig)