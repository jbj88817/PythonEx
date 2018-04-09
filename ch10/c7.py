# 边界匹配

import re

qq = '100000001'

# 4~8
# r = re.findall('^\d{4,8}$', qq)  # ^和$匹配完整的字符串

# ^ 是表示头
# $ 是表示尾
r = re.findall('^000$', qq)  # 这个不能匹配，因为头尾都不匹配
print(r)

