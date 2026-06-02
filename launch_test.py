#用于测试火箭发射功能_2026.5.31
import krpc
import time

address = '127.0.0.1'
port = 50000

conn = krpc.connect(name='Launch Test', address=address, rpc_port=port)
vessel = conn.space_center.active_vessel
#发射
vessel.auto_pilot.target_pitch_and_heading(90, 90)
vessel.auto_pilot.engage()
vessel.control.throttle = 1
print('正在准备发射...')
time.sleep(1)
vessel.control.activate_next_stage()


#检测固体燃料量（while循环，不要用）
#while True:
#    print("当前燃料量:", vessel.resources.amount("SolidFuel"))
#   time.sleep(1)

#检测固体燃料量，低于30.1时分离
fuel = conn.get_call(vessel.resources.amount, "SolidFuel")
expr = conn.krpc.Expression.less_than(conn.krpc.Expression.call(fuel),conn.krpc.Expression.
                                      constant_float(30.1)) #测试时用的火箭逃逸塔里面还有30燃料，所以这里设置为30.1
event = conn.krpc.add_event(expr)
with event.condition:
   event.wait()
print('分离助推器中...')
print("固推剩余燃料量：",vessel.resources.amount("SolidFuel"))
vessel.control.activate_next_stage()

#边检测边分离
# fuel_stream = conn.add_stream(vessel.resources.amount, "SolidFuel")
# while fuel_stream() > 30.0:     #测试时用的火箭逃逸塔里面还有30燃料，所以这里设置为30.1
#     print("当前燃料量:", fuel_stream())
#     time.sleep(1)
# vessel.control.activate_next_stage()
# print("固推分离，固推剩余燃料量：",vessel.resources.amount("SolidFuel"))