import matplotlib.pyplot as plt

# PID 控制器参数
goal = 1000          # 目标值
start = 1        # 初始值
Kp = 0.10           # 比例系数
Ki =0        # 积分系数
Kd = 0          # 微分系数

# PID 控制器状态
integral = 0      # 积分项累积
previous_error = 0  # 上一次的误差

# 结果记录
history = []
for i in range(100):
    error = goal - start                 # 计算当前误差
    integral += error                    # 累积误差（积分项）
    derivative = error - previous_error  # 误差变化率（微分项）
    
    # 计算PID调整量
    adjustment = Kp * error + Ki * integral + Kd * derivative
    
    start += adjustment                   # 调整当前值
    history.append(start)                 # 记录当前值
    
    previous_error = error                # 更新上一次的误差
    
    print(f"Iteration {i+1}: start = {start:.4f}")

# 可视化结果
plt.figure(figsize=(10, 5))
plt.plot(range(1, 101), history, label='Start Value')
plt.axhline(y=goal, color='r', linestyle='--', label='Goal')
plt.title('PID')
plt.xlabel('time')
plt.ylabel('value')
plt.legend()
plt.grid(True)
plt.show()