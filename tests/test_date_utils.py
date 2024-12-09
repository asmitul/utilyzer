from datetime import datetime
import pytz
from utilyzer.date_utils import get_day_range


def test_get_day_range():
    # Test current day
    result = get_day_range(0)
    tz = pytz.timezone("Asia/Shanghai")
    now = datetime.now(tz)

    # Basic structure tests
    assert isinstance(result, dict)
    assert "start" in result
    assert "end" in result
    assert "date" in result["start"]
    assert "timestamp" in result["start"]
    assert "date" in result["end"]
    assert "timestamp" in result["end"]

    # Time range tests
    assert (
        result["end"]["timestamp"] - result["start"]["timestamp"] == 86399
    )  # 24h - 1s

    # Format tests
    assert result["start"]["date"].endswith("00:00:00")
    assert result["end"]["date"].endswith("23:59:59")

    # Test past day
    past_result = get_day_range(1)
    assert past_result["start"]["timestamp"] < result["start"]["timestamp"]
    assert past_result["end"]["timestamp"] < result["start"]["timestamp"]
