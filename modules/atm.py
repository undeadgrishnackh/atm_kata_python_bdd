NOTES_INSIDE_THE_ATM = [500, 200, 100, 50, 20, 10]


def withdrawn(amount_to_withdraw):
    """📂 withdrawn the amount of money requested and return the number of notes"""

    notes_count = 0
    amount = int(amount_to_withdraw)

    if amount < 1 or amount > 1500:
        return -1

    for note in NOTES_INSIDE_THE_ATM:
        notes_count += amount // note
        amount = amount - note * (amount // note)

    if amount > 0:
        return 0
    return notes_count
