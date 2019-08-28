import csv


def write_csv_temple():
    with open('开发计划.csv', 'w+', encoding='utf-8') as file:
        fieldnames = ['No.', '项目', '开发阶段', '工作内容', '是否是预期计划', '当前工作进度', '本周预计完成进度', '负责人',
                      '预计工时(小时)', '实际工时(小时)', '实际完成进度', '是否达到本周计划进度', '未完成原因']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
    with open('人员统计.csv', 'w+', encoding='utf-8') as file2:
        fieldnames = ['负责人', '项目', '工作内容', '是否是预期计划', '实际工时(日)', '实际完成进度', '是否达到本周计划进度',
                      '未完成原因']
        writer = csv.DictWriter(file2, fieldnames=fieldnames)
        writer.writeheader()


write_csv_temple()
