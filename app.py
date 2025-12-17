import streamlit as st
import pandas as pd


def get_grade(percentage: float) -> str:
    """Return grade based on percentage."""
    if percentage >= 90:
        return "A+"
    if percentage >= 80:
        return "A"
    if percentage >= 70:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 50:
        return "D"
    return "F"


st.set_page_config(page_title="Student Grade Calculator", layout="centered")

st.title("Student Grade Calculator")
st.write(
    "Enter the number of subjects, then enter each subject name and marks (out of 100). The app will compute total, percentage and grade."
)

num = st.number_input("Number of subjects", min_value=1, max_value=20, value=5, step=1, key="num_subjects")

with st.form("marks_form"):
    subjects = []
    marks = []
    for i in range(int(num)):
        name = st.text_input(f"Subject {i+1} name", value=f"Subject {i+1}", key=f"name_{i}")
        m = st.number_input(
            f"Marks for {name}", min_value=0, max_value=100, value=0, step=1, key=f"marks_{i}"
        )
        subjects.append(name)
        marks.append(m)

    submitted = st.form_submit_button("Calculate")

if submitted:
    total = sum(marks)
    max_total = int(num) * 100
    percentage = (total / max_total) * 100 if max_total > 0 else 0
    grade = get_grade(percentage)

    df = pd.DataFrame({"Subject": subjects, "Marks": marks})

    st.subheader("Score Breakdown")
    st.table(df)

    st.write(f"**Total Marks:** {total} / {max_total}")
    st.write(f"**Percentage:** {percentage:.2f}%")
    st.write(f"**Grade:** {grade}")

    if percentage < 40:
        st.warning("Student is failing.")
    else:
        st.success("Student has passed.")
