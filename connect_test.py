import krpc

connect = krpc.connect(name='Test Connection')
print(f"KSP_Version: {connect.krpc.get_status().version}")

print('Connected to KSP version', connect.krpc.get_status().version)