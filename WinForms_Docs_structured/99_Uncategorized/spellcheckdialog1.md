---
title: spellcheckdialog1.md
original_path: WinForms_Docs/99_Uncategorized/spellcheckdialog1.md
created_at: 2025-08-05
---






#### SpellCheckDialog {#spellcheckdialog style="tab-stops: 0pt"}

Spell Checker contains in-built dialog for checking spellings for any input control. SpellChecker will not directly checks spelling for the control. You need to create a wrapper class for that control by implementing the interface **ISpellEditor** and you need to define all the members given in the interface. Using this interface the SpellChecker will interact with any control.

 

Methods

**[]** 


  --------------------------------------------- ------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Method                                        Prototype                                                          Description
  [SpellCheckForEditor]   [SpellCheckForEditor(ISpellEditor editor)]   [If you use this method for checking spellings, the SpellChecker will launch a SpellCheckDialog.Using this dialog you can ignore, replace  and add the selected word to the dictionary.]
  --------------------------------------------- ------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 

Events

***[]*** 


  ------------------------------------------------------- ------------------------------ -------------------------------------------------------------------------------------------------------------------------------------
  Event[]   Parameters                     Description
  [SpellCheckCompleted]             [ Nil]   [This event will be triggered when the spell checking is completed for the input text using SpellCheckDialog]
  ------------------------------------------------------- ------------------------------ -------------------------------------------------------------------------------------------------------------------------------------


**** 

[] 

Spell Checking Using ISpellEditor

In the below code snippet, a wrapper class is created for TextBox by implementing ISpellEditor interface.****

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                             |
| [        [public] [class] [TextBoxSpellEditor] : ISpellEditor]                                      |
|                                                                                                                                                                                                                             |
| [        {]                                                                                                                                                           |
|                                                                                                                                                                                                                             |
| [            [private] [TextBox] textBox;]                                                                               |
|                                                                                                                                                                                                                             |
| [            [public] TextBoxSpellEditor([Control] control)]                                                             |
|                                                                                                                                                                                                                             |
| [            {]                                                                                                                                                       |
|                                                                                                                                                                                                                             |
| [                ControlToCheck = control;]                                                                                                                           |
|                                                                                                                                                                                                                             |
| [            }]                                                                                                                                                       |
|                                                                                                                                                                                                                             |
| [            [public] [Control] ControlToCheck]                                                                          |
|                                                                                                                                                                                                                             |
| [            {]                                                                                                                                                       |
|                                                                                                                                                                                                                             |
| [                [get]]                                                                                                                          |
|                                                                                                                                                                                                                             |
| [                {]                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| [                    [return] textBox;]                                                                                                          |
|                                                                                                                                                                                                                             |
| [                }]                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| [                [set]]                                                                                                                          |
|                                                                                                                                                                                                                             |
| [                {]                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| [                    textBox = [value] [as] [TextBox];]                                             |
|                                                                                                                                                                                                                             |
| [                }]                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| [            }]                                                                                                                                                       |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [            [public] [string] SelectedText]                                                                                |
|                                                                                                                                                                                                                             |
| [            {]                                                                                                                                                       |
|                                                                                                                                                                                                                             |
| [                [get]]                                                                                                                          |
|                                                                                                                                                                                                                             |
| [                {]                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| [                    [return] textBox.SelectedText;]                                                                                             |
|                                                                                                                                                                                                                             |
| [                }]                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| [                [set]]                                                                                                                          |
|                                                                                                                                                                                                                             |
| [                {]                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| [                    textBox.SelectedText = [value];]                                                                                            |
|                                                                                                                                                                                                                             |
| [                }]                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| [            }]                                                                                                                                                       |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [            [public] [string] Text]                                                                                        |
|                                                                                                                                                                                                                             |
| [            {]                                                                                                                                                       |
|                                                                                                                                                                                                                             |
| [                [get]]                                                                                                                          |
|                                                                                                                                                                                                                             |
| [                {]                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| [                    [return] textBox.Text;]                                                                                                     |
|                                                                                                                                                                                                                             |
| [                }]                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| [                [set]]                                                                                                                          |
|                                                                                                                                                                                                                             |
| [                {]                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| [                    textBox.Text = [value];]                                                                                                    |
|                                                                                                                                                                                                                             |
| [                }]                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| [            }]                                                                                                                                                       |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [            [public] [void] Select([int] selectionStart, [int] selectionLength)] |
|                                                                                                                                                                                                                             |
| [            {]                                                                                                                                                       |
|                                                                                                                                                                                                                             |
| [                textBox.Select(selectionStart, selectionLength);]                                                                                                    |
|                                                                                                                                                                                                                             |
| [            }]                                                                                                                                                       |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [            [public] [bool] HasMoreTextToCheck()]                                                                          |
|                                                                                                                                                                                                                             |
| [            {]                                                                                                                                                       |
|                                                                                                                                                                                                                             |
| [                [return] [false];]                                                                                         |
|                                                                                                                                                                                                                             |
| [            }]                                                                                                                                                       |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [            [public] [void] Focus()]                                                                                       |
|                                                                                                                                                                                                                             |
| [            {]                                                                                                                                                       |
|                                                                                                                                                                                                                             |
| [                textBox.Focus();]                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [            }]                                                                                                                                                       |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [            [public] [void] UpdateTextField()]                                                                             |
|                                                                                                                                                                                                                             |
| [            {]                                                                                                                                                       |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [            }]                                                                                                                                                       |
|                                                                                                                                                                                                                             |
| [        }]                                                                                                                                                           |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

After creating the wrapper class, you need to pass the instance of the ISpellEditor to SpellCheckForEditor method as given in the following code snippet:

**** 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                |
| [SpellChecker spellCheck = [new] SpellChecker();]                   |
|                                                                                                                                                |
| [TextBoxSpellEditor spellEditor = [new] TextBoxSpellEditor(txtbx);] |
|                                                                                                                                                |
| [spellCheck.SpellCheckForEditor(spellEditor);]                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Sample Link

To access the sample link:

1.   Open the Synfusion Dashboard.

2.   Select **User Interface**.

3.   Click the WPF drop-down list and select **Explore Samples**.

4.   Navigate to **Tools** -\> **SpellChecker** -\> **SpellCheckerDemo**.

 

 

[]{#related-topics}

