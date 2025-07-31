---
title: usecasescenario13.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usecasescenario13.md
created_at: 2025-07-03
---






##### Use Case Scenario {#use-case-scenario style="tab-stops: 0pt"}

Starting with Internet Explorer 9, Microsoft has made a series of core-architectural changes to Internet Explorer.  One of them was to use DirectX (a.k.a, D2D) to render webpage to achieve full-hardware acceleration development to support HTML5 standard features instead of GDI based rendering. As our HTML to PDF conversion depends on IE's GDI based rendering during conversion, our HTML Converter will not be able to generate PDF documents that contain selectable text.  Hence, if the machine has IE9 or later installed, then you should consider using our Gecko based rendering.  This approach will reliably generate PDF documents that are text selectable and printer friendly.

 

[]{#related-topics}

