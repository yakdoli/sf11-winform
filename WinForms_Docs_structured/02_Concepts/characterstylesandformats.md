---
title: characterstylesandformats.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\characterstylesandformats.md
created_at: 2025-07-03
---






#### Character Styles and Formats {#character-styles-and-formats style="tab-stops: 0pt"}

 

**Character Styles**

 

**CharacterStyle** class represents character style in the Word document. CharacterStyle has two properties.

 

**StyleType**: returns the StyleType.CharacterStyle

**BaseStyle**: defines the base character style

 

Collection of DocIO character styles is accessible through the **WordDocument.Styles** property.

 


{border="0"}Note: DocIO does not provide support to add user-defined character styles to the document.


 

Class Hierarchy

 

Style

   \|

    CharacterStyle

 

Public Properties

 


  ------------------------- --------------------------------------------------------------------------------------------------------------
  Name                      Description
  BaseStyle                 Gets the base style.
  StyleType                 Gets the type of the style.  
  UseContextualAlternates   Gets or sets a value indicating whether to use contextual alternates (Microsoft Word 2010 specific property)
  Ligatures                 Gets or sets the ligatures type (Microsoft Word 2010 specific property)
  NumberForm                Gets or sets the number form type (Microsoft Word 2010 specific property)
  NumberSpacing             Gets or sets the number spacing type (Microsoft Word 2010 specific property)
  StylisticSet              Gets or sets the stylistic set type (Microsoft Word 2010 specific property)
  ------------------------- --------------------------------------------------------------------------------------------------------------


 

Public Methods

 


  --------------- ----------------------------------------------
  Name            Description
  Clone           Clones itself.
  NameToBuiltIn   Converts string style names to BuiltinStyle.
  --------------- ----------------------------------------------


 

Character Formats

 

**WCharacterFormat** class represents character formatting in the Word document.

 

WCharacterFormat class is used to get or set the formatting for text chunks, special symbol or marker (for example marker of picture, text box, footnote, etc). WCharacterFormat customizes the appearance of the element (for example text chunk or symbol) in the document, starting with font name to the style of texture and spacing between characters.

             

**Class Hierarchy**

 

FormatBase

       \|

       WCharacterFormat

 

**Public Constructor**

 


  --------------------------------------------------- -----------------------------------------------------------
  Name                                                Description
  WCharacterFormat.WCharacterFormat (IWordDocument)   Initializes a new instance of the WCharacterFormat class.
  --------------------------------------------------- -----------------------------------------------------------


 

Public Properties

 


  Name                  Description
  --------------------- ----------------------------------------------------------------------------------
  AllCaps               Gets or sets AllCaps property of text.
  Bidi                  Gets or sets right-to-left property of text.  
  Bold                  Gets or sets bold style.
  BoldBidi              Gets or sets bold property for right-to-left text.  
  Border                Gets border.
  CharacterSpacing      Gets or sets space width between characters.  
  DoubleStrike          Gets or sets doublestrikeout style.  
  Emboss                Gets or sets emboss property of text.  
  Engrave               Gets or sets Engrave property of text.  
  Font                  Gets or sets font as System.Drawing.Font. 
  FontName              Gets or sets font name.
  FontNameBidi          Gets or sets font name for right-to-left text.  
  FontSize              Gets or sets font size (in points).
  FontSizeBidi          Gets or sets font size of the right-to-left text (in points).  
  Hidden                Gets or sets Hidden property of text.  
  HighlightColor        Gets or sets highlight color of text.  
  Italic                Gets or sets italic style.  
  ItalicBidi            Gets or sets italic property for right-to-left text.  
  LineBreak             Gets or sets line break after.  
  OutLine               Gets or sets outline character property.  
  Position              Gets or sets text vertical position.  
  Shadow                Gets or sets shadow property of text.  
  SmallCaps             Gets or sets SmallCaps property of text.  
  Strikeout             Gets or sets strikeout style.  
  SubSuperScript        Gets or sets subscript / superscript mode.  
  TextBackgroundColor   Gets or sets text background color.  
  TextColor             Gets or sets text color.  
  UnderlineStyle        Gets or sets underline style.
  LocaleIdASCII         Gets or sets the locale identifier (language) of the formatted characters.
  LocaleIdFarEast       Gets or sets the locale identifier (language) of the formatted Asian characters.


 

