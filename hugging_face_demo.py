from huggingface_hub.inference_api import InferenceApi
import streamlit as st
import json


#input_sentence = "I need to collect 15 qty for item A004 in location LocationTwo."
#input_sentence = "I want to move for item A001 to location Master."
#input_sentence = "Increment item A006 quantity to 60 and assign it to person Ahmed."


def classify_input(input_sentence):
    classification_inputs = input_sentence
    classification_params = {"candidate_labels": ["move", "receive", "adjust", "dispose"]}

    classification_inference = InferenceApi(repo_id=st.secrets["classification_model"],
                                            token=st.secrets["api_token"])
    classification_output = classification_inference(classification_inputs, classification_params)
    transaction_type = classification_output['labels'][0]
    return transaction_type


def process_input(input_sentence):
    # Transaction Classification
    transaction_type = classify_input(input_sentence)
    if transaction_type:
        return transaction_type
    else:
        return None  # Unable to classify


def question_answering_inference():

    qa_inference = InferenceApi(repo_id=st.secrets["question_answering_model"],
                                token=st.secrets["api_token"])
    return qa_inference


def question_stock_number(input_sentence, qa_inference):
    qa_inputs = {"question": "what is the stock number?", "context": input_sentence}
    qa_output = qa_inference(qa_inputs)
    return qa_output['answer']


def question_location(input_sentence, qa_inference):
    qa_inputs = {"question": "where is the location?", "context": input_sentence}
    qa_output = qa_inference(qa_inputs)
    return qa_output['answer']


def question_quantity(input_sentence, qa_inference):
    qa_inputs = {"question": "what is the quantity?", "context": input_sentence}
    qa_output = qa_inference(qa_inputs)
    return qa_output['answer']


def question_location_from(input_sentence, qa_inference):
    qa_inputs = {"question": "where is the movement from?", "context": input_sentence}
    qa_output = qa_inference(qa_inputs)
    return qa_output['answer']


def question_location_to(input_sentence, qa_inference):
    qa_inputs = {"question": "where is the movement to?", "context": input_sentence}
    qa_output = qa_inference(qa_inputs)
    return qa_output['answer']


def question_new_quantity(input_sentence, qa_inference):
    qa_inputs = {"question": "what is the incremented quantity?", "context": input_sentence}
    qa_output = qa_inference(qa_inputs)
    return qa_output['answer']


def question_person(input_sentence, qa_inference):
    qa_inputs = {"question": "who is the new person?", "context": input_sentence}
    qa_output = qa_inference(qa_inputs)
    return qa_output['answer']


def question_dispose_quantity(input_sentence, qa_inference):
    qa_inputs = {"question": "what is the dispose quantity?", "context": input_sentence}
    qa_output = qa_inference(qa_inputs)
    return qa_output['answer']


def extract_parameters(input_text, transaction_type):
    # Parameter Extraction based on transaction type

    qa_inference_object = question_answering_inference()

    if transaction_type == "move":

        return {
            "stock_number": question_stock_number(input_text, qa_inference_object),
            "location_from": question_location_from(input_text, qa_inference_object),
            "location_to": question_location_to(input_text, qa_inference_object)
        }
    elif transaction_type == "adjust":
        return {
            "stock_number": question_stock_number(input_text, qa_inference_object),
            "new_quantity": question_new_quantity(input_text, qa_inference_object),
            "person": question_person(input_text, qa_inference_object),
        }
    elif transaction_type == "dispose":

        return {
            "stock_number": question_stock_number(input_text, qa_inference_object),
            "dispose_quantity": question_dispose_quantity(input_text, qa_inference_object)
        }
    elif transaction_type == "receive":
        return {
            "stock_number": question_stock_number(input_text, qa_inference_object),
            "location": question_location(input_text, qa_inference_object),
            "quantity": question_quantity(input_text, qa_inference_object)
        }
    return None  # Unable to extract parameters


def generate_response(transaction_type, parameters):
    # Response Generation
    if transaction_type == "move":
        return f"Transaction Name: Move\nStock number: {parameters['stock_number']}\nLocation from: {parameters['location_from']}\nLocation to: {parameters['location_to']}"
    elif transaction_type == "adjust":
        return f"Transaction Name: Adjust\nStock number: {parameters['stock_number']}\nNew Quantity: {parameters['new_quantity']}\nNew Person: {parameters['person']}"
    elif transaction_type == "dispose":
        return f"Transaction Name: Dispose\nStock number: {parameters['stock_number']}\nDispose Quantity: {parameters['dispose_quantity']}"
    elif transaction_type == "receive":
        return f"Transaction Name: Receive\nStock number: {parameters['stock_number']}\nLocation: {parameters['location']}\nQuantity: {parameters['quantity']}"
    else:
        return "Unable to generate response"


# Main function for testing
def main():
    input_sentence = input("Enter text command: ")

    # Input Processing
    transaction_type = process_input(input_sentence)

    if transaction_type:
        # Parameter Extraction
        parameters = extract_parameters(input_sentence, transaction_type)

        if parameters:
            # Response Generation
            response = generate_response(transaction_type, parameters)
            print(response)
        else:
            print("Unable to extract parameters")
    else:
        print("Unable to classify transaction type")


if __name__ == "__main__":
    main()
