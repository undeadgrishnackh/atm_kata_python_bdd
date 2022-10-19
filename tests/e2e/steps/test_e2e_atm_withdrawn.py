import sys

from pytest_bdd import given, when, then, scenarios, parsers

from modules import atm


scenarios('../features/atm_withdrawn.feature')


@given("the ATM machine")
def give_an_atm_machine(mocker):
    mocker.resetall()


@when(parsers.parse("an user wants to withdrawn {amount}"), target_fixture="withdrawn")
def withdrawn(amount, capsys):
    returned_notes_count = atm.withdrawn(amount)
    out, err = capsys.readouterr()
    return returned_notes_count, out.strip(), err.strip()


@then(parsers.parse("the ATM will provide {notes_count} notes"))
def then_the_atm_will_provide_1_note(notes_count, withdrawn):
    returned_notes_count, _out, _err = withdrawn
    assert returned_notes_count == int(notes_count)
