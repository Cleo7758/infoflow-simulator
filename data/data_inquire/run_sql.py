import sqlite3
import os

DB = "seed710_2000.db"

SQL_FILES = [
    "basic_CET.sql",
    "density_dropout.sql",
    "familiarity_dropout.sql"
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    for sql_file in SQL_FILES:
        print("▶️ 执行:", sql_file)
        with open(sql_file, "r", encoding="utf-8") as f:
            cur.executescript(f.read())
        print("✅ 完成:", sql_file)

    conn.commit()
    conn.close()
    print("\n🎉 三张表已成功创建！")

if __name__ == "__main__":
    main()
