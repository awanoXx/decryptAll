import pyodbc


def connect_to_sql_server():
    try:
        conn = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=192.168.2.243;'
            'DATABASE=newaiderdb;'
            'UID=dataquery;'
            'PWD=data@2024'
        )
        print("连接成功！")

        cursor = conn.cursor()
        cursor.execute('SELECT top 1 * FROM Ln_Ziliaoshouji')  # 替换为你的表名
        for row in cursor:
            print(row)

    except Exception as e:
        print("发生错误:", e)
    finally:
        if 'conn' in locals():
            conn.close()
            print("连接已关闭。")


if __name__ == '__main__':
    connect_to_sql_server()
