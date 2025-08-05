---
title: lexicalanalysisandsemanticparsing.md
original_path: WinForms_Docs/99_Uncategorized/lexicalanalysisandsemanticparsing.md
created_at: 2025-08-05
---








  









### Lexical Analysis And Semantic Parsing {#lexical-analysis-and-semantic-parsing style="tab-stops: 0pt"}

[] 

Text parsing occurs when a new document is loaded or when modifications occur in an already loaded document. In case of modifications, the Edit Control intelligently reparses only what is necessary to ensure that the text model is up to date with the contents of the editor. Ideally, parsing the Edit Control occurs in a two-phase approach. The first phase is lexical analysis and the second one is semantic parsing.

[] 

Lexical Analysis breaks up text into tokens, while semantic parsing goes a step further and assigns extra contextual meaning to the tokens. Semantic relations recognized by the semantic parser are based on how human beings represent knowledge of the world. Semantic parsing allows tokens to be accessed and processed in a more meaningful way than lexical analysis, moving the automation of understanding the tokens to a higher level. A semantic parser consumes the output of the lexical analyzer, and operates by analyzing the sequence of tokens returned. The parser matches these sequences to an end state which may be one of the possible end states. The end states define the goals of the parser. When an end state is reached, the program using the parser implements some action-specific code.

[] 

Additionally, parsers can detect the situation when no legal end state can be reached, from the sequence of tokens that have been processed.

[] 

Lexical Analysis

[] 

Lexical Analysis is the process of scanning text in a document and breaking it up into meaningful tokens. The purpose of lexical analyzers is to take a stream of input characters, and decode them into higher level tokens that a semantic parser can understand. In this stage, the text is split into tokens with the help of some special rules specified by the user. For instance, the user can specify \"=+\" or \"end if \" expressions as single tokens using the Split tag in the configuration file. Tokens are plain text, and have no additional information or meaning associated with them.

[] 

Semantic Parsing

[] 

In this stage, the syntax highlighting rules are applied. These rules can be as simple as identifying the format name of the token, and applying the appropriate font or color settings. But this simple two-phase procedure was not very flexible in complex scenarios involving embedded scripts. Hence the entire process has been enhanced from the very beginning, by merging the lexical analysis and semantic parsing.

 

The **Parser** property indicates the parser used for parsing the currently loaded document in the Edit Control. The parsing process could be performed for any (or all) of the following purposes - syntax highlighting, intellisense, outlining and so on. The rules for the parsing process are specified in the XML based configuration file used.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                   |
|                                                                                                                                                  |
| []                                                                                             |
|                                                                                                                                                  |
| [// Indicates the parser used for parsing the currently loaded document in the Edit Control. ] |
|                                                                                                                                                  |
| [RenderableLexemParser lexemParser = [this].editControl1.Parser;]                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                       |
|                                                                                                                                                                                                          |
| []                                                                                                                                                     |
|                                                                                                                                                                                                          |
| [\' Indicates the parser used for parsing the currently loaded document in the Edit Control. ]                                                         |
|                                                                                                                                                                                                          |
| [Dim][ lexemParser [As] RenderableLexemParser = [Me].editControl1.Parser] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Parsing Modes

[] 

Edit Control supports several modes of text parsing which can be specified to the **ParsingMode** property by using the **TextParsingMode** enumerator. The default value of the ParsingMode property is set to **PartialParsingNoFallback**.

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Edit Control Property             | Description                                                                                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ParsingMode                       | Gets / sets text parsing mode. User can select between high parsing speed or high syntax highlighting accuracy. The options provided are |
|                                   |                                                                                                                                          |
|                                   | *[]*                                                       |
|                                   |                                                                                                                                          |
|                                   | [·      ]FullParsing                                                                                        |
|                                   |                                                                                                                                          |
|                                   | [·      ]PartialParsingNoFallback                                                                           |
|                                   |                                                                                                                                          |
|                                   | [·      ]PartialParsingWithFallback                                                                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+


[] 

When ParsingMode is set to **FullParsing**, the text in the Edit Control is parsed completely and accurately, and then features like syntax highlighting, outlining, bracket highlighting, indentation guidelines, and so on are applied. FullParsing is time consuming, and can potentially cause performance issues as Edit Control stays frozen till this process is completed. Ideally, it should be undertaken for small files only.

 

When ParsingMode is set to **PartialParsingNoFallback**, text parsing is done on a need basis, i.e., only those regions of the text in the Edit Control that have to be displayed get parsed. The text parsing is not always accurate in such scenarios, and hence features like syntax highlighting, outlining, bracket highlighting, indentation guidelines, and so on, maybe incorrectly applied. This is the fastest ParsingMode in the Edit Control, and hence should be used in large file handling scenarios.

 

When ParsingMode is set to **PartialParsingWithFallback**, text parsing is once again done on a need basis like in PartialParsingNoFallback mode. The only difference is that if the text gets incorrectly parsed, the incorrectly parsed text is treated as of type regular \"Text\" format, and features like syntax highlighting, outlining, bracket highlighting, indentation guidelines, and so on, get applied as per Text format specifications in the associated configuration settings.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [// ParsingMode is set to FullParsing.]                                                                                                                        |
|                                                                                                                                                                                                                  |
| [this][.editControl1.ParsingMode = Syncfusion.Windows.Forms.Edit.Enums.[TextParsingMode].FullParsing;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                     |
|                                                                                                                                                                                        |
| []                                                                                                                                   |
|                                                                                                                                                                                        |
| [\' ParsingMode is set to FullParsing.]                                                                                              |
|                                                                                                                                                                                        |
| [Me][.editControl1.ParsingMode = Syncfusion.Windows.Forms.Edit.Enums.TextParsingMode.FullParsing] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p91} 

[]{#related-topics}

