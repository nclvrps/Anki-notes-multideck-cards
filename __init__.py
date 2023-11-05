from aqt import mw, dialogs
from aqt.utils import show_info, qconnect
from aqt.qt import *

config = mw.addonManager.getConfig(__name__)

def display_notes() -> None:
    """Display notes which have cards in more than one deck"""

    multideck_note_ids : list = []
    multideck_note_ids_maxlen : int = config['display only this many notes']
    multideck_note_ids_maxlen_exceeded : bool = False

    search_string : str = config['search string']
    for note_id in mw.col.find_notes(search_string, False):
        multideck_cards_found : bool = False

        card_ids = mw.col.card_ids_of_note(note_id)
        if len(card_ids) < 2:
            continue
        old_deck_id = None
        for card_id in card_ids:
            card = mw.col.get_card(card_id)
            deck_id = card.current_deck_id()
            if old_deck_id is None:
                old_deck_id = deck_id
            elif deck_id != old_deck_id:
                multideck_cards_found = True
                break

        if multideck_cards_found:
            # A maxlen limit of zero or less means no limit
            if multideck_note_ids_maxlen > 0 and len(multideck_note_ids) == multideck_note_ids_maxlen:
                multideck_note_ids_maxlen_exceeded = True
                break

            multideck_note_ids.append(note_id)

    if len(multideck_note_ids) == 0:
        show_info(f"No notes were found (using the configured search string) to have cards in more than one deck.")
    else:
        if multideck_note_ids_maxlen_exceeded:
            show_info(f"Number of notes displayed limited to only: {multideck_note_ids_maxlen}.\n\nThis limit can be configured in Tools / Add-ons / Config.")
        nid_string = ",".join([str(x) for x in multideck_note_ids])
        browser = dialogs.open('Browser', mw)
        # Don't need to include search_string here because the set of nids has already been filtered.
        # But include it as a visual cue to the user.
        browser.setFilter(f'{search_string} nid:{nid_string}')
        browser.setWindowState(
            browser.windowState() & ~Qt.WindowState.WindowMinimized | Qt.WindowState.WindowActive
        )

action = QAction("Notes that have cards in more than one deck", mw)
qconnect(action.triggered, display_notes)
mw.form.menuTools.addAction(action)
