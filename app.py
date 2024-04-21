import streamlit as st
from hugging_face_demo import extract_parameters, classify_input, generate_response


def main():
    st.title("Text Classification and Parameter Extraction Demo")

    # Text input box for user prompt
    user_prompt = st.text_input("Enter your text prompt:")

    # Button to trigger classification and extraction
    if st.button("Analyze"):
        # Text classification
        transaction_type = classify_input(user_prompt)
        parameter_extraction_result = ""
        if transaction_type:
            # Parameter extraction
            parameters = extract_parameters(user_prompt, transaction_type)
            if parameters:
                parameter_extraction_result = generate_response(transaction_type, parameters)

        # Display results
        st.write("### Classification Result:")
        st.write(transaction_type)

        st.write("### Parameter Extraction Result:")
        textsplit = parameter_extraction_result.splitlines()
        for x in textsplit:
            st.write(x)


if __name__ == "__main__":
    main()
