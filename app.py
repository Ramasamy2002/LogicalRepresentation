import streamlit as st

# Define parsing rules
def parse_sentence(sentence):
    logical_form = ""
    propositions = {}

    tokens = sentence.lower().split()

    for idx, token in enumerate(tokens):
        if token == "and":
            logical_form += " ∧ "
        elif token == "or":
            logical_form += " ∨ "
        elif token == "not":
            logical_form += " ¬ "
        elif token == "either":
            logical_form += " ⋁ "
        elif token == "nor":
            logical_form += " ⋁¬ "
        elif token == "neither":
            logical_form += " ¬⋁¬ "
        elif token == "both":
            logical_form += " ⋀ "
        elif token == "but":
            logical_form += " ⋀¬ "
        elif token == "provided" and idx < len(tokens) - 1 and tokens[idx + 1] == "that":
            logical_form += " ⇒ "
        elif token == "whenever":
            logical_form += " ⇒ "
        else:
            if token not in propositions:
                propositions[token] = token
            logical_form += propositions[token]+" "

    return logical_form, propositions

# Streamlit UI
st.set_page_config(
    page_title="Logical Representation Parser",
    page_icon=":1234:",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("Logical Representation Parser")

# Text input for user to enter a sentence
sentence = st.text_input("Enter a sentence:")

# Button to trigger parsing
if st.button("Parse", key="parse_button"):
    # Parse the sentence
    logical_form, propositions = parse_sentence(sentence)
    st.markdown("---")
    st.subheader("Parsed Result:")
    st.write(f"**Logical Form:** {logical_form}")
    
 