The following example illustrates how to use the WCharacterFormat class.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                            |
| [/][/ Write different font name / font size]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                            |
| [string][\[\] fontNames = [new] [string]\[\] { [\"Times New Roman\"], [\"Verdana\"], [\"Symbol\"], };] |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [IWSection][ section = doc.AddSection();]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                            |
| [IWParagraph][ paragraph;]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                            |
| [IWTextRange][ textRange;]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [for][ ([int] j = 0, len = fontNames.Length; j \< len; j++)]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                            |
| [    paragraph = section.AddParagraph();]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                            |
| [    [string] fontName = fontNames\[j\];]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [    [for] ([int] i = 9; i \< 40; i++)]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                            |
| [        textRange = paragraph.AppendText(fontName + [\" \"] + i.ToString() + [\" \"]);]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                            |
| [        textRange.CharacterFormat.FontSize = i;]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                            |
| [        textRange.CharacterFormat.FontName = fontName;]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                            |
| [        [if] (i \> 15)]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                            |
| [            i += 5;]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                            |
| [    [IWTextRange] txtRange2 = paragraph.AppendText(fontName + [\"34,5 \"]);]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                            |
| [    txtRange2.CharacterFormat.FontSize = ([float])34.5;]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                            |
| [    txtRange2.CharacterFormat.FontName = fontName;]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [// Write bold / italic / underline / strike text.]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                            |
| [paragraph = section.AddParagraph();]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                            |
| [textRange = paragraph.AppendText([\"Bold Text_Bold Text   \"]);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.Bold = [true];]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                            |
| [textRange = paragraph.AppendText([\"Italic Text_Italic Text   \"]);]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.Italic = [true];]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                            |
| [textRange = paragraph.AppendText([\"Underline Text_Underline Text   \"]);]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.UnderlineStyle = [UnderlineStyle].Dash;]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                            |
| [textRange = paragraph.AppendText([\"Strike Text_Strike Text   \"]);]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.Strikeout = [true];]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [textRange = paragraph.AppendText([\"Shadow Text_Shadow Text   \"]);]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.Shadow = [true];]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [paragraph = section.AddParagraph();]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                            |
| [paragraph = section.AddParagraph();]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [textRange = paragraph.AppendText([\"Merged Font Style Text_Merged Font Style Text\"]);]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.Bold = [true];]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.Italic = [true];]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.Strikeout = [true];]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.UnderlineStyle = [UnderlineStyle].Dash;]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                            |
| [// Specify the locale so Microsoft Word recognizes.]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                            |
| [// For the list of locale identifiers see [http://www.microsoft.com/globaldev/reference/lcid-all.mspx]{.underline}.]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                            |
| [// Sets the locale identifier (language) of the formatted characters.\                                                                                                                                                                                                                                    |
| ][textRange.CharacterFormat.LocaleIdASCII = ( [short] )[LocaleIDs].uk_UA; ]                                                                                             |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                            |
| [// or]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.LocaleIdASCII = 1093; ]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                            |
| [// Sets the locale identifier (language) of the formatted Asian characters. ]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.LocaleIdFarEast = 2052]                                                                                                                                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\' Write different font name / font size.]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                            |
| [Dim][ fontNames [As] [String]() = [New] [String]() { [\"Times New Roman\"], [\"Verdana\"], [\"Symbol\"], }] |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                            |
| [Dim][ section [As] IWSection = doc.AddSection()]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                            |
| [Dim][ paragraph [As] IWParagraph]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                            |
| [Dim][ textRange [As] IWTextRange]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                            |
| [Dim][ j [As] [Integer] = 0]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                            |
| [len = fontNames.Length]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                            |
| [Do][ [While] j \< len]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                            |
| [      paragraph = section.AddParagraph()]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                            |
| [Dim][ fontName [As] [String] = fontNames(j)]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                            |
| [      [For] i [As] [Integer] = 9 [To] 39]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                            |
| [            textRange = paragraph.AppendText(fontName & [\" \"] & i.ToString() & [\" \"])]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                            |
| [            textRange.CharacterFormat.FontSize = i]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                            |
| [            textRange.CharacterFormat.FontName = fontName]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                            |
| [            [If] i \> 15 [Then]]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                            |
| [                  i += 5]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                            |
| [            [End] [If]]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                            |
| [      [Next] i]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                            |
| [Dim][ txtRange2 [As] IWTextRange = paragraph.AppendText(fontName & [\"34,5 \"])]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                            |
| [      txtRange2.CharacterFormat.FontSize = [CSng](34.5)]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                            |
| [      txtRange2.CharacterFormat.FontName = fontName]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                            |
| [      j += 1]                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                            |
| [Loop]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\' Write bold / italic / underline / strike text.]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                            |
| [paragraph = section.AddParagraph()]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                            |
| [textRange = paragraph.AppendText([\"Bold Text_Bold Text   \"])]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.Bold = [True]]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                            |
| [textRange = paragraph.AppendText([\"Italic Text_Italic Text   \"])]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.Italic = [True]]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                            |
| [textRange = paragraph.AppendText([\"Underline Text_Underline Text   \"])]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.UnderlineStyle = UnderlineStyle.Dash]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                            |
| [textRange = paragraph.AppendText([\"Strike Text_Strike Text   \"])]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.Strikeout = [True]]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                            |
| [textRange = paragraph.AppendText([\"Shadow Text_Shadow Text   \"])]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.Shadow = [True]]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                            |
| [paragraph = section.AddParagraph()]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                            |
| [paragraph = section.AddParagraph()]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                            |
| [textRange = paragraph.AppendText([\"Merged Font Style Text_Merged Font Style Text\"])]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.Bold = [True]]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.Italic = [True]]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.Strikeout = [True]]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.UnderlineStyle = UnderlineStyle.Dash]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\' Specify the locale so Microsoft Word recognizes.]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\' For the list of locale identifiers, see [http://www.microsoft.com/globaldev/reference/lcid-all.mspx]{.underline}.]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\' Sets the locale identifier (language) of the formatted characters. ]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.LocaleIdASCII = [CType](LocaleIDs.uk_UA, [Short])]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\' or]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.LocaleIdASCII = 1093]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\' Sets the locale identifier (language) of the formatted Asian characters. ]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                            |
| [textRange.CharacterFormat.LocaleIdFarEast = 2052]                                                                                                                                                                                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

