import pytest
from main import calculate_api_gravity, calculate_flow_rate

def test_api_gravity():
    assert calculate_api_gravity(1.0) == 10.0
    assert calculate_api_gravity(0.85) == 34.97

def test_flow_rate():
    assert calculate_flow_rate(2, 0.5) == 0.3927