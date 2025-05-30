import json
datafile = open('sample-data.json').read()
x = json.loads(datafile)
print(
"Interface Status" "\n"
"================================================================================" "\n"
"DN                                                 Description           Speed    MTU" "\n"
"-------------------------------------------------- --------------------  ------  ------"
)
y = x["imdata"]

for i in range(3):
    DN = y[i]["l1PhysIf"]["attributes"]["dn"]
    Description = y[i]["l1PhysIf"]["attributes"]["descr"]
    Speed = y[i]["l1PhysIf"]["attributes"]["speed"]
    MTU = y[i]["l1PhysIf"]["attributes"]["mtu"]
    print(f'{DN}                              {Description}{Speed}   {MTU}')