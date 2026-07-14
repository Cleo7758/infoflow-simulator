# ============ 图2：Density_Dropout ============
print("\n📊 正在处理 Sheet 2：Density_Dropout")
df2 = pd.read_excel('dropout_tables_EN.xlsx', sheet_name='Density_Dropout')

# 🧹 强制清洗列名：去掉首尾空格 + 转小写 + 替换特殊字符
df2.columns = df2.columns.str.strip().str.lower().str.replace(r'\s+', '_', regex=True)

# 打印清洗后的列名（供你核对）
print(f"  -> 清洗后列名: {list(df2.columns)}")

# ✅ 现在用标准名字去找
x_col = 'information_density'
y_col = 'dropout_flag'

print(f"  -> 正在寻找: '{x_col}' 和 '{y_col}'")

if x_col in df2.columns and y_col in df2.columns:
    summary2 = df2.groupby(x_col)[y_col].agg(
        total='count', dropped='sum'
    ).reset_index()
    summary2['dropout_rate'] = (summary2['dropped'] / summary2['total']) * 100

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=summary2, x=x_col, y='dropout_rate', s=120, color='#E67E22')
    sns.regplot(data=summary2, x=x_col, y='dropout_rate', scatter=False, color='#27AE60', line_kws={"linewidth": 2})
    plt.title('图2：信息密度与流失率关系 (Density Dropout)', fontsize=16, pad=15)
    plt.xlabel('信息密度 (Information Density)', fontsize=12)
    plt.ylabel('流失率 (%)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    for i in range(len(summary2)):
        plt.text(summary2[x_col][i], summary2['dropout_rate'][i] + 1,
                 f"{summary2['dropout_rate'][i]:.1f}%", ha='center', fontsize=10)
    plt.tight_layout()
    plt.savefig('chart_2_density_dropout.png', dpi=300)
    print("  ✅ 图2已保存：chart_2_density_dropout.png")
    plt.close()
else:
    print(f"  ❌ 错误：找不到列！请检查Excel文件。")
    print(f"     清洗后列名: {list(df2.columns)}")
    print(f"     你要找的: {x_col}, {y_col}")