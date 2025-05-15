import streamlit as st

def transform_elec(b4: str) -> str:
    b10 = "FF1122331C234F0000-CCDDEE00"
    first_part, second_part = b10.split("-", 1)
    cleaned_b4 = b4[-9:].replace("-", "")
    return first_part + cleaned_b4 + second_part

def transform_gas(b4: str) -> str:
    b10 = "FF1122334411020000-CCDDEE00"
    first_part, second_part = b10.split("-", 1)
    cleaned_b4 = b4[-9:].replace("-", "")
    return first_part + cleaned_b4 + second_part

def detect_guid_type(guid: str) -> str:
    guid = guid.strip()
    if len(guid) != 23:
        return "invalid"
    if guid.startswith("1C-23-4F"):
        return "elec"
    elif guid.startswith("44-11-02"):
        return "gas"
    return "invalid"

# App title
st.title("EDMI Install Code Generator")

st.write("Paste a GUID below – the app will detect if it’s Electric or Gas and create the install code for you.")

guid_input = st.text_input("GUID")

if st.button("Generate Code"):
    guid_type = detect_guid_type(guid_input)

    if guid_type == "invalid":
        st.error("Please check your GUID. It should be formatted like XX-XX-XX-XX-XX-XX-XX-XX and start with either '1C-23-4F' (Elec) or '44-11-02' (Gas).")
    else:
        if guid_type == "elec":
            result = transform_elec(guid_input)
            label = "Electric install code"
        else:
            result = transform_gas(guid_input)
            label = "Gas install code"

        st.write(f"Here’s your **{label}**:")
        st.code(result, language="text")


