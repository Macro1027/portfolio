import streamlit as st
from streamlit_modal import Modal
from scripts.constant import media, projects, awards, info
from scripts.elements import display_footer

def setup():
    st.set_page_config(page_title='Portfolio' ,layout="wide",page_icon='👧🏻')
    with open("style/style.css") as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)

    st.title("📝 Portfolio")

def display_modal(modal, item):
    if modal.is_open():
        with modal.container():
            st.markdown(f'<h2 class="modal-title">{item["text"]}</h2>', unsafe_allow_html=True)
            st.markdown('<div class="modal-body">', unsafe_allow_html=True)

            # Image
            if "modal-image" in item:
                st.markdown(f'<div class="modal-image"><img src="{item["modal-image"]}" alt="{item["text"]}"></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="modal-image"><img src="{item["image"]}" alt="{item["text"]}"></div>', unsafe_allow_html=True)

            # Text below the image
            st.markdown(f'<div class="modal-text">{item["description"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="modal-text"><a href={item["link"]}>{item["link-text"]}</a></div>', unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)  # Close modal-body

# Example of a responsive layout for your categories
def display_category(category, title):
    modal = Modal(key=title, title="Details")
    st.header(title)
    if "item" not in st.session_state:
        st.session_state["item"] = {}

    for i, item in enumerate(category):
        cols = st.columns(3) if i % 3 == 0 else cols  # Responsive columns
        with cols[i % 3]:
            st.markdown(f'<div class="item-container">', unsafe_allow_html=True)
            st.markdown(f'<div class="image-container"><img src="{item["image"]}" alt="{item["text"]}" style="width:100%; height:200px; object-fit: cover;"></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="text-container">{item["text"]}</div>', unsafe_allow_html=True)
            button_key = f"{title.lower()}-{i}-{item['text']}"
            if st.button("View Details", key=button_key):
                st.session_state["item"] = item
                modal.open()
            st.markdown('</div>', unsafe_allow_html=True)  # Close item-container

    display_modal(modal, st.session_state.get("item", {}))



# Main Function
def main():
    setup()
    display_category(projects, "Projects")
    display_category(awards, "Awards")
    display_category(media, "Media")
    display_footer()

if __name__ == "__main__":
    main()
