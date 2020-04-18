import streamlit as st

def main():
    st.title("Hello World, StreamLit")
    
    st.header("Começando a usar StreamLit!")
    
    st.subheader("O que é o StreamLit")
    st.write("O StreamLit é uma ferramenta para exibição de conteúdo, ela é bastante fácil de trabalhar, e sua API permite fazer muitas coisas diferentes!")
    
    st.subheader("É possível adicionar **imagens**!")
    st.image("logo.png")
    
    st.subheader("É possível adicionar **áudios**!")
    # st.audio("audio.webm")
    st.audio(r"https://www.dropbox.com/s/t5sgl6fz11t5bpv/Cartoon%20-%20Why%20We%20Lose%20%28feat.%20Coleman%20Trapp%29%20_NCS%20Release_.mp3?dl=1")
    
    st.subheader("É possível adicionar **vídeos**!")
    st.video("https://www.youtube.com/watch?v=WeJU_HxUxy0")
    
    st.subheader("E utilizar *sintaxe* de ~~html~~ **MarkDown**!")
    st.write('Utilizando "\*" e "~"')

    

if __name__ == "__main__":
    main()