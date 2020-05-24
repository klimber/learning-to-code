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

    st.header("Aula StreamLit 3")
    
    st.subheader("Como utilizar botões!")
    st.write("Clique no botão a seguir:")
    botao = st.button("Clique em mim!")
    if botao:
        st.write("Você clicou no botão!")
    
    st.subheader("Agora vamos fazer um checkbox!")
    checkbox = st.checkbox("Eu sou um checkbox!")
    if(checkbox):
        st.write("O checkbox está marcado!")

    st.subheader("Agora vamos fazer um radioGroup!")
    radio = st.radio("Um radioGroup tem diversas opções!", ("Eu sou a opção 1", "Opção 2, eu sou"))
    if radio == "Eu sou a opção 1":
        st.write("Você selecionou a primeira opção!")
    if radio == "Opção 2, eu sou":
        st.write("Que a força esteja com você!")
    
    st.subheader("E uma caixa de seleção única?")
    selectBox = st.selectbox("Eu sou a sua caixa de seleção favorita", ("Choose an Option","Red Pill", "Blue Pill", "Yellow Pill?"))
    if selectBox == "Red Pill":
        st.write("Uma verdade desegradável será revelada.")
    if selectBox == "Blue Pill":
        st.write("A ignorância é uma virtude.")
    if selectBox == "Yellow Pill?":
        st.write("Are you okai?")
    
    st.subheader("A famigerada caixa de seleção MÚLTIPLA:")
    multiSelect = st.multiselect("Eu sou a caixa de seleção múltipla, muitos devs não gostam de mim, sniff", ("Press F", "The answer is 42", "All of the above"))
    if "Press F" in multiSelect:
        st.write("You paid the due respect!")
    if "The answer is 42" in multiSelect:
        st.write("Yes, it is.")
    if "All of the above" in multiSelect:
        if len(multiSelect) > 1:
            st.write("Redundant, aren't we?")
        else:
            st.write("This is a multiselection box, you know?")
    
    st.subheader("Dá pra enviar arquivos?")
    st.write("Dá sim, parceiro, saca só:")
    myFile = st.file_uploader("Pode vir quente!", 'csv')
    if myFile is not None:
        st.write("Seu arquivo está seguro em minhas mãos!")
    




if __name__ == "__main__":
    main()