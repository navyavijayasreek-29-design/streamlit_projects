
import requests
import streamlit as st

st.title("Weather API Demo")

# API Key - Demo Mode
API_KEY = st.secrets.get("API_KEY", "demo_key")

# Enter City
city = st.text_input("Enter city", "Chennai")

# Get Weather
if st.button("Get Weather"):

    resp = None

    # Live API only if API key is available
    if API_KEY != "demo_key":

        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        try:

            with st.spinner("Fetching weather..."):

                response = requests.get(
                    url,
                    params=params,
                    timeout=10
                )

                response.raise_for_status()
                data = response.json()

            resp = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "condition": data["weather"][0]["main"],
                "humidity": data["main"]["humidity"],
            }

        except requests.exceptions.Timeout:
            st.error("Request timed out. Try again.")
            st.stop()

        except requests.exceptions.HTTPError:
            st.error("API error. Check API key or city.")
            st.stop()

        except Exception as e:
            st.error(f"Request failed: {e}")
            st.stop()

    # Demo Mode
    if resp is None:

        st.info("Using simulated data (Demo Mode).")

        resp = {
            "city": city,
            "temperature": 30,
            "condition": "Sunny",
            "humidity": 65,
        }

    # Display Weather
    st.subheader("Weather Details")

    st.json(resp)

    # Display Metrics
    c1, c2, c3 = st.columns(3)

    c1.metric("Temperature", f"{resp['temperature']}°C")
    c2.metric("Condition", resp["condition"])
    c3.metric("Humidity", f"{resp['humidity']}%")

# HTTP Methods
st.markdown("---")

st.subheader("HTTP Methods")

st.markdown("""
- **GET** - Retrieve data
- **POST** - Send data
- **PUT** - Update data
- **DELETE** - Delete data
""")

# API Information
st.markdown("---")

st.subheader("API Information")

st.write("API Provider: OpenWeatherMap")
st.write("Weather API is used to retrieve weather information.")
