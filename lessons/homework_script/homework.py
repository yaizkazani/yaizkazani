import ezsheets, os, pathlib, pprint, smtplib, shutil, sys, openpyxl, logging, send2trash
import Email_sender_v2_attachments as email
from openpyxl.styles import Alignment

logging.basicConfig(level=logging.INFO, format='%(levelname)s %(message)s')


def preparing_stats(student_name, homework_data):
    """
    :param student_name: name of the student to get data for
    :type student_name: str
    :param homework_data: dictionary with homework data
    :type homework_data: dict
    :return: path to Excel file with student's data
    :rtype: pathlib.WindowsPath
    """
    lesson_tasks = {"1": [3, 0],  # first value = mandatory tasks in lesson, second value = optional tasks
                    "2": [6, 3],
                    "3": [8, 3],
                    "4": [12, 2],
                    "5": [18, 9],
                    "6": [7, 7],
                    }
    total_mandatory_solved = 0  # counters
    total_optional_solved = 0
    student_data = dict()
    # student_data structure:
    # student_data = {1: {"mandatory": [1, 2, 3],
    #                     "optional": [2, 3]
    #                     },
    #                 2: {"mandatory": [1, 2, 3, 4],
    #                     "optional": [3]
    #                     }
    #                 }
    # input_data = {'Student1-lesson1': ['1', '2', '3'],
    #         'Student1-lesson2': [['1', '2', '3', '4'], ['1']],
    #         'Student2-lesson1': ['1', '2'],
    #         'Student2-lesson2': [['1', '2', '3', '4', '5', '6'], ['1', '2', '3']],
    #         'Student3-lesson1': ['1'],
    #         'Student3-lesson2': [['3', '6'], ['2']],
    #         'Student4-lesson2': [['2', '3', '4'], ['']]}

    #  Gathering data for student
    if not student_name in str(homework_data.keys()):  # checking if homework data exist for our student
        return pathlib.Path(f"Empty_hw-{student_name}.xlsx")

    for key in homework_data.keys():  # we go through keys and
        if student_name in key:  # look if key belongs to our student
            lesson_number = str(key)[-1:]
            student_data[lesson_number] = {"mandatory": homework_data[key][0],
                                           "optional": homework_data[key][1] if len(homework_data[
                                                                                        key]) > 1 else []}  # we get data from original dict, checking if there are optional tasks or not
            total_mandatory_solved += len(homework_data[key][0])  # counting totals for mandatory and optional tasks
            total_optional_solved = total_optional_solved + len(homework_data[key][1]) if len(
                homework_data[key][1]) > 0 else total_optional_solved



    #  Creating folder and Excel file with cumulative stats for student

    wb = openpyxl.Workbook()
    ss = wb.active
    ss["A1"].value = f"Hello {student_name}, here you can see your homework stats:"
    ss["A3"].value = "Lesson"
    ss["B3"].value = "Mandatory tasks solved"
    ss["C3"].value = "Mandatory tasks total"
    ss["D3"].value = "Optional tasks solved"
    ss["E3"].value = "Optional tasks total"
    ss["F3"].value = "Cumulative stats"
    for col_letter in ["B", "C", "D", "E"]:
        ss.column_dimensions[f"{col_letter}"].width = 30
    ss.merge_cells("F3:J3")
    for i in range(4, max(map(int, student_data.keys())) + 4):  # shift needed since we have some strings busy with descriptions and headers
        ss[f"A{i}"].value = i - 3  # lesson number
        ss[f"B{i}"].value = ",".join(student_data[str(i - 3)]["mandatory"])  # mandatory tasks solved for the lesson
        ss[f"B{i}"].alignment = Alignment(horizontal="right")
        ss[f"C{i}"].value = lesson_tasks[f"{i - 3}"][0]  # mandatory tasks total
        ss[f"D{i}"].value = ",".join(student_data[str(i - 3)]["optional"]) if ",".join(
            student_data[str(i - 3)]["optional"]) else 0
        ss[f"D{i}"].alignment = Alignment(horizontal="right")
        # from openpyxl import cell
        # c = ss[f"D{i}"]
        # assert isinstance(c, openpyxl.cell.cell.Cell)
        # c.alignment = Alignment(horizontal="right")
        ss[f"E{i}"].value = lesson_tasks[f"{i - 3}"][1]
    ss[f"A{i + 1}"].value = "TOTAL: "
    ss[f"B{i + 1}"].value = total_mandatory_solved
    ss[f"C{i + 1}"].value = sum([int(lesson_tasks[j][0]) for j in lesson_tasks.keys() if int(j) <= i - 3])
    ss[f"D{i + 1}"].value = total_optional_solved
    ss[f"E{i + 1}"].value = sum([int(lesson_tasks[j][1]) for j in lesson_tasks.keys() if int(j) <= i - 3])
    ss[f"B{i + 3}"].value = "Mandatory not solved total:"
    ss[f"C{i + 3}"].value = "Mandatory tasks total:"
    ss[f"D{i + 3}"].value = "Optional not solved total:"
    ss[f"E{i + 3}"].value = "Optional tasks total:"
    ss[f"B{i + 2}"].value = sum([int(lesson_tasks[j][0]) for j in lesson_tasks.keys() if int(j) <= i - 3]) - total_mandatory_solved
    ss[f"C{i + 2}"].value = sum([int(lesson_tasks[j][0]) for j in lesson_tasks.keys() if int(j) <= i - 3])
    ss[f"D{i + 2}"].value = sum([int(lesson_tasks[j][1]) for j in lesson_tasks.keys() if int(j) <= i - 3]) - total_optional_solved
    ss[f"E{i + 2}"].value = sum([int(lesson_tasks[j][1]) for j in lesson_tasks.keys() if int(j) <= i - 3])

    # lesson_tasks = {"1": [3, 0],  # first value = mandatory tasks in lesson, second value = optional tasks
    #                 "2": [6, 3],
    #                 "3": [8, 3],
    #                 "4": [12, 2],
    #                 "5": [18, 9],
    #                 "6": [7,7],
    #                }

    from openpyxl import chart  # creating Pie chart
    chart_data = openpyxl.chart.Reference(ss, min_col=2, min_row=i + 2, max_col=3, max_row=i + 2)
    labels = openpyxl.chart.Reference(ss, min_col=2, max_col=3, min_row=i + 3, max_row=i + 3)
    seriesObj = openpyxl.chart.Series(chart_data, title='Mandatory tasks solved')
    chartObj = openpyxl.chart.PieChart()
    chartObj.title = 'Mandatory tasks progress'
    chartObj.append(seriesObj)
    chartObj.set_categories(labels)
    ss.add_chart(chartObj, "F4")  # F4 is the top left corner of chart window
    #pprint.pprint(student_data)
    try:
        wb.save(f"Excel_homework_{student_name}_{lesson_number}.xlsx")
        logging.info(f"Excel file for student {student_name} created")
        return pathlib.Path(f"Excel_homework_{student_name}_{lesson_number}.xlsx")
    except Exception as e:
        logging.critical(f"Error creating excel file for student {student_name} Error: {e}")
        return None


