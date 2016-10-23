# ---[ Extension Tool 1 ]---
from com.parasoft.api import *

def storeValue(input, context): 
	arr = ['Blue','Cars','House'] 
	context.put("myArray", arr)
#---


#---[ Extension Tool 2 ]---
from com.parasoft.api import *

def getValue(input, context):
	arr = context.get("myArray")
	Application.showMessage(arr[0]) # Shows Blue in the console view ---
