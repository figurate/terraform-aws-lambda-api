from diagrams import Diagram
from diagrams.aws.network import APIGateway
from diagrams.aws.compute import Lambda

with Diagram("AWS Lambda API", show=False, direction="TB"):
    APIGateway("api target") >> Lambda("lambda function")
