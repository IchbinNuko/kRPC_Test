import krpc
conn = krpc.connect(name='Test Connection')
vessel = conn.space_center.active_vessel
print(vessel.name)