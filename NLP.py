import streamlit as st

def main():
    st.title('NLP Resource Hub')
    st.caption('Click on the arrow in the top left corner to explore the NLP Resource Hub sections.')

    st.sidebar.header('Select the Platform/Tool/Framework')
    sections = [
        'Hugging Face Tasks', 
        'OpenAI Docs', 
        'Langchain', 
        'Langsmith', 
        'ChainLit', 
        'LlamaIndex', 
        'Google Scholar'
    ]
    selection = st.sidebar.radio("Go to", sections)

    if selection == 'Hugging Face Tasks':
         st.subheader('Hugging Face Tasks')
         st.write('Explore a variety of machine learning models and datasets for NLP tasks offered by Hugging Face. This platform is pivotal for anyone looking to experiment with pre-trained models or develop and share their own.')
         st.markdown('[Hugging Face Models](https://huggingface.co/models)')
         st.markdown('[Hugging Face Datasets](https://huggingface.co/datasets)')
         st.markdown('[Hugging Face Tasks](https://huggingface.co/TASKS)')


    elif selection == 'OpenAI Docs':
        st.subheader('OpenAI Documentation')
        st.write('Dive into the comprehensive documentation of OpenAI’s API, where you can learn how to integrate advanced AI models into your applications and services.')
        st.markdown('[OpenAI API Docs](https://beta.openai.com/docs/)')

    elif selection == 'Langchain':
        st.subheader('Langchain')
        st.write('Langchain is a library that enables the combination of language models with other systems to create chain-of-thought reasoning applications. It’s a toolkit for developers to expand the utility of language models.')
        st.markdown('[Langchain](https://www.langchain.com/)')

    elif selection == 'Langsmith':
        st.subheader('Langsmith')
        st.write('It lets you debug, test, evaluate, and monitor chains and intelligent agents built on any LLM framework and seamlessly integrates with LangChain, the go-to open source framework for building with LLMs. LangSmith is developed by LangChain, the company behind the open source LangChain framework.')
        st.markdown('[Langsmith](https://www.langchain.com/langsmith)') # Replace '#' with the actual link.

    elif selection == 'ChainLit':
        st.subheader('ChainLit')
        st.write('Chainlit is an open-source async Python framework that makes it incredibly fast to build Chat GPT like applications with your own business logic and data.')
        st.markdown('[ChainLit](https://docs.chainlit.io/get-started/overview)') # Replace '#' with the actual link.

    elif selection == 'LlamaIndex':
        st.subheader('LlamaIndex')
        st.write('LlamaIndex is a simple, flexible data framework for connecting custom data sources to large language models.')
        st.markdown('[LlamaIndex Documentation](https://www.llamaindex.ai/)') # Replace '#' with the actual link.

    elif selection == 'Google Scholar':
        st.subheader('Google Scholar Research Papers')
        st.write('Google Scholar is a freely accessible web search engine that indexes the full text of scholarly literature across an array of publishing formats and disciplines. Use it to stay up to date with the latest NLP research.')
        st.markdown('[Google Scholar NLP Papers](https://scholar.google.com/)')

    # Creator's credit
    st.markdown("---")
    st.markdown("Provided By,")
    st.markdown("Ankush Mulkar - NLP Engineer") 
    st.markdown('(https://ankushmulkar.github.io/Portfolio/)')
   

    #
if __name__ == "__main__":
    main()

