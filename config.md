*display only this many notes* limits how many notes will be displayed (a very long list may take a long time to display). A value of 0 or less means there is no limit.

*search string* can filter the set of notes to be examined. It uses the same syntax as searches in the Browse window. For example, you may want to exclude some note types that intentionally have cards in more than one deck.

A note type named Foo can be excluded by setting *search string* to `"-note:Foo"`. If your search string needs quotation marks, they can be escaped with backslash: a note type named Foo Bar can be excluded by setting *search string* to `"-\"note:Foo Bar\""`
