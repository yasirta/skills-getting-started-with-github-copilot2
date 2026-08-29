from copy import deepcopy

import pytest

from src.app import activities


@pytest.fixture(autouse=True)
def reset_activities_state():
    baseline = deepcopy(activities)

    activities.clear()
    activities.update(deepcopy(baseline))

    yield

    activities.clear()
    activities.update(deepcopy(baseline))
