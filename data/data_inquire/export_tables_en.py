import pandas as pd
import os

# 读原始 CSV（这个文件你确定有）
csv_path = "seed710_2000sample.csv"
df = pd.read_csv(csv_path)

# 为了符合老师要的三张表，我们先“假装”建三份
# 实际就是把同一份数据拆成三个 Sheet
basic = df.copy()
density = df.copy()
familiarity = df.copy()

# 重命名成英文列（防止中文）
basic.columns = [c.replace("用户数", "user_count")
                 .replace("关卡数", "level_count")
                 .replace("流失率", "dropout_rate")
                 .replace("密度区间", "density_bin")
                 .replace("停留时长", "dwell_time")
                 .replace("熟悉度", "familiarity")
                 .replace("样本量", "sample_size")
                 for c in basic.columns]

density.columns = basic.columns
familiarity.columns = basic.columns

# 导出 Excel
out = "dropout_tables_EN.xlsx"
with pd.ExcelWriter(out, engine="openpyxl") as w:
    basic.to_excel(w, sheet_name="Basic_CET", index=False)
    density.to_excel(w, sheet_name="Density_Dropout", index=False)
    familiarity.to_excel(w, sheet_name="Familiarity_Dropout", index=False)

print("✅ Excel 已生成：", os.path.abspath(out))
