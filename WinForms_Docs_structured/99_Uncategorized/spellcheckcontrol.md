---
title: spellcheckcontrol.md
original_path: WinForms_Docs/99_Uncategorized/spellcheckcontrol.md
created_at: 2025-08-05
---








  









### SpellCheckControl {#spellcheckcontrol style="MARGIN-LEFT: 1.8pt; tab-stops: 1.8pt"}

 

The ASP.NET SpellCheckControl component, including an electronic dictionary, allows you to easily perform a spell check on any of the ASP.NET controls text values and automatically provides the user, suggestions for correcting misspelled words using an in-built dialog.

 

[Powerful Spell Check Engine]

 

The SpellCheckControl implements a complex spell checking algorithm. The suggestion list for a misspelled word is generated using **Near Miss Strategy** and **Phonetic** (sounds like) matching.

 

[·      ]The Near Miss Strategy is a simple way to generate the suggestion list with words that closely match the spelling of the mistyped word.

[·      ]A phonetic match provides the suggestion list with words that sound similar to the misspelled word using **Soundex** algorithm.

 

The list is then ranked using the **Edit Distance** algorithm and gets displayed in the Suggestion list.

 

AJAX enabled

 

When spell check is invoked, the SpellCheckControl uses the 2.0 AJAX framework to perform a callback with the sentence to spell check as an argument. The callback then returns the misspelled word and suggestion list which gets displayed in the in-built dialog box to let the user pick the correct words. Using callbacks significantly improves performance and lowers the load on the server.

 

Built-in Integration

 

The Essential Tools RichTextEditor control incorporates SpellCheckControl to automatically support spell check the contents edited by the user. Similarly, the control could be easily integrated with any other custom controls.

 

Client API

 

Simple API on the client side lets you optionally, manually invoke a spell check on any string and also provides a user friendly UI during run time for spell correction.

 

Spell Dialog Form

 

The control comes with a built-in rich dialog form. This aspx page needs to be deployed in the application folder. You can change the style settings and page layout based on your design requirements to fully customize the page.

 

Check For Repeated Words

 

The spell check engine also detects repeated words and lets the user correct it.

 

Check Selection

 

The control can also restrict it\'s spell check to the selected text.

[]{#p143} 

More:









