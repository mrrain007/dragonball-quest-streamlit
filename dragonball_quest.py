st.title("Dragon Ball Quest")
st.write("Welcome to Dragon Ball Quest! Choose your character to begin your adventure:")

character = st.selectbox("Choose your character", ["Goku", "Vegeta", "Gohan", "Piccolo"])

if st.button("Start Quest"):
    st.write(f"Awesome! {character} is ready to begin their quest.")
    st.write("More game logic goes here...")
  
