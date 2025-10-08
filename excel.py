import pandas as pd

# 创建每个 Sprint 的 burndown 表格数据
sprint_data = {
    "Sprint 1 – Planning and Project Setup": [
        ["Task 1: Define project objectives and overall scope.", "2h", "Done"],
        ["Task 2: Create detailed user stories and assign roles.", "2h", "Done"],
        ["Task 3: Develop burndown chart template for progress tracking.", "1.5h", "Done"],
        ["Task 4: Initialize GitHub repository and allocate responsibilities.", "2h", "Done"],
        ["Task 5: Prepare Micro:bit hardware components.", "2h", "Done"]
    ],
    "Sprint 2 – Core Function Implementation": [
        ["Task 1: Implement forward/backward movement.", "2h", "Done"],
        ["Task 2: Add directional control.", "2h", "Done"],
        ["Task 3: Add user-defined speed control.", "1.5h", "Done"],
        ["Task 4: Conduct debugging and testing.", "2h", "In Progress"],
        ["Task 5: Record sprint progress.", "1h", "Planned"]
    ],
    "Sprint 3 – Path Control and System Integration": [
        ["Task 1: Develop user-defined path following.", "2h", "Done"],
        ["Task 2: Integrate movement/direction/speed modules.", "2.5h", "Done"],
        ["Task 3: Merge final code branches.", "1h", "Done"],
        ["Task 4: Document testing results.", "1.5h", "In Progress"]
    ],
    "Sprint 4 – Documentation and Presentation": [
        ["Task 1: Compile and finalize project report.", "2h", "Done"],
        ["Task 2: Record and upload demo video.", "1.5h", "Done"],
        ["Task 3: Complete Socio-Technical and CDP report.", "2h", "In Progress"],
        ["Task 4: Proofread documentation.", "1h", "Planned"],
        ["Task 5: Upload final deliverables.", "1h", "Planned"]
    ]
}

# 将所有 sprint 数据写入 Excel
with pd.ExcelWriter("/mnt/data/ProjectRobot1_Burndown_Tables.xlsx") as writer:
    for sprint, tasks in sprint_data.items():
        df = pd.DataFrame(tasks, columns=["Task Description", "Estimated Time", "Status"])
        df.to_excel(writer, sheet_name=sprint[:30], index=False)

"/mnt/data/ProjectRobot1_Burndown_Tables.xlsx"
