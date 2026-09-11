import streamlit as st
from google import genai


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Email Generator",
    page_icon="✉️",
    layout="centered"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .main {
        padding-top: 2rem;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #777;
        font-size: 17px;
        margin-bottom: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# GET GEMINI API KEY
# =========================================================

try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

except Exception:
    st.error("❌ Gemini API key is not configured.")

    st.info(
        "Please add GEMINI_API_KEY in Streamlit Secrets."
    )

    st.stop()


# =========================================================
# GEMINI CLIENT
# =========================================================

@st.cache_resource
def get_gemini_client():

    return genai.Client(
        api_key=GEMINI_API_KEY
    )


client = get_gemini_client()


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">✉️ AI Email Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Create professional emails instantly using Gemini AI'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# EMAIL DETAILS
# =========================================================

st.subheader("📝 Email Details")


email_type = st.selectbox(
    "Email Type",
    [
        "Professional",
        "Job Application",
        "Follow-up",
        "Complaint",
        "Inquiry",
        "Thank You",
        "Meeting Request",
        "Sales",
        "Custom"
    ]
)


recipient = st.text_input(
    "Recipient",
    placeholder="e.g. Hiring Manager, Professor, Client"
)


purpose = st.text_area(
    "What is the purpose of this email?",
    placeholder=(
        "Example: I want to apply for a web development internship."
    ),
    height=120
)


tone = st.selectbox(
    "Tone",
    [
        "Professional",
        "Friendly",
        "Formal",
        "Persuasive",
        "Concise"
    ]
)


length = st.selectbox(
    "Email Length",
    [
        "Short",
        "Medium",
        "Detailed"
    ]
)


additional_details = st.text_area(
    "Additional Details",
    placeholder=(
        "Add deadlines, names, dates, requirements, "
        "or any other important information."
    ),
    height=120
)


# =========================================================
# GENERATE EMAIL
# =========================================================

if st.button(
    "✨ Generate Email",
    type="primary",
    use_container_width=True
):

    # -----------------------------------------------------
    # VALIDATION
    # -----------------------------------------------------

    if not purpose.strip():

        st.warning(
            "⚠️ Please enter the purpose of the email."
        )

        st.stop()


    # -----------------------------------------------------
    # CREATE PROMPT
    # -----------------------------------------------------

    prompt = f"""
You are an expert professional email writer.

Generate a complete email based strictly on the information provided.

EMAIL TYPE:
{email_type}

RECIPIENT:
{recipient if recipient.strip() else "Not specified"}

PURPOSE:
{purpose}

TONE:
{tone}

LENGTH:
{length}

ADDITIONAL DETAILS:
{additional_details if additional_details.strip() else "None"}

IMPORTANT RULES:

1. Create an appropriate subject line.
2. Write a natural and polished email.
3. Match the requested tone.
4. Match the requested length.
5. Do not invent facts, names, dates, companies, or information.
6. Do not explain your answer.
7. Use an appropriate greeting.
8. Use an appropriate closing.
9. Make the email ready to copy and send.
10. Return only the subject and email.

Use this structure:

Subject: [subject]

[email body]
"""


    # -----------------------------------------------------
    # CALL GEMINI
    # -----------------------------------------------------

    try:

        with st.spinner(
            "✨ Gemini is writing your email..."
        ):

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )


        # -------------------------------------------------
        # GET GENERATED EMAIL
        # -------------------------------------------------

        generated_email = response.text


        if not generated_email:

            st.error(
                "❌ Gemini returned an empty response."
            )

            st.stop()


        # -------------------------------------------------
        # DISPLAY RESULT
        # -------------------------------------------------

        st.success(
            "✅ Email generated successfully!"
        )

        st.divider()

        st.subheader(
            "📧 Generated Email"
        )


        edited_email = st.text_area(
            "Edit your email if needed:",
            value=generated_email,
            height=400
        )


        # -------------------------------------------------
        # DOWNLOAD
        # -------------------------------------------------

        st.download_button(
            label="⬇️ Download Email",
            data=edited_email,
            file_name="generated_email.txt",
            mime="text/plain",
            use_container_width=True
        )


    except Exception as error:

        st.error(
            "❌ Unable to generate the email."
        )

        st.warning(
            "Please check your Gemini API key and try again."
        )

        with st.expander("Technical details"):

            st.code(
                str(error)
            )
