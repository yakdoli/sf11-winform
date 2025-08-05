---
title: fonts4.md
original_path: WinForms_Docs/99_Uncategorized/fonts4.md
created_at: 2025-08-05
---






#### Fonts {#fonts style="tab-stops: 0pt"}

[] 

**PdfFont** is the base class for all the fonts. The design of the fonts is similar to Microsoft.NET fonts. Fonts are immutable objects, i.e., they cannot be modified, once created.

[] 


{border="0"}Note: There are special constructors that are used to create a new font from a prototype font, but with different settings.


[] 

The following are the features of the PDF fonts:

[] 

[·      ]PDF font objects do not have any size; the size is set only during text printing. This provides the advantage of being able to use the same fonts with different sizes.

[·      ]There are no Underline and Strikeout font styles in PDF. Underline and Strikeout font styles are emulated by drawing a line.

[] 

As mentioned above, all the fonts derived from PdfFonts are immutable. However, there are capabilities for fonts caching. It means, if there are two similar fonts that have different sizes and Underline or Strikeout styles, just one font object will be stored in the PDF file. So, if a lot of similar fonts with different sizes, and Underline or Strikeout styles are created, there is a huge benefit from the fonts caching in terms of speed and memory usage.

[] 


{border="0"}Note: Fonts caching works for all font types that are supported.


 

The following are the classes derived from PdfFont.

 

1\. PdfStandardFont

[] 

PdfStandardFont represents a font that is recognized by any Adobe Reader. It supports 14 types of fonts.

 

The following are some of the fonts supported by this class.

[] 

[·      ]Times-Roman (Regular, Bold, Italic, Bold Italic)

[·      ]Helvetica (Regular, Bold, Italic, Bold Italic)

[·      ]Courier (Regular, Bold, Italic, Bold Italic)

[·      ]Symbol

[·      ]ZapfDingbats

[] 


{border="0"}Note: Fonts that belong to this type do not support Unicode symbols. They take very less memory space, and it is suggested to use these fonts only when ASCII text has to be printed.


[] 

2\. PdfTrueTypeFont

[] 

PdfTrueTypeFont fonts are created from TrueType fonts. The PdfTrueTypeFont fonts are created either from the System.Drawing.Font class or TTF file (a file containing the information about TrueType font). There are a variety of constructors that can enable to create fonts with different settings. This class is used to embed the specified font in the PDF document.

[] 


{border="0"}Note: There is a unicode parameter in some of the constructors that indicate whether the font should support unicode symbols. The fonts created from a TTF file support unicode symbols, by default. If there is no need to use Unicode symbols, it is suggested to set the unicode parameter to False. Fonts that do not support Unicode takes less memory space in the file.


[] 

[·      ]Right To Left Support

[] 

Unicode TrueType fonts created from the System.Drawing.Font class are used for RTL text output. Also, the languages with symbols substitution (like Arabic) are supported. To enable RTL and characters substitution, set **RightToLeft** property to ***True*** in the **PdfStringFormat** class.

[] 


{border="0"}Note:

 



***[·    ]***RightToLeft property does not change the text alignment. It just enables the RTL engine and prints the text in RTL order. Use the Alignment property of PdfStringFormat to set the horizontal alignment of the text.

***[·    ]***Do not enable this feature if RTL support is not needed, because RTL support reduces the text printing speed.


[] 

CJK Fonts

[] 

There is a set of standard PDF fonts that support Chinese, Japanese and Korean characters. These fonts are supported through the **PdfCjkStandardFont** class. Although creating such fonts is similar to the PdfStandardFont, it requires the following families in addition:

[] 

[·      ]HanyangSystemsGothicMedium

[·      ]HanyangSystemsShinMyeongJoMedium

[·      ]HeiseiKakuGothicW5

[·      ]HeiseiMinchoW3

[·      ]MonotypeHeiMedium

[·      ]MonotypeSungLight

[·      ]SinoTypeSongLight

[] 

Text Measuring

[] 

The **MeasureString** method of the PdfFont class calculates the size of the text, number of lines that fit in the bounds, and number of characters in the text.

 

 

[]{#related-topics}

