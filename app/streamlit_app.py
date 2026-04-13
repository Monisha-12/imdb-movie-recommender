import streamlit as st
from scripts.recommend import recommend_movie

st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

st.title("🎬 Movie Recommendation System")
st.caption("Find similar movies based on storyline using NLP")

user_input = st.text_area("Enter a movie storyline")

if st.button("Recommend"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a storyline")
    else:
        with st.spinner("🔍 Finding similar movies..."):
            results = recommend_movie(user_input)

        if results.empty:
            st.warning("No similar movies found. Try a different storyline.")
        else:
            st.success("Top Recommendations:")

            for _, row in results.iterrows():
                st.subheader(row["Movie Name"])

                score = float(row["Similarity Score"])

                # ⭐ Show score
                st.write(f"⭐ Similarity Score: {score:.2f}")

                # 📊 Progress bar
                st.progress(min(score, 1.0))

                # 🎯 ADD THIS BLOCK HERE
                if score > 0.3:
                    st.success(f"Highly Similar ({score:.2f})")
                elif score > 0.15:
                    st.info(f"Moderately Similar ({score:.2f})")
                else:
                    st.warning(f"Low Similarity ({score:.2f})")

                # 📖 Storyline
                st.write(row["Storyline"])
                st.markdown("---")