# Connecting to Google Sheets
myss = ezsheets.Spreadsheet("1s9aPZCtvSKCOZdhfgYPr0W2_6EJflC2ej4MSEcEDo5o")

# Preparing file of course students
if not pathlib.Path.exists(pathlib.Path(r"students.py")):
    columns = [l for l in myss.sheets[0].getColumns() if [i for i in l if i]]  # extracting not empty columns from 1st sheet to get students and emails
    google_sheet_0_data = dict()
    for i in range(1, len([i for i in myss.sheets[0].getColumn("C") if i])):  # filtering from empty values and get len() to know how many students we have
        google_sheet_0_data.setdefault(str(columns[2][i]), str(columns[3][i]))  # getting emails + student names
    with open("students.py", mode="a") as file:
        file.write("google_sheet_0_data=" + pprint.pformat(google_sheet_0_data))  # writing data to file to use later
else:
    import students  # we have file so we just use it
    students_dict = students.students


# Checking folder structure

if not pathlib.Path(pathlib.Path("homework_repo")).exists():  # homework repository must exist and not be empty
    os.mkdir("homework_repo")
    print("homework_repo is missing, folder created")
if not os.listdir("homework_repo"):
    sys.exit("homework_repo is empty, please ensure that it will be filled with homework files\nFiles format is homework[1-n].txt where n is number of lessons")

# Creating folder for the lesson

for lesson_ended in range(1, max(list(map(lambda x: int(str(x)[-1:]), list(pathlib.Path("..").glob("Lesson*"))))) + 1):  # looking for maximum number of lessons, go from 1 to that value
    if not pathlib.Path.exists(pathlib.Path(f"homework{lesson_ended}")):  # checking if folders for homework exist meaning that we have processed this lesson's homework
        os.makedirs(f"homework{lesson_ended}", exist_ok=True)  # if not yet - create a new directory for data
        break


if not pathlib.Path.exists(pathlib.Path(r"homework_data.py")):  # checking if homework_data exists
    homework_data = dict()
else:
    import homework_data  # import data if it exist so we keep data across the lessons
    homework_data = homework_data.data


for i in range(lesson_ended):  # we read sheets from first (index 0) to N - 1 where N is number of lesson that have ended
    current_sheet = myss[i]  # type:ezsheets.Sheet
    current_sheet_rows = current_sheet.getRows()
    for j in range(1, len([r for r in current_sheet_rows if [s for s in r if s]])):  # we read all nonempty rows
        row = current_sheet_rows[j]
        if i == 0:  # we have little difference for 1st lesson in data
            homework_data.setdefault(f"{row[2]}-lesson{i + 1}", []) # Student1-lesson1
            mandatory_tasks = [list(map(lambda x: str(x)[-1:], row[1].split(","))), []] # [['1', '2', '3'], []]
            homework_data[f"{row[2]}-lesson{i + 1}"] = mandatory_tasks
        else:
            homework_data.setdefault(f"{row[1]}-lesson{i + 1}", [])  # Student1-lesson2
            mandatory_tasks = list(map(lambda x: str(x)[-1:], row[2].split(",")))
            hard_tasks = list(map(lambda x: str(x)[-1:], row[3].split(",")))
            homework_data[f"{row[1]}-lesson{i + 1}"] = [mandatory_tasks, hard_tasks]  # [['1', '2', '3', '4'], ['1']]


# Save data to file
if pathlib.Path.exists(pathlib.Path(r"homework_data.py")):
    os.makedirs("homework_data_backup", exist_ok=True)
    shutil.copy("homework_data.py", f"homework_data_backup\\{lesson_ended}.py")  # making backup of the file
with open("homework_data.py", mode="w") as homework_data_file:  # overwriting our dictionary with homework data to file
    homework_data_file.write("data=" + pprint.pformat(homework_data))

# ##### TODO DEBUG
#
# students_dict = 

for student in students_dict.keys():
    homework_excel_path = preparing_stats(student, homework_data)  # we get cumulative homework results for each student, write them to .xlsx file
    if "Empty" in str(homework_excel_path):  # if student doesnt have any homework done yet
        shutil.copy(pathlib.Path("Empty_hw.xlsx"), pathlib.Path(f"homework{lesson_ended}\\Empty_hw_{str(homework_excel_path).split('-')[1]}"))  # we send him special file
    elif homework_excel_path:  # if we have data and .xlsx was created
        shutil.copy(homework_excel_path, pathlib.Path(f"homework{lesson_ended}"))  # copy it to lesson's folder
    else:
        sys.exit("preparing_stats() returned None - excel file was not created, exiting")  # wasn't created - something is wrong


# Cleaning up
for f in pathlib.Path.cwd().glob("Excel_homework*.xlsx"):  # delete files from cwd
    send2trash.send2trash(f.name)


# Sending out
pprint.pprint(homework_data)  # debug

for student in students_dict.keys():  # prepare paths, send out files as letter's attachments
    student_hw_file_path = list(pathlib.Path(f"homework{lesson_ended}").glob(f"*{student}*"))[0]
    homework_file_path = pathlib.Path.joinpath(pathlib.Path(r"homework_repo"), rf"{lesson_ended + 1}.txt")
    email.send_email(students_dict[student], subject=f"Hello mr.{student}, here is your stats and homework", body_text=f"Demo file link:\n https://github.com/yaizkazani/yaizkazani/blob/master/lessons/{lesson_ended + 1}.py", att_file=[rf"{homework_file_path}", rf"{student_hw_file_path}"])
