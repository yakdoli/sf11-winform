---
title: intellipromptfeatures.md
original_path: WinForms_Docs/02_Concepts/intellipromptfeatures.md
created_at: 2025-08-05
---






##### IntelliPrompt Features {#intelliprompt-features style="tab-stops: 0pt"}

 

This section covers the following topics:

 

[] 

###### []{#_Code_Snippets}4.6.6.2.2.1 Code Snippets {#code-snippets style="tab-stops: 0pt"}

 

Essential Edit supports an advanced feature of VS 2005 like Code Snippets. It is also used to load / save VS.NET 2005-compatible XML snippets.

 

Code Snippets are inserted into the Edit Control by following the procedure given below:

 

1.   Type the snippet name. For example \"do\".

2.   Pressing the TAB key, or CTRL + \' combination.

3.   Select an item from the list as shown in the image below.

[] 

{border="0"}

Figure 55: Inserting Code Snippets into the Edit Control

 

The code snippets allow you to input data to the highlighted fields.

 

Code Snippets can also be inserted into the Edit Control by using the static **Extract** method of the **CodeSnippetsExtractor** class. The Extract method takes the following two parameters:

 

1.   Path of the folder containing the code snippets.

2.   Instance of the Edit Control into which the extracted code snippet should be inserted.

 

This is illustrated in the code given below.

 

+----------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                       |
|                                                                                                                      |
| []                                                                 |
|                                                                                                                      |
| [CodeSnippetsExtractor.Extract(csharpsnippetsPath, editControl1);] |
+----------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                              |
|                                                                                                                 |
| []                                                            |
|                                                                                                                 |
| [CodeSnippetsExtractor.Extract(vbsnippetsPath, editControl1)] |
+-----------------------------------------------------------------------------------------------------------------+

 

Code Snippets are added to the current language of the Edit Control by using the below given method.

 


  --------------------- --------------------------------------------
  Edit Control Method   Description
  AddCodeSnippet        Adds new code snippet to current language.
  --------------------- --------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                          |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                         |
