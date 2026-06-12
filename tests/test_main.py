import pytest
from main import main

def test_main():
    with pytest.raises(SystemExit):
        main()
