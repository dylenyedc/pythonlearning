# 学生成绩管理系统

def display_menu():
    """显示主菜单"""
    print("\n欢迎使用学生成绩管理系统！")
    print("请选择操作：")
    print("1. 添加学生信息")
    print("2. 查看所有学生成绩")
    print("3. 查找学生成绩")
    print("4. 修改学生成绩")
    print("5. 删除学生信息")
    print("6. 退出系统")

def add_student(students):
    """添加学生信息"""
    name = input("请输入学生姓名：").strip()
    if name in students:
        print(f"学生{name}已存在，成绩为 {students[name]}")
        return
    while True:
        try:
            score = float(input(f"请输入{name}的成绩："))
            if score < 0 or score > 100:
                print("成绩应在0到100之间，请重新输入。")
                continue
            break
        except ValueError:
            print("无效输入，请输入一个有效的数字。")
    students[name] = score
    print(f"学生{name}的成绩已添加！")

def view_all_students(students):
    """查看所有学生成绩"""
    if not students:
        print("当前没有学生信息。")
        return
    print("\n所有学生成绩：")
    print("{:<20} {:<10}".format("姓名", "成绩"))
    print("-" * 30)
    for name, score in students.items():
        print("{:<20} {:<10}".format(name, score))

def find_student(students):
    """查找特定学生的成绩"""
    name = input("请输入要查找的学生姓名：").strip()
    if name in students:
        print(f"{name} 的成绩是 {students[name]}")
    else:
        print(f"未找到学生{name}的信息。")

def modify_student(students):
    """修改学生成绩"""
    name = input("请输入要修改成绩的学生姓名：").strip()
    if name in students:
        while True:
            try:
                new_score = float(input(f"请输入{name}的新成绩："))
                if new_score < 0 or new_score > 100:
                    print("成绩应在0到100之间，请重新输入。")
                    continue
                break
            except ValueError:
                print("无效输入，请输入一个有效的数字。")
        students[name] = new_score
        print(f"{name} 的成绩已更新为 {new_score}")
    else:
        print(f"未找到学生{name}的信息。")

def delete_student(students):
    """删除学生信息"""
    name = input("请输入要删除的学生姓名：").strip()
    if name in students:
        del students[name]
        print(f"学生{name}的信息已删除。")
    else:
        print(f"未找到学生{name}的信息。")

def main():
    """主函数，控制程序流程"""
    students = {}  # 存储学生信息的字典，格式为 {姓名: 成绩}

    while True:
        display_menu()
        choice = input("请输入你的选择（1-6）：")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_all_students(students)
        elif choice == '3':
            find_student(students)
        elif choice == '4':
            modify_student(students)
        elif choice == '5':
            delete_student(students)
        elif choice == '6':
            print("感谢使用学生成绩管理系统，再见！")
            break
        else:
            print("无效的选择，请输入1到6之间的数字。")

if __name__ == "__main__":
    main()
