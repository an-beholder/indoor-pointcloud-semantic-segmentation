import ollama

def ollama_function():
    res=ollama.list()
    for model in res.models:
        print(model.model)
    model=input("请输入模型名称：")
    messages=[]
    while(True):
        chat=input("请输入：")
        if chat=="exit":
            break
        messages.append({"role": "user", "content": chat})
        res=ollama.chat(
            model=model,
            messages=messages
            )
        print(res.message.content)
        
    
if __name__ == "__main__":
    ollama_function()
