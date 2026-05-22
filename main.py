import io
import csv
from daytona import Daytona
from langchain_daytona import DaytonaSandbox


data = [
    ["Date", "Product", "Units Sold", "Revenue"],
    ["2025-08-01", "Widget A", 10, 250],
    ["2025-08-02", "Widget B", 5, 125],
    ["2025-08-03", "Widget A", 7, 175],
    ["2025-08-04", "Widget C", 3, 90],
    ["2025-08-05", "Widget B", 8, 200],
]


def create_csv(data: list[list]) -> bytes:
    text_buf = io.StringIO()
    writer = csv.writer(text_buf)
    writer.writerows(data)
    return text_buf.getvalue().encode("utf-8")


def main():
    daytona = Daytona()
    sandbox = daytona.create()
    backend = DaytonaSandbox(sandbox=sandbox)

    csv_bytes = create_csv(data)
    upload_response = backend.upload_files([("/home/daytona/data/sales_data.csv", csv_bytes)])
    print("Upload response:", upload_response)

    exec_response = backend.execute("echo Hello from deepagents-data-analysis!")
    print("Execute response", exec_response.output)


if __name__ == "__main__":
    main()
