import streamlit as st
from datetime import date

# Page configuration
st.set_page_config(
    page_title="Smart Farming Advisor",
    page_icon="🌱",
    layout="wide"
)

# Application title
st.title("🌱 Smart Farming & Crop Planting Advisor")

st.write(
    "Welcome to your intelligent farming assistant. "
    "Get crop information, planting advice and farm management support."
)

st.divider()

# Sidebar navigation
st.sidebar.title("Farm Navigation")

menu = st.sidebar.selectbox(
    "Select a Section",
    [
        "Dashboard",
        "Farm Details",
        "Crop Selection",
        "Weather Information",
        "Planting Calendar",
        "AI Farming Advisor",
        "Pest & Weather Warnings",
        "Farm Logs"
    ]
)

# Dashboard
if menu == "Dashboard":

    st.header("Farm Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Farm Status", "Active")
    col2.metric("Available Crops", "5")
    col3.metric("System Status", "Online")

    st.subheader("Welcome to Smart Farming")

    st.info(
        "Use the navigation menu to manage your farm "
        "and receive farming recommendations."
    )

# Farm Details
elif menu == "Farm Details":

    st.header("Enter Your Farm Details")

    with st.form("farm_form"):

        farm_name = st.text_input("Farm Name")
        location = st.text_input("Farm Location")

        farm_size = st.number_input(
            "Farm Size (hectares)",
            min_value=0.1
        )

        soil_type = st.selectbox(
            "Soil Type",
            ["Loamy", "Clay", "Sandy", "Silty"]
        )

        submitted = st.form_submit_button("Save Farm Details")

        if submitted:
            st.success("Farm details submitted successfully!")

            st.write("Farm Name:", farm_name)
            st.write("Location:", location)
            st.write("Farm Size:", farm_size)
            st.write("Soil Type:", soil_type)

# Crop Selection
elif menu == "Crop Selection":

    st.header("Select Your Crop")

    crop = st.selectbox(
        "Choose a crop",
        ["Maize", "Rice", "Tomato", "Cassava", "Beans"]
    )

    st.success(f"You selected {crop}.")

    st.write("Crop selection will be connected to the crop recommendation module.")

# Weather Information
elif menu == "Weather Information":

    st.header("Weather Information")

    st.info(
        "Weather information will be connected "
        "to the weather API module."
    )

# Planting Calendar
elif menu == "Planting Calendar":

    st.header("Planting Calendar")

    planting_date = st.date_input(
        "Select your planned planting date",
        value=date.today()
    )

    st.write("Planned planting date:", planting_date)

# AI Farming Advisor
elif menu == "AI Farming Advisor":

    st.header("AI Farming Recommendations")

    question = st.text_area(
        "Ask your farming question"
    )

    if st.button("Get Farming Advice"):
        if question:
            st.info(
                "Your question will be processed "
                "by the AI farming advisor module."
            )
        else:
            st.warning("Please enter a question.")

# Warnings
elif menu == "Pest & Weather Warnings":

    st.header("Farm Alerts")

    st.warning(
        "Weather and pest alerts will appear here "
        "when connected to the relevant modules."
    )

# Farm Logs
elif menu == "Farm Logs":

    st.header("Farm Activity Logs")

    activity = st.text_area(
        "Enter your farming activity"
    )

    if st.button("Save Activity"):
        if activity:
            st.success("Farm activity recorded!")
        else:
            st.warning("Please enter an activity.")

# Footer
st.divider()

st.caption(
    "Smart Farming & Crop Planting Advisor | "
    "Developed by the UI & Frontend Team"
)
