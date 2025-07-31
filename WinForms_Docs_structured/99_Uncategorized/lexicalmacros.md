---
title: lexicalmacros.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\lexicalmacros.md
created_at: 2025-07-03
---






#### Lexical Macros {#lexical-macros style="tab-stops: 0pt"}

 

Edit Control allows you to define macros that represent regular expression elements. These macros are valid for use in any regular expression.

 

**Usage**

 

Using defined macros is easy. To reference a macro, simply type its name within curly braces ({ \... }). The following examples illustrate this feature better:

 

[•] This regular expression uses a macro that represents the character class \[0-9\] to build a decimal number regular expression.

{DigitMacro}+ (\\. {DigitMacro}+)?

 

[•] This regular expression builds a C# identifier using two macros.

(\_ \| {AlphaMacro})({WordMacro})\*

 

**Built-In Macros**

 

Edit Control recognizes a number of built-in macros. If a language definition defines a lexical macro of the same name as a built-in lexical macro, the user\'s definition will override the system definition. The following table summarizes the built-in macros of Edit Control.

 


  ---------------------------------- -------------------------------------------------------------------------------------------------------------------------------
  Macro                              Description
  AllMacro                           Contains all Unicode characters. This is the same as \[\\u0000-\\uFFFF\]
  AlphaMacro                         Contains all Unicode alphanumeric digits. This is the same as: \[a-zA-Z\]
  DigitMacro                         Contains all Unicode decimal digits. This is the same as: \[0-9\]
  HexDigitMacro                      Contains all Unicode hexadecimal digits. This is same as:\[0-9a-fA-F\]
  LineTerminatorMacro                Contains all Unicode line terminators. This is the same as: \[\\r\\n\\u2028\\u2029\]
  LineTerminatorWhitespaceMacro      Contains all Unicode line terminators and whitespace characters. This is the same as: \[ \\r\\n\\u2028\\u2029\\f\\t\\v\\x85\]
  NonAlphaMacro                      Contains the inverse of AlphaMacro.
  NonDigitMacro                      Contains the inverse of DigitMacro.
  NoneMacro                          Contains no characters.
  NonHexDigitMacro                   Contains the inverse of HexDigitMacro.
  NonLineTerminatorMacro             Contains the inverse of LineTerminatorMacro.
  NonLineTerminatorWhitespaceMacro   Contains the inverse of LineTerminatorWhitespaceMacro.
  NonWhitespaceMacro                 Contains the inverse of WhitespaceMacro.
  NonWordMacro                       Contains the inverse of WordMacro.
  WhitespaceMacro                    Contains all Unicode whitespace characters. This is the same as: \[\\f\\t\\v\\x85\]
  WordMacro                          Contains all Unicode word characters. This is the same as: \[0-9a-zA-Z\]
  ---------------------------------- -------------------------------------------------------------------------------------------------------------------------------


 

The lexical macros are used to specify configuration settings, and can be added to the current configuration language settings, as shown below.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [// Create and add a lexical macro to the Edit Control.LexicalMacrosManager\'s collection.]                                                                               |
|                                                                                                                                                                                                                             |
| [// The Add method also returns the IMacro object associated with the lexical macro.]                                                                                     |
|                                                                                                                                                                                                                             |
| [IMacro macro = [this].Edit Control1.LexicalMacrosManager.Add([\"testMacro\"], [\".+\"]);]                           |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [// Consider a scenario where configuration settings are being created dynamically in code.]                                                                              |
|                                                                                                                                                                                                                             |
| [// Create a config lexem that belongs to a custom format. ]                                                                                                              |
|                                                                                                                                                                                                                             |
| [ConfigLexem configLex = [new] ConfigLexem([\"\<%@\"], [\"%\>\"], FormatType.Custom, [false]);] |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [// The actual regex can then be substituted with the lexical macro while defining the config lexem.]                                                                     |
|                                                                                                                                                                                                                             |
| [// NameInConfig returns the name of the macro rounded with braces, like \"{testmacro}\".]                                                                                |
|                                                                                                                                                                                                                             |
| [configLex.ContinueBlock = macro.NameInConfig;]                                                                                                                                         |
|                                                                                                                                                                                                                             |
| [configLex.IsContinueRegex = [true];]                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                             |
| [\' Create and add a lexical macro to the Edit Control.LexicalMacrosManager\'s collection.]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                             |
| [\' The Add method also returns the IMacro object associated with the lexical macro.]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                             |
| [Dim][ macro [As] IMacro = [Me].Edit Control1.LexicalMacrosManager.Add([\"testMacro\"], [\".+\"])]                             |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                             |
| [\' Consider a scenario where configuration settings are being created dynamically in code.]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                             |
| [\' Create a config lexem that belongs to a custom format. ]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                             |
| [Dim][ configLex [As] ConfigLexem = [New] ConfigLexem([\"\<%@\"], [\"%\>\"], FormatType.Custom, [False])] |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                             |
| [\' The actual regex can then be substituted with the lexical macro while defining the config lexem.]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                             |
| [\' NameInConfig returns name of the macro rounded with braces, like \"{testmacro}\".]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                             |
| [configLex.ContinueBlock = macro.NameInConfig ]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                             |
| [configLex.IsContinueRegex = [True]]                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[Language Elements]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#p27} 

[]{#related-topics}

