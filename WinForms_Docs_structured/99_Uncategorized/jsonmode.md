---
title: jsonmode.md
original_path: WinForms_Docs/99_Uncategorized/jsonmode.md
created_at: 2025-08-05
---








  









### JSON Mode {#json-mode style="tab-stops: 0pt"}

 

JSON (JavaScript Object Notation) is a lightweight data interchange format for serialization of structured data. It defines a small set of formatting rules for the portable representation of structured data. It is human readable, platform independent, and has a wide availability of implementations. You will use this JSON format to exchange data in the MVC architecture.

In JSON mode, the only possible operations are paging and sorting. Operation in the JSON mode can be handled by you. The **PagingParams** instance holds the essential information about the current request. ASP.NET client-side templates have the responsibility of generating HTML from JSON. This mode gives better performance than the server mode. The initial rendering is done in the server mode only.

 

 

More:







