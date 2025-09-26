import matplotlib.pyplot as plt

students_names=["Thinush", "Harnith", "Leo", "Das", "Antony", "Harold", "Rukku", "sathya"]
students_marks=[45,47,25,45,25,40,25,40]

marks_perc = []

for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)

print(marks_perc)

print ()

def line_chart_of_students_and_marks():
    plt.plot(students_names, students_marks)
    plt.title("Students Marks Graph")
    plt.xlabel ("Students Names")
    plt.ylabel("Students Marks")
    plt.show()

line_chart_of_students_and_marks()

# bar chart
def percentage_bar_chart():
    plt.bar(students_names, marks_perc)
    plt. title("Students' Percentage Graph")
    plt.xlabel ("Student Names")
    plt.ylabel ("Student Percentage")
    plt. show()

percentage_bar_chart()

