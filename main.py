from daytona import Daytona
from langchain_daytona import DaytonaSandbox


def main():
    sandbox = Daytona().create()
    backend = DaytonaSandbox(sandbox=sandbox)

    response = backend.execute("echo Hello from deepagents-data-analysis!")
    print(response.output)


if __name__ == "__main__":
    main()
