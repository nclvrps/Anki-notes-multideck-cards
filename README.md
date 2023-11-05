# Anki-notes-multideck-cards
Anki add-on for displaying notes whose cards are not all in the same deck

== Description ==

Notes can have multiple cards, and each of these cards could be in a different deck. However, you often want all cards of any given note to be in the same deck.

But when moving cards between decks, you might accidentally leave some cards of a note in the old deck while moving the others to the new deck.

This add-on finds notes whose cards are not all in the same deck, and displays them in the Browse window.

== Configuration ==

This add-on can be configured with Tools / Add-ons / Config. Changes only take effect when Anki is restarted.

You can limit the maximum number of found notes to display in the Browse window.

You can also configure a search string to filter the set of notes to be examined.

== How it could be done manually instead ==

Without this add-on, you could perform the same function manually by doing the following:
* Switch to Notes mode in the Browse window.
* Make sure that the Deck column is displayed in Notes mode (by default, this column is only displayed in Cards mode).
* Click on the Deck column header to sort the table by that column.
* Scroll to the top (or bottom) of the table, and see if there are any Deck values that show a number in parentheses instead of a deck name. That means the note has cards in more than one deck, and the number in parentheses shows the number of different decks the note's cards are in.
