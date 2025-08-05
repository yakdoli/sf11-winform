---
title: autoformattingrepository1.md
original_path: WinForms_Docs/99_Uncategorized/autoformattingrepository1.md
created_at: 2025-08-05
---








  









## AutoFormatting Repository {#autoformatting-repository style="tab-stops: 0pt"}

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [public][ [static] [class] [AutoFormatRepository]]                                                       |
|                                                                                                                                                                                                                                                                 |
| [    {]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                 |
| [        [///][ ][\<summary\>]]                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| [        [///][ Get all AutoFormatting data.]]                                                                                                                                   |
|                                                                                                                                                                                                                                                                 |
| [        [///][ ][\</summary\>]]                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| [        [///][ ][\<returns\>\</returns\>]]                                                                                                                 |
|                                                                                                                                                                                                                                                                 |
| [        [public] [static] [IList]\<[AutoFormatting]\> GetData()]                                                                 |
|                                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                 |
| [            [List]\<[AutoFormatting]\> result = [new] [List]\<[AutoFormatting]\>();]                  |
|                                                                                                                                                                                                                                                                 |
| [            result.Add([new] [AutoFormatting]([Convert].ToDateTime([\"10/10/2005 6:30AM\"]), 15123.45m, 1362, 458792658));]   |
|                                                                                                                                                                                                                                                                 |
| [            result.Add([new] [AutoFormatting]([Convert].ToDateTime([\"10/9/2006 7:20PM\"]), 12893.45m, 234, 254879362));]     |
|                                                                                                                                                                                                                                                                 |
| [            result.Add([new] [AutoFormatting]([Convert].ToDateTime([\"9/10/2007 8:45AM\"]), 45123.45m, 1298, 569786269));]    |
|                                                                                                                                                                                                                                                                 |
| [            result.Add([new] [AutoFormatting]([Convert].ToDateTime([\"5/10/2004 7:45PM\"]), 67189.45m, 3362, 163840382));]    |
|                                                                                                                                                                                                                                                                 |
| [            result.Add([new] [AutoFormatting]([Convert].ToDateTime([\"2/3/2009 5:34AM\"]), 23190.45m, 1839, 983729405));]     |
|                                                                                                                                                                                                                                                                 |
| [            result.Add([new] [AutoFormatting]([Convert].ToDateTime([\"6/8/2020 9:56PM\"]), 43145.45m, 89982, 937292033));]    |
|                                                                                                                                                                                                                                                                 |
| [            result.Add([new] [AutoFormatting]([Convert].ToDateTime([\"3/2/2001 1:45AM\"]), 5198.45m, 6739, 473920219));]      |
|                                                                                                                                                                                                                                                                 |
| [            result.Add([new] [AutoFormatting]([Convert].ToDateTime([\"2/1/2003 2:23PM\"]), 345123.45m, 2262, 987654321));]    |
|                                                                                                                                                                                                                                                                 |
| [            result.Add([new] [AutoFormatting]([Convert].ToDateTime([\"11/12/2005 9:56PM\"]), 315123.45m, 48393, 123456789));] |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [            [return] result;]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                 |
| [    }]                                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

