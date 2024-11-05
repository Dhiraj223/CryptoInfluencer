from cryptinfluencer import get_llm_response, setup_pinecone, filter_pinecone, VectorStore

def CryticAgent(username, user_query):
    chunks = [{
        "text" : user_query
    }]
    vectorstore = VectorStore()
    vectorstore.add_texts(chunks=chunks, user_id=username)
    vectors = vectorstore.vectors
    index_name = "cryptostore"
    index = setup_pinecone(index_name=index_name, vectors=vectors)
    previous_interactions = filter_pinecone(index=index,user_id=username)
    response = get_llm_response(memory=previous_interactions, user_query=user_query)
    return response

if __name__ == "__main__" :
    username = input("Enter your Username : ")
    print(f"Welcome to CryptoWhiz {username}, how may I help you?")
    while True :
        user_query = input("Enter your Query or type 'quit' to exit: ")
        if user_query != "quit" :
            response = CryticAgent(username=username, user_query=user_query)
            print(response)
        else :
            print(f"Thank you for using our service {username}. Have a great day!")
            break
