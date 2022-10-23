"""Project pipelines."""
from typing import Dict
from kedro.pipeline import Pipeline
from python_kedro.pipelines.data_processing import pipeline as de


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    data_processing_pipeline = de.create_pipeline()

    return {
        "__default__": data_processing_pipeline,
        "data_processing": data_processing_pipeline
    }
