import streamlit as st

st.set_page_config(layout='wide')

# MARKDOWN
st.markdown('*Streamlit* is **really** ***cool!***', help='Example of markdown can do!')

st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

# text area examples
md = st.text_area('Type in your markdown string (without outer quotes)',
                  "Happy Streamlit-ing! :balloon:")

st.code(f"""
import streamlit as st

st.markdown('''{md}''')
""")

st.markdown(md)

# TITLE
st.title('This is a title')

st.title('_Streamlit_ is :blue[cool] :sunglasses:')

st.title('Test achor', anchor=None, help='Testing anchor on st title')


# HEADER
# divider options: bool or “blue”, “green”, “orange”, “red”, “violet”, “gray”/"grey", or “rainbow”
st.header('This is a header with a divider', divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')

# SUB-HEADER
st.subheader('This is a subheader with a divider', divider='rainbow')
st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')

# CAPTION
st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

# CODE
# available language: https://github.com/react-syntax-highlighter/react-syntax-highlighter/blob/master/AVAILABLE_LANGUAGES_PRISM.MD
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python', line_numbers=True)

# TEXT
st.text('This is some text.')

# LATEX
# doc: https://katex.org/docs/supported.html
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# Slider and Divider
st.write("This is some text.")

st.slider("This is a slider", 0, 100, (25, 75))

st.divider()  # 👈 Draws a horizontal rule

st.write("This text is between the horizontal rules.")

st.divider()  # 👈 Another horizontal rule
