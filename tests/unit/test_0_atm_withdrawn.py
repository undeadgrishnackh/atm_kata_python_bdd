import pytest

from modules import atm


def describe_configure_the_notes_the_atm_has_inside():
    """📂 configure the notes the ATM has inside"""
    notes_expected_in_the_atm = [500, 200, 100, 50, 20, 10]

    @pytest.mark.parametrize("note", notes_expected_in_the_atm)
    def should_test_something_with_params(note):
        """🧪 should have a specific type of notes"""
        assert note in atm.NOTES_INSIDE_THE_ATM

    def should_not_have_a_5_notes():
        """🧪 should not have a 5$ notes"""
        assert 5 not in atm.NOTES_INSIDE_THE_ATM


def describe_basic_withdrawn():
    """📂 scenario to cover basic withdrawn functionality with only a single type of note"""
    withdrawn_and_expected_notes = [
        (500, 1),
        (1000, 2),
        (1500, 3),
        (200, 1),
        (100, 1),
    ]

    @pytest.mark.parametrize("amount, notes_expected", withdrawn_and_expected_notes)
    def should_test_something_with_params(amount, notes_expected):
        """🧪 should return the correct amount of a single note"""
        assert atm.withdrawn(amount) == notes_expected


def describe_more_complicated_with_multiple_type_of_notes():
    """📂 more complicated scenarios with multiple types of notes"""
    withdrawn_and_expected_notes = [
        (30, 2),
        (40, 2),
        (60, 2),
        (110, 2),
        (1490, 7)
    ]

    @pytest.mark.parametrize("amount, notes_expected", withdrawn_and_expected_notes)
    def should_test_something_with_params(amount, notes_expected):
        """🧪 should return the correct amount of notes, multiple types"""
        assert atm.withdrawn(amount) == notes_expected


def describe_guardians():
    """📂 guardians"""

    def should_raise_an_error_for_amount_below_1():
        """🧪 should raise an error for amount below 1"""
        assert atm.withdrawn(0) == -1

    def should_raise_an_error_for_amount_above_1500():
        """🧪 should raise an error for amount above 1500"""
        assert atm.withdrawn(1501) == -1

    def should_raise_0_notes_for_a_crazy_amount_like_11():
        """🧪 should raise 0 notes for a crazy amount like 11$"""
        assert atm.withdrawn(11) == 0
