---
title: barcode.md
original_path: WinForms_Docs/99_Uncategorized/barcode.md
created_at: 2025-08-05
---






##### Barcode {#barcode style="tab-stops: 0pt"}

[] 

Bar codes provide a simple and inexpensive method of encoding text information that is easily read by inexpensive electronic readers. A bar code consists of a series of parallel, adjacent bars and spaces. Predefined bar and space patterns or \"symbologies\" are used to encode small strings of character data into a printed symbol.

 

The basic structure of a bar code consists of a leading and trailing quiet zone, a start pattern, one or more data characters, optionally one or two check characters, and a stop pattern. Essential PDF supports 1D / linear barcodes and 2D barcode.

 

1D / Linear Barcodes

 

Following codes are the 1D / linear barcodes. This section also includes details of each code with coding examples.

[] 

[·      ]Code39

[·      ]Code39Extended

[·      ]Code11

[·      ]Codabar

[·      ]Code32

[·      ]Code93

[·      ]Code93Extended

[·      ]Code128

[·      ]Code128A

[·      ]Code128B

[·      ]Code128C

 

Code39

[] 

The Code 39 character set includes the digits 0-9, the letters A-Z (upper case only), and the following symbols: space, minus (-), plus (+), period (.), dollar sign (\$), slash (/), and percent (%). A special start / stop character is placed at the beginning and end of each barcode. The barcode may be of any length, although more than 25 characters really begin to push the bounds. Code 39 is just about the only type of barcode in common use that does not require a checksum.

 

