#用于测试火箭发射功能_2026.5.31
import krpc
import time

conn = krpc.connect(name='Launch Test')
vessel = conn.space_center.active_vessel

vessel.auto_pilot.target_pitch_and_heading(90, 90)
vessel.auto_pilot.engage()
vessel.control.throttle = 1
time.sleep(1)

print('正在准备发射...')
vessel.control.activate_next_stage()

fuel = conn.get_call(vessel.resources.amount, 'SolidFuel')
expr = conn.krpc.Expression.less_than(conn.krpc.Expression.call(fuel),conn.krpc.Expression.constant_float(0.1))
event = conn.krpc.add_event(expr)
with event.condition:
    event.wait()
print('分离助推器中...')
vessel.control.activate_next_stage()
