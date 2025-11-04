
# Import necessary modules and components for the RAG pipeline
from components.retriever import Retriever
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from constants import MODEL, TEMPERATURE

class RAGChain:
    """
    RAGChain encapsulates the Retrieval-Augmented Generation (RAG) pipeline, including model, retriever, prompt, and parser setup.
    """
    def __init__(self):
        """
        Loads environment variables required for the pipeline.
        """
        load_dotenv()

    def get_model(self):
        """
        Initializes and returns the generative AI chat model with specified parameters.
        Returns:
            ChatGoogleGenerativeAI: The language model instance.
        """
        model = ChatGoogleGenerativeAI(
            model=MODEL,
            temperature=TEMPERATURE
        )
        return model

    def get_parser(self):
        """
        Returns a string output parser for model responses.
        Returns:
            StrOutputParser: The output parser instance.
        """
        parser = StrOutputParser()
        return parser

    def get_retriever(self):
        """
        Initializes and returns a retriever object for document search.
        Returns:
            Retriever: The retriever object for fetching relevant documents.
        """
        retriever_obj = Retriever()
        retriever = retriever_obj.get_retriever()
        return retriever

    def get_prompt(self):
        """
        Returns a prompt template for the RAG pipeline.
        Returns:
            PromptTemplate: The prompt template instance.
        """
        prompt = PromptTemplate(
            template="""
            You are a helpful assistant.
            Answer the user's query from the given documents or provided context.
            If the answer is not present inside the provided text, then instead of giving a random answer just give one polite
            response which is similar to "I don't know".

            Provided Context: 
            {context}

            User's query:
            {query}
            """,
            input_variables=['context', 'query']
        )
        return prompt

    def get_chain(self):
        """
        Assembles the RAG pipeline chain by connecting retriever, model, prompt, and parser.
        Returns:
            The complete RAG chain (not fully implemented in this snippet).
        """
        retriever = self.get_retriever()
        model = self.get_model()
        prompt = self.get_prompt()
        parser = self.get_parser()

        def format_context(relevant_docs):
            """
            Formats the relevant documents into a single string for the prompt context.
            Args:
                relevant_docs (list): List of relevant Document objects.
            Returns:
                str: Concatenated page content from relevant documents.
            """
            return '\n\n'.join(doc.page_content for doc in relevant_docs)

        parallel_chain = RunnableParallel(
            {
                'context': retriever | RunnableLambda(format_context),
                'query': RunnablePassthrough()
            }
        )

        rag_chain = parallel_chain | prompt | model | parser
        
        return rag_chain