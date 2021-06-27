import os
from bs4 import BeautifulSoup
import codecs
import re
import pandas as pd
import numpy as np

# =============================================================================
# # Iterated throught a bunch of local html file
# directory = './ArticlesHtml'
# dia_range = pd.DataFrame(columns=('min', 'max'))
# for filename in os.listdir(directory):
#     if filename.endswith('.html'):
# =============================================================================
dia_range = pd.DataFrame(columns=('min', 'max'))
# Get article text from a saved html file
path = './ArticlesHtml/012.html'
f = codecs.open(path, 'r', 'utf-8')
document = BeautifulSoup(f.read(),features='html.parser').get_text()
f.close()

# Get diameter
dia_rex = r'fib.*\s(\d+\s?±\s?\d+\s?[μ|n]m)|n?a?n?o?fibers?\swith\san?\s?a?v?e?r?a?g?e?\sdiameters?\s.*[\s≈~](\d+?\.?\d+[\s| ]?[μ|n]m)|diameters?\sof\sn?a?n?o?fibers?\s.*\s(\d+?\.?\d+[\s| ]?[μ|n]m)|fibers?\sdiameters?.*\s(\d+?\.?\d+\s?[μ|n]?m?\s\w+\s\d+?\.?\d+\s?[μ|n]?m?)|fibers?\sdiameters?.*[\s(](\d+[–|-]\d+\s?[μ|n]m)'

test1 = 'to form fibres as 400 ± 100 nm in diameter at 4000 r min−1.'
dia = re.findall(dia_rex, document)
dia1 = re.findall(dia_rex, test1)

# =============================================================================
# # Keep only a range
# # clean tuple list of dia 
# # (remove empty string → false min, space, comma and untis → conversion)
# dia = [(x.replace(',', '').replace(' ', '') if isinstance(x, str) else x for x in _ if x) for _ in dia]
# dia = [(tuple(int(x) if x.isdigit() else x for x in _ if x)) for _ in dia]
# # find minimum dia
# min0 = 300000000
# for match in range(len(dia)):
#     if isinstance(dia[match], int):
#         min_dmatch = dia[match]
#     else:
#         min_dmatch = min(dia[match])
#     if min_dmatch < min0:
#         min0 = min_dmatch
#         min_dia = min_dmatch
# # find maximum dia        
# max0 = 0
# for match in range(len(dia)):
#     if isinstance(dia[match], int):
#         max_dmatch = dia[match]
#     else:
#         max_dmatch = max(dia[match])
#     if  max0 < max_dmatch:
#         max0 = max_dmatch
#         max_dia = max_dmatch
# # if no match is found
# if not dia:
#     min_dia = np.nan
#     max_dia = np.nan
#     min_dmatch = None
#     max_dmatch = None
# # put min max dia for a single article in a dataframe
# dia_range1 = [min_dia, max_dia]
# dia_range1 = pd.DataFrame(dia_range1, index=('min', 'max')).transpose()
# # put min max dia for each article in a dataframe
# dia_range = dia_range.append(dia_range1)
# # clean before the new iteration of the loop
# del min_dmatch, min_dia, max_dmatch, max_dia
# =============================================================================
