import streamlit as st

# Initialize session state to store listings
if 'farmer_listings' not in st.session_state:
    st.session_state['farmer_listings'] = []

if 'company_listings' not in st.session_state:
    st.session_state['company_listings'] = []

# Function to display the home page
def home():
    st.title("EarthWise")
    st.subheader("Connecting Farmers and Companies for a Sustainable Future")
    st.write("""
        Welcome to EarthWise, the platform that connects farmers and event managers with organic waste to companies
        that can utilize these materials to create sustainable products. Join us in promoting
        a circular economy and reducing waste.
    """)

# Function to display the farmer section
def farmer_section():
    st.header("Farmer Section")
    st.write("List your organic waste here:")

    farmer_name = st.text_input("Farmer Name")
    contact_info = st.text_input("Contact Information")
    waste_type = st.selectbox("Type of Organic Waste", ["Coconut Peat", "Dried Flowers", "Ice Apple Waste", "Dung", "Other"])
    waste_quantity = st.number_input("Quantity (in kg)", min_value=1)
    waste_description = st.text_area("Description")

    if st.button("Submit"):
        new_listing = {
            "name": farmer_name,
            "contact": contact_info,
            "type": waste_type,
            "quantity": waste_quantity,
            "description": waste_description,
        }
        st.session_state['farmer_listings'].append(new_listing)
        st.success("Your listing has been submitted successfully!")

# Function to display the company section
def company_section():
    st.header("Company Section")
    st.write("Specify your organic waste requirements here:")

    company_name = st.text_input("Company Name")
    contact_info = st.text_input("Contact Information")
    required_waste_type = st.selectbox("Required Waste Type", ["Coconut Peat", "Dried Flowers", "Ice Apple Waste", "Dung", "Other"])
    required_quantity = st.number_input("Required Quantity (in kg)", min_value=1)
    additional_info = st.text_area("Additional Information")

    if st.button("Submit"):
        new_requirement = {
            "name": company_name,
            "contact": contact_info,
            "type": required_waste_type,
            "quantity": required_quantity,
            "info": additional_info,
        }
        st.session_state['company_listings'].append(new_requirement)
        st.success("Your requirements have been submitted successfully!")

# Function to display the matching section
def matching_section():
    st.header("Matching Section")
    st.write("Here are the matches between farmers and companies:")

    farmer_listings = st.session_state['farmer_listings']
    company_listings = st.session_state['company_listings']

    matches = []
    for company in company_listings:
        for farmer in farmer_listings:
            if company['type'] == farmer['type'] and company['quantity'] <= farmer['quantity']:
                matches.append((farmer, company))

    if matches:
        for i, (farmer, company) in enumerate(matches):
            st.subheader(f"Match {i+1}")
            st.write(f"**Farmer Name:** {farmer['name']}")
            st.write(f"**Farmer Contact:** {farmer['contact']}")
            st.write(f"**Waste Type:** {farmer['type']}")
            st.write(f"**Waste Quantity:** {farmer['quantity']} kg")
            st.write(f"**Waste Description:** {farmer['description']}")
            st.write("---")
            st.write(f"**Company Name:** {company['name']}")
            st.write(f"**Company Contact:** {company['contact']}")
            st.write(f"**Required Waste Quantity:** {company['quantity']} kg")
            st.write(f"**Additional Info:** {company['info']}")
            st.write("===")
    else:
        st.write("No matches found.")

# Function to display the contact section
def contact_section():
    st.header("Contact Us")
    st.write("For more information or support, please contact us at:")
    st.write("Email: support@earthwise.com")
    st.write("Phone: +91 9059069630")

# Streamlit app layout
st.sidebar.title("EarthWise")
st.sidebar.header("Navigation")
options = ["Home", "Farmer Section", "Company Section", "Matching Section", "Contact Us"]
selection = st.sidebar.radio("Go to", options)

if selection == "Home":
    home()
elif selection == "Farmer Section":
    farmer_section()
elif selection == "Company Section":
    company_section()
elif selection == "Matching Section":
    matching_section()
elif selection == "Contact Us":
    contact_section()
