from app.core.llm import llm


def main():
    response = llm.invoke("Say hello in one sentence.")
    print(response.content)


if __name__ == "__main__":
    main()