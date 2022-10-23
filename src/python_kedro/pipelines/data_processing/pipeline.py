"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.3
"""
from kedro.pipeline import Pipeline, node, pipeline
from .nodes import test_node

def test_pipeline(**kwargs):
    return Pipeline(
    [
        node(
            func=test_node,
            inputs = None,
            outputs = "test_output",
            name = "test_node",
            tags = ["test"]
        )
    ], tags = ["test_pipeline"])
def create_pipeline(**kwargs) -> Pipeline:
    return test_pipeline()
