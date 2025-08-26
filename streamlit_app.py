import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("💰Personal Expense Tracker")

# Session state to store expenses
if "expenses" not in st.session_state:
    st.session_state["expenses"] = []

# Input form
with st.form("expense_form"):
    category = st.text_input("Enter Category (Food, Travel, Bills etc.)")
    amount = st.number_input("Enter Amount (₹)", min_value=0.0, step=10.0)
    submitted = st.form_submit_button("➕ Add Expense")

    if submitted and category:
        st.session_state["expenses"].append({"Category": category, "Amount": amount})
        st.success(f"Added {category}: ₹{amount}")

# Convert to DataFrame
df = pd.DataFrame(st.session_state["expenses"])

# Show summary
if not df.empty:
    st.subheader("📊 Expense Summary")
    st.dataframe(df)

    # Total
    total = df["Amount"].sum()
    st.write(f"**Total Expenses: ₹{total}**")

    # Pie Chart
    fig, ax = plt.subplots()
    df.groupby("Category")["Amount"].sum().plot.pie(autopct="%1.1f%%", ax=ax)
    st.pyplot(fig)
