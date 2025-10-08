import matplotlib.pyplot as plt
import numpy as np

# 定义 Sprint 数据
sprints = {
    "Sprint 1 – Planning and Project Setup (2 Days)": {
        "days": 2,
        "ideal": [5, 2.5, 0],
        "actual": [5, 3, 0]
    },
    "Sprint 2 – Core Function Implementation (3 Days)": {
        "days": 3,
        "ideal": [5, 3.3, 1.6, 0],
        "actual": [5, 4, 2.5, 0]
    },
    "Sprint 3 – Path Control and System Integration (3 Days)": {
        "days": 3,
        "ideal": [4, 2.6, 1.3, 0],
        "actual": [4, 3.5, 2, 0]
    },
    "Sprint 4 – Documentation and Presentation (2 Days)": {
        "days": 2,
        "ideal": [5, 2.5, 0],
        "actual": [5, 1.5, 0]
    }
}

# 绘图
plt.figure(figsize=(12, 10))
for i, (title, data) in enumerate(sprints.items(), 1):
    plt.subplot(2, 2, i)
    days = np.arange(0, data["days"] + 1)
    plt.plot(days, data["ideal"], 'r--', label='Ideal Progress')
    plt.plot(days, data["actual"], 'b-', marker='o', label='Actual Progress')
    plt.title(title, fontsize=10, pad=10)
    plt.xlabel("Days")
    plt.ylabel("Remaining Workload (Tasks)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