| [this][.editControl1.AddCodeSnippet([string] title, ArrayList literals, [string] code);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                      |
| [Me][.editControl1.AddCodeSnippet([String] title, ArrayList literals, [String] code)] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The code snippets can also be contained in containers and displayed in the pop-up of the snippets. The static Extract method of the CodeSnippetsExtractor class is used to extract and fill the container object. The container object can be added to the SnippetsContainer of the Edit Control by using the **AddContainer** method. This is illustrated in the code given below.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| [private][ CodeSnippetsContainer container = [new] Syncfusion.Windows.Forms.Edit.Utils.CodeSnippets.[CodeSnippetsContainer](); ] |
|                                                                                                                                                                                                                                                                 |
| [container = CodeSnippetsExtractor.Extract(csharpsnippetsPath[@\"\\Loops\"]);]                                                                                                                       |
|                                                                                                                                                                                                                                                                 |
| [container.Name = [\"Loops\"];]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                 |
| [this][.editControl1.Language.SnippetsContainer.AddContainer(container);]                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                    |
|                                                                                                                                                                                                       |
| []                                                                                                                                                  |
|                                                                                                                                                                                                       |
| [container [As] CodeSnippetsContainer = [New] Syncfusion.Windows.Forms.Edit.Utils.CodeSnippets.CodeSnippetsContainer()] |
|                                                                                                                                                                                                       |
| [container = CodeSnippetsExtractor.Extract(vbsnippetsPath [\"\\Loops\"])]                                                                  |
|                                                                                                                                                                                                       |
| [container.Name = [\"Loops\"]]                                                                                                             |
|                                                                                                                                                                                                       |
| [Me][.editControl1.Language.SnippetsContainer.AddContainer(container)]                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Code snippets can also be created by using the configuration file. For example, the code snippet for a structure in C# can be created as shown below.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<CodeSnippetsContainer Name =[\"Container 2\"]\>]                                        |
|                                                                                                                                                       |
| [\<CodeSnippet Format =[\"1.0.0\"]\>]                                                      |
|                                                                                                                                                       |
| [       \<Header\>]                                                                                               |
|                                                                                                                                                       |
| [        \<Title\>[struct]\</Title\>]                                                        |
|                                                                                                                                                       |
| [         \<Shortcut\>[struct]\</Shortcut\>]                                                 |
|                                                                                                                                                       |
| [ \<Description\>Code snippet [for] [struct]\</Description\>]           |
|                                                                                                                                                       |
| [     \</Header\>]                                                                                                |
|                                                                                                                                                       |
| [     \<Snippet\>]                                                                                                |
|                                                                                                                                                       |
| [          \<Declarations\>]                                                                                      |
|                                                                                                                                                       |
| [        \<Literal\>]                                                                                             |
|                                                                                                                                                       |
| [         \<ID\>name\</ID\>]                                                                                      |
|                                                                                                                                                       |
| [         \<ToolTip\>Struct name\</ToolTip\>]                                                                     |
|                                                                                                                                                       |
| [        \<Default\>MyStruct\</Default\>]                                                                         |
|                                                                                                                                                       |
| [      \</Literal\>]                                                                                              |
|                                                                                                                                                       |
| [         \</Declarations\>]                                                                                      |
|                                                                                                                                                       |
| [       \<Code Language =[\"csharp\"]\>\<\![CDATA\[[struct] \$name\$] |
|                                                                                                                                                       |
| [       {]                                                                                                        |
|                                                                                                                                                       |
| []                                                                                                                |
|                                                                                                                                                       |
| [       }\]\]\>]                                                                                                  |
|                                                                                                                                                       |
| [       \</Code\>]                                                                                                |
|                                                                                                                                                       |
| [\</Snippet\>]                                                                                                    |
|                                                                                                                                                       |
| [\</CodeSnippet\>]                                                                                                |
|                                                                                                                                                       |
| [\</CodeSnippetsContainer\>]                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The Literal element is used to identify a replacement for a piece of code that is entirely contained within the snippet, but one that will likely be customized after it is inserted into the code. For example, literal strings, numeric values, and some variable names should be declared as literals. The symbol \$ is placed at the beginning and end of the literal ID element value. For example, if a literal has an ID element that contains the value MyID, you must reference that literal in the code element as \$MyID\$. All code snippets must be placed between \<\![CDATA\[ and \]\]\> brackets.

[] 

Showing Code Snippets

[] 

[You can programmatically show the choice list of code snippets by calling ShowCodeSnippets method given below.]

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                    |
|                                                                                                                                                                                   |
| []                                                                                                                              |
|                                                                                                                                                                                   |
| [// Shows the code snippets\' choice list.\                                                                                                                                       |
| ][this][.editControl1.ShowCodeSnippets();] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                             |
|                                                                                                                                                                                |
| []                                                                                                                           |
|                                                                                                                                                                                |
| [\' Shows the code snippets\' choice list.\                                                                                                                                    |
| ][Me][.editControl1.ShowCodeSnippets()] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Border Settings

[] 

Border can be set for the active code snippets by using the **DrawCodeSnippetBorder** property of the Edit Control.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                  |
|                                                                                                                                                                 |
| []                                                                                                            |
|                                                                                                                                                                 |
| [this][.editControl1.DrawCodeSnippetBorder = [true];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                           |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [Me][.editControl1.DrawCodeSnippetBorder = [True]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

A sample demonstrating the above feature is available in the following sample installation path.

 

***..\\My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Edit.Windows\\Samples\\2.0\\Intellisense Functions\\ContextSnippetsDemo***

[]{#p76} 

 

###### []{#_Context_Choice}4.6.6.2.2.2 Context Choice {#context-choice style="tab-stops: 0pt"}

[] 

The Context Choice support allows you to create pop-ups for displaying a list of options that are used to complete what the user is typing. This feature is modeled on the **List Members** intellisense feature of Visual Studio, and is very convenient when editing programming languages. For example, in C# or VB.NET, when the . (period) character is typed after a class instance, a pop-up containing all the members of the class gets displayed. As you type in the editor, the list automatically changes selection to synchronize with the text that has been entered. You can also autocomplete the word by using the UP/DOWN ARROW keys to choose the Context Choice item and pressing the TAB key. The Context Choice pop-up can be dismissed by pressing the ESC key.

[] 

{border="0"}

Figure 56: Context Choice List

[] 

The Context Choice displaying characters are specified in the configuration file by using the **DropContextChoiceList** field in the lexem for the corresponding character. If you wish to display the Context Choice dropdown in response to the period (\".\") or comma (\",\") being typed, use the following XML code.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][lexem][ ][BeginBlock][=\".\"][ ][Type][=\"Operator\"][ ][DropContextChoiceList][=\"true\"/\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][lexem][ ][BeginBlock][=\",\"][ ][Type][=\"Operator\"][ ][DropContextChoiceList][=\"true\"/\>] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The preceding code has to be placed within the [\<][lexems][\>] section of the configuration file.

[] 

AutoCompleteSingleLexem

[] 

The **AutoCompleteSingleLexem** property indicates whether the Context Choice list gets autocompleted when a single lexem remains in the list.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                   |
| [this][.editControl1.AutoCompleteSingleLexem = [true];] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                             |
|                                                                                                                                                                |
| []                                                                                                           |
|                                                                                                                                                                |
| [Me][.editControl1.AutoCompleteSingleLexem = [True]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Populating the Context Choice List Items

[] 

The Context Choice list is populated by handling the **ContextChoiceOpen** event of the Edit Control, and adding items to the **Items** collection associated with the **IContextChoiceController** object.

[] 


  -------------------- -------------------------------------------------------------------
  Edit Control Event   Description
  ContextChoiceOpen    This event occurs when the Context Choice window has been opened.
  -------------------- -------------------------------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [private][ [void] editControl1_ContextChoiceOpen(Syncfusion.Windows.Forms.Edit.Interfaces.[IContextChoiceController] controller)]          |
|                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [// Add items to the Items collection associated with the IContextChoiceController object.]                                                                                                                             |
|                                                                                                                                                                                                                                                                           |
| [controller.Items.Add([\"Method\"], [\"Method\"], [this].editControl1.ContextChoiceController.Images\[[\"Image0\"]\]);]                     |
|                                                                                                                                                                                                                                                                           |
| [controller.Items.Add([\"FindText\"], [\"FindText\"], [this].editControl1.ContextChoiceController.Images\[[\"Image1\"]\]);    ]             |
|                                                                                                                                                                                                                                                                           |
| [controller.Items.Add([\"GetTextAsHTML\"], [\"GetTextAsHTML\"], [this].editControl1.ContextChoiceController.Images\[[\"Image2\"]\]);]       |
|                                                                                                                                                                                                                                                                           |
| [controller.Items.Add([\"LoadFile\"], [\"LoadFile\"], [this].editControl1.ContextChoiceController.Images\[[\"Image3\"]\]);]                 |
|                                                                                                                                                                                                                                                                           |
| [controller.Items.Add([\"ToString\"], [\"ToString\"], [this].editControl1.ContextChoiceController.Images\[[\"Image4\"]\]);]                 |
|                                                                                                                                                                                                                                                                           |
| [controller.Items.Add([\"Event\"], [\"Event\"], [this].editControl1.ContextChoiceController.Images\[[\"Image5\"]\]);                      ] |
|                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] editControl1_ContextChoiceOpen([ByVal] controller [As] Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController) [Handles] EditControl1.ContextChoiceOpen] |
|                                                                                                                                                                                                                                                                                                                                                               |
| [\' Add items to the Items collection associated with the IContextChoiceController object.]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                               |
| [controller.Items.Add([\"Method\"], [\"Method\"], [Me].editControl1.ContextChoiceController.Images([\"Image0\"]))]                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                               |
| [controller.Items.Add([\"FindText\"], [\"FindText\"], [Me].editControl1.ContextChoiceController.Images([\"Image1\"]))]                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                               |
| [controller.Items.Add([\"GetTextAsHTML\"], [\"GetTextAsHTML\"], [Me].editControl1.ContextChoiceController.Images([\"Image2\"]))]                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                               |
| [controller.Items.Add([\"LoadFile\"], [\"LoadFile\"], [Me].editControl1.ContextChoiceController.Images([\"Image3\"]))]                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                               |
| [controller.Items.Add([\"ToString\"], [\"ToString\"], [Me].editControl1.ContextChoiceController.Images([\"Image4\"]))]                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                               |
| [controller.Items.Add([\"Event\"], [\"Event\"], [Me].editControl1.ContextChoiceController.Images([\"Image5\"]))]                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[\
]Adding Custom Images to List Items

[] 

Custom images can also be added to the Context Choice list items by indexing them into the **Images** collection of the IContextChoiceController object associated with the Edit Control. The Images collection of the IContextChoiceController can be populated by using the code given below.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                              |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [int][ index = 0;]                                                                                                     |
|                                                                                                                                                                                                             |
| [foreach][ ([Image] img [in] [this].imageList1.Images)] |
|                                                                                                                                                                                                             |
| [{]                                                                                                                                                                     |
|                                                                                                                                                                                                             |
| [// Populating images using an external ImageList.]                                                                                                       |
|                                                                                                                                                                                                             |
| [this][.editControl1.ContextChoiceController.AddImage([\"Image\"] + index.ToString(), img);]    |
|                                                                                                                                                                                                             |
| [index++;]                                                                                                                                                              |
|                                                                                                                                                                                                             |
| [}     ]                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                    |
|                                                                                                                                                                                                       |
| []                                                                                                                                                  |
|                                                                                                                                                                                                       |
| [Dim][ index [As] [Integer] = 0]                                       |
|                                                                                                                                                                                                       |
| [Dim][ img [As] Image]                                                                      |
|                                                                                                                                                                                                       |
| [For][ [Each] img [In]  [Me].imageList1.Images]   |
|                                                                                                                                                                                                       |
| [\' Populating images using an external ImageList.]                                                                                                 |
|                                                                                                                                                                                                       |
| [Me][.editControl1.ContextChoiceController.AddImage([\"Image\"] + index.ToString(), img)] |
|                                                                                                                                                                                                       |
| [index += 1]                                                                                                                                                      |
|                                                                                                                                                                                                       |
| [Next][ img]                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

List Item ToolTip

[] 

ToolTip text is specified for each Context Choice list item while adding the items to the IContextChoiceController, as shown in the following code snippet.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                 |
| [// Specify tooltip text for each Context Choice list item.]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                 |
| [controller.Items.Add([\"LoadFile\"], [\"Use this method to open a file in EditControl.\"], [this].editControl1.ContextChoiceController.Images\[[\"Image3\"]\]);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                              |
| [\' Specify tooltip text for each Context Choice list item.]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                              |
| [controller.Items.Add([\"LoadFile\"], [\"Use this method to open a file in EditControl.\"], [Me].editControl1.ContextChoiceController.Images\[[\"Image3\"]\])] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Customization

[] 

[Border Settings]

[] 

The border color of the Context Choice form is set by using the **ContextChoiceBorderColor** property.

[] 


+-----------------------------------+----------------------------------------------------------------------------------+
| Edit Control Property             | Description                                                                      |
+-----------------------------------+----------------------------------------------------------------------------------+
| ContextChoiceBorderColor          | Specifies the color of the Context Choice form border.                           |
|                                   |                                                                                  |
|                                   |                                                                                  |
|                                   |                                                                                  |
|                                   | Used when UseXPStyle property is set to \'False\'. Otherwise 3D border is drawn. |
+-----------------------------------+----------------------------------------------------------------------------------+


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                                        |
| []                                                                                                                                   |
|                                                                                                                                                                                        |
| [this][.editControl1.ContextChoiceBorderColor = System.Drawing.[Color].Red;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                           |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [Me][.editControl1.ContextChoiceBorderColor = System.Drawing.Color.Red] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Size Settings

 

The size of the Context Choice form can be set by using the ContextChoiceSize property.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [this][.editControl1.ContextChoiceSize = [new] System.Drawing.[Size](100, 50);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                   |
|                                                                                                                                                                                      |
| []                                                                                                                                 |
|                                                                                                                                                                                      |
| [Me][.editControl1.ContextChoiceSize = [New] System.Drawing.Size(100, 50)] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Context Choice Operations

 

The Edit Control provides the following set of events for performing Context Choice operations.

 


  ------------------------- --------------------------------------------------------------------
  Edit Control Event        Description
  ContextChoiceBeforeOpen   This event occurs when the Context Choice window is about to open.
  ------------------------- --------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [private][ [void] editControl1_ContextChoiceBeforeOpen([object] sender, System.ComponentModel.[CancelEventArgs] e)] |
|                                                                                                                                                                                                                                                                         |
| [{                        ]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
| [// Display Context Choice popup if the lexem used to invoke Context Choice is \"this\" or \"me\" only]                                                                                                               |
|                                                                                                                                                                                                                                                                         |
| [int][ ind = GetContextChoiceCharIndex(lexemLine);]                                                                                                                                |
|                                                                                                                                                                                                                                                                         |
| [ILexem lex = lexemLine.LineLexems\[ind-1\] [as] ILexem;]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [if][ ((lex.Text == [\"this\"]) \|\| (lex.Text == [\"me\"]))]                                                                        |
|                                                                                                                                                                                                                                                                         |
| [e.Cancel = [false];]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| [else]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [// Cancels the display of the Context Choice list.]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [e.Cancel = [true];]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Private][ [Sub] editControl1_ContextChoiceBeforeOpen([ByVal] sender [As] [Object], [ByVal] e [As] System.ComponentModel.CancelEventArgs) [Handles] EditControl1.ContextChoiceBeforeOpen] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\' Display Context Choice popup if the lexem used to invoke the Context Choice is \"this\" or \"me\" only]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Dim][ ind [As] [Integer] = GetContextChoiceCharIndex(lexemLine)]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [ Dim][ lex [As] ILexem = lexemLine.LineLexems(ind - 1)]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [If][ lex.Text = [\"this\"] [OrElse] lex.Text = [\"me\"] [Then]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [e.Cancel = [False]]                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Else]                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\' Cancel the display of the Context Choice list.]                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [e.Cancel = [True]]                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [If]]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


  ------------------------------------- -------------------------------------------------------------------
           Edit Control Event           Description
  ContextChoiceClose                    This event occurs when the Context Choice window has been closed.
  ------------------------------------- -------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                          |
| [private][ [void] editControl1_ContextChoiceClose(Syncfusion.Windows.Forms.Edit.Interfaces.[IContextChoiceController] controller, System.Windows.Forms.[DialogResult] dialogresult)] |
|                                                                                                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                          |
| [// Clear the Context Choice items. ]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                          |
| [this][.editControl1.ContextChoiceController.Items.Clear();]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] editControl1_ContextChoiceClose([ByVal] controller [As] Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController, [ByVal] dialogresult [As] System.Windows.Forms.DialogResult) [Handles] EditControl1.ContextChoiceClose] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\' Clear the Context Choice items.]                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Me][.editControl1.ContextChoiceController.Items.Clear()]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


  --------------------------------- ----------------------------------------------------------------------------------------------------------------------------
           Edit Control Event       Description
  ContextChoiceItemSelected         This event is raised when a Context Choice list item is selected.
  ContextChoiceSelectedTextInsert   This event is raised when the editor is about to insert selected Context Choice item to the text. Action can be cancelled.
  --------------------------------- ----------------------------------------------------------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [private][ [void] editControl1_ContextChoiceItemSelected(Syncfusion.Windows.Forms.Edit.Interfaces.[IContextChoiceController] sender, Syncfusion.Windows.Forms.Edit.[ContextChoiceItemSelectedEventArgs] e)] |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [// Gets the selected item.]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [IContextChoiceController controller = sender [as] IContextChoiceController;]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [string][ selectedItemText = e.SelectedItem.Text;]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ [Sub] editControl1_ContextChoiceItemSelected([ByVal] sender [As] Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController, [ByVal] e [As] Syncfusion.Windows.Forms.Edit.ContextChoiceItemSelectedEventArgs) [Handles] EditControl1.ContextChoiceItemSelected] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\' Gets the selected item.]                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Dim][ controller [As] IContextChoiceController = sender]                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Dim][ selectedItemText [As] [String] = e.SelectedItem.Text]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [private][ [void] editControl1_ContextChoiceSelectedTextInsert(Syncfusion.Windows.Forms.Edit.Interfaces.[IContextChoiceController] sender, Syncfusion.Windows.Forms.Edit.[ContextChoiceTextInsertEventArgs] e)] |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [IContextChoiceController controller = sender [as] IContextChoiceController;]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [// Gets the displayed text.]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [string][ displayText = e.DisplayText;]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [// Gets the text to be inserted.]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [string][ insertText = e.InsertText;]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [// Gets the item selected.]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [string][ selectedItemText = e.SelectedItem.Text;]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] editControl1_ContextChoiceSelectedTextInsert([ByVal] sender [As] Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController, [ByVal] e [As] Syncfusion.Windows.Forms.Edit.ContextChoiceTextInsertEventArgs) [Handles] EditControl1.ContextChoiceSelectedTextInsert] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ controller [As] IContextChoiceController = sender]                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\' Gets the displayed text.]                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ displayText [As] [String] = e.DisplayText]                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\' Gets the text to be inserted.]                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ insertText [As] [String] = e.InsertText]                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\' Gets the item selected.]                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ selectedItemText [As] [String] = e.SelectedItem.Text]                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub] [\'editControl1_ContextChoiceSelectedTextInsert]]                                                                                                                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Filtering AutoComplete Items

[] 

Edit Control provides options to filter items in AutoComplete. This can be done by using the **FilterAutoCompleteItems** property.

 


  ------------------------- --------------------------------------------------------------------------------------------
  Edit Control Property     Description
  FilterAutoCompleteItems   Gets / sets value indicating whether Context Choice items should be filtered while typing.
  ------------------------- --------------------------------------------------------------------------------------------


[] 

FilterAutoCompleteItems property when set to **True**, filters the item in the AutoComplete Context Choice, and the filtered item alone will be visible. When set to **False**, all the items will be visible, and the selection will be navigated to the item.

[] 

{border="0"}

Figure 57: Filtering Items in AutoComplete Context Choice

[] 

Showing / Hiding Context Choice Pop-up

[] 

You can also programmatically show / hide the Context Choice pop-up by calling the **ShowContextChoice** and

**CloseContextChoice** methods.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| [// Shows the Context Choice pop-up window.\                                                                                                                                                      |
| ][this][.editControl1.ShowContextChoice();]                |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [// Closes the ContextChoice pop-up window.\                                                                                                                                                      |
| ][this][.editControl1.CloseContextChoice();] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                             |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [\' Shows the Context Choice pop-up window.\                                                                                                                                                   |
| ][Me][.editControl1.ShowContextChoice()]                |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [\' Closes the ContextChoice pop-up window.\                                                                                                                                                   |
| ][Me][.editControl1.CloseContextChoice()] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A sample demonstrating the Context Choice feature is available in the below sample installation path.

 

***..\\My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Edit.Windows\\Samples\\2.0\\Intellisense Functions\\ContextChoiceandPromptDemo***

 

**See Also**

 

[Context Prompt]{.UGHyperlink}[]{.UGHyperlink}

 

###### []{#p77}[]{#_Context_Prompt}4.6.6.2.2.3 Context Prompt {#context-prompt style="tab-stops: 0pt"}

[] 

The **Context Prompt** feature allows you to create pop-ups for displaying variations of syntax for the text input by using the[ ][[Context Choice.]{.UGHyperlink}]() This feature is modeled on the **Parameter Info** intellisense feature of Visual Studio. Each of the context prompt items can have a syntax specifier string and text message providing additional information on each item. The user is able to scroll through the syntax variations either by using the UP/DOWN ARROW keys or clicking on the UP/DOWN buttons on the pop-up.

[] 

{border="0"}

Figure 58: Context Prompt Pop-Up

[] 

The Context Prompt displaying characters are specified in the configuration file by using the **DropContextPrompt** field in the lexem for the corresponding character. If you wish to display the ContextPrompt pop-up in response to the opening brace - \"(\" or opening curly brace -\"{\" being typed, use the following XML code.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][lexem][ ][BeginBlock][=\"(\"][ ][Type][=\"Operator\"][ ][DropContextPrompt][=\"true\"/\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][lexem][ ][BeginBlock][=\"{\"][ ][Type][=\"Operator\"][ ][DropContextPrompt][=\"true\"/\>] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The preceding code has to be placed within the [\<][lexems][\>] section of the configuration file.

[] 

Populating Context Prompt Popup

[] 

The Context Prompt is populated by handling the **ContextPromptOpen** event of Edit Control, and adding new prompts using the **AddPrompt** method.

[] 


  -------------------- ------------------------------------------------------------
  Edit Control Event   Description
  ContextPromptOpen    This event occurs when the Context Prompt has been opened.
  -------------------- ------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                  |
| [private][ [void] editControl1_ContextPromptOpen([object] sender, Syncfusion.Windows.Forms.Edit.[ContextPromptUpdateEventArgs] e)]           |
|                                                                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                  |
| [// Populate the Context Prompt.]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                  |
| [e.AddPrompt( [\"Control.Items.Add(string text, string tooltipText, int imageIndex, int selectedImageIndex)\"], [\"Specify the text of the item, its tooltip text, image index and selected image index\"] );] |
|                                                                                                                                                                                                                                                                                                  |
| [e.AddPrompt( [\"Control.Items.Add(string text, string tooltipText, int imageIndex)\"], [\"Specify the text of the item, its tooltip text, and image index\"] );]                                              |
|                                                                                                                                                                                                                                                                                                  |
| [e.AddPrompt( [\"Control.Items.Add(string text, string tooltipText)\"], [\"Specify the text of the item, and its tooltip text\"] );]                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] editControl1_ContextPromptOpen([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Edit.ContextPromptUpdateEventArgs) [Handles] EditControl1.ContextPromptOpen] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\' Populate the Context Prompt.]                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [e.AddPrompt([\"Control.Items.Add(string text, string tooltipText, int imageIndex, int selectedImageIndex)\"], [\"Specify the text of the item, its tooltip text, image index and selected image index\"])]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [e.AddPrompt([\"Control.Items.Add(string text, string tooltipText, int imageIndex)\"], [\"Specify the text of the item, its tooltip text, and image index\"])]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [e.AddPrompt([\"Control.Items.Add(string text, string tooltipText)\"], [\"Specify the text of the item, and its tooltip text\"])]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Customization**

 

**Background Brush**

[] 

The brush for the Context Prompt background is set by using the **ContextPromptBackgroundBrush** property of the Edit Control.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [this][.editControl1.ContextPromptBackgroundBrush = [new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[GradientStyle].BackwardDiagonal, System.Drawing.[Color].PapayaWhip, System.Drawing.[Color].LemonChiffon);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                        |
| [Me][.editControl1.ContextPromptBackgroundBrush = [New] Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.BackwardDiagonal, System.Drawing.Color.PapayaWhip, System.Drawing.Color.LemonChiffon)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Border Settings

[] 

The border color of the Context Prompt form is set by using the **ContextPromptBorderColor** property.

[] 


+-----------------------------------+------------------------------------------------------------------------------+
| Edit Control Property             | Description                                                                  |
+-----------------------------------+------------------------------------------------------------------------------+
| ContextPromptBorderColor          | Specifies the color of the Context Choice form border.                       |
|                                   |                                                                              |
|                                   |                                                                              |
|                                   |                                                                              |
|                                   | Used when UseXPStyle property is set to False. Otherwise 3D border is drawn. |
+-----------------------------------+------------------------------------------------------------------------------+


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                          |
|                                                                                                                                                                                         |
| []                                                                                                                                    |
|                                                                                                                                                                                         |
| [this][.editControl1.ContextPromptBorderColor = System.Drawing.[Color].Pink;] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                            |
|                                                                                                                                                               |
| []                                                                                                          |
|                                                                                                                                                               |
| [Me][.editControl1.ContextPromptBorderColor = System.Drawing.Color.Pink] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Size Settings

 

The size of the Context Prompt form can be set by using the below given properties.

[] 


  ---------------------------- -----------------------------------------------------------------------------------
  Edit Control Property        Description
  ContextPromptSize            Gets / sets the size of the Context Prompt form.
  UseCustomSizeContextPrompt   Gets / sets a value indicating whether custom Context Prompt size should be used.
  ---------------------------- -----------------------------------------------------------------------------------


 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [this][.editControl1.ContextPromptSize = [new] System.Drawing.[Size](125, 75);] |
|                                                                                                                                                                                                                |
| [this][.editControl1.UseCustomSizeContextPrompt = [true];]                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                   |
|                                                                                                                                                                                      |
| []                                                                                                                                 |
|                                                                                                                                                                                      |
| [Me][.editControl1.ContextPromptSize = [New] System.Drawing.Size(125, 75)] |
|                                                                                                                                                                                      |
| [Me][.editControl1.UseCustomSizeContextPrompt = [True]]                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Context Prompt Operations

 

The Edit Control provides the following set of events for performing Context Prompt operations.

 


  ------------------------------- ----------------------------------------------------------------------------------------
  Edit Control Event              Description
  ContextPromptBeforeOpen         This event occurs when the Context Prompt window is about to open. User can cancel it.
  ContextPromptClose              This event occurs when the Context Prompt window has been closed.
  ContextPromptSelectionChanged   This event occurs when a Context Prompt item has been selected.
  ------------------------------- ----------------------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [// Store the lexem name invoking the ContextPrompt popup.]                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [string][ contextPromptLexem = [\"\"];]                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [private][ [void] editControl1_ContextPromptBeforeOpen([object] sender, System.ComponentModel.[CancelEventArgs] e)]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [{                 ]                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [ILexem][ lex;]                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [ILexemLine][ lexemLine = [this].editControl1.GetLine([this].editControl1.CurrentLine);]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [// Gets the index of the current word in that line.]                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [int][ ind = GetContextPromptCharIndex(lexemLine);]                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [if][ (ind\<=0)]                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [e.Cancel = [true];]                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [return][;]                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [lex = lexemLine.LineLexems\[ind-1\] [as] [ILexem];]                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [               ]                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [// If the count is less than \'2\', do not show the Context Prompt popup.]                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [if][ (lexemLine.LineLexems.Count\<2)]                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [e.Cancel = [true];]                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [else]                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [// Display Context Choice popup if the lexem used to invoke them is \"this\" or \"me\" only.]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [if][ ((lex.Text == [\"Chat\"]) \|\| (lex.Text == [\"Database\"]) \|\| (lex.Text == [\"NewFile\"]) \|\| (lex.Text == [\"Find\"]) \|\| (lex.Text == [\"Home\"]) \|\| (lex.Text == [\"PieChart\"]) \|\| (lex.Text == [\"Tools\"]))] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [this][.contextPromptLexem = lex.Text;]                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [e.Cancel = [false];]                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [else]                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [e.Cancel = [true];]                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\' Store the lexem name invoking the Context Prompt popup.]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ contextPromptLexem [As] [String] = [\"\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Private][ [Sub] editControl1_ContextPromptBeforeOpen([ByVal] sender [As] [Object], [ByVal] e [As] System.ComponentModel.CancelEventArgs) [Handles] editControl1.ContextPromptBeforeOpen]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ lex [As] ILexem]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ lexemLine [As] ILexemLine = [Me].editControl1.GetLine([Me].editControl1.CurrentLine)]                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\' Gets the index of the current word in that line.]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ ind [As] [Integer] = GetContextPromptCharIndex(lexemLine)]                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [If][ ind \<= 0 [Then]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [e.Cancel = [True]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Return]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [End][ [If]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [lex = lexemLine.LineLexems(ind - 1) ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\' If the count is less than \'2\', do not show the Context Prompt popup.]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [If][ lexemLine.LineLexems.Count \< 2 [Then]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [e.Cancel = [True]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Else]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\' Display Context Choice popup if the lexem used to invoke them is \"this\" or \"me\" only.]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [If][ lex.Text = [\"Chat\"] [OrElse] lex.Text = [\"Database\"] [OrElse] lex.Text = [\"NewFile\"] [OrElse] lex.Text = [\"Find\"] [OrElse] lex.Text = [\"Home\"] [OrElse] lex.Text = [\"PieChart\"] [OrElse] lex.Text = [\"Tools\"] [Then]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.contextPromptLexem = lex.Text]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [e.Cancel = [False]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Else]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [e.Cancel = [True]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [End][ [If]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [End][ [If]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                        |
| [// Clear the Context Prompt lexem name on close.]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                        |
| [private][ [void] editControl1_ContextPromptClose([object] sender, Syncfusion.Windows.Forms.Edit.[ContextPromptCloseEventArgs] e)] |
|                                                                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                        |
| [this][.contextPromptLexem = [\"\"];]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                        |
| [}     ]                                                                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [\' Clear the Context Prompt lexem name on close.]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] editControl1_ContextPromptClose([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Edit.ContextPromptCloseEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [Me][.contextPromptLexem = [\"\"]]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                               |
| [// Display the selected Context Prompt item\'s index.]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                               |
| [private][ [void] editControl1_ContextPromptSelectionChanged(Syncfusion.Windows.Forms.Edit.Forms.Popup.[ContextPrompt] sender, Syncfusion.Windows.Forms.Edit.[ContextPromptSelectionChangedEventArgs] e)] |
|                                                                                                                                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                               |
| [Console][.WriteLine([\"SelectedIndex : \"] + e.SelectedIndex.ToString());]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                               |
| [Console][.WriteLine([\"ContextPromptSelectionChanged\"]);      ]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                               |
| [}     ]                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\' Display the selected Context Prompt item\'s index.]                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] editControl1_ContextPromptSelectionChanged([ByVal] sender [As] Syncfusion.Windows.Forms.Edit.Forms.Popup.ContextPrompt, [ByVal] e [As] Syncfusion.Windows.Forms.Edit.ContextPromptSelectionChangedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Console.WriteLine([\"SelectedIndex : \"] + e.SelectedIndex.ToString())]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Console.WriteLine([\"ContextPromptSelectionChanged\"])]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Advanced Customization

 

If you wish to do some advanced customization in the Context Prompt feature, like highlighting the current parameter to be input in bold, you can use the **ContextPromptOpen** and **ContextPromptUpdate** events.

 

For example, add the bolded items in the **ContextPromptOpen** event handler. The indices for the exact position of the text that needs to be bolded has to be manually calculated and specified along with some text information associated with that particular argument. The following code snippet illustrates this.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [// To display some text in bold within the prompt.]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                         |
| [private][ [void] editControl1_ContextPromptOpen([object] sender, Syncfusion.Windows.Forms.Edit.[ContextPromptUpdateEventArgs] e)]                  |
|                                                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| [Console][.WriteLine([\"ContextPromptOpen\"]);]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                         |
| [                        ]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                         |
| [// Bolded Items should be added in this handler.]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [ContextPromptItem item = [null];      ]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                         |
| [item = e.AddPrompt( [\"Control.Items.Add(string text, string tooltipText, int imageIndex, int selectedImageIndex)\"], [\"Specify the text of the item, its tooltip text, image index and selected image index\"] );] |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                         |
| [// Specify the text to be displayed in bold in the Context Prompt.]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                         |
| [item.BoldedItems.Add( 18, 11, [\"Text to be added\"] );]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [item.BoldedItems.Add( 31, 18, [\"Text of the tooltip\"] );]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| [item.BoldedItems.Add( 51, 14, [\"Zero-based index of the image or -1 if no image should be used.\"] );]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| [item.BoldedItems.Add( 67, 14, [\"Zero-based index of the image for selection or -1 if no image should be used.\"] );]                                                                                                                       |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                         |
| [item = e.AddPrompt( [\"Control.Items.Add(string text, string tooltipText, int imageIndex)\"], [\"Specify the text of the item, its tooltip text, and image index\"] );]                                              |
|                                                                                                                                                                                                                                                                                                         |
| [item.BoldedItems.Add( 18, 11, [\"Text to be added\"] );]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [item.BoldedItems.Add( 31, 18, [\"Text of the tooltip\"] );]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| [item.BoldedItems.Add( 51, 14, [\"Zero-based index of the image or -1 if no image should be used.\"] );]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| [    ]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                         |
| [item = e.AddPrompt( [\"Control.Items.Add(string text, string tooltipText)\"], [\"Specify the text of the item, and its tooltip text\"] );]                                                                           |
|                                                                                                                                                                                                                                                                                                         |
| [item.BoldedItems.Add( 18, 11, [\"Text to be added\"] );]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [item.BoldedItems.Add( 31, 18, [\"Text of the tooltip\"] );]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\' To display some text in bold within the prompt.]                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] editControl1_ContextPromptOpen([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Edit.ContextPromptUpdateEventArgs) [Handles] EditControl1.ContextPromptOpen] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Console.WriteLine([\"ContextPromptOpen\"])]                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\' Bolded Items should be added in this handler.]                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Dim][ item [As] ContextPromptItem]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [item = e.AddPrompt([\"Control.Items.Add(string text, string tooltipText, int imageIndex, int selectedImageIndex)\"], [\"Specify the text of the item, its tooltip text, image index and selected image index\"])]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\' Specify the text to be displayed in bold in the Context Prompt.]                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [item.BoldedItems.Add(18, 11, [\"Text to be added\"])]                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [item.BoldedItems.Add(31, 18, [\"Text of the tooltip\"])]                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [item.BoldedItems.Add(51, 14, [\"Zero-based index of the image or -1 if no image should be used.\"])]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [item.BoldedItems.Add(67, 14, [\"Zero-based index of the image for selection or -1 if no image should be used.\"])]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [item = e.AddPrompt([\"Control.Items.Add(string text, string tooltipText, int imageIndex)\"], [\"Specify the text of the item, its tooltip text, and image index\"])]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [item.BoldedItems.Add(18, 11, [\"Text to be added\"])]                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [item.BoldedItems.Add(31, 18, [\"Text of the tooltip\"])]                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [item.BoldedItems.Add(51, 14, [\"Zero-based index of the image or -1 if no image should be used.\"])]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [item = e.AddPrompt([\"Control.Items.Add(string text, string tooltipText)\"], [\"Specify the•\_]]                                                                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Select the items that should be bolded in the ContextPromptUpdate event handler. The following code snippet illustrates this.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                          |
| [private][ [void] editControl1_ContextPromptUpdate([object] sender, Syncfusion.Windows.Forms.Edit.[ContextPromptUpdateEventArgs] e)] |
|                                                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                          |
| [// Select the items that should be bolded.]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                          |
| [if][( e.List.SelectedItem != [null] )]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| [// Get list of the lexems that are inside the current stack.]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                          |
| [IList list = editControl1.GetLexemsInsideCurrentStack( [false] );]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                          |
| [if][( list == [null] ) [return];]                                                                                                                        |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| [int][ iBoldedIndex = 0;]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                          |
| [foreach][( ILexem lexem [in] list )]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                          |
| [if][( lexem.Text == [\",\"] )]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                          |
| [iBoldedIndex++;]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| [if][( iBoldedIndex \>= e.List.SelectedItem.BoldedItems.Count )]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                          |
| [e.List.SelectedItem.BoldedItems.SelectedItem = [null];]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                          |
| [else]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                          |
| [// Gets or sets selected item.]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                          |
| [e.List.SelectedItem.BoldedItems.SelectedItem = e.List.SelectedItem.BoldedItems\[iBoldedIndex\];]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                          |
| [}         ]                                                                                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] editControl1_ContextPromptUpdate([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Edit.ContextPromptUpdateEventArgs) [Handles] EditControl1.ContextPromptUpdate] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\' Select the items that should be bolded.]                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [If][ [Not] (e.List.SelectedItem [Is] [Nothing]) [Then]]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\' Get list of the lexems that are inside the current stack.]                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ list [As] IList = editControl1.GetLexemsInsideCurrentStack([False])]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [If][ list [Is] [Nothing] [Then]]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Return]                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [End][ [If]]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ iBoldedIndex [As] [Integer] = 0]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ lexem [As] ILexem]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [For][ [Each] lexem [In] list]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [If][ lexem.Text = [\",\"] [Then]]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [iBoldedIndex += 1]                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [End][ [If]]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Next][ lexem]                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [If][ iBoldedIndex \>= e.List.SelectedItem.BoldedItems.Count [Then]]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [e.List.SelectedItem.BoldedItems.SelectedItem = [Nothing]]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Else]                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\' Gets or sets selected item.]                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [e.List.SelectedItem.BoldedItems.SelectedItem = e.List.SelectedItem.BoldedItems(iBoldedIndex)]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [End][ [If]]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [End][ [If]]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Showing / Hiding Context Prompt Pop-up**

 

You can also programmatically show / hide the Context Prompt pop-up using the **ShowContextPrompt** and **CloseContextPrompt** methods.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| [// Shows the Context Prompt pop-up window.\                                                                                                                                                      |
| ][this][.editControl1.ShowContextPrompt();]                |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| [// Closes the Context Prompt pop-up window.\                                                                                                                                                     |
| ][this][.editControl1.CloseContextPrompt();] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                              |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [\' Shows the Context Prompt pop-up window.\                                                                                                                                                    |
| ][Me][.editControl1.ShowContextPrompt()]                 |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [\' Closes the Context Prompt pop-up window.\                                                                                                                                                   |
| ][Me][.editControl1.CloseContextPrompt();] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

A sample demonstrating the Context Prompt feature is available in the below sample installation path.

 

***..\\My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Edit.Windows\\Samples\\2.0\\Intellisense Functions\\ContextChoiceandPromptDemo***

 

[]{#p78} 

###### []{#_Context_ToolTip}4.6.6.2.2.4 Context ToolTip {#context-tooltip style="tab-stops: 0pt"}

[] 

The **Context ToolTip** displays helpful tooltips when the mouse is hovered over a lexem in the Edit Control. This feature is modeled on the **Quick Info** intellisense feature of Visual Studio. Whenever the mouse hovers over a token, the UpdateContextTooltip event is fired for quick information on the lexem. If some text information is provided, it is displayed in a tooltip.

[] 

{border="0"}

Figure 59: Context ToolTip

 

The Context ToolTip can be populated with additional information on the corresponding lexem by handling the **UpdateContextTooltip** event of Edit Control.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                      |
| [private][ [void] editControl1_UpdateContextToolTip([object] sender, Syncfusion.Windows.Forms.Edit.Dialogs.UpdateTooltipEventArgs e)] |
|                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [        [if]( e.Text == [string].Empty )]                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [                [Point] pointVirtual = editControl1.PointToVirtualPosition( [new] [Point]( e.X, e.Y ) );]                                                        |
|                                                                                                                                                                                                                                                                      |
| [                [if]( pointVirtual.Y \> 0 )]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [                {]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [                        [// Get the current line]]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                      |
| [                        ILexemLine line = editControl1.GetLine( pointVirtual.Y );]                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [                        [if]( line != [null] )]                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| [                        {]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [                                [// Get tokens from the current line]]                                                                                                                                    |
|                                                                                                                                                                                                                                                                      |
| [                                ILexem lexem = line.FindLexemByColumn( pointVirtual.X );]                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| [                                [if]( lexem != [null] )]                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [                                {]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [                                        [// Set the desired information tooltip]]                                                                                                                         |
|                                                                                                                                                                                                                                                                      |
| [                                        e.Text = [\"This is additional information on \"] + lexem.Text;]                                                                                                 |
|                                                                                                                                                                                                                                                                      |
| [                                }]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [                        }]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [                }]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Private][ [Sub] editControl1_UpdateContextToolTip([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Edit.Dialogs.UpdateTooltipEventArgs) [Handles] EditControl1.UpdateContextToolTip] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [        [If] e.Text = [String].Empty [Then]]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            [Dim] pointVirtual [As] Point = editControl1.PointToVirtualPosition([New] Point(e.X, e.Y))]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            [If] pointVirtual.Y \> 0 [Then]]                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                [\' Get the current line]]                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                [Dim] line [As] ILexemLine = editControl1.GetLine(pointVirtual.Y)]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                [If] [Not] (line [Is] [Nothing]) [Then]]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                    [\' Get tokens from the current line]]                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                    [Dim] lexem [As] ILexem = line.FindLexemByColumn(pointVirtual.X)]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                    [If] [Not] (lexem [Is] [Nothing]) [Then]]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                        [\' Set the desired information tooltip]]                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                       e.Text = [\"This is additional information on \"] + lexem.Text;]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                    [End] [If]]                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                [End] [If]]                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            [End] [If]]                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [        [End] [If]]                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Customization**

[] 

**Background Brush**

[] 

The brush for the Context ToolTip background can be set by using the **ContextTooltipBackgroundBrush** property.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| [this][.editControl1.ContextTooltipBackgroundBrush = [new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[PatternStyle].Percent05, System.Drawing.[Color].LavenderBlush, System.Drawing.[Color].Khaki);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                             |
| [Me][.editControl1.ContextTooltipBackgroundBrush = [New] Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.PatternStyle.Percent05, System.Drawing.Color.LavenderBlush, System.Drawing.Color.Khaki)] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Border Settings

[] 

The border color of the Context ToolTip form is set by using the **ContextTooltipBorderColor** property.

[] 


+-----------------------------------+------------------------------------------------------------------------------+
| Edit Control Property             | Description                                                                  |
+-----------------------------------+------------------------------------------------------------------------------+
| ContextTooltipBorderColor         | Specifies the color of the Context Tooltip form border.                      |
|                                   |                                                                              |
|                                   |                                                                              |
|                                   |                                                                              |
|                                   | Used when UseXPStyle property is set to False. Otherwise 3D border is drawn. |
+-----------------------------------+------------------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                             |
|                                                                                                                                                                                            |
| []                                                                                                                                       |
|                                                                                                                                                                                            |
| [this][.editControl1.ContextTooltipBorderColor = System.Drawing.[Color].Orange;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                               |
|                                                                                                                                                                  |
| []                                                                                                             |
|                                                                                                                                                                  |
| [Me][.editControl1.ContextTooltipBorderColor = System.Drawing.Color.Orange] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Showing the ToolTip

[] 

The Context ToolTip window can be shown by setting the ShowContextTooltip property to **True**.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                 |
| [// Shows the Context ToolTip pop-up window.\                                                                                                                                                                   |
| ][this][.editControl1.ShowContextTooltip = [true];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                        |
|                                                                                                                                                           |
| []                                                                                                      |
|                                                                                                                                                           |
| [\' Shows the Context ToolTip pop-up window.]                                                           |
|                                                                                                                                                           |
| [Me][.editControl1.ShowContextTooltip = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

ToolTip Delay

[] 

It is also possible to specify the time delay after which the tooltip should be displayed by using the **ToolTipDelay** property.

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[ ]                           |
|                                                                                                                                 |
| []                                                                                          |
|                                                                                                                                 |
| [// Displays the tooltip pop-up after 1000 milliseconds( 1 sec )]             |
|                                                                                                                                 |
| [this][.editControl1.ToolTipDelay = 1000;] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                             |
|                                                                                                                              |
| []                                                                                       |
|                                                                                                                              |
| [\' Displays the tooltip pop-up after 1000 milliseconds( 1 sec )]          |
|                                                                                                                              |
| [Me][.edtiControl1.ToolTipDelay = 1000] |
+------------------------------------------------------------------------------------------------------------------------------+

[] 

Closing the ToolTip

[] 

The Context ToolTip window is closed by using the **CloseContextTooltip** method.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [// Closes the Context ToolTip pop-up window.\                                                                                                                                                     |
| ][this][.editControl1.CloseContextTooltip();] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                               |
|                                                                                                                                                                                                  |
| []                                                                                                                                             |
|                                                                                                                                                                                                  |
| [\' Closes the Context ToolTip pop-up window.\                                                                                                                                                   |
| ][Me][.editControl1.CloseContextTooltip();] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

A sample demonstrating the Context Tooltip feature is available in the below sample installation path.

 

***..\\My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Edit.Windows\\Samples\\2.0\\Intellisense Functions\\ContextTooltipDemo***

[]{#p79} 

[]{#related-topics}

