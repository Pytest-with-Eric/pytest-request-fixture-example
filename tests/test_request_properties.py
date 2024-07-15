import pytest


def test_show_request_properties(request):
    print(f"Test Function Name: {request.node.name}")
    print(f"Test Module Name: {request.node.module.__name__}")
    print(f"Test File Path: {request.node.fspath}")
    print(f"Test Directory: {request.node.fspath.dirname}")
    print(f"Test File Name: {request.node.fspath.basename}")
    print(f"Test Function: {request.node.originalname}")
    print(f"Test Class: {request.node.cls}")
    print(f"Test Function Scope: {request.scope}")
    print(f"Test Function Keywords: {request.keywords}")


# Parameterize a test function with different pairs of numbers
@pytest.mark.parametrize("a,b", [(1, 2), (2, 3), (3, 4)])
def test_addition(request, a, b):
    # Accessing the parameters used in this test instance
    params = request.node.callspec.params

    # Print the parameters and result
    print(f"Parameters: {params}")
