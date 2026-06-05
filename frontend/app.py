import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="AI Data Extraction System",
    page_icon="🤖",
    layout="wide"
)

if "documents_loaded" not in st.session_state:
    st.session_state.documents_loaded = 0

if "queries_asked" not in st.session_state:
    st.session_state.queries_asked = 0

st.title("🤖 AI Data Extraction & Query System")



#Sidebar

with st.sidebar:

    st.header("📥 Data Ingestion")

    st.success("🟢 FastAPI Connected")

    # st.info(
    #     """
    #     Vector Database:
    #     Pinecone

    #     Embedding Model:
    #     Llama Text Embed V2

    #     LLM:
    #     GPT-4o-mini
    #     """
    # )

    st.divider()

    load_option = st.radio(
        "Choose Source",
        [
            "URL",
            "PDF",
            "Image"
        ]
    )

    st.divider()

    st.metric(
        "Documents Loaded",
        st.session_state.documents_loaded
    )

    st.metric(
        "Queries Asked",
        st.session_state.queries_asked
    )



#Url Upload

if load_option == "URL":

    url = st.text_input(
        "Enter Website URL"
    )

    if st.button("Load URL"):

        with st.spinner(
            "Extracting and indexing content..."
        ):

            response = requests.post(
                f"{API_URL}/load/url",
                params={
                    "url": url
                }
            )

        if response.status_code == 200:

            st.session_state.documents_loaded += 1

            st.success(
                "URL indexed successfully"
            )

            # st.json(
            #     response.json()
            # )

        else:

            st.error(
                response.text
            )


# PDF upload

elif load_option == "PDF":

    pdf_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if pdf_file:

        if st.button(
            "Process PDF"
        ):

            with st.spinner(
                "Processing PDF..."
            ):

                files = {
                    "file": (
                        pdf_file.name,
                        pdf_file,
                        "application/pdf"
                    )
                }

                data = {
                    "source_type": "file"
                }

                response = requests.post(
                    f"{API_URL}/load",
                    files=files,
                    data=data
                )

            if response.status_code == 200:

                st.session_state.documents_loaded += 1

                st.success(
                    "PDF indexed successfully"
                )

                # st.json(
                #     response.json()
                # )

            else:

                st.error(
                    response.text
                )


# image upload

elif load_option == "Image":

    image_file = st.file_uploader(
        "Upload Image",
        type=[
            "jpg",
            "jpeg",
            "png"
        ]
    )

    if image_file:

        # st.image(
        #     image_file,
        #     caption="Uploaded Image",
        #     use_container_width=True
        # )

        if st.button(
            "Process Image"
        ):

            with st.spinner(
                "Running OCR..."
            ):

                files = {
                    "file": (
                        image_file.name,
                        image_file,
                        image_file.type
                    )
                }

                data = {
                    "source_type": "image"
                }

                response = requests.post(
                    f"{API_URL}/load",
                    files=files,
                    data=data
                )

            if response.status_code == 200:

                st.session_state.documents_loaded += 1

                st.success(
                    "Image indexed successfully"
                )

                # st.json(
                #     response.json()
                # )

            else:

                st.error(
                    response.text
                )


# Two Column

left_col, right_col = st.columns(
    [3, 1]
)

# Right Column

with right_col:

    with st.expander(
        "📘 Supported Sources",
        expanded=True
    ):

        st.markdown(
            """
            • URLs

            • PDFs

            • JPG Images

            • PNG Images

            """
        )

# Left Column

with left_col:

    st.subheader(
        "💬 Ask Questions"
    )

    query = st.text_input(
        "Enter your question"
    )


# Query Section

if st.button(
    "Get Answer"
):

    with st.spinner(
        "Searching documents..."
    ):

        response = requests.post(
            f"{API_URL}/query",
            json={
                "query": query
            }
        )

    if response.status_code == 200:

        st.session_state.queries_asked += 1

        result = response.json()

        # st.success(
        #     "Answer generated successfully"
        # )

        st.markdown(
            "## 🤖 AI Response"
        )

        st.container()

        st.write(
            result["answer"]
        )

    else:

        st.error(
            response.text
        )