The following code example illustrates how to draw Code39 Barcode.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                   |
|                                                                                                                                                                    |
| []                                                                                                             |
|                                                                                                                                                                    |
| [// Drawing Code39 barcode]                                                                                      |
|                                                                                                                                                                    |
| [PdfCode39Barcode][ barcode = new [PdfCode39Barcode]();] |
|                                                                                                                                                                    |
| []                                                                                                               |
|                                                                                                                                                                    |
| [// Setting height of the barcode]                                                                               |
|                                                                                                                                                                    |
| [barcode.BarHeight = 45;]                                                                                                      |
|                                                                                                                                                                    |
| [barcode.Text = \"CODE39\$\";]                                                                                                 |
|                                                                                                                                                                    |
| []                                                                                                               |
|                                                                                                                                                                    |
| [// Printing barcode on to the Pdf.]                                                                             |
|                                                                                                                                                                    |
| [barcode.Draw(page, new PointF(25, 70 ));]                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                            |
|                                                                                                                                                                                                 |
| []                                                                                                                                          |
|                                                                                                                                                                                                 |
| [\' Drawing Code39 barcode]                                                                                                                   |
|                                                                                                                                                                                                 |
| [Dim][ barcode [As] PdfCode39Barcode = [New] PdfCode39Barcode()] |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [\' Setting height of the barcode]                                                                                                            |
|                                                                                                                                                                                                 |
| [barcode.BarHeight = 45]                                                                                                                                    |
|                                                                                                                                                                                                 |
| [barcode.Text = \"CODE39\$\"]                                                                                                                               |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [\' Printing barcode on to the Pdf.]                                                                                                          |
|                                                                                                                                                                                                 |
| [barcode.Draw(page, [New] PointF(25, 70))]                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

ExtendedCode39

 

Code 39 Extended is an extended version of Code 39 that supports the ASCII character set. So with Code 39 Extended, you can also code the 26 lower letters (a-z) and the special characters you have on your keyboard.

 

The following code example illustrates how to draw Code39Extended barcode.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                                       |
| [// Drawing Code39Extended barcode]                                                                                                 |
|                                                                                                                                                                                       |
| [PdfCode39ExtendedBarcode][ barcodeExt = new [PdfCode39ExtendedBarcode]();] |
|                                                                                                                                                                                       |
| [barcodeExt.TextAlignment = PdfBarcodeTextAlignment.Left;]                                                                                        |
|                                                                                                                                                                                       |
| [barcodeExt.Text = \"CODE39Ext\"[;]]                                                                                        |
|                                                                                                                                                                                       |
| [//Printing barcode on to the Pdf.]                                                                                                 |
|                                                                                                                                                                                       |
| [barcodeExt.Draw(page, new PointF(25, 200));]                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [\' Drawing Code39Extended barcode]                                                                                                                              |
|                                                                                                                                                                                                                    |
| [Dim][ barcodeExt [As] PdfCode39ExtendedBarcode = [New] PdfCode39ExtendedBarcode()] |
|                                                                                                                                                                                                                    |
| [barcodeExt.TextAlignment = PdfBarcodeTextAlignment.Left]                                                                                                                      |
|                                                                                                                                                                                                                    |
| [barcodeExt.Text = \"CODE39Ext\"]                                                                                                                                              |
|                                                                                                                                                                                                                    |
| [\'Printing barcode on to the Pdf.]                                                                                                                              |
|                                                                                                                                                                                                                    |
| [barcodeExt.Draw(page, [New] PointF(25, 200))]                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Code 11

 

Code 11 is used primarily for labeling telecommunications equipment. The character set includes the digits 0 to 9, a dash ( - ), and a start / stop code. Each character is encoded with three bars and two spaces. Of these five elements, there may be two wide and three narrow elements, or one wide and four narrow elements. 

 

The following code example illustrates how to draw Code 11 Barcode.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                     |
|                                                                                                                                                                      |
| []                                                                                                               |
|                                                                                                                                                                      |
| [// Drawing Code 11 barcode]                                                                                       |
|                                                                                                                                                                      |
| [PdfCode11Barcode][ barcode11 = new [PdfCode11Barcode]();] |
|                                                                                                                                                                      |
| [barcode11.Text = \"012345678\";]                                                                                                |
|                                                                                                                                                                      |
| [barcode11.EncodeStartStopSymbols = true;]                                                                                       |
|                                                                                                                                                                      |
| [ //Printing barcode on to the Pdf.]                                                                               |
|                                                                                                                                                                      |
| [barcode11.Draw(page, new PointF(25, 300));]                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                              |
|                                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                                   |
| [\' Drawing Code 11 barcode]                                                                                                                    |
|                                                                                                                                                                                                   |
| [Dim][ barcode11 [As] PdfCode11Barcode = [New] PdfCode11Barcode()] |
|                                                                                                                                                                                                   |
| [barcode11.Text = \"012345678\"]                                                                                                                              |
|                                                                                                                                                                                                   |
| [barcode11.EncodeStartStopSymbols = [True]]                                                                                              |
|                                                                                                                                                                                                   |
| [ [\'Printing barcode on to the Pdf.]]                                                                                                  |
|                                                                                                                                                                                                   |
| [barcode11.Draw(page, [New] PointF(25, 300))]                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

CodaBar

**[]** 

CodaBar is a variable length symbology that performs encoding of the following 20 characters:

            0123456789-\$:/.+ABCD.

 

CodaBar uses the characters, A, B, C and D, only as start and stop characters. Codabar is used in libraries, blood banks, the overnight package delivery industry, and a variety of other information processing applications.

 

The following code example illustrates how to draw Codabar barcode.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                 |
| [ // Drawing Codabar barcode]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                 |
| [PdfCodabarBarcode][ ][codabar = [new][ ][PdfCodabarBarcode][();]] |
|                                                                                                                                                                                                                                                                                                 |
| [codabar.Text = \"0123\";     [      ]]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                 |
| [//Printing barcode on to the Pdf.]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                 |
| [codabar.Draw(page, new PointF(25, 400));]                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                              |
|                                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                                   |
| [ [\' Drawing Codabar barcode]]                                                                                                         |
|                                                                                                                                                                                                   |
| [Dim][ codabar [As] PdfCodabarBarcode = [New] PdfCodabarBarcode()] |
|                                                                                                                                                                                                   |
| [codabar.Text = \"0123\"]                                                                                                                                     |
|                                                                                                                                                                                                   |
| [\'Printing barcode on to the Pdf.]                                                                                                             |
|                                                                                                                                                                                                   |
| [codabar.Draw(page, [New] PointF(25, 400))]                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Code 32

 

It is mainly used for coding pharmaceuticals, cosmetics and dietetics. Code 32 is mainly used to encode pharmaceutical products in Italy. Code 32 is used to encode Italian Pharmacode, which has the following structure:

 

[·      ]\'A\' character (ASCII 65), which is not really encoded

[·      ]8 digits for Pharmacode (It generally begins / is prefixed with 0)

[·      ]1 digit for Checksum module 10, which is automatically calculated by Barcode Professional

 

The value to be encoded (that is passed to Barcode Professional), must be 8 digits pharmacode (prefix it with \'0\' if necessary), because the 9th digit (the checksum) is automatically calculated by Barcode Professional products.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                         |
|                                                                                                                                                                                          |
| []                                                                                                                                   |
|                                                                                                                                                                                          |
| [PdfCode32Barcode][ code32 = [new] [PdfCode32Barcode]();] |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [code32.Font = font;]                                                                                                                                |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [// Setting height of the barcode]                                                                                                     |
|                                                                                                                                                                                          |
| [code32.BarHeight = 45;]                                                                                                                             |
|                                                                                                                                                                                          |
| [code32.Text = [\"01234567\"];]                                                                                               |
|                                                                                                                                                                                          |
| [code32.TextDisplayLocation = [TextLocation].Bottom;]                                                                           |
|                                                                                                                                                                                          |
| [code32.EnableCheckDigit = [true];]                                                                                             |
|                                                                                                                                                                                          |
| [code32.ShowCheckDigit = [true];]                                                                                               |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [//Printing barcode on to the Pdf.]                                                                                                    |
|                                                                                                                                                                                          |
| [code32.Draw(page, [new] [PointF](25, 500));]                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                        |
|                                                                                                                                                                             |
| []                                                                                                                      |
|                                                                                                                                                                             |
| [Dim][ code32 [As] [New] PdfCode32Barcode()] |
|                                                                                                                                                                             |
| []                                                                                                                                      |
|                                                                                                                                                                             |
| [code32.Font = font]                                                                                                                    |
|                                                                                                                                                                             |
| []                                                                                                                                      |
|                                                                                                                                                                             |
| [\' Setting height of the barcode]                                                                                        |
|                                                                                                                                                                             |
| [code32.BarHeight = 45]                                                                                                                 |
|                                                                                                                                                                             |
| [code32.Text = [\"01234567\"]]                                                                                   |
|                                                                                                                                                                             |
| [code32.TextDisplayLocation = TextLocation.Bottom]                                                                                      |
|                                                                                                                                                                             |
| [code32.EnableCheckDigit = [True]]                                                                                 |
|                                                                                                                                                                             |
| [code32.ShowCheckDigit = [True]]                                                                                   |
|                                                                                                                                                                             |
| []                                                                                                                         |
|                                                                                                                                                                             |
| [\'Printing barcode on to the Pdf.]                                                                                       |
|                                                                                                                                                                             |
| [code32.Draw(page, [New] PointF(25, 500))]                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Code93

 

Code 93 was designed to complement and improve upon Code 39. It can represent the full ASCII character set by using combinations of 2 characters. Code 93 is a continuous, variable-length symbology and produces denser code.

 

[·      ]The Standard Mode (default implementation) can encode uppercase letters (A through Z), digits (0 through 9), and special characters like the **\***, **-**, **\$**, **%**, (Space), **.**, **/**, and **+**.

[·      ]The Full ASCII Mode or Extended Version can encode all 128 ASCII characters.

 

The asterisk (\*) is not a true encodable character, but is the start and stop \'symbol\' for Code 93.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                         |
|                                                                                                                                                                                          |
| []                                                                                                                                       |
|                                                                                                                                                                                          |
| [PdfCode93Barcode][ code93 = [new] [PdfCode93Barcode]();] |
|                                                                                                                                                                                          |
| [// Setting height of the barcode]                                                                                                     |
|                                                                                                                                                                                          |
| [code93.BarHeight = 45;]                                                                                                                             |
|                                                                                                                                                                                          |
| [code93.Text = [\"ABC 123456789\"];]                                                                                          |
|                                                                                                                                                                                          |
| [//Printing barcode on to the Pdf.]                                                                                                    |
|                                                                                                                                                                                          |
| [code93.Draw(page, [new] [PointF](25, 600));]                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                        |
|                                                                                                                                                                             |
| []                                                                                                                      |
|                                                                                                                                                                             |
| [Dim][ code93 [As] [New] PdfCode93Barcode()] |
|                                                                                                                                                                             |
| [\' Setting height of the barcode]                                                                                        |
|                                                                                                                                                                             |
| [code93.BarHeight = 45]                                                                                                                 |
|                                                                                                                                                                             |
| [code93.Text = [\"ABC 123456789\"]]                                                                              |
|                                                                                                                                                                             |
| [\'Printing barcode on to the Pdf.]                                                                                       |
|                                                                                                                                                                             |
| [code93.Draw(page, [New] PointF(25, 600))]                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Code93Extended

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                            |
|                                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [PdfCode93ExtendedBarcode][ code93ext = [new] [PdfCode93ExtendedBarcode]();] |
|                                                                                                                                                                                                             |
| [//Setting height of the barcode]                                                                                                                         |
|                                                                                                                                                                                                             |
| [code93ext.BarHeight = 45;]                                                                                                                                             |
|                                                                                                                                                                                                             |
| [code93ext.EncodeStartStopSymbols = [true];]                                                                                                       |
|                                                                                                                                                                                                             |
| [code93ext.Text = [\"(abc) 123456789\"];]                                                                                                        |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [//Printing barcode on to the Pdf.]                                                                                                                       |
|                                                                                                                                                                                                             |
| [page = doc.Pages.Add();]                                                                                                                                               |
|                                                                                                                                                                                                             |
| [code93ext.Draw(page, [new] [PointF](25, 50));]                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                   |
|                                                                                                                                                                                        |
| []                                                                                                                                 |
|                                                                                                                                                                                        |
| [Dim][ code93ext [As] [New] PdfCode93ExtendedBarcode()] |
|                                                                                                                                                                                        |
| [\'Setting height of the barcode]                                                                                                    |
|                                                                                                                                                                                        |
| [code93ext.BarHeight = 45]                                                                                                                         |
|                                                                                                                                                                                        |
| [code93ext.EncodeStartStopSymbols = [True]]                                                                                   |
|                                                                                                                                                                                        |
| [code93ext.Text = [\"(abc) 123456789\"]]                                                                                    |
|                                                                                                                                                                                        |
| []                                                                                                                                  |
|                                                                                                                                                                                        |
| [\'Printing barcode on to the Pdf.]                                                                                                  |
|                                                                                                                                                                                        |
| [page = doc.Pages.Add()]                                                                                                                           |
|                                                                                                                                                                                        |
| [code93ext.Draw(page, [New] PointF(25, 50))]                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Code128

 

Code 128 is a variable length, high density, alphanumeric, linear bar code symbology, capable of encoding the full 128-character ASCII character set and extended character sets. This Symbology includes a checksum digit for verification, and the barcode may also be verified character-by-character verifying the parity of each data byte.

[] 

Code 128 Code Sets

**[]** 

[·      ]Code Set A (or Chars Set A) includes all of the standard upper case U.S. alphanumeric keyboard characters and punctuation characters together with the control characters, (i.e. characters with ASCII values from 0 to 95 inclusive), and seven special characters.

[·      ]Code Set B (or Chars Set B) includes all of the standard upper case alphanumeric keyboard characters and punctuation characters together with the lower case alphabetic characters (i.e. characters with ASCII values from 32 to 127 inclusive), and seven special characters.

[·      ]Code Set C (or Chars Set C) includes the set of 100 digit pairs from 00 to 99 inclusive, as well as three special characters. This allows numeric data to be encoded as two data digits per symbol character, at effectively twice the density of standard data.

 

Code 128 Special characters

 

The last seven characters of Code Sets A and B (character values 96 - 102) and the last three characters of Code Set C (character values 100 - 102) are special non-data characters with no ASCII character equivalents, which have particular significance to the bar code reading device.


 

{border="0"}Note: If you specify that the data must be encoded by using Char Set C, then the number of characters after it must be even.


 

Code128A

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                  |
|                                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                                   |
| [PdfCode128ABarcode][ barcode128A = [new] [PdfCode128ABarcode]();] |
|                                                                                                                                                                                                   |
| [// Setting height of the barcode]                                                                                                              |
|                                                                                                                                                                                                   |
| [barcode128A.BarHeight = 45;]                                                                                                                                 |
|                                                                                                                                                                                                   |
| [barcode128A.Text = [\"ABCD 12345\"];]                                                                                                 |
|                                                                                                                                                                                                   |
| [barcode128A.EnableCheckDigit = [true];]                                                                                                 |
|                                                                                                                                                                                                   |
| [barcode128A.EncodeStartStopSymbols = [true];]                                                                                           |
|                                                                                                                                                                                                   |
| [barcode128A.ShowCheckDigit = [true];]                                                                                                   |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [//Printing barcode on to the Pdf.]                                                                                                             |
|                                                                                                                                                                                                   |
| [barcode128A.Draw(page, [new] [PointF](25, 135));]                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                               |
|                                                                                                                                                                                    |
| []                                                                                                                             |
|                                                                                                                                                                                    |
| [Dim][ barcode128A [As] [New] PdfCode128ABarcode()] |
|                                                                                                                                                                                    |
| [\' Setting height of the barcode]                                                                                               |
|                                                                                                                                                                                    |
| [barcode128A.BarHeight = 45]                                                                                                                   |
|                                                                                                                                                                                    |
| [barcode128A.Text = [\"ABCD 12345\"]]                                                                                   |
|                                                                                                                                                                                    |
| [barcode128A.EnableCheckDigit = [True]]                                                                                   |
|                                                                                                                                                                                    |
| [barcode128A.EncodeStartStopSymbols = [True]]                                                                             |
|                                                                                                                                                                                    |
| [barcode128A.ShowCheckDigit = [True]]                                                                                     |
|                                                                                                                                                                                    |
| []                                                                                                                                |
|                                                                                                                                                                                    |
| [\'Printing barcode on to the Pdf.]                                                                                              |
|                                                                                                                                                                                    |
| [barcode128A.Draw(page, [New] PointF(25, 135))]                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Code128B

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                  |
|                                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                                   |
| [PdfCode128BBarcode][ barcode128B = [new] [PdfCode128BBarcode]();] |
|                                                                                                                                                                                                   |
| [// Setting height of the barcode]                                                                                                              |
|                                                                                                                                                                                                   |
| [barcode128B.BarHeight = 45;]                                                                                                                                 |
|                                                                                                                                                                                                   |
| [barcode128B.Text = [\"12345 abcd\"];]                                                                                                 |
|                                                                                                                                                                                                   |
| [barcode128B.EnableCheckDigit = [true];]                                                                                                 |
|                                                                                                                                                                                                   |
| [barcode128B.EncodeStartStopSymbols = [true];]                                                                                           |
|                                                                                                                                                                                                   |
| [barcode128B.ShowCheckDigit = [true];]                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                               |
|                                                                                                                                                                                    |
| []                                                                                                                             |
|                                                                                                                                                                                    |
| [Dim][ barcode128B [As] [New] PdfCode128BBarcode()] |
|                                                                                                                                                                                    |
| [\' Setting height of the barcode]                                                                                               |
|                                                                                                                                                                                    |
| [barcode128B.BarHeight = 45]                                                                                                                   |
|                                                                                                                                                                                    |
| [barcode128B.Text = [\"12345 abcd\"]]                                                                                   |
|                                                                                                                                                                                    |
| [barcode128B.EnableCheckDigit = [True]]                                                                                   |
|                                                                                                                                                                                    |
| [barcode128B.EncodeStartStopSymbols = [True]]                                                                             |
|                                                                                                                                                                                    |
| [barcode128B.ShowCheckDigit = [True]]                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Code128C

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                  |
|                                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                                   |
| [PdfCode128CBarcode][ barcode128C = [new] [PdfCode128CBarcode]();] |
|                                                                                                                                                                                                   |
| [// Setting height of the barcode]                                                                                                              |
|                                                                                                                                                                                                   |
| [barcode128C.BarHeight = 45;]                                                                                                                                 |
|                                                                                                                                                                                                   |
| [barcode128C.Text = [\"001122334455\"];]                                                                                               |
|                                                                                                                                                                                                   |
| [barcode128C.EnableCheckDigit = [true];]                                                                                                 |
|                                                                                                                                                                                                   |
| [barcode128C.EncodeStartStopSymbols = [true];]                                                                                           |
|                                                                                                                                                                                                   |
| [barcode128C.ShowCheckDigit = [true];]                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                               |
|                                                                                                                                                                                    |
| []                                                                                                                             |
|                                                                                                                                                                                    |
| [Dim][ barcode128C [As] [New] PdfCode128CBarcode()] |
|                                                                                                                                                                                    |
| [\' Setting height of the barcode]                                                                                               |
|                                                                                                                                                                                    |
| [barcode128C.BarHeight = 45]                                                                                                                   |
|                                                                                                                                                                                    |
| [barcode128C.Text = [\"001122334455\"]]                                                                                 |
|                                                                                                                                                                                    |
| [barcode128C.EnableCheckDigit = [True]]                                                                                   |
|                                                                                                                                                                                    |
| [barcode128C.EncodeStartStopSymbols = [True]]                                                                             |
|                                                                                                                                                                                    |
| [barcode128C.ShowCheckDigit = [True]]                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2D Barcode

 

DataMatrix Barcode

 

DataMatrix barcode is a two dimensional barcode that consists of a grid of dark and light dots or blocks forming square or rectangular symbol. The data encoded in the barcode can either be number or alphanumeric. The **PdfDataMatrixBarcode** class available in Syncfusion.Pdf.Barcode namespace sets the suitable encoding type and size for the input data. However, the size, encoding type and dimension of individual blocks can also be set using the properties.

 


{border="0"}By default, the width of the quiet zone on all four sides of the barcode is equal to the dimension of the blocks.

 


Use case scenario

 

The DataMatrix bar codes are widely used in printed media such as labels and letters. It can be read easily by a bar code reader and also by mobile phones.

 

[**[Properties, Methods and Events]**]{.apple-style-span}

Properties

Table 1: Properties Table


  Property []    Description []                               Data Type []
  --------------------------------------- --------------------------------------------------------------------- --------------------------------------------------
  Encoding[]     Gets or sets the encoding type.[]            PdfDataMatrixEncoding[]
  Size[]         Gets or sets the size of the symbol.[]       PdfDataMatrixSize[]
  Text[]         Gets or sets the data.[]                     String[]
  XDimension[]   Gets or sets the dimension of the blocks[]   float[]


[] 

Methods

Table 2:Methods Table


  Method    Description                 Parameters          Return Type
  --------- --------------------------- ------------------- -------------
  Draw      Draws barcode in PdfPage    (PdfPage, PointF)   Void
  ToImage   Converts barcode to Image   None                Image


[] 

The following code snippet illustrates how to draw a DataMatrix barcode:

**** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| [// Create a DataMatrix barcode.]                                                                                                                                                                |
|                                                                                                                                                                                                                                                    |
| [PdfDataMatrixBarcode][ dataMatrix = [new] [PdfDataMatrixBarcode]([\"Syncfusion\"]);] |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [// Set the dimension.]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                    |
| [dataMatrix.XDimension = 3;]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [// Set the encoding.]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                    |
| [dataMatrix.Encoding = [PdfDataMatrixEncoding].ASCII;]                                                                                                                                 |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [// Choose the matrix size.]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| [dataMatrix.Size = [PdfDataMatrixSize].Size12x12;]                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [// Draw the barcode on PdfPage.]                                                                                                                                                                |
|                                                                                                                                                                                                                                                    |
| [dataMatrix.Draw(page, [PointF].Empty);]                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [\' Create a DataMatrix barcode][]                                                                                                    |
|                                                                                                                                                                                                                             |
| [Dim][ dataMatrix [As] [New] PdfDataMatrixBarcode([\"Syncfusion\"])] |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [\' Set the dimension][]                                                                                                              |
|                                                                                                                                                                                                                             |
| [dataMatrix.XDimension = 3]                                                                                                                                                             |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [\' Set the encoding][]                                                                                                               |
|                                                                                                                                                                                                                             |
| [dataMatrix.Encoding = PdfDataMatrixEncoding.ASCII]                                                                                                                                     |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [\' Choose the matrix size][]                                                                                                         |
|                                                                                                                                                                                                                             |
| [dataMatrix.Size = PdfDataMatrixSize.Size12x12]                                                                                                                                         |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [\' Draw the barcode on PdfPage][]                                                                                                    |
|                                                                                                                                                                                                                             |
| [dataMatrix.Draw(page, PointF.Empty)]                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Barcode as Image

 

Barcode that is generated by using Essential PDF is simultaneously converted to an image. The following code example illustrates this.

 

+---------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                            |
|                                                                                                                                             |
| []                                                                                      |
|                                                                                                                                             |
| [Image][ img = barcode.ToImage();]                  |
|                                                                                                                                             |
| [img.Save([\"Code38Barcode.png\"], [ImageFormat].Png);] |
+---------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                     |
|                                                                                                                                                          |
| []                                                                                                   |
|                                                                                                                                                          |
| [Private][ img [As] Image = barcode.ToImage()] |
|                                                                                                                                                          |
| [img.Save([\"Code38Barcode.png\"], ImageFormat.Png)]                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

