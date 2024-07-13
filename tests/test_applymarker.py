import pytest


@pytest.fixture
def mark_test(request):
    request.applymarker(pytest.mark.skip(reason="This test will be skipped"))


def test_to_be_marked(request):
    request.applymarker(pytest.mark.skip(reason="This test will be skipped"))
    assert False
