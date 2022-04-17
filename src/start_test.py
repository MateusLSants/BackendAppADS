from .start import soma


def test_soma():
    """testing soma"""

    result_soma = soma(1, 2)
    assert result_soma == 